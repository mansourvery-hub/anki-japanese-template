#!/usr/bin/env python3
"""Definition Compactor regression tests.

Extracts the `display:none` rules from section 6b of the REAL
`Card 1 - Style.css` and applies them (simulated via DOM removal) to the
fixtures in tests/fixtures/. This catches:
  - CSS regressions (selector typos, accidental scoping changes)
  - Yomitan markup drift (fixture updates from real mined cards)

Run directly:  python3 tests/test_compactor.py
Also wired as finish.sh step 0 (auto-skipped when this file is absent).

Dependencies: beautifulsoup4 + soupsieve (pure Python, no Anki needed).
"""
import os
import re
import sys

from bs4 import BeautifulSoup
import soupsieve as sv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSS = os.path.join(ROOT, "Card 1 - Style.css")
FIXTURES = os.path.join(HERE, "fixtures")

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}")
    if cond:
        PASS += 1
    else:
        FAIL += 1


def load_hide_selectors():
    """Pull every display:none rule from the 6b compactor section."""
    with open(CSS, encoding="utf-8") as f:
        css = f.read()
    # Anchor on the first rule's comment, not the section banner (the banner
    # comment wraps the "6b." marker itself and would leak header text).
    start = css.index("/* --- Collapse all dictionary entries after the first --- */")
    end = css.index("7. CIRCULAR AUDIO BUTTON")
    block = css[start:end]
    block = re.sub(r"/\*.*?\*/", "", block, flags=re.S)
    selectors = []
    for rule in re.findall(r"([^{}]+)\{[^{}]*display:\s*none[^{}]*\}", block):
        sel = " ".join(rule.split())
        if sel and not sel.startswith("@"):
            for part in sel.split(","):
                part = part.strip()
                if part:
                    selectors.append(part)
    if not selectors:
        raise RuntimeError("no compactor display:none rules found in CSS")
    return selectors


def visible_text(html):
    """Text after applying all hide rules (hidden subtrees removed)."""
    soup = BeautifulSoup(html, "html.parser")
    for sel in load_hide_selectors():
        for el in sv.select(sel, soup):
            el.decompose()
    return " ".join(soup.get_text().split())


def fixture(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as f:
        return f.read().strip()


def main():
    # --- 1. Verbatim Yomitan structured entry (大辞林 + 大辞泉) ---
    field = f'<div class="definition-box primary-definition">{fixture("yomitan_daijirin_daijisen.html")}</div>'
    out = visible_text(field)
    check("D1 headword kept (澄ます・清ます)", "澄ます" in out and "清ます" in out)
    check("D1 sense ① kept", "水などを濁りのない状態にする" in out)
    check("D1 sense ② kept", "雑念を払って、心を落ち着かせる" in out)
    check("D1 sense ③+ hidden", "一つのことに注意を向ける" not in out)
    check("D1 sense ④-⑨ hidden", "洗い清める" not in out and "道理を明らかにする" not in out)
    check("D1 sub-sense ㋐ hidden", "一心に…する" not in out)
    check("D1 補説G hidden", "に対する他動詞" not in out)
    check("D1 可能形 hidden", "すませる" not in out)
    check("D1 accent [2] hidden", "[2]" not in out)
    check("D2 (大辞泉) fully hidden", "汲み置いて井戸水を" not in out)
    check("D2 類語 commentary hidden", "類語" not in out)
    check("exactly 2 senses visible overall",
          out.count("。") <= 10 and "①" in out and "②" in out and "③" not in out)

    # --- 2. Plain-gloss dictionary (JMdict-style merged list) ---
    field = f'<div class="definition-box primary-definition">{fixture("yomitan_plain_gloss.html")}</div>'
    out = visible_text(field)
    check("plain: gloss 1 kept", "to clear up (a liquid)" in out)
    check("plain: gloss 2 kept", "to concentrate (attention)" in out)
    check("plain: gloss 3+ hidden", "to look unconcerned" not in out and "fifth gloss" not in out)
    check("plain: second dictionary hidden", "Proper name entry" not in out)

    # --- 3. Extended definition control (must be UNTOUCHED) ---
    ext = fixture("extended_definition_control.html")
    out = visible_text(ext)
    check("ext: third sense still visible", "THIS THIRD SENSE MUST REMAIN VISIBLE." in out)
    check("ext: second dictionary still visible", "SECOND DICTIONARY MUST REMAIN VISIBLE." in out)

    # --- 4. Scope guard: selectors must all be prefixed .primary-definition ---
    leaked = [s for s in load_hide_selectors() if not s.startswith(".primary-definition")]
    check("all hide rules scoped to .primary-definition", not leaked)

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
