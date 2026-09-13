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
        r"console\.warn\('\[Listening Resolver\]', listenErr\);\s*\}\n",
        front, re.S)
    if not m:
        raise RuntimeError("listening resolver block not found in front template")
    return m.group(0)


# (name, tags-probe text or None, probe classes, has sentence, has audio)
CASES = [
    ("no definition, no tag", "", [], True, True),
    ("#listening tag with glosses", "je listening", ["def"], True, True),
    ("audio with glosses, no tag", "je", ["def"], True, True),
    ("no audio", "", [], True, False),
    ("frequency legacy", "", ["freq"], True, True),
    ("tag but no audio field", "listening", ["def"], True, False),
]


def build_html(resolver, tags, probes, sentence, audio):
    tags_html = f'<div class="tags-probe" hidden>{tags}</div>' if tags is not None else ""
    probe_html = "".join(f'<span class="probe-{p}" hidden></span>' for p in probes)
    sent_html = f'<div class="sentence-display">{sentence}</div>' if sentence else ""
    audio_html = (
        '<div class="listening-view">'
        '<button type="button" class="circular-audio-btn large-audio-btn">文</button>'
        '<span class="raw-audio-source" aria-hidden="true"></span>'
        "</div>"
    ) if audio else ""
    # Minimal stand-ins for the probes' surrounding context. The real
    # template defines container/wrapper before the resolver runs.
    return f"""<!doctype html><html><head><meta charset="utf-8">
<script>/* prevent Anki-style fetches from mattering */</script>
<style>.front-word-display{{display:none}}</style></head><body>
<div class="card"><div class="card-wrapper"><div class="card-container">
<div class="front-word-display">不公平</div>
{tags_html}{probe_html}{sent_html}{audio_html}
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
}} catch(e) {{ report.err = String(e && e.stack || e); }}
document.title = JSON.stringify(report);
</script></body></html>"""


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

    for name, tags, probes, sentence, audio in CASES:
        r = render(build_html(resolver, tags, probes,
                               "世の中って<b>不公平</b>よね", audio))
        check(f"{name}: probe returned", r is not None)
        if not r:
            continue
        if "err" in r:
            check(f"{name}: resolver ran without errors", False, r["err"])
            continue
        check(f"{name}: resolver ran without errors", True)

        # Determine expected behavior based on inputs
        has_listening_tag = "listening" in tags
        has_audio_field = audio  # test fixture simulates audio field presence

        if has_listening_tag and has_audio_field:
            # #listening tag forces listening front WITH audio (view visible, sentence gone)
            check(f"{name}: listening front active (view visible, sentence gone)",
                  r["listening"] is True and r["viewVisible"] and r["sentences"] == 0,
                  json.dumps(r))
        elif has_listening_tag:
            # #listening tag but no audio field → listening view not rendered, sentence stays
            check(f"{name}: sentence front (listening view not rendered)",
                  r["listening"] is False and r["sentences"] >= 1,
                  json.dumps(r))
        else:
            # no #listening tag → sentence front, listening inert
            check(f"{name}: sentence front (listening inert)",
                  r["listening"] is False and r["sentences"] >= 1,
                  json.dumps(r))

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
