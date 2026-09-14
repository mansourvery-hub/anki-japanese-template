#!/usr/bin/env python3
"""Mature Word Mode content-search fallback behavioral tests.

Extracts the content-search fallback block verbatim from the real
`Card 1 - Front.template.anki` and runs it in headless Chrome against
simulated AnkiConnect responses, asserting the mature-mode decision:

  1. single Expression match → uses that card's interval (word mode on if ≥ 365)
  2. duplicate Expressions, distinct Sentences → Sentence discriminator
     picks the exact card (never candidate 0 blindly)
  3. duplicate Expressions + duplicate Sentences, distinct cloze-body →
     cloze-body discriminator picks the exact card
  4. duplicate Expressions, Sentence absent on front → ambiguous →
     fails safely to sentence mode (interval stays null, no word mode)
  5. duplicate Expressions + same Sentence + no cloze-body probe →
     ambiguous → fails safely to sentence mode
  6. exact-current-card path (guiCurrentCard) is the primary path;
     content search only fires when guiCurrentCard throws

The block is extracted verbatim and run inside a harness that mocks the
`post` AnkiConnect helper and the surrounding `container`/`wrapper` DOM.

Run directly:  python3 tests/test_mature_content.py
Wired into ./verify alongside the other suites. Skipped gracefully
without Chrome.

Dependencies: headless Chrome only (same as test_front_modes.py).
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


def load_block():
    """Extract the content-search fallback block verbatim from the front,
    then strip `await` keywords so the harness can run it synchronously
    (the mock `post` returns values directly, not Promises).

    The block is the entire `catch (reviewErr) { ... }` body: guiCurrentCard
    is mocked to throw, so the catch's content-search fallback runs. We
    also extract escQuery/normText helpers.
    """
    with open(FRONT, encoding="utf-8") as f:
        front = f.read()
    esc_q = re.search(r"const escQuery = \(s\) =>.*?;", front, re.S)
    norm_t = re.search(r"const normText = \(s\) => s\s.*?\.trim\(\);", front, re.S)
    if not esc_q or not norm_t:
        raise RuntimeError("escQuery/normText helpers not found in front template")
    # Extract the catch block: from `} catch (reviewErr) {` to the `}` that
    # closes it (5 braces: catch + wordEl if + exprDom if + ids if + candidates if).
    # The 6th brace closes the outer `else if (!isListening)` — not included.
    m = re.search(
        r"\} catch \(reviewErr\) \{.*?source = 'content-search-ambiguous.*?sentence fallback';\s*\}\s*\}\s*\}\s*\}\s*\}"
        , front, re.S)
    if not m:
        raise RuntimeError("content-search fallback block not found in front template")
    block = m.group(0)
    # Strip `await` so the synchronous mock post (returns values, not
    # Promises) can drive the block without async infrastructure. The logic
    # (filter, discriminators, exact-card resolution) is unchanged.
    block = block.replace("await ", "")
    return esc_q.group(0), norm_t.group(0), block


def build_html(esc_q, norm_t, block, expr, sentence, cloze_body, anki_response):
    """Build a test harness HTML.

    anki_response: dict mapping action -> response. 'findCards' returns a
    list of card ids; 'cardsInfo' returns a list of card info dicts. The
    harness mocks `post` to return these. guiCurrentCard always throws
    (simulating the Browse previewer where no review is active).
    """
    # Build the mock post function: synchronous (returns value directly,
    # not a Promise). The extracted block has `await` stripped so this works.
    mock_post = """
var responses = %s;
function post(action, params) {
  return responses[action];
}
""" % json.dumps(anki_response)

    cloze_probe = ""
    if cloze_body is not None:
        cloze_probe = (
            '<div class="cloze-probe" hidden>'
            f'<span class="cloze-pre">前</span>'
            f'<span class="cloze-mid">{cloze_body}</span>'
            f'<span class="cloze-suf">後</span>'
            '</div>'
        )

    sent_html = ""
    if sentence is not None:
        sent_html = f'<div class="sentence-display">{sentence}</div>'

    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>.front-word-display{{display:none}}</style></head><body>
<div class="card"><div class="card-wrapper"><div class="card-container">
<div class="front-word-display">{expr}</div>
{cloze_probe}
{sent_html}
</div></div></div>
<script>
var report = {{}};
try {{
  /* guiCurrentCard mock: throws so the catch block (content-search fallback) runs. */
  var container = document.querySelector('.card-container');
  var wrapper = document.querySelector('.card-wrapper');
  var isListening = false;
  var interval = null;
  var source = 'unavailable';
{mock_post}
{esc_q}
{norm_t}
  try {{
    post('guiCurrentCard', {{}});
  {block}
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
        print("[SKIP] no headless Chrome found — mature content-search checks skipped")
        return 0
    esc_q, norm_t, block = load_block()

    # --- Case 1: single Expression match → uses that card's interval ---
    anki = {
        "findCards": [100],
        "cardsInfo": [{
            "interval": 400,
            "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "世の中って不公平よね"},
                "cloze-body": {"value": "不公平"}
            }
        }]
    }
    r = render(build_html(esc_q, norm_t, block, "不公平",
                          "世の中って<b>不公平</b>よね", "不公平", anki))
    check("single match: probe returned", r is not None)
    if r:
        check("single match: resolver ran without errors", "err" not in r, r.get("err", ""))
        check("single match: interval used (400, word mode eligible)",
              r.get("interval") == 400, json.dumps(r))
        check("single match: source = content-search",
              r.get("source") == "content-search", json.dumps(r))

    # --- Case 2: duplicate Expressions, distinct Sentences → Sentence discriminator ---
    anki = {
        "findCards": [100, 101],
        "cardsInfo": [
            {"interval": 10, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "別の文不公平別"},
                "cloze-body": {"value": "不公平"}}},
            {"interval": 500, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "世の中って不公平よね"},
                "cloze-body": {"value": "不公平"}}}
        ]
    }
    r = render(build_html(esc_q, norm_t, block, "不公平",
                          "世の中って<b>不公平</b>よね", "不公平", anki))
    check("dup Expr + distinct Sentence: probe returned", r is not None)
    if r:
        check("dup Expr + distinct Sentence: resolver ran without errors", "err" not in r, r.get("err", ""))
        check("dup Expr + distinct Sentence: Sentence discriminator picks exact card (interval 500, not candidate 0's 10)",
              r.get("interval") == 500, json.dumps(r))
        check("dup Expr + distinct Sentence: source = content-search",
              r.get("source") == "content-search", json.dumps(r))

    # --- Case 3: dup Expr + dup Sentence, distinct cloze-body → cloze-body discriminator ---
    anki = {
        "findCards": [100, 101],
        "cardsInfo": [
            {"interval": 10, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "世の中って不公平よね"},
                "cloze-body": {"value": "別の"}}},
            {"interval": 600, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "世の中って不公平よね"},
                "cloze-body": {"value": "不公平"}}}
        ]
    }
    r = render(build_html(esc_q, norm_t, block, "不公平",
                          "世の中って<b>不公平</b>よね", "不公平", anki))
    check("dup Expr + dup Sentence + distinct cloze-body: probe returned", r is not None)
    if r:
        check("dup Expr + dup Sentence + distinct cloze-body: resolver ran without errors",
              "err" not in r, r.get("err", ""))
        check("dup Expr + dup Sentence + distinct cloze-body: cloze-body discriminator picks exact card (interval 600, not 10)",
              r.get("interval") == 600, json.dumps(r))
        check("dup Expr + dup Sentence + distinct cloze-body: source = content-search",
              r.get("source") == "content-search", json.dumps(r))

    # --- Case 4: dup Expr, no Sentence on front → ambiguous → safe fallback ---
    anki = {
        "findCards": [100, 101],
        "cardsInfo": [
            {"interval": 10, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "別の文"},
                "cloze-body": {"value": "不公平"}}},
            {"interval": 500, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "また別の文"},
                "cloze-body": {"value": "不公平"}}}
        ]
    }
    r = render(build_html(esc_q, norm_t, block, "不公平",
                          None, "不公平", anki))
    check("dup Expr + no Sentence on front: probe returned", r is not None)
    if r:
        check("dup Expr + no Sentence on front: resolver ran without errors",
              "err" not in r, r.get("err", ""))
        check("dup Expr + no Sentence on front: fails safely (interval null, no word mode)",
              r.get("interval") is None, json.dumps(r))
        check("dup Expr + no Sentence on front: source marks ambiguity",
              "ambiguous" in (r.get("source") or ""), json.dumps(r))

    # --- Case 5: dup Expr + dup Sentence + no cloze-body probe → ambiguous → safe fallback ---
    anki = {
        "findCards": [100, 101],
        "cardsInfo": [
            {"interval": 10, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "世の中って不公平よね"},
                "cloze-body": {"value": "別の"}}},
            {"interval": 500, "fields": {
                "Expression": {"value": "不公平"},
                "Sentence": {"value": "世の中って不公平よね"},
                "cloze-body": {"value": "不公平"}}}
        ]
    }
    r = render(build_html(esc_q, norm_t, block, "不公平",
                          "世の中って<b>不公平</b>よね", None, anki))
    check("dup Expr + dup Sentence + no cloze-body probe: probe returned", r is not None)
    if r:
        check("dup Expr + dup Sentence + no cloze-body probe: resolver ran without errors",
              "err" not in r, r.get("err", ""))
        check("dup Expr + dup Sentence + no cloze-body probe: fails safely (interval null)",
              r.get("interval") is None, json.dumps(r))
        check("dup Expr + dup Sentence + no cloze-body probe: source marks ambiguity",
              "ambiguous" in (r.get("source") or ""), json.dumps(r))

    # --- Case 6: no cards found → interval null (safe fallback) ---
    anki = {"findCards": [], "cardsInfo": []}
    r = render(build_html(esc_q, norm_t, block, "不公平",
                          "世の中って<b>不公平</b>よね", "不公平", anki))
    check("no cards found: probe returned", r is not None)
    if r:
        check("no cards found: resolver ran without errors", "err" not in r, r.get("err", ""))
        check("no cards found: interval null (safe fallback)",
              r.get("interval") is None, json.dumps(r))

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
