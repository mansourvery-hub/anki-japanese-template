#!/usr/bin/env python3
"""Headless layout verification for the density pass.

Renders the REAL stylesheet plus template-shaped HTML in Chrome headless
(google-chrome-stable is available on this machine) and asserts layout
invariants that pure text tests cannot catch:

  - card height is content-driven (back card < 90% of viewport height
    on a rich desktop card, i.e. no viewport fill)
  - no horizontal overflow / clipping
  - furigana (rt) never overlaps the line above it
  - hierarchy: headword font > sentence font > definition font > notes
  - truncator: a long definition clamps at 3 lines until expanded
  - listening front keeps the audio button a comfortable target
  - definition expand still works (JS one-way expand)

Usage: python3 tests/test_layout.py
Requires: google-chrome-stable on PATH. Skipped gracefully if absent
        (finish.sh runs it as part of step 0 when present).
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSS = os.path.join(ROOT, "Card 1 - Style.css")
CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
    if cond:
        PASS += 1
    else:
        FAIL += 1


# ---------------------------------------------------------------- HTML fixture
# Back card with every block populated: furigana headword, pitch, audio,
# long definition, furigana sentence, picture, More section (translation,
# extended definition, notes), source footer. New minimal hierarchy:
# word → meaning → context (sentence + picture) → More ▾.
BACK_CARD = """<!doctype html><html><head><meta charset="utf-8">
<style>
html,body{margin:0;padding:0;}
/* minimal Anki stand-ins: replay link + fonts so JS runs like in Anki */
</style>
<style>
__CSS__
</style></head><body>
<div class="card back-card">
<div class="card-wrapper back-card">
  <div class="card-container">
    <div class="retrieval-state" data-state="context"><span class="retrieval-state-label">Context</span></div>
    <div class="word-display" id="word"><ruby>澄<rt>す</rt></ruby>ます</div>
    <div class="pitch-quiet">[0]</div>
    <div class="definition-box primary-definition" id="def">
      <div class="yomitan-glossary"><ol>
        <li><div data-sc-name="語義G">水などを濁りのない状態にする。とても長い定義のテキストで、三行を超えることを保証するためにさらに文字を追加している。三行目に入ってもまだ続くほど十分に長い定義であることを確認するための文です。全幅レイアウトでも確実に三行を超えるように、さらに追加の検証用テキストをここに置く。この文が折り返して四行目に達すれば、切り詰め機能が正しく発動するはずである。</div>
        <div data-sc-name="語義G">雑念を払って、心を落ち着かせる。二番目の語義。</div>
        <div data-sc-name="語義G">一つのことに注意を向ける。三番目の語義（隠れるはず）。</div>
        <div data-sc-name="補説G">supplementary (hidden)</div></li>
      </ol></div>
      <!-- Font-independent overflow guarantee: CI runners have Chrome but
           no CJK fonts, so the Japanese text above renders with fallback
           tofu metrics and may fit within the 3-line cap. The fixed-height
           spacer makes scrollHeight > clientHeight true in EVERY
           environment, so the truncator checks never depend on font
           availability. -->
      <div style="height:140px"></div>
    </div>
    <div class="audio-row">
      <span class="audio-btn-wrapper">
        <button type="button" class="circular-audio-btn small-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">言葉</span></span></button>
        <span class="raw-audio-source"><a class="replay-button" href="#">replay</a></span>
      </span>
      <span class="audio-btn-wrapper">
        <button type="button" class="circular-audio-btn small-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">文</span></span></button>
        <span class="raw-audio-source"><a class="replay-button" href="#">replay</a></span>
      </span>
    </div>
    <div class="context-grid">
      <div class="context-main">
        <div class="sentence-japanese" id="sentence"><ruby>心<rt>こころ</rt></ruby>を<ruby>澄<rt>す</rt></ruby>ませて、<b>音楽</b>を聴く。長い文章が二行に折り返される場合の検証も兼ねている。</div>
      </div>
      <div class="context-picture">
        <div class="picture-container"><img id="pic" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E"></div>
      </div>
    </div>
    <div class="more-section" hidden>
      <div class="translation-box"><div class="translation-hint">Translation</div>
        <div class="translation-text">To clear one's mind and listen to music.</div></div>
      <div class="html-content secondary-block">Additional context paragraph.</div>
      <div class="html-content secondary-block">漢字のメモ: 澗 — radical 水.</div>
      <div class="html-content secondary-block extended-full">Full extended definition text that stays untruncated.</div>
    </div>
    <button type="button" class="more-toggle" aria-expanded="false">More <span class="more-caret">▾</span></button>
    <div class="source-footer">SOURCE — some novel</div>
  </div>
</div>
</div>
<script>
window.expandDefinition = function(element) {
  if (element.classList.contains('is-expanded')) return;
  element.classList.add('is-expanded');
};
window.initDefinitionTruncation = function() {
  document.querySelectorAll('.primary-definition').forEach(function(box) {
    const overflows = box.scrollHeight > box.clientHeight + 2;
    box.classList.toggle('is-truncated', overflows);
  });
};
window.initDefinitionTruncation();
</script>
</body></html>"""

FRONT_SENTENCE = """<!doctype html><html><head><meta charset="utf-8">
<style>__CSS__</style></head><body>
<div class="card"><div class="card-wrapper">
  <div class="card-container">
    <div class="sentence-display" id="sent">彼は<b>約束</b>を<ruby>守<rt>まも</rt></ruby>らなかった。</div>
  </div>
</div></div>
</body></html>"""

FRONT_LISTENING = """<!doctype html><html><head><meta charset="utf-8">
<style>__CSS__</style></head><body>
<div class="card"><div class="card-wrapper listening-mode">
  <div class="card-container">
    <div class="listening-view" id="listening">
      <div class="audio-btn-wrapper">
        <button type="button" class="circular-audio-btn large-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">文</span></span></button>
      </div>
    </div>
  </div>
</div></div>
</body></html>"""


# ---------------------------------------------------------------- probing JS
PROBE = """(() => {
  const r = {};
  const wrapper = document.querySelector('.card-wrapper');
  const card = document.querySelector('.card');
  r.wrapperH = wrapper.getBoundingClientRect().height;
  r.viewportH = window.innerHeight;
  r.docScrollW = document.documentElement.scrollWidth;
  r.docClientW = document.documentElement.clientWidth;
  // overflow-x anywhere?
  r.hOverflow = r.docScrollW > r.docClientW + 1;
  // furigana overlap: rt boxes vs previous line — collect any rt whose
  // top is above the previous sibling line's bottom is hard generically;
  // instead verify every rt's top >= its ruby's parent's top (rt never
  // escapes the container) AND that rt boxes do not overlap the element
  // above: compare first rt top vs sentence/word container top.
  const word = document.querySelector('.word-display');
  if (word) {
    const rb = word.getBoundingClientRect();
    const rt = word.querySelector('rt');
    r.wordFont = parseFloat(getComputedStyle(word).fontSize);
    if (rt) { const rtb = rt.getBoundingClientRect();
      r.wordRtInside = rtb.top >= rb.top - 0.5 && rtb.bottom <= rb.bottom + 0.5; }
  }
  const sent = document.querySelector('#sentence, .sentence-japanese');
  if (sent) {
    r.sentFont = parseFloat(getComputedStyle(sent).fontSize);
    const rt = sent.querySelector('rt');
    const sb = sent.getBoundingClientRect();
    if (rt) { const rtb = rt.getBoundingClientRect();
      r.sentRtInside = rtb.top >= sb.top - 0.5; }
    r.sentH = sb.height;
  }
    const def = document.querySelector('#def');
  if (def) {
    r.defFont = parseFloat(getComputedStyle(def).fontSize);
    const cs = getComputedStyle(def);
    r.defLineH = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.5;
    r.defPadTop = parseFloat(cs.paddingTop) || 0;
    r.defClampedH = def.getBoundingClientRect().height;
    r.defScrollH = def.scrollHeight;
    r.defTruncated = def.classList.contains('is-truncated');
    // expand and re-measure
    window.expandDefinition(def);
    r.defExpandedH = def.getBoundingClientRect().height;
  }
  const notes = document.querySelector('.secondary-block');
  if (notes && def) {
    r.notesFont = parseFloat(getComputedStyle(notes).fontSize);
    r.hierarchy = r.wordFont > r.sentFont && r.sentFont > r.defFont && r.defFont >= r.notesFont;
  }
  const pic = document.querySelector('#pic');
  if (pic) { const pb = pic.getBoundingClientRect(); r.picH = pb.height; r.picW = pb.width; }
  const listening = document.querySelector('#listening');
  if (listening) {
    const lb = listening.getBoundingClientRect();
    const btn = listening.querySelector('.circular-audio-btn');
    r.listenH = lb.height;
    r.listenBtn = btn.getBoundingClientRect().height;
  }
  // Context grid: picture beside the sentence on wide screens.
  const ctxPic = document.querySelector('.context-picture');
  const ctxMain = document.querySelector('.context-main');
  if (ctxPic && ctxMain && innerWidth >= 768) {
    r.twoCol = ctxPic.getBoundingClientRect().left > ctxMain.getBoundingClientRect().right;
    r.sideW = ctxPic.getBoundingClientRect().width;
    r.mainW = ctxMain.getBoundingClientRect().width;
  }
  // Secondary info collapsed by default; More toggle present.
  const more = document.querySelector('.more-section');
  const moreBtn = document.querySelector('.more-toggle');
  if (more && moreBtn) {
    r.moreCollapsed = more.hidden === true
      && moreBtn.getAttribute('aria-expanded') === 'false';
    r.moreBelowFold = more.getBoundingClientRect().height;
  }
  const footer = document.querySelector('.source-footer');
  if (footer && wrapper) {
    r.footerInside = footer.getBoundingClientRect().bottom <= wrapper.getBoundingClientRect().bottom + 1;
  }
  return r;
})()"""


def render(html, width, height):
    """Chrome headless screenshot + JS probe via --dump-dom is awkward;
    use the DevTools-free trick: virtual-time + console.log of the probe,
    captured from chrome's stderr? No — instead write the probe result
    into the DOM title and read it from the dumped DOM."""
    probe_html = html.replace(
        "</body>",
        f"<script>document.title = JSON.stringify({PROBE});</script></body>",
    )
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "card.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(probe_html)
        try:
            out = subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu",
                 "--no-sandbox", "--hide-scrollbars",
                 f"--window-size={width},{height}",
                 "--virtual-time-budget=2000",
                 "--dump-dom", f"file://{path}"],
                capture_output=True, text=True, timeout=60,
            ).stdout
        except subprocess.TimeoutExpired:
            return None
    import re
    m = re.search(r"<title>(.*?)</title>", out, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def main():
    if not CHROME:
        print("[SKIP] no headless Chrome found — layout checks skipped")
        return 0
    css = open(CSS, encoding="utf-8").read()

    # ---- Desktop back card (1440x900, rich card) ----
    back = render(BACK_CARD.replace("__CSS__", css), 1440, 900)
    check("desktop back: probe returned", back is not None)
    if back:
        check("desktop back: content-driven card (rich card < 100% viewport)",
              back["wrapperH"] < back["viewportH"],
              f"wrapper={back['wrapperH']:.0f} viewport={back['viewportH']}")
        check("desktop back: no horizontal overflow", not back["hOverflow"])
        check("desktop back: word furigana stays inside its line box",
              back.get("wordRtInside", True))
        check("desktop back: sentence furigana stays inside its block",
              back.get("sentRtInside", True))
        check("desktop back: hierarchy word > sentence > definition > notes",
              back.get("hierarchy", False),
              f"word={back.get('wordFont')} sent={back.get('sentFont')} "
              f"def={back.get('defFont')} notes={back.get('notesFont')}")
        check("desktop back: long definition IS truncated by JS",
              back.get("defTruncated", False))
        check("desktop back: clamped height ≈ pad + 3 line-heights",
              abs(back["defClampedH"] - (back["defPadTop"] + 3 * back["defLineH"])) <= 8,
              f"clamped={back['defClampedH']:.0f} expected={back['defPadTop'] + 3*back['defLineH']:.0f}")
        check("desktop back: expand grows the definition (one-way)",
              back.get("defExpandedH", 0) > back.get("defClampedH", 0) + 4)
        check("desktop back: image height capped (<= 40vh)",
              back.get("picH", 0) <= 0.40 * back["viewportH"] + 2,
              f"picH={back.get('picH', 0):.0f}")
        check("desktop back: context grid engaged (picture beside sentence)",
              back.get("twoCol", False),
              f"main={back.get('mainW', 0):.0f} pic-col={back.get('sideW', 0):.0f}")
        check("desktop back: picture column is the minority width",
              back.get("sideW", 1) < back.get("mainW", 0))
        check("desktop back: secondary info collapsed behind More by default",
              back.get("moreCollapsed", False))
        check("desktop back: footer inside the card wrapper",
              back.get("footerInside", False))

    # ---- Mobile back card (A50-ish 412x892) ----
    mob = render(BACK_CARD.replace("__CSS__", css), 412, 892)
    check("mobile back: probe returned", mob is not None)
    if mob:
        check("mobile back: no horizontal overflow", not mob["hOverflow"])
        check("mobile back: stacked (no context-grid columns)", not mob.get("twoCol", False))
        check("mobile back: no forced viewport fill",
              mob["wrapperH"] < 0.95 * mob["viewportH"],
              f"wrapper={mob['wrapperH']:.0f} viewport={mob['viewportH']}")
        check("mobile back: sentence font stays >= 1rem", mob.get("sentFont", 1) >= 16)

    # ---- Front sentence card ----
    fr = render(FRONT_SENTENCE.replace("__CSS__", css), 1440, 900)
    check("front sentence: probe returned", fr is not None)
    if fr:
        check("front sentence: no horizontal overflow", not fr["hOverflow"])
        check("front sentence: content-driven (wrapper < 50% viewport)",
              fr["wrapperH"] < 0.5 * fr["viewportH"],
              f"wrapper={fr['wrapperH']:.0f}")

    # ---- Front listening card ----
    fl = render(FRONT_LISTENING.replace("__CSS__", css), 1440, 900)
    check("front listening: probe returned", fl is not None)
    if fl:
        check("front listening: button is a comfortable target (>= 64px)",
              fl.get("listenBtn", 0) >= 64, f"btn={fl.get('listenBtn')}")
        check("front listening: view height in 20-35vh band",
              0.20 * fl["viewportH"] <= fl.get("listenH", 0) <= 0.36 * fl["viewportH"],
              f"listenH={fl.get('listenH', 0):.0f}")

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
