#!/usr/bin/env python3
"""Mature Word Mode: best-effort preview content fallback behavioral tests.

Extracts the `resolveMatureByContent` helper verbatim from the real
`Card 1 - Front.template.anki` and runs it in Node against stubbed
AnkiConnect responses, asserting the duplicate-card resolution semantics:

  1. single candidate                    -> uses its interval (content-search)
  2. duplicate Expressions, distinct
     Sentences, DOM Sentence matches     -> picks the card with matching Sentence
  3. duplicate Expressions/Sentences,
     distinct cloze-body, DOM matches    -> picks the card with matching cloze-body
  4. ambiguous duplicates remain         -> null (fail safely, NEVER candidate 0)
  5. no Expression in DOM                -> null
  6. no findCards hits                   -> null

The exact current-card path (guiCurrentCard) is separate and authoritative;
this suite covers only the heuristic preview fallback.

Run directly:  python3 tests/test_mature_content.py
Wired into ./verify alongside the other suites. Skipped gracefully without Node.
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
NODE = shutil.which("node")

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


def load_helper():
    with open(FRONT, encoding="utf-8") as f:
        front = f.read()
    m = re.search(r"const resolveMatureExactCard = async .*?\n      \};\n\n      /\* --- MATURE WORD MODE: best-effort preview content fallback ---\n.*?const resolveMatureByContent = async .*?\n      \};\n", front, re.S)
    if not m:
        raise RuntimeError("mature-mode helpers not found in front template")
    fn = m.group(0)
    return re.sub(r"^      ", "", fn, flags=re.M)


HELPER = load_helper()

# (name, dom_expr, dom_sentence, dom_cloze_mid, cards, expected_interval_or_marker)
# cards = list of {Expression, Sentence, cloze-body, interval}
CASES = [
    (
        "single candidate uses its interval",
        "不公平", "世の中って不公平よね", "",
        [{"Expression": "不公平", "Sentence": "世の中って不公平よね", "cloze-body": "", "interval": 400}],
        "EXACT_400",
    ),
    (
        "duplicate Expression, DOM Sentence disambiguates",
        "不公平", "世の中って不公平よね", "",
        [
            {"Expression": "不公平", "Sentence": "別の文だよ", "cloze-body": "不公平", "interval": 10},
            {"Expression": "不公平", "Sentence": "世の中って不公平よね", "cloze-body": "不公平", "interval": 500},
        ],
        "EXACT_500",
    ),
    (
        "duplicate Expression/Sentence, cloze-body disambiguates",
        "不公平", "世の中って不公平よね", "不公平",
        [
            {"Expression": "不公平", "Sentence": "世の中って不公平よね", "cloze-body": "違う", "interval": 20},
            {"Expression": "不公平", "Sentence": "世の中って不公平よね", "cloze-body": "不公平", "interval": 800},
        ],
        "EXACT_800",
    ),
    (
        "ambiguous duplicates remain -> fail safely (never candidate 0)",
        "不公平", "世の中って不公平よね", "不公平",
        [
            {"Expression": "不公平", "Sentence": "世の中って不公平よね", "cloze-body": "不公平", "interval": 10},
            {"Expression": "不公平", "Sentence": "世の中って不公平よね", "cloze-body": "不公平", "interval": 900},
        ],
        "AMBIGUOUS",
    ),
    (
        "no Expression in DOM -> null",
        "", "", "",
        [{"Expression": "不公平", "Sentence": "", "cloze-body": "", "interval": 500}],
        "NONE",
    ),
    (
        "no findCards hits -> null",
        "不公平", "世の中って不公平よね", "",
        [],
        "NONE",
    ),
]

# Exact current-card retrieval tests.
# (name, dom_expr, guiCurrentCard_response, cardsInfo_for_current, expected_interval_or_marker)
# guiCurrentCard_response: dict with cardId + fields, or None (no review), or raises.
EXACT_CASES = [
    (
        "exact current-card path wins over any duplicate (Expression match)",
        "不公平",
        {"cardId": 1001, "fields": {"Expression": {"value": "不公平"}}},
        [{"interval": 720}],
        "EXACT_720",
    ),
    (
        "exact current-card path used even when duplicates share Expression",
        "不公平",
        {"cardId": 1002, "fields": {"Expression": {"value": "不公平"}}},
        [{"interval": 640}],
        "EXACT_640",
    ),
    (
        "no active review (guiCurrentCard null) -> falls through to null",
        "不公平",
        None,
        [],
        "NONE",
    ),
    (
        "current-card Expression mismatch throws -> no interval leaked",
        "不公平",
        {"cardId": 1003, "fields": {"Expression": {"value": "別の表現"}}},
        [{"interval": 999}],
        "MISMATCH",
    ),
]


def build_node_source(case):
    name, dom_expr, dom_sentence, dom_cloze_mid, cards, _ = case

    def card_js(c):
        expr = json.dumps(c["Expression"])
        sent = json.dumps(c["Sentence"])
        cloze = json.dumps(c["cloze-body"])
        return (
            "{ fields: {"
            f" Expression: {{ value: {expr} }},"
            f" Sentence: {{ value: {sent} }},"
            f" \"cloze-body\": {{ value: {cloze} }}"
            f" }}, interval: {c['interval']} }}"
        )

    cards_js = "[" + ", ".join(card_js(c) for c in cards) + "]"
    ids_js = "[" + ", ".join(str(i) for i in range(len(cards))) + "]"

    return f"""
const normText = (s) => String(s)
  .replace(/<br\\s*\\/?>/gi, ' ')
  .replace(/<[^>]+>/g, ' ')
  .replace(/&nbsp;/gi, ' ')
  .replace(/\\s+/g, ' ')
  .trim();
const escQuery = (s) => s.replace(/\\\\/g, '\\\\\\\\').replace(/"/g, '\\\\"').replace(/([*_])/g, '\\\\$1');

{HELPER}

const cards = {cards_js};
let findCount = 0;
const post = async (action, params) => {{
  if (action === 'findCards') {{ findCount++; return {ids_js}; }}
  if (action === 'cardsInfo') return cards;
  throw new Error('unexpected action ' + action);
}};

const expr = {{ innerText: {json.dumps(dom_expr)}, textContent: {json.dumps(dom_expr)} }};
const sent = {{ innerText: {json.dumps(dom_sentence)}, textContent: {json.dumps(dom_sentence)} }};
const clozeMid = {{ textContent: {json.dumps(dom_cloze_mid)} }};
const probe = {{
  querySelector(sel) {{
    if (sel === '.cloze-mid') return clozeMid;
    return null;
  }}
}};
const container = {{
  querySelector(sel) {{
    if (sel === '.front-word-display') return expr;
    if (sel === '.sentence-display') return sent;
    if (sel === '.cloze-probe') return probe;
    return null;
  }}
}};
resolveMatureByContent(container, post, normText, escQuery).then(r => {{
  console.log(JSON.stringify({{ interval: r && r.interval, source: r && r.source, findCount }}));
}}).catch(e => {{
  console.log(JSON.stringify({{ error: String(e && e.stack || e) }}));
}});
"""


def run_node(case):
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "mature.mjs")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_node_source(case))
        try:
            out = subprocess.run(
                [NODE, path],
                capture_output=True, text=True, timeout=30,
            )
        except subprocess.TimeoutExpired:
            return None
        if out.returncode != 0:
            return {"node_error": out.stderr.strip()[:500]}
        try:
            return json.loads(out.stdout.strip().splitlines()[-1])
        except json.JSONDecodeError:
            return {"parse_error": out.stdout.strip()[:500]}


def build_exact_node_source(case):
    name, dom_expr, current_resp, cards_info, _ = case

    if current_resp is None:
        current_js = "null"
    elif current_resp == "RAISE":
        current_js = "(() => { throw new Error('AnkiConnect wedged'); })()"
    else:
        current_js = json.dumps(current_resp)

    return f"""
const normText = (s) => String(s)
  .replace(/<br\\s*\\/?>/gi, ' ')
  .replace(/<[^>]+>/g, ' ')
  .replace(/&nbsp;/gi, ' ')
  .replace(/\\s+/g, ' ')
  .trim();
const escQuery = (s) => s.replace(/\\\\/g, '\\\\\\\\').replace(/"/g, '\\\\"').replace(/([*_])/g, '\\\\$1');

{HELPER}

const infos = {json.dumps(cards_info)};
const post = async (action, params) => {{
  if (action === 'guiCurrentCard') return {current_js};
  if (action === 'cardsInfo') return infos;
  throw new Error('unexpected action ' + action);
}};

resolveMatureExactCard(post, normText, {json.dumps(dom_expr)}).then(r => {{
  console.log(JSON.stringify({{ interval: r && r.interval, source: r && r.source }}));
}}).catch(e => {{
  console.log(JSON.stringify({{ error: String(e && e.message || e) }}));
}});
"""


def run_exact_node(case):
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "exact.mjs")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_exact_node_source(case))
        try:
            out = subprocess.run(
                [NODE, path],
                capture_output=True, text=True, timeout=30,
            )
        except subprocess.TimeoutExpired:
            return None
        if out.returncode != 0:
            return {"node_error": out.stderr.strip()[:500]}
        try:
            return json.loads(out.stdout.strip().splitlines()[-1])
        except json.JSONDecodeError:
            return {"parse_error": out.stdout.strip()[:500]}


def main():
    if not NODE:
        print("[SKIP] no Node found — mature-content fallback checks skipped")
        return 0

    for name, dom_expr, dom_sentence, dom_cloze, cards, expected in CASES:
        r = run_node((name, dom_expr, dom_sentence, dom_cloze, cards, expected))
        check(f"{name}: probe returned", r is not None)
        if not r:
            continue
        if "error" in r or "node_error" in r or "parse_error" in r:
            check(f"{name}: ran without errors", False, json.dumps(r))
            continue

        if expected == "NONE":
            check(f"{name}: returns null", r.get("interval") is None, json.dumps(r))
        elif expected == "AMBIGUOUS":
            check(f"{name}: returns null and marks ambiguous (never candidate 0)",
                  r.get("interval") is None and "ambiguous" in (r.get("source") or ""),
                  json.dumps(r))
        else:
            exp_ivl = int(expected.split("_")[1])
            check(f"{name}: selects the disambiguated card's interval ({exp_ivl})",
                  r.get("interval") == exp_ivl,
                  json.dumps(r))

    for name, dom_expr, current_resp, cards_info, expected in EXACT_CASES:
        r = run_exact_node((name, dom_expr, current_resp, cards_info, expected))
        check(f"{name}: probe returned", r is not None)
        if not r:
            continue
        if "node_error" in r or "parse_error" in r:
            check(f"{name}: ran without errors", False, json.dumps(r))
            continue

        if expected == "NONE":
            check(f"{name}: no interval leaked (null)", r.get("interval") is None, json.dumps(r))
        elif expected == "MISMATCH":
            check(f"{name}: expression mismatch never leaks another card's interval",
                  r.get("error") and "mismatch" in r.get("error", ""),
                  json.dumps(r))
        else:
            exp_ivl = int(expected.split("_")[1])
            check(f"{name}: uses exact current-card interval ({exp_ivl})",
                  r.get("interval") == exp_ivl,
                  json.dumps(r))

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())