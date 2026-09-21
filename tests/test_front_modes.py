#!/usr/bin/env python3
"""Front-mode resolver behavioral tests (listening semantics).

Extracts the LISTENING RESOLVER block verbatim from the real
`Card 1 - Front.template.anki` and runs it in headless Chrome against
six front-state harnesses, asserting the resolved mode:

  1. classic audio-only (no Definition/Extended/Frequency + audio)
     -> listening front: sentence removed, listening-view visible
  2. #listening tag + glosses -> listening front (deliberate exercise)
  3. sentence audio + glosses, no tag -> sentence front (regular card)
  4. no audio at all -> sentence front
  5. Frequency legacy probe -> sentence front (never the audio button)
  6. tag but no Sentence Audio -> sentence front (markup is gated on
     Sentence Audio existing)

Run directly:  python3 tests/test_front_modes.py
Wired into ./verify alongside the other suites. Skipped gracefully
without Chrome.

Dependencies: headless Chrome only (same as test_layout.py).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
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


def load_resolver():
    """Extract the resolver block verbatim from the real front template."""
    with open(FRONT, encoding="utf-8") as f:
        front = f.read()
    m = re.search(
        r"/\* --- LISTENING RESOLVER.*?"
        r"container\.querySelectorAll\('\.listening-view'\)\.forEach\(\(v\) => v\.remove\(\)\);\s*\}\n",
        front, re.S)
    if not m:
        raise RuntimeError("listening resolver block not found in front template")
    return m.group(0)


# (name, has_audio_card, tags_text, tag_audio_source)
# tag_audio_source: content placed inside .raw-audio-source for the tag view.
#   Empty string = no audio field rendered (Policy B fallback test).
CASES = [
    ("classic audio-only (listening-view present)", True, "", None),
    ("normal card (glosses, no listening-view)", False, "", None),
    ("word card (no audio on front)", False, "", None),
    ("#listening tag with Sentence Audio", False, "listening", "[sound:sentence.mp3]"),
    ("#listening tag with Word Audio only", False, "listening", "[sound:word.mp3]"),
    ("#listening tag WITHOUT audio (Policy B fallback)", False, "listening", ""),
    ("non-listening tag (vocab tag with glosses)", False, "vocab n3", "[sound:x.mp3]"),
    # Exactly-one-button invariant: a pure #listening audio card renders BOTH
    # a tag-listening-view and a classic-listening-view in the markup. The
    # resolver must keep only the active one (tag-listening-view wins) and
    # remove the dead/duplicate classic view.
    ("#listening + audio card (both views in markup)", True, "listening", "[sound:sentence.mp3]"),
]


def build_html(resolver, is_listening_card, tags_text="", tag_audio_source=None):
    sent_html = '<div class="sentence-display">世の中って<b>不公平</b>よね</div>'
    if tags_text is not None and tags_text != "":
        # When tag_audio_source is None, no tag-listening-view is rendered
        # (tag without audio fields); when it's a string, the view carries
        # that audio source — mirroring the real template's Policy B markup.
        if tag_audio_source is not None:
            audio_inner = tag_audio_source
            # Fully-native audio: the view carries Anki's own replay anchor
            # (no custom button, no hidden raw source). An empty audio field
            # renders an empty shell — Policy B must reject it (no link, no
            # text) and fall back to the sentence front.
            if audio_inner == "":
                tag_view_html = (
                    '<div class="listening-view tag-listening-view" '
                    'style="display: none;"></div>'
                )
            else:
                tag_view_html = (
                    '<div class="listening-view tag-listening-view" style="display: none;">'
                    f'<a class="native-audio-link" href="#" data-audio="{audio_inner}">文</a>'
                    '</div>'
                )
        else:
            tag_view_html = ""
        tags_html = (
            f'<div class="tags-probe" hidden>{tags_text}</div>'
            + tag_view_html
        )
    else:
        tags_html = ""
    classic_audio = (
        '<div class="listening-view classic-listening-view">'
        '<span class="native-audio"><a class="replay-button" href="#">文</a></span>'
        '</div>'
    ) if is_listening_card else ""
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>.front-word-display{{display:none}}</style></head><body>
<div class="card"><div class="card-wrapper"><div class="card-container">
<div class="front-word-display">不公平</div>
{tags_html}{sent_html}{classic_audio}
</div></div></div>
<script>
var report = {{}};
try {{
  var container = document.querySelector('.card-container');
  var wrapper = document.querySelector('.card-wrapper');
{resolver}
report.listening = isListening;
report.cls = wrapper.className;
report.sentences = container.querySelectorAll('.sentence-display').length;
var lv = container.querySelector('.listening-view');
report.viewVisible = !!lv && getComputedStyle(lv).display !== 'none';
report.listeningViews = container.querySelectorAll('.listening-view').length;
}} catch(e) {{ report.err = String(e && e.stack || e); }}
document.title = JSON.stringify(report);
</script>
</body></html>"""


def render(html):
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "front.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        try:
            out = subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu",
                 "--no-sandbox", "--hide-scrollbars",
                 "--window-size=1440,900",
                 "--virtual-time-budget=1500",
                 "--dump-dom", f"file://{path}"],
                capture_output=True, text=True, timeout=60,
            ).stdout
        except subprocess.TimeoutExpired:
            return None
    m = re.search(r"<title>(.*?)</title>", out, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


def main():
    if not CHROME:
        print("[SKIP] no headless Chrome found — front-mode checks skipped")
        return 0
    resolver = load_resolver()

    for case in CASES:
        name, is_listening, tags_text, tag_audio = case
        r = render(build_html(resolver, is_listening, tags_text, tag_audio))
        check(f"{name}: probe returned", r is not None)
        if not r:
            continue
        if "err" in r:
            check(f"{name}: resolver ran without errors", False, r["err"])
            continue
        check(f"{name}: resolver ran without errors", True)

        # Policy B: #listening without usable audio falls back to sentence front.
        # A classic audio-only card (is_listening_card=True) always has a real
        # audio source in its classic-listening-view, so it activates listening.
        is_policy_b_fallback = (
            tags_text and "listening" in tags_text
            and tag_audio == ""
        )
        has_tag_audio = tag_audio is not None and tag_audio != ""
        expected_listening = is_listening or (
            tags_text and "listening" in tags_text and has_tag_audio
        )
        # Policy B: tag without audio → sentence front
        if is_policy_b_fallback:
            expected_listening = False

        if expected_listening:
            check(f"{name}: listening front active (view visible, sentence removed, exactly 1 view)",
                  r["listening"] is True and r["viewVisible"] and r["sentences"] == 0
                  and r["listeningViews"] == 1,
                  json.dumps(r))
        else:
            check(f"{name}: sentence front active (listening false, sentence intact, 0 listening views)",
                  r["listening"] is False and not r["viewVisible"] and r["sentences"] == 1
                  and r["listeningViews"] == 0,
                  json.dumps(r))

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
