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


def load_template_and_resolver():
    """Extract the template HTML and the listening resolver from the real front template."""
    with open(FRONT, encoding="utf-8") as f:
        front = f.read()
    m_script = re.search(r"<script>(.*?)</script>", front, re.S)
    if not m_script:
        raise RuntimeError("script not found in front template")
    script = m_script.group(1)

    m_res = re.search(
        r"/\* --- LISTENING RESOLVER.*?"
        r"container\.querySelectorAll\('\.listening-view'\)\.forEach\(\(lv\) => lv\.remove\(\)\);\s*\}\n",
        script, re.S)
    if not m_res:
        raise RuntimeError("listening resolver block not found in front template")
    resolver = m_res.group(0)
    html_markup = front[:m_script.start()].strip()
    return html_markup, resolver


def expand_anki_template(template_text, fields):
    """Simulate Anki's template conditional and field expansion."""
    pattern = re.compile(r"\{\{([#^])([^}]+)\}\}(.*?)\{\{/\2\}\}", re.S)
    text = template_text
    while True:
        m = pattern.search(text)
        if not m:
            break
        sig, field_name, inner = m.group(1), m.group(2).strip(), m.group(3)
        val = fields.get(field_name, "")
        is_truthy = bool(val and str(val).strip())
        if sig == "#":
            replacement = inner if is_truthy else ""
        else:
            replacement = "" if is_truthy else inner
        text = text[:m.start()] + replacement + text[m.end():]

    def replace_field(m):
        raw = m.group(1).strip()
        field_name = raw.split(":")[-1].strip()
        val = fields.get(field_name, "")
        if field_name in ("Sentence Audio", "Word Audio") and val:
            return f'<a class="replay-button soundLink" href="playsound:0">{val}</a>'
        return val

    text = re.sub(r"\{\{([^#/][^}]*)\}\}", replace_field, text)
    return text


# Test cases covering Policy B and all listening edge cases:
# (name, fields, expected_listening, expected_audio_label)
CASES = [
    (
        "#listening + usable Sentence Audio -> listening mode",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Definition": "unfair",
            "Tags": "listening",
            "Sentence Audio": "[sound:sentence.mp3]",
        },
        True,
        "文",
    ),
    (
        "#listening + usable Word Audio (no sentence audio) -> listening mode",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Definition": "unfair",
            "Tags": "listening",
            "Word Audio": "[sound:word.mp3]",
        },
        True,
        "言葉",
    ),
    (
        "#listening + no usable audio -> safe fallback to sentence front",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Definition": "unfair",
            "Tags": "listening",
        },
        False,
        None,
    ),
    (
        "#listening + audio, no glosses (tag+classic views coexist) -> exactly ONE sound button",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Tags": "listening",
            "Sentence Audio": "[sound:sentence.mp3]",
        },
        True,
        "文",
    ),
    (
        "no #listening + normal definitions + sentence audio -> normal sentence front",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Definition": "unfair",
            "Sentence Audio": "[sound:sentence.mp3]",
        },
        False,
        None,
    ),
    (
        "no #listening + normal definitions + no audio -> normal sentence front",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Definition": "unfair",
        },
        False,
        None,
    ),
    (
        "no #listening + unrelated tag + definitions -> normal sentence front",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Definition": "unfair",
            "Tags": "vocab::jlpt_n3",
            "Sentence Audio": "[sound:sentence.mp3]",
        },
        False,
        None,
    ),
    (
        "no #listening + legacy audio-only card (Sentence Audio) -> listening mode",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Sentence Audio": "[sound:sentence.mp3]",
        },
        True,
        "文",
    ),
    (
        "no #listening + legacy audio-only card (Word Audio) -> listening mode",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
            "Word Audio": "[sound:word.mp3]",
        },
        True,
        "言葉",
    ),
    (
        "no #listening + legacy card without audio -> fallback sentence front",
        {
            "Expression": "不公平",
            "Sentence": "世の中って<b>不公平</b>よね",
        },
        False,
        None,
    ),
]


def build_html(html_markup, resolver, fields):
    expanded = expand_anki_template(html_markup, fields)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>.front-word-display{{display:none}}</style></head><body>
{expanded}
<script>
var report = {{}};
try {{
  var container = document.querySelector('.card-container');
  var wrapper = document.querySelector('.card-wrapper');
{resolver}
report.listening = isListening;
report.cls = wrapper.className;
report.sentences = container.querySelectorAll('.sentence-display').length;
var lvs = container.querySelectorAll('.listening-view');
report.viewVisible = !!lvs.length;
report.audioButtons = 0;
for (var vi = 0; vi < lvs.length; vi++) {{
  if (getComputedStyle(lvs[vi]).display !== 'none') report.audioButtons++;
}}
var firstLv = lvs[0];
var labelEl = firstLv ? firstLv.querySelector('.audio-btn-label') : null;
report.visibleLabel = (labelEl ? labelEl.textContent.trim() : null);
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
    html_markup, resolver = load_template_and_resolver()

    for name, fields, expected_listening, expected_audio_label in CASES:
        r = render(build_html(html_markup, resolver, fields))
        check(f"{name}: probe returned", r is not None)
        if not r:
            continue
        if "err" in r:
            check(f"{name}: resolver ran without errors", False, r["err"])
            continue
        check(f"{name}: resolver ran without errors", True)

        if expected_listening:
            label_ok = (expected_audio_label is None) or (r.get("visibleLabel") == expected_audio_label)
            check(
                f"{name}: listening front active (view visible, sentence removed, label={expected_audio_label})",
                r["listening"] is True and r["viewVisible"] and r["sentences"] == 0 and label_ok,
                json.dumps(r),
            )
            check(
                f"{name}: exactly one visible sound button (no duplicate/dead view)",
                r.get("audioButtons") == 1,
                json.dumps(r),
            )
        else:
            check(
                f"{name}: sentence front active (listening false, sentence intact)",
                r["listening"] is False and not r["viewVisible"] and r["sentences"] >= 1,
                json.dumps(r),
            )
            check(
                f"{name}: no sound button rendered when audio is missing",
                r.get("audioButtons") == 0,
                json.dumps(r),
            )

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
