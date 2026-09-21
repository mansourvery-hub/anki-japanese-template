This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where line numbers have been added.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: chat_history/**, conversations/**, Card 1 - Front.template.anki.*, backups/**, dist/**, reports/**, **/__pycache__/**, **/.ruff_cache/**, .anki_fields.json, repomix-output.*, repomix.md, *.apkg
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Line numbers have been added to the beginning of each line
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
````
.github/
  workflows/
    verify.yml
docs/
  adr/
    001-mature-word-mode-interval.md
    002-definition-compactor-css.md
    003-native-audio-delegation.md
    004-single-command-release.md
tests/
  fixtures/
    extended_definition_control.html
    yomitan_daijirin_daijisen.html
    yomitan_dict_label.html
    yomitan_plain_gloss.html
  test_back_more.py
  test_compactor.py
  test_front_modes.py
  test_layout.py
  test_mature_content.py
  test_templates.py
.gitignore
.opencodeignore
AGENTS.md
ARCHITECTURE.md
Card 1 - Back.template.anki
Card 1 - Front.template.anki
Card 1 - Style.css
fetch_anki_fields.py
finish.sh
fix_summary.md
HANDOFF.md
IMPLEMENTATION_PLAN.md
MVP.md
PRODUCT.md
QUALITY.md
README.md
release_apkg.py
sync_to_anki.py
TEST_STRATEGY.md
verify
````

# Files

## File: tests/fixtures/extended_definition_control.html
````html
1: <div class="extended-def-content"><div class="yomitan-glossary"><ol><li data-dictionary="大辞林　第四版"><span><div data-sc-name="語義G">①水などを濁りのない状態にする。</div><div data-sc-name="語義G">②雑念を払って、心を落ち着かせる。</div><div data-sc-name="語義G">③THIS THIRD SENSE MUST REMAIN VISIBLE.</div></span></li><li data-dictionary="大辞泉 第二版"><span>SECOND DICTIONARY MUST REMAIN VISIBLE.</span></li></ol></div></div>
````

## File: tests/fixtures/yomitan_daijirin_daijisen.html
````html
1: <div style="text-align: left;" class="yomitan-glossary"><ol><li data-dictionary="大辞林　第四版"><span><span data-sc-name="見出部"><span data-sc-name="見出仮名" lang="ja" style="font-weight: bold;">すま<span data-sc-name="活用分節" lang="ja">・</span>す</span><span data-sc-name="アクセントG" style="font-size: 0.7em; vertical-align: super; margin-left: 0.25em; margin-right: 0.25em;"><span data-sc-name="アクセント"><span data-sc-name="accent">[2]</span></span></span><span data-sc-name="表記G" lang="ja">【<span data-sc-name="標準表記" lang="ja">澄ます</span>・<span data-sc-name="標準表記" lang="ja"><ruby lang="ja">清<rt>▽</rt></ruby>ます</span>】</span></span><div data-sc-name="解説部"><div data-sc-name="大語義"><span data-sc-name="品詞G"><span data-sc-name="品詞subG" lang="ja">（<span data-sc-name="品詞" lang="ja">動<span data-sc-name="品詞行" lang="ja" style="font-size: 0.6em; vertical-align: super;">(サ)</span><span data-sc-name="品詞活用" lang="ja">五</span>［<span data-sc-name="品詞活用" lang="ja">四</span>］</span>）</span></span><div data-sc-name="準大語義"><div data-sc-name="中語義"><div data-sc-name="語義G"><span data-sc-name="語義Gnum">①</span><span data-sc-name="語釈" lang="ja">水などを濁りのない状態にする。</span><div data-sc-name="用例" lang="ja">「水を<span data-sc-name="語幹相当部">━</span><span data-sc-name="活用分節" lang="ja">・</span>す」</div></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">②</span><span data-sc-name="語釈" lang="ja">雑念を払って、心を落ち着かせる。</span><div data-sc-name="用例" lang="ja">「心を<span data-sc-name="語幹相当部">━</span><span data-sc-name="活用分節" lang="ja">・</span>して字を書く」</div></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">③</span><span data-sc-name="語釈" lang="ja">一つのことに注意を向ける。</span><div data-sc-name="用例" lang="ja">「耳を<span data-sc-name="語幹相当部">━</span><span data-sc-name="活用分節" lang="ja">・</span>す」</div></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">④</span><span data-sc-name="語釈" lang="ja">曇りを取り去って、さえた状態にする。</span></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">⑤</span><span data-sc-name="語釈" lang="ja">（自動詞的に用いて）よそ行きの表情やそぶりをする。そんなことにはかかわりがないという表情やそぶりをする。</span></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">⑥</span><span data-sc-name="語釈" lang="ja">（動詞の連用形の下に付いて）</span><div data-sc-name="副義"><span data-sc-name="副義num">㋐</span><span data-sc-name="語釈" lang="ja">一心に…する。</span></div><div data-sc-name="副義"><span data-sc-name="副義num">㋑</span><span data-sc-name="語釈" lang="ja">すっかり…する。完全に…する。</span></div></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">⑦</span><span data-sc-name="語釈" lang="ja">洗い清める。</span></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">⑧</span><span data-sc-name="語釈" lang="ja">世の中が平安になるようにする。鎮定する。</span></div><div data-sc-name="語義G"><span data-sc-name="語義Gnum">⑨</span><span data-sc-name="語釈" lang="ja">道理を明らかにする。是非をはっきりさせる。</span></div><div data-sc-name="補説G" lang="ja">〔<span data-sc-name="補説" lang="ja">「澄む」に対する他動詞</span>〕</div></div></div><span data-sc-name="可能形" lang="ja"><span style="vertical-align: text-bottom; margin-right: 0.25em;"><a target="_blank" rel="noreferrer noopener" href="yomitan_dictionary_media_0e7fe8030ce28701453a0080c9fde387d235b663.svg" style="cursor:inherit;display:inline-block;position:relative;line-height:1;max-width:100%;color:inherit;"><span title="可能" style="display:inline-block;white-space:nowrap;max-width:100%;max-height:100vh;position:relative;vertical-align:top;line-height:0;overflow:hidden;font-size:1px;font-size:1em;width: 2em;"><span style="display:inline-block;width:0;vertical-align:top;font-size:0;padding-top: 50%;"></span><span style="--image:none;position:absolute;left:0;top:0;width:100%;height:100%;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center center;-webkit-mask-mode:alpha;-webkit-mask-size:contain;-webkit-mask-image:var(--image);mask-repeat:no-repeat;mask-position:center center;mask-mode:alpha;mask-size:contain;mask-image:var(--image);background-color:currentColor;--image: url(&quot;yomitan_dictionary_media_0e7fe8030ce28701453a0080c9fde387d235b663.svg&quot;);"></span><span style="position:absolute;left:0;top:0;width:100%;height:100%;font-size:calc(1em * var(--font-size-no-units));line-height:var(--line-height);display:table;table-layout:fixed;white-space:normal;color:var(--text-color-light3);"></span><img width="70" height="35" src="yomitan_dictionary_media_0e7fe8030ce28701453a0080c9fde387d235b663.svg" style="display:inline-block;vertical-align:top;object-fit:contain;border:none;outline:none;position:absolute;left:0;top:0;width:100%;height:100%;--shadow-settings:0 0 0.01px var(--text-color);filter:grayscale(1) opacity(0.5) drop-shadow(var(--shadow-settings)) drop-shadow(var(--shadow-settings)) saturate(1000%) brightness(1000%);opacity:0;width: 100%; height: 100%;"></span><span style="display:none;line-height:var(--line-height);">Image</span></a></span>すませる</span></div></div></span></li><style>.yomitan-glossary ul[data-sc-content="glossary"] > li:not(:first-child)::before { white-space: pre-wrap; content: " | "; display: inline; color: rgb(119, 119, 119); }
2: .yomitan-glossary ul[data-sc-content="glossary"] > li { display: inline; }
3: .yomitan-glossary ul[data-sc-content="glossary"] { display: inline; list-style: none; padding-left: 0px; }</style><li data-dictionary="大辞泉 第二版"><span><span data-sc-html="" data-sc-lang="ja" data-sc-hmhtml="2" data-sc-xmlns="http://www.w3.org/1999/xhtml"><span data-sc-body=""><div data-sc-contents="" data-sc-xmlns=""><div data-sc見出-g=""><span data-sc-headword="" data-sc見出="" data-sc-class="見出"><span lang="ja">すま</span><span data-sc-hdot=""><span lang="ja">・</span></span><span lang="ja">す</span></span><span data-sc-headword="" data-sc表記="" data-sc-class="表記"><span lang="ja">【澄ます</span><span data-sc-hyoki-s=""><span>┊</span></span><span data-sc-a="" data-sc-href="$jo"><span data-sc常外音訓-m=""><span>▽</span></span></span><span lang="ja">清ます】</span></span><div data-sc-m-accent-audio-g=""><span data-sc-a="" data-sc-href="$c-accent"><span data-sc補足ロゴ-g=""><span data-sc補足ロゴ=""><span lang="ja">アクセント</span></span></span></span><span lang="ja"> すま</span><span data-sc-m-accent-m=""><span>↓</span></span><span lang="ja">す </span><span data-sc-a="" data-sc-href="s00003432.aac"><span data-sc-img="" data-sc-audio="" data-sc-class="audio" data-sc-src="Audio.png"></span></span></div></div><div data-sc解説-g=""><div data-sc-m-g="" data-sc-id=""><div data-sc-meaning=""><span data-sc-hinshi=""><span lang="ja">〘</span><span data-sc-a="" data-sc-href="$hi"><span lang="ja">動サ五（四）</span></span><span lang="ja">〙</span></span></div></div><div data-sc-m-g="" data-sc-l3="" data-sc-id="196552-C001" data-sc-class="L3"><div data-sc-meaning=""><span data-sc-a="" data-sc-href="$g"><span data-sc-rect="" data-sc-l3="" data-sc-bold="" data-sc-f-m="" data-sc-class="L3 bold FM"><span>1</span></span></span><span lang="ja">液体の、にごり・よごれなどの不純物を除いて透き通った状態にする。</span><span data-sc-ex-g="" data-sc-id="196552-5001"><span lang="ja">「汲み置いて井戸水を―・す」</span></span></div></div><div data-sc-m-g="" data-sc-l3-a="" data-sc-id="196552-C002" data-sc-class="L3A"><div data-sc-meaning=""><span data-sc-a="" data-sc-href="$g"><span data-sc-rect="" data-sc-l3="" data-sc-bold="" data-sc-f-m="" data-sc-class="L3 bold FM"><span>2</span></span></span><span lang="ja">気持ちを落ち着かせて雑念のない状態にする。</span><span data-sc-ex-g="" data-sc-id="196552-5002"><span lang="ja">「座禅を組んで心を―・す」</span></span></div></div><div data-sc-m-g="" data-sc-l3-a="" data-sc-id="196552-C003" data-sc-class="L3A"><div data-sc-meaning"><span lang="ja">3 耳・目に注意を集中する。</span></div></div><div data-sc-m-g="" data-sc-l3-a="" data-sc-id="196552-C004" data-sc-class="L3A"><div data-sc-meaning"><span>4 平然と構える。</span></div></div><div data-sc-m-g="" data-sc-l3-a="" data-sc-id="196552-C005" data-sc-class="L3A"><div data-sc-meaning"><span>5 洗い清める。</span></div></div><div data-sc-m-g="" data-sc-l3-a="" data-sc-id="196552-C007" data-sc-class="L3A"><div data-sc-meaning"><span>6 平定する。</span></div></div><div data-sc-m-g="" data-sc-l3-a="" data-sc-id="196552-C008" data-sc-class="L3A"><div data-sc-meaning"><span>7 完全に…する。</span></div></div><div data-sc-m-g="" data-sc-id=""><div data-sc-meaning="" data-sc-c="" data-sc-class="C"><span>可能 すませる</span></div><div data-sc-meaning="" data-sc-c="" data-sc-class="C"><span>類語 澄む・冴える…</span></div></div></div></span></span></span></li></ol></div>
````

## File: tests/fixtures/yomitan_dict_label.html
````html
1: <div style="text-align: center;" class="yomitan-glossary"><ol><li data-dictionary="大辞林　第四版"><i>(大辞林　第四版)</i> <span><span data-sc-name="見出部"><span data-sc-name="見出仮名" lang="ja" style="font-weight: bold;">かい<span data-sc-name="語構成" style="margin-right: 0.5em;"></span>しゃ</span><span data-sc-name="歴史仮名" lang="ja" style="font-size: 0.6em;">(くわい—)</span><span data-sc-name="アクセントG" style="font-size: 0.7em; vertical-align: super; margin-left: 0.25em; margin-right: 0.25em;"><span data-sc-name="アクセント"><span data-sc-name="accent">[0]</span></span></span><span data-sc-name="表記G" lang="ja">【<span data-sc-name="標準表記" lang="ja">会社</span>】</span></span><div data-sc-name="解説部"><div data-sc-name="大語義"><div data-sc-name="準大語義"><div data-sc-name="中語義"><div data-sc-name="語義G"><span data-sc-name="語義Gnum">①</span><span data-sc-name="語釈" lang="ja">営利を目的とする社団法人で、会社法による株式会社・合名会社・合資会社・合同会社の総称。</span></div></div></div></div></div></span></li><li data-dictionary="大辞林　第四版"><i>(子, 大辞林　第四版)</i> <ul><li><span><a href="#"><span lang="ja">会社員</span></a></span></li></ul></li></ol></div>
````

## File: tests/fixtures/yomitan_plain_gloss.html
````html
1: <div class="yomitan-glossary"><ol><li data-dictionary="JMdict"><span><div data-sc-headword="澄ます">澄ます</div><ul data-sc-content="glossary"><li>to clear up (a liquid); to make clear</li><li>to concentrate (attention); to clear (one's mind)</li><li>to look unconcerned; to put on a serious look</li><li>to make clean; to purify</li><li>fifth gloss that must be hidden</li></ul></span></li><li data-dictionary="JMnedict"><span>Proper name entry that must be hidden entirely</span></li></ol></div>
````

## File: release_apkg.py
````python
 1: #!/usr/bin/env python3
 2: """Export the sample deck to dist/anki-japanese-template.apkg via Anki-Connect.
 3: 
 4: Called by finish.sh; can also be run standalone. The real Anki-Connect action
 5: is `exportPackage` (params: deck, path, includeSched). The apkg is gitignored
 6: (`*.apkg` in .gitignore) — it is distributed via GitHub Releases, never the
 7: repo itself.
 8: """
 9: import os
10: import sys
11: import json
12: import urllib.request
13: import urllib.error
14: 
15: ANKI_CONNECT_URL = "http://127.0.0.1:8765"
16: DECK_NAME = "My Life Decks::Japanese::anki-japanese-template"
17: SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
18: EXPORT_PATH = os.path.join(SCRIPT_DIR, "dist", "anki-japanese-template.apkg")
19: 
20: 
21: def main() -> int:
22:     os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)
23:     payload = {
24:         "action": "exportPackage",
25:         "version": 6,
26:         "params": {"deck": DECK_NAME, "path": EXPORT_PATH, "includeSched": False},
27:     }
28:     
29:     req = urllib.request.Request(
30:         ANKI_CONNECT_URL,
31:         data=json.dumps(payload).encode("utf-8"),
32:         headers={"Content-Type": "application/json"},
33:     )
34:     
35:     try:
36:         with urllib.request.urlopen(req, timeout=180) as response:
37:             result = json.loads(response.read().decode("utf-8"))
38:     except urllib.error.URLError:
39:         print("ERROR: cannot reach Anki-Connect (is Anki running with the add-on?)")
40:         return 1
41:     except Exception as e:
42:         print(f"ERROR: export request failed: {e}")
43:         return 1
44: 
45:     if result.get("error") or not result.get("result"):
46:         print(f"ERROR: Anki-Connect export failed: {result.get('error') or 'unknown error'}")
47:         return 1
48: 
49:     if not os.path.isfile(EXPORT_PATH) or os.path.getsize(EXPORT_PATH) == 0:
50:         print(f"ERROR: expected export missing or empty: {EXPORT_PATH}")
51:         return 1
52: 
53:     print(f"Export OK: {EXPORT_PATH} ({os.path.getsize(EXPORT_PATH) / 1e6:.1f} MB)")
54:     return 0
55: 
56: 
57: if __name__ == "__main__":
58:     sys.exit(main())
````

## File: .github/workflows/verify.yml
````yaml
 1: name: verify
 2: 
 3: on:
 4:   push:
 5:   pull_request:
 6: 
 7: jobs:
 8:   verify:
 9:     runs-on: ubuntu-latest
10:     steps:
11:       - uses: actions/checkout@v4
12:       - uses: actions/setup-python@v5
13:         with:
14:           python-version: "3.x"
15:       - name: Install test-only deps (compactor)
16:         run: pip install beautifulsoup4 soupsieve
17:       - name: Run local quality gate
18:         run: ./verify
````

## File: docs/adr/002-definition-compactor-css.md
````markdown
 1: # ADR 002 — Definition Compactor as structural CSS
 2: 
 3: ## Context
 4: 
 5: Yomitan mines the full multi-dictionary gloss into `Definition`, far too
 6: verbose for the main card, while `Extended definition` must stay complete.
 7: 
 8: ## Options considered
 9: 
10: 1. Trim at mining time (Yomitan settings/handlers) — fragile per-dictionary,
11:    lost on re-mine.
12: 2. Trim in JS at render time — flash of full text, more failure modes.
13: 3. **Structural CSS hiding (chosen).**
14: 
15: ## Decision
16: 
17: CSS §6b collapses to the first dictionary, ≤2 senses, no appendices, matched
18: on structure (`data-sc-*`, glossary lists) — never dictionary names — and
19: scoped strictly to `.primary-definition`.
20: 
21: ## Consequences
22: 
23: Dictionary-agnostic and flash-free; Yomitan markup drift is caught by
24: `test_compactor.py` fixtures taken from real mined cards.
````

## File: tests/test_back_more.py
````python
  1: #!/usr/bin/env python3
  2: """Back More-section lazy extended definition + prune behavior tests.
  3: 
  4: Extracts toggleMore / initSecondarySection / pruneCompactedGlossary verbatim
  5: from the real `Card 1 - Back.template.anki` and runs them in headless Chrome:
  6: 
  7:   1. lazy: template content stays out of the DOM until first More open,
  8:      then stamps into its host exactly once.
  9:   2. cleanup keeps More alive when the template is the only content.
 10:   3. cleanup removes More + toggle when the section is truly empty.
 11:   4. prune: fixture glossary compacts to the same visible text as CSS §6b
 12:      (①② kept, ③+ hidden) while shrinking the live DOM.
 13: 
 14: Run directly:  python3 tests/test_back_more.py
 15: Wired into ./verify alongside the other suites. Skipped gracefully
 16: without Chrome.
 17: """
 18: import os
 19: import re
 20: import shutil
 21: import subprocess
 22: import sys
 23: import tempfile
 24: 
 25: HERE = os.path.dirname(os.path.abspath(__file__))
 26: ROOT = os.path.dirname(HERE)
 27: BACK = os.path.join(ROOT, "Card 1 - Back.template.anki")
 28: FIXTURE = os.path.join(HERE, "fixtures", "yomitan_daijirin_daijisen.html")
 29: CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")
 30: 
 31: PASS = 0
 32: FAIL = 0
 33: 
 34: 
 35: def check(name, cond, detail=""):
 36:     global PASS, FAIL
 37:     tag = "PASS" if cond else "FAIL"
 38:     print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
 39:     if cond:
 40:         PASS += 1
 41:     else:
 42:         FAIL += 1
 43: 
 44: 
 45: def load_functions():
 46:     """Extract the three window.* functions verbatim from the back template."""
 47:     with open(BACK, encoding="utf-8") as f:
 48:         back = f.read()
 49:     funcs = {}
 50:     for name in ("toggleMore", "initSecondarySection", "pruneCompactedGlossary"):
 51:         m = re.search(r"window\.%s = function.*?^\s{4}\};" % name, back, re.S | re.M)
 52:         if not m:
 53:             raise RuntimeError(f"{name} not found in back template")
 54:         funcs[name] = m.group(0)
 55:     return funcs
 56: 
 57: 
 58: def build_html(funcs, more_inner, def_inner=""):
 59:     return f"""<!doctype html><html><head><meta charset="utf-8"></head><body>
 60: <div class="card-wrapper back-card"><div class="card-container">
 61: <div class="definition-box primary-definition">{def_inner}</div>
 62: <div class="more-section" hidden>{more_inner}</div>
 63: <button type="button" class="more-toggle" aria-expanded="false">More</button>
 64: </div></div>
 65: <script>
 66: var report = {{}};
 67: try {{
 68: {funcs['toggleMore']}
 69: {funcs['initSecondarySection']}
 70: {funcs['pruneCompactedGlossary']}
 71: window.initSecondarySection();
 72: window.pruneCompactedGlossary();
 73: var section = document.querySelector('.more-section');
 74: var btn = document.querySelector('.more-toggle');
 75: report.moreAlive = !!(section && section.parentNode);
 76: report.btnAlive = !!(btn && btn.parentNode);
 77: var host = document.querySelector('.extended-full');
 78: report.hostKids = host ? host.childNodes.length : -1;
 79: report.hostHidden = host ? host.hasAttribute('hidden') : null;
 80: if (btn && report.moreAlive) window.toggleMore(btn);
 81: var host2 = document.querySelector('.extended-full');
 82: report.stamped = host2 ? host2.textContent : null;
 83: report.tplGone = document.querySelector('template.extended-full-tpl') === null;
 84: report.expanded = btn ? btn.getAttribute('aria-expanded') : null;
 85: var def = document.querySelector('.primary-definition');
 86: report.defText = def ? def.textContent : '';
 87: report.defNodes = def ? def.querySelectorAll('*').length : -1;
 88: if (btn && report.moreAlive) window.toggleMore(btn);
 89: var stillEl = document.querySelector('.extended-full');
 90: report.stillStamped = stillEl ? stillEl.textContent : null;
 91: }} catch(e) {{ report.err = String(e && e.stack || e); }}
 92: document.title = 'X' + JSON.stringify(report) + 'X';
 93: </scr""" + "ipt></body></html>"
 94: 
 95: 
 96: def render(html):
 97:     import json as _json
 98:     with tempfile.TemporaryDirectory() as td:
 99:         path = os.path.join(td, "back.html")
100:         with open(path, "w", encoding="utf-8") as f:
101:             f.write(html)
102:         try:
103:             out = subprocess.run(
104:                 [CHROME, "--headless=new", "--disable-gpu",
105:                  "--no-sandbox", "--hide-scrollbars",
106:                  "--window-size=412,892",
107:                  "--virtual-time-budget=1500",
108:                  "--dump-dom", f"file://{path}"],
109:                 capture_output=True, text=True, timeout=60,
110:             ).stdout
111:         except subprocess.TimeoutExpired:
112:             return None
113:     m = re.search(r"<title>X(.*?)X</title>", out, re.S)
114:     if not m:
115:         return None
116:     try:
117:         return _json.loads(m.group(1))
118:     except ValueError:
119:         return None
120: 
121: 
122: def main():
123:     if not CHROME:
124:         print("[SKIP] no headless Chrome found — back-more checks skipped")
125:         return 0
126:     funcs = load_functions()
127:     fixture = open(FIXTURE, encoding="utf-8").read()
128: 
129:     # Case 1: template + one text block → lazy stamp on open, kept section.
130:     more = ('<div class="html-content secondary-block">ctx</div>'
131:             '<div class="extended-def-wrapper"><div class="extended-def-header">x</div>'
132:             '<template class="extended-full-tpl"><div>LAZY-EXTENDED-MARKER</div></template>'
133:             '<div class="html-content secondary-block extended-full" data-lazy hidden></div></div>')
134:     r = render(build_html(funcs, more))
135:     check("lazy More: probe returned", r is not None)
136:     if r:
137:         check("lazy More: ran without errors", "err" not in r, r.get("err", ""))
138:         check("lazy More: host empty before open", r.get("hostKids") == 0, str(r))
139:         check("lazy More: stamped on first open", (r.get("stamped") or "").strip() == "LAZY-EXTENDED-MARKER", str(r))
140:         check("lazy More: template consumed + toggle opened",
141:               r.get("tplGone") is True and r.get("expanded") == "true", str(r))
142:         check("lazy More: second toggle keeps stamped content",
143:               (r.get("stillStamped") or "").strip() == "LAZY-EXTENDED-MARKER", str(r))
144: 
145:     # Case 2: template is the ONLY content → More survives cleanup.
146:     more_only = ('<div class="extended-def-wrapper"><div class="extended-def-header">x</div>'
147:                  '<template class="extended-full-tpl"><div>ONLY</div></template>'
148:                  '<div class="html-content secondary-block extended-full" data-lazy hidden></div></div>')
149:     r = render(build_html(funcs, more_only))
150:     check("template-only More: probe returned", r is not None)
151:     if r:
152:         check("template-only More: section + toggle survive", r.get("moreAlive") and r.get("btnAlive"), str(r))
153:         check("template-only More: stamps on open", (r.get("stamped") or "").strip() == "ONLY", str(r))
154: 
155:     # Case 3: truly empty section → More + toggle removed.
156:     r = render(build_html(funcs, '<div class="html-content secondary-block">   </div>'))
157:     check("empty More: probe returned", r is not None)
158:     if r:
159:         check("empty More: section + toggle self-remove",
160:               r.get("moreAlive") is False and r.get("btnAlive") is False, str(r))
161: 
162:     # Case 4: prune compacts the real fixture in a real browser.
163:     r = render(build_html(funcs, '<div class="html-content secondary-block">ctx</div>', fixture))
164:     check("prune: probe returned", r is not None)
165:     if r:
166:         check("prune: ran without errors", "err" not in r, r.get("err", ""))
167:         t = r.get("defText", "")
168:         check("prune: senses ①② kept", "水などを濁りのない状態にする" in t and "雑念を払って" in t, t[:120])
169:         check("prune: sense ③+ gone", "一つのことに注意を向ける" not in t, t[:120])
170:         check("prune: 2nd dictionary gone", "汲み置いて井戸水を" not in t, t[:120])
171:         check("prune: live DOM shrunk (< 612 nodes)", 0 < r.get("defNodes", 9999) < 612, str(r.get("defNodes")))
172: 
173:     print()
174:     print(f"{PASS} passed, {FAIL} failed")
175:     return 1 if FAIL else 0
176: 
177: 
178: if __name__ == "__main__":
179:     sys.exit(main())
````

## File: tests/test_compactor.py
````python
  1: #!/usr/bin/env python3
  2: """Definition Compactor regression tests.
  3: 
  4: Extracts the `display:none` rules from section 6b of the REAL
  5: `Card 1 - Style.css` and applies them (simulated via DOM removal) to the
  6: fixtures in tests/fixtures/. This catches:
  7:   - CSS regressions (selector typos, accidental scoping changes)
  8:   - Yomitan markup drift (fixture updates from real mined cards)
  9: 
 10: Run directly:  python3 tests/test_compactor.py
 11: Also wired as finish.sh step 0 (auto-skipped when this file is absent).
 12: 
 13: Dependencies: beautifulsoup4 + soupsieve (pure Python, no Anki needed).
 14: """
 15: import os
 16: import re
 17: import sys
 18: 
 19: from bs4 import BeautifulSoup
 20: import soupsieve as sv
 21: 
 22: HERE = os.path.dirname(os.path.abspath(__file__))
 23: ROOT = os.path.dirname(HERE)
 24: CSS = os.path.join(ROOT, "Card 1 - Style.css")
 25: FIXTURES = os.path.join(HERE, "fixtures")
 26: 
 27: PASS = 0
 28: FAIL = 0
 29: 
 30: 
 31: def check(name, cond):
 32:     global PASS, FAIL
 33:     tag = "PASS" if cond else "FAIL"
 34:     print(f"[{tag}] {name}")
 35:     if cond:
 36:         PASS += 1
 37:     else:
 38:         FAIL += 1
 39: 
 40: 
 41: def load_hide_selectors():
 42:     """Pull every display:none rule from the 6b compactor section."""
 43:     with open(CSS, encoding="utf-8") as f:
 44:         css = f.read()
 45:     # Anchor on the first rule's comment, not the section banner (the banner
 46:     # comment wraps the "6b." marker itself and would leak header text).
 47:     start = css.index("/* --- Collapse all dictionary entries after the first --- */")
 48:     end = css.index("7. CIRCULAR AUDIO BUTTON")
 49:     block = css[start:end]
 50:     block = re.sub(r"/\*.*?\*/", "", block, flags=re.S)
 51:     selectors = []
 52:     for rule in re.findall(r"([^{}]+)\{[^{}]*display:\s*none[^{}]*\}", block):
 53:         sel = " ".join(rule.split())
 54:         if sel and not sel.startswith("@"):
 55:             for part in sel.split(","):
 56:                 part = part.strip()
 57:                 if part:
 58:                     selectors.append(part)
 59:     if not selectors:
 60:         raise RuntimeError("no compactor display:none rules found in CSS")
 61:     return selectors
 62: 
 63: 
 64: def visible_text(html):
 65:     """Text after applying all hide rules (hidden subtrees removed)."""
 66:     soup = BeautifulSoup(html, "html.parser")
 67:     for sel in load_hide_selectors():
 68:         for el in sv.select(sel, soup):
 69:             el.decompose()
 70:     return " ".join(soup.get_text().split())
 71: 
 72: 
 73: def fixture(name):
 74:     with open(os.path.join(FIXTURES, name), encoding="utf-8") as f:
 75:         return f.read().strip()
 76: 
 77: 
 78: def apply_prune(html):
 79:     """Mirror of Back's pruneCompactedGlossary (BLOAT-01A): remove exactly
 80:     what the §6b hide rules hide. Grouped per parent like CSS `~`."""
 81:     soup = BeautifulSoup(html, "html.parser")
 82:     for box in sv.select(".primary-definition", soup):
 83:         for sel, keep in [
 84:             (".yomitan-glossary > ol > li", 1),
 85:             ('div[data-sc-name="語義G"]', 2),
 86:             ("div[data-sc-l3]", 2),
 87:             ("div[data-sc-l3-a]", 1),
 88:             ('[data-sc-content="glossary"] > li', 2),
 89:         ]:
 90:             groups = {}
 91:             for el in sv.select(sel, box):
 92:                 groups.setdefault(id(el.parent), []).append(el)
 93:             for group in groups.values():
 94:                 for el in group[keep:]:
 95:                     el.decompose()
 96:         for el in box.select(
 97:             'div[data-sc-name="補説G"], span[data-sc-name="可能形"], '
 98:             'span[data-sc-name="歴史仮名"], span[data-sc-name="アクセントG"], '
 99:             'li[data-sc-content="forms"], div[data-sc-content="attribution"], i'
100:         ):
101:             el.decompose()
102:     return soup
103: 
104: 
105: def main():
106:     # --- 1. Verbatim Yomitan structured entry (大辞林 + 大辞泉) ---
107:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_daijirin_daijisen.html")}</div>'
108:     out = visible_text(field)
109:     check("D1 headword kept (澄ます・清ます)", "澄ます" in out and "清ます" in out)
110:     check("D1 sense ① kept", "水などを濁りのない状態にする" in out)
111:     check("D1 sense ② kept", "雑念を払って、心を落ち着かせる" in out)
112:     check("D1 sense ③+ hidden", "一つのことに注意を向ける" not in out)
113:     check("D1 sense ④-⑨ hidden", "洗い清める" not in out and "道理を明らかにする" not in out)
114:     check("D1 sub-sense ㋐ hidden", "一心に…する" not in out)
115:     check("D1 補説G hidden", "に対する他動詞" not in out)
116:     check("D1 可能形 hidden", "すませる" not in out)
117:     check("D1 accent [2] hidden", "[2]" not in out)
118:     check("D2 (大辞泉) fully hidden", "汲み置いて井戸水を" not in out)
119:     check("D2 類語 commentary hidden", "類語" not in out)
120:     check("exactly 2 senses visible overall",
121:           out.count("。") <= 10 and "①" in out and "②" in out and "③" not in out)
122: 
123:     # --- 2. Plain-gloss dictionary (JMdict-style merged list) ---
124:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_plain_gloss.html")}</div>'
125:     out = visible_text(field)
126:     check("plain: gloss 1 kept", "to clear up (a liquid)" in out)
127:     check("plain: gloss 2 kept", "to concentrate (attention)" in out)
128:     check("plain: gloss 3+ hidden", "to look unconcerned" not in out and "fifth gloss" not in out)
129:     check("plain: second dictionary hidden", "Proper name entry" not in out)
130: 
131:     # --- 2b. Dictionary labels / sub-entries (会社 sample) ---
132:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_dict_label.html")}</div>'
133:     out = visible_text(field)
134:     check("label: <i>(大辞林　第四版)</i> hidden", "(大辞林　第四版)" not in out)
135:     check("label: sub-entry <i>(子, ...)</i> hidden", "(子," not in out)
136:     check("label: sub-entry word 会社員 hidden", "会社員" not in out)
137:     check("label: headword kept", "会社" in out)
138:     check("label: sense kept", "営利を目的とする社団法人" in out)
139: 
140:     # --- 2c. Extended-definition FALLBACK box (when Definition is absent)
141:     #     must be compacted identically (it also carries primary-definition) ---
142:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_dict_label.html")}</div>'
143:     out_fallback = visible_text(field)
144:     check("fallback: compacted like main Definition",
145:           "(大辞林　第四版)" not in out_fallback and "会社員" not in out_fallback
146:           and "営利を目的とする社団法人" in out_fallback)
147: 
148:     # --- 3. Extended definition control (must be UNTOUCHED) ---
149:     ext = fixture("extended_definition_control.html")
150:     out = visible_text(ext)
151:     check("ext: third sense still visible", "THIS THIRD SENSE MUST REMAIN VISIBLE." in out)
152:     check("ext: second dictionary still visible", "SECOND DICTIONARY MUST REMAIN VISIBLE." in out)
153: 
154:     # --- 4. Scope guard: selectors must all be prefixed .primary-definition ---
155:     leaked = [s for s in load_hide_selectors() if not s.startswith(".primary-definition")]
156:     check("all hide rules scoped to .primary-definition", not leaked)
157: 
158:     # --- 5. Prune mirror (BLOAT-01A): JS removal == CSS hiding, per fixture ---
159:     for name in ("yomitan_daijirin_daijisen.html", "yomitan_plain_gloss.html",
160:                  "yomitan_dict_label.html"):
161:         field = f'<div class="definition-box primary-definition">{fixture(name)}</div>'
162:         css_only = visible_text(field)
163:         pruned = apply_prune(field)
164:         leftover = [s for s in load_hide_selectors() if sv.select(s, pruned)]
165:         check(f"prune removes everything CSS would hide ({name})", not leftover)
166:         check(f"prune preserves visible text ({name})",
167:               visible_text(str(pruned)) == css_only)
168: 
169:     print()
170:     print(f"{PASS} passed, {FAIL} failed")
171:     return 1 if FAIL else 0
172: 
173: 
174: if __name__ == "__main__":
175:     sys.exit(main())
````

## File: .opencodeignore
````
1: logs/transcripts/**
2: .opencode/transcripts/**
3: *.md.log
````

## File: HANDOFF.md
````markdown
  1: # HANDOFF — build these features on top of the reverted baseline
  2: 
  3: You are continuing on the **reverted working baseline**: commit `59ac56f`
  4: (HEAD, tagged `v1.8.2`, CSS header `v1.7.6`). `main` == `v1.8.2` == `59ac56f`.
  5: The repo's methodology lives in `PRODUCT.md` / `MVP.md` / `ARCHITECTURE.md` /
  6: `QUALITY.md` / `TEST_STRATEGY.md` / `IMPLEMENTATION_PLAN.md` / `AGENTS.md`.
  7: 
  8: > **Read order first:** `PRODUCT.md` + `MVP.md` → `ARCHITECTURE.md` → `QUALITY.md`
  9: > + `TEST_STRATEGY.md` → `IMPLEMENTATION_PLAN.md`. Then run
 10: > `python3 fetch_anki_fields.py` (field names live in Anki, never in the repo)
 11: > and read the gitignored `.anki_fields.json` **before any template work**.
 12: > Run `./verify` before declaring done; release via `./finish.sh`.
 13: 
 14: ## What happened before you
 15: 
 16: A previous implementation (now **reverted**) tried to add the features below
 17: as v1.8.0/v1.8.1 but introduced a **blank front in real Anki during review**
 18: (all cards). It was reverted. The headless test suite passed the broken
 19: build, so the bug was environment-specific: **you cannot fully validate the
 20: front by headless Chrome alone.** Verify the front in a REAL Anki review
 21: session on desktop before releasing.
 22: 
 23: ## Features to build (after `59ac56f`)
 24: 
 25: 1. **`R` shortcut is Anki-owned, never template-owned.** Do not add or
 26:    modify an `R` shortcut. Remove the `R` hint from the back's shortcut UI
 27:    if present. Keep custom template shortcuts **`Z`** (furigana toggle),
 28:    **`X`** (translation toggle), **`C`** (expanded-info toggle). Don't
 29:    interfere with Anki's native `R` replay.
 30: 
 31: 2. **Listening mode — Policy B.** `#listening` (or the legacy audio-only
 32:    shape) activates the listening front **only when usable audio exists**.
 33:    `#listening` + no usable audio must fall back safely to the normal
 34:    sentence front. Never leave a dead/empty listening UI.
 35: 
 36: 3. **Listening audio source bug (NEW, confirmed in the live baseline).**
 37:    In `Card 1 - Front.template.anki`, the `tag-listening-view` audio source
 38:    is hardcoded to
 39:    `<a class="replay-button soundLink" href="#" onclick="...pycmd('play:a:0')...">`
 40:    (`play:a:0` = "first audio field"). On listening cards this plays the
 41:    **Word Audio** field instead of the intended **Sentence Audio**, even
 42:    though the button is labelled 文 (sentence). Fix: bind the listening
 43:    button's audio source to the actual `{{Sentence Audio}}` field, falling
 44:    back to `{{Word Audio}}` only when Sentence Audio is absent. The label
 45:    must match what actually plays.
 46: 
 47: 4. **Audio terminology.** The native audio system is intentionally **not a
 48:    real progress indicator**. Rename internal comments/terminology from
 49:    "progress ring" toward **playback indicator** where practical. Do **not**
 50:    recreate playback progress with `new Audio()`; preserve native Anki /
 51:    AnkiDroid audio delegation (sibling replay link, re-tap debounce,
 52:    restart-only).
 53: 
 54: 5. **Front template size is not a problem.** Do not aggressively split /
 55:    refactor the front to reduce line count. Correctness > file size.
 56: 
 57: 6. **Mature Word Mode — exact current-card interval.** During review, select
 58:    the interval of the **exact current card** (`guiCurrentCard` →
 59:    `cardsInfo` on desktop; AnkiDroid bridge `ankiGetCardInterval()` on
 60:    mobile). Content search (Expression → Sentence → cloze-body) is **only** a
 61:    best-effort preview/browser fallback when exact identity is unavailable.
 62:    If content fallback yields multiple candidates, **never pick candidate 0**
 63:    — use Sentence and cloze-body discriminators; if ambiguity remains, fail
 64:    safely to the normal sentence mode. Add regression tests for duplicate
 65:    Expressions / duplicate notes.
 66: 
 67: 7. **`:has()` is accepted architecture.** Do not remove or redesign `:has()`
 68:    usage for theoretical portability.
 69: 
 70: 8. **Deterministic release ordering in `finish.sh`.** Order must be:
 71:    `verify → version stamp → sync to Anki → export apkg → commit → push main
 72:    → create GitHub release/tag (--target main) → fetch tag`. The tag must
 73:    point at the exact pushed release commit. Preserve the existing no-op
 74:    (nothing-to-commit) protection.
 75: 
 76: 9. **Tests** (extend the current architecture: structural + headless
 77:    behavioral + layout + CI). Prioritize behavioral tests for:
 78:    `#listening` without audio; `#listening` with audio; duplicate-Expression
 79:    mature candidates; exact-current-card interval; ambiguous preview fallback
 80:    → safe sentence mode; audio failure/reset; release-script ordering / no-op.
 81:    Add a regression that **exactly one** listening sound button is ever
 82:    visible (a pure `#listening` audio card renders both a tag view and a
 83:    classic view in markup — the resolver must keep only the active one, and
 84:    must remove every dead/duplicate view when audio/sentence is missing).
 85: 
 86: 10. **Docs audit.** `QUALITY.md`, `TEST_STRATEGY.md`, `ARCHITECTURE.md`,
 87:     `PRODUCT.md`, `README.md`, template comments, and CSS comments must
 88:     describe the actual architecture: R is Anki-owned; `#listening` requires
 89:     usable audio; the ring is a playback indicator; mature mode distinguishes
 90:     exact-card retrieval from heuristic preview fallback; `:has()` is
 91:     intentional; front size is not a defect.
 92: 
 93: ## CRITICAL pitfall — do not repeat it
 94: 
 95: The reverted v1.8.x set `visibility:hidden` on `.card-container` and relied
 96: on an async + `setTimeout` reveal. In real Anki review the async AnkiConnect
 97: round-trip could stall, the reveal timer never fired, and **every front
 98: rendered blank** (back card unaffected — it has no visibility gate). A
 99: synchronous-reveal attempt was also reverted. Whatever you do:
100: 
101: - Keep the front reveal **deterministic and safe**: it must never depend on a
102:   single async path or timer that can be throttled, and it must never leave a
103:   blank/hung card.
104: - Preserve the intended anti-flash behavior for mature cards **without**
105:   risking a blank front.
106: - **Test in a real Anki review session on desktop** (and ideally AnkiDroid)
107:   before releasing, in addition to `./verify`. If you cannot reproduce a real
108:   review, say so explicitly rather than claiming it is fixed.
109: 
110: ## Do NOT do
111: 
112: - No unnecessary frameworks.
113: - No HTML5 `Audio()` replacing native delegation.
114: - Don't remove `:has()` for portability.
115: - Don't arbitrarily pick the first duplicate card in mature mode.
116: - Don't add a shortcut that conflicts with Anki.
117: - Don't add visual UI unless it directly improves learning/retrieval.
118: - Don't refactor the Front just to reduce line count.
119: 
120: ## Current test baseline
121: 
122: `./verify` is green on `59ac56f` (compactor 25, template invariants 99,
123: front-mode 15, layout 28). `tests/` = `test_compactor.py`, `test_templates.py`,
124: `test_front_modes.py`, `test_layout.py` (+ `test_mature_content.py` existed
125: only in the reverted branch and is not present on this baseline).
````

## File: docs/adr/003-native-audio-delegation.md
````markdown
 1: # ADR 003 — Native-only audio delegation
 2: 
 3: ## Context
 4: 
 5: Custom circular buttons (`文` / `言葉`) must play audio on Desktop and
 6: AnkiDroid without overlapping playback.
 7: 
 8: ## Options considered
 9: 
10: 1. HTML5 `new Audio(filename)` — AnkiDroid render links carry no usable
11:    filename (old builds emit `playsound:q:0`), causing bogus-file loads.
12: 2. Nest the replay link inside `<button>` — invalid HTML, Android WebView
13:    mishandles taps.
14: 3. **`playCircularAudio` delegating to the sibling native replay link
15:    (chosen).**
16: 
17: ## Decision
18: 
19: The `.raw-audio-source` span lives **outside** the button, visually hidden
20: but kept in layout (never `display:none`, which breaks programmatic
21: `.click()`). Every play path resets state first; re-taps on the playing
22: button are ignored (native audio can't be stopped); the ring is a playback
23: indicator (a decorative play-pulse), not true progress.
24: 
25: ## Consequences
26: 
27: No filenames are ever constructed in JS. Markup/JS contract is pinned by
28: `test_templates.py` §§2–3b.
````

## File: docs/adr/004-single-command-release.md
````markdown
 1: # ADR 004 — Single-command release with pre-sync snapshots
 2: 
 3: ## Context
 4: 
 5: Multi-step endings (test → sync → export → commit → push → release) were
 6: dropped late in sessions when run manually.
 7: 
 8: ## Decision
 9: 
10: `finish.sh` runs the full chain in deterministic order and stops on first
11: failure: `verify → version stamp → sync_to_anki.py → release_apkg.py →
12: commit → push main → gh release create --target main → fetch tag`. The tag
13: points at the exact pushed commit. `./verify` is the side-effect-free
14: subset it delegates to. `sync_to_anki.py` snapshots the live Anki state to
15: `backups/<timestamp>/` (microsecond stamps) before overwriting and aborts
16: on empty live state. `release_apkg.py` uses the only verified export action
17: (`exportPackage`) into gitignored `dist/`; the apkg ships as a GitHub
18: Release asset, never in the repo. No-op runs never publish.
19: 
20: ## Consequences
21: 
22: One command to remember; snapshots make Anki-side overwrites recoverable;
23: tag, tree, and live templates agree (CSS header is stamped before sync).
24: Push-before-release ordering guarantees the tag commit == the pushed
25: commit on main.
````

## File: tests/test_mature_content.py
````python
  1: #!/usr/bin/env python3
  2: """Mature Word Mode content-search fallback behavioral tests.
  3: 
  4: Extracts the content-search fallback block verbatim from the real
  5: `Card 1 - Front.template.anki` and runs it in headless Chrome against
  6: simulated AnkiConnect responses, asserting the mature-mode decision:
  7: 
  8:   1. single Expression match → uses that card's interval (word mode on if ≥ 365)
  9:   2. duplicate Expressions, distinct Sentences → Sentence discriminator
 10:      picks the exact card (never candidate 0 blindly)
 11:   3. duplicate Expressions + duplicate Sentences, distinct cloze-body →
 12:      cloze-body discriminator picks the exact card
 13:   4. duplicate Expressions, Sentence absent on front → ambiguous →
 14:      fails safely to sentence mode (interval stays null, no word mode)
 15:   5. duplicate Expressions + same Sentence + no cloze-body probe →
 16:      ambiguous → fails safely to sentence mode
 17:   6. exact-current-card path (guiCurrentCard) is the primary path;
 18:      content search only fires when guiCurrentCard throws
 19: 
 20: The block is extracted verbatim and run inside a harness that mocks the
 21: `post` AnkiConnect helper and the surrounding `container`/`wrapper` DOM.
 22: 
 23: Run directly:  python3 tests/test_mature_content.py
 24: Wired into ./verify alongside the other suites. Skipped gracefully
 25: without Chrome.
 26: 
 27: Dependencies: headless Chrome only (same as test_front_modes.py).
 28: """
 29: import json
 30: import os
 31: import re
 32: import shutil
 33: import subprocess
 34: import sys
 35: import tempfile
 36: 
 37: HERE = os.path.dirname(os.path.abspath(__file__))
 38: ROOT = os.path.dirname(HERE)
 39: FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
 40: CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")
 41: 
 42: PASS = 0
 43: FAIL = 0
 44: 
 45: 
 46: def check(name, cond, detail=""):
 47:     global PASS, FAIL
 48:     tag = "PASS" if cond else "FAIL"
 49:     print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
 50:     if cond:
 51:         PASS += 1
 52:     else:
 53:         FAIL += 1
 54: 
 55: 
 56: def load_block():
 57:     """Extract the content-search fallback block verbatim from the front,
 58:     then strip `await` keywords so the harness can run it synchronously
 59:     (the mock `post` returns values directly, not Promises).
 60: 
 61:     The block is the `if (!isListening) { ... }` body inside the main
 62:     try: content search IS the primary path now (the live guiCurrentCard
 63:     reviewer read was removed). We also extract escQuery/normText helpers.
 64:     """
 65:     with open(FRONT, encoding="utf-8") as f:
 66:         front = f.read()
 67:     esc_q = re.search(r"const escQuery = \(s\) =>.*?;", front, re.S)
 68:     norm_t = re.search(r"const normText = \(s\) => s\s.*?\.trim\(\);", front, re.S)
 69:     if not esc_q or not norm_t:
 70:         raise RuntimeError("escQuery/normText helpers not found in front template")
 71:     # Extract the `if (!isListening) { ... }` content-search block: from
 72:     # the branch opener to the closing brace before the outer catch.
 73:     m = re.search(
 74:         r"if \(!isListening\) \{\s*\n\s*/\* BROWSE-PREVIEWER CONTENT SEARCH.*?"
 75:         r"source = 'content-search-ambiguous.*?sentence fallback';\s*\}\s*\}\s*\}\s*\}\s*\}",
 76:         front, re.S)
 77:     if not m:
 78:         raise RuntimeError("content-search fallback block not found in front template")
 79:     block = m.group(0)
 80:     # Strip `await` so the synchronous mock post (returns values, not
 81:     # Promises) can drive the block without async infrastructure. The logic
 82:     # (filter, discriminators, exact-card resolution) is unchanged.
 83:     block = block.replace("await ", "")
 84:     return esc_q.group(0), norm_t.group(0), block
 85: 
 86: 
 87: def build_html(esc_q, norm_t, block, expr, sentence, cloze_body, anki_response):
 88:     """Build a test harness HTML.
 89: 
 90:     anki_response: dict mapping action -> response. 'findCards' returns a
 91:     list of card ids; 'cardsInfo' returns a list of card info dicts. The
 92:     harness mocks `post` to return these. guiCurrentCard always throws
 93:     (simulating the Browse previewer where no review is active).
 94:     """
 95:     # Build the mock post function: synchronous (returns value directly,
 96:     # not a Promise). The extracted block has `await` stripped so this works.
 97:     mock_post = """
 98: var responses = %s;
 99: function post(action, params) {
100:   return responses[action];
101: }
102: """ % json.dumps(anki_response)
103: 
104:     cloze_probe = ""
105:     if cloze_body is not None:
106:         cloze_probe = (
107:             '<div class="cloze-probe" hidden>'
108:             f'<span class="cloze-pre">前</span>'
109:             f'<span class="cloze-mid">{cloze_body}</span>'
110:             f'<span class="cloze-suf">後</span>'
111:             '</div>'
112:         )
113: 
114:     sent_html = ""
115:     if sentence is not None:
116:         sent_html = f'<div class="sentence-display">{sentence}</div>'
117: 
118:     return f"""<!doctype html><html><head><meta charset="utf-8">
119: <style>.front-word-display{{display:none}}</style></head><body>
120: <div class="card"><div class="card-wrapper"><div class="card-container">
121: <div class="front-word-display">{expr}</div>
122: {cloze_probe}
123: {sent_html}
124: </div></div></div>
125: <script>
126: var report = {{}};
127: try {{
128:   /* guiCurrentCard mock: throws so the catch block (content-search fallback) runs. */
129:   var container = document.querySelector('.card-container');
130:   var wrapper = document.querySelector('.card-wrapper');
131:   var isListening = false;
132:   var interval = null;
133:   var source = 'unavailable';
134: {mock_post}
135: {esc_q}
136: {norm_t}
137:   {block}
138: }} catch(e) {{ report.err = String(e && e.stack || e); }}
139: document.title = JSON.stringify(report);
140: </script>
141: </body></html>"""
142: 
143: 
144: def render(html):
145:     with tempfile.TemporaryDirectory() as td:
146:         path = os.path.join(td, "front.html")
147:         with open(path, "w", encoding="utf-8") as f:
148:             f.write(html)
149:         try:
150:             out = subprocess.run(
151:                 [CHROME, "--headless=new", "--disable-gpu",
152:                  "--no-sandbox", "--hide-scrollbars",
153:                  "--window-size=1440,900",
154:                  "--virtual-time-budget=1500",
155:                  "--dump-dom", f"file://{path}"],
156:                 capture_output=True, text=True, timeout=60,
157:             ).stdout
158:         except subprocess.TimeoutExpired:
159:             return None
160:     m = re.search(r"<title>(.*?)</title>", out, re.S)
161:     if not m:
162:         return None
163:     try:
164:         return json.loads(m.group(1))
165:     except json.JSONDecodeError:
166:         return None
167: 
168: 
169: def main():
170:     if not CHROME:
171:         print("[SKIP] no headless Chrome found — mature content-search checks skipped")
172:         return 0
173:     esc_q, norm_t, block = load_block()
174: 
175:     # --- Case 1: single Expression match → uses that card's interval ---
176:     anki = {
177:         "findCards": [100],
178:         "cardsInfo": [{
179:             "interval": 400,
180:             "fields": {
181:                 "Expression": {"value": "不公平"},
182:                 "Sentence": {"value": "世の中って不公平よね"},
183:                 "cloze-body": {"value": "不公平"}
184:             }
185:         }]
186:     }
187:     r = render(build_html(esc_q, norm_t, block, "不公平",
188:                           "世の中って<b>不公平</b>よね", "不公平", anki))
189:     check("single match: probe returned", r is not None)
190:     if r:
191:         check("single match: resolver ran without errors", "err" not in r, r.get("err", ""))
192:         check("single match: interval used (400, word mode eligible)",
193:               r.get("interval") == 400, json.dumps(r))
194:         check("single match: source = content-search",
195:               r.get("source") == "content-search", json.dumps(r))
196: 
197:     # --- Case 2: duplicate Expressions, distinct Sentences → Sentence discriminator ---
198:     anki = {
199:         "findCards": [100, 101],
200:         "cardsInfo": [
201:             {"interval": 10, "fields": {
202:                 "Expression": {"value": "不公平"},
203:                 "Sentence": {"value": "別の文不公平別"},
204:                 "cloze-body": {"value": "不公平"}}},
205:             {"interval": 500, "fields": {
206:                 "Expression": {"value": "不公平"},
207:                 "Sentence": {"value": "世の中って不公平よね"},
208:                 "cloze-body": {"value": "不公平"}}}
209:         ]
210:     }
211:     r = render(build_html(esc_q, norm_t, block, "不公平",
212:                           "世の中って<b>不公平</b>よね", "不公平", anki))
213:     check("dup Expr + distinct Sentence: probe returned", r is not None)
214:     if r:
215:         check("dup Expr + distinct Sentence: resolver ran without errors", "err" not in r, r.get("err", ""))
216:         check("dup Expr + distinct Sentence: Sentence discriminator picks exact card (interval 500, not candidate 0's 10)",
217:               r.get("interval") == 500, json.dumps(r))
218:         check("dup Expr + distinct Sentence: source = content-search",
219:               r.get("source") == "content-search", json.dumps(r))
220: 
221:     # --- Case 3: dup Expr + dup Sentence, distinct cloze-body → cloze-body discriminator ---
222:     anki = {
223:         "findCards": [100, 101],
224:         "cardsInfo": [
225:             {"interval": 10, "fields": {
226:                 "Expression": {"value": "不公平"},
227:                 "Sentence": {"value": "世の中って不公平よね"},
228:                 "cloze-body": {"value": "別の"}}},
229:             {"interval": 600, "fields": {
230:                 "Expression": {"value": "不公平"},
231:                 "Sentence": {"value": "世の中って不公平よね"},
232:                 "cloze-body": {"value": "不公平"}}}
233:         ]
234:     }
235:     r = render(build_html(esc_q, norm_t, block, "不公平",
236:                           "世の中って<b>不公平</b>よね", "不公平", anki))
237:     check("dup Expr + dup Sentence + distinct cloze-body: probe returned", r is not None)
238:     if r:
239:         check("dup Expr + dup Sentence + distinct cloze-body: resolver ran without errors",
240:               "err" not in r, r.get("err", ""))
241:         check("dup Expr + dup Sentence + distinct cloze-body: cloze-body discriminator picks exact card (interval 600, not 10)",
242:               r.get("interval") == 600, json.dumps(r))
243:         check("dup Expr + dup Sentence + distinct cloze-body: source = content-search",
244:               r.get("source") == "content-search", json.dumps(r))
245: 
246:     # --- Case 4: dup Expr, no Sentence on front → ambiguous → safe fallback ---
247:     anki = {
248:         "findCards": [100, 101],
249:         "cardsInfo": [
250:             {"interval": 10, "fields": {
251:                 "Expression": {"value": "不公平"},
252:                 "Sentence": {"value": "別の文"},
253:                 "cloze-body": {"value": "不公平"}}},
254:             {"interval": 500, "fields": {
255:                 "Expression": {"value": "不公平"},
256:                 "Sentence": {"value": "また別の文"},
257:                 "cloze-body": {"value": "不公平"}}}
258:         ]
259:     }
260:     r = render(build_html(esc_q, norm_t, block, "不公平",
261:                           None, "不公平", anki))
262:     check("dup Expr + no Sentence on front: probe returned", r is not None)
263:     if r:
264:         check("dup Expr + no Sentence on front: resolver ran without errors",
265:               "err" not in r, r.get("err", ""))
266:         check("dup Expr + no Sentence on front: fails safely (interval null, no word mode)",
267:               r.get("interval") is None, json.dumps(r))
268:         check("dup Expr + no Sentence on front: source marks ambiguity",
269:               "ambiguous" in (r.get("source") or ""), json.dumps(r))
270: 
271:     # --- Case 5: dup Expr + dup Sentence + no cloze-body probe → ambiguous → safe fallback ---
272:     anki = {
273:         "findCards": [100, 101],
274:         "cardsInfo": [
275:             {"interval": 10, "fields": {
276:                 "Expression": {"value": "不公平"},
277:                 "Sentence": {"value": "世の中って不公平よね"},
278:                 "cloze-body": {"value": "別の"}}},
279:             {"interval": 500, "fields": {
280:                 "Expression": {"value": "不公平"},
281:                 "Sentence": {"value": "世の中って不公平よね"},
282:                 "cloze-body": {"value": "不公平"}}}
283:         ]
284:     }
285:     r = render(build_html(esc_q, norm_t, block, "不公平",
286:                           "世の中って<b>不公平</b>よね", None, anki))
287:     check("dup Expr + dup Sentence + no cloze-body probe: probe returned", r is not None)
288:     if r:
289:         check("dup Expr + dup Sentence + no cloze-body probe: resolver ran without errors",
290:               "err" not in r, r.get("err", ""))
291:         check("dup Expr + dup Sentence + no cloze-body probe: fails safely (interval null)",
292:               r.get("interval") is None, json.dumps(r))
293:         check("dup Expr + dup Sentence + no cloze-body probe: source marks ambiguity",
294:               "ambiguous" in (r.get("source") or ""), json.dumps(r))
295: 
296:     # --- Case 6: no cards found → interval null (safe fallback) ---
297:     anki = {"findCards": [], "cardsInfo": []}
298:     r = render(build_html(esc_q, norm_t, block, "不公平",
299:                           "世の中って<b>不公平</b>よね", "不公平", anki))
300:     check("no cards found: probe returned", r is not None)
301:     if r:
302:         check("no cards found: resolver ran without errors", "err" not in r, r.get("err", ""))
303:         check("no cards found: interval null (safe fallback)",
304:               r.get("interval") is None, json.dumps(r))
305: 
306:     print()
307:     print(f"{PASS} passed, {FAIL} failed")
308:     return 1 if FAIL else 0
309: 
310: 
311: if __name__ == "__main__":
312:     sys.exit(main())
````

## File: sync_to_anki.py
````python
  1: import urllib.request
  2: import json
  3: import os
  4: import shutil
  5: import sys
  6: from datetime import datetime
  7: 
  8: # Configuration for the Japanese Note Type
  9: ANKI_CONNECT_URL = "http://127.0.0.1:8765"
 10: MODEL_NAME = "Japanese Note type (Sentence card by Default)"
 11: 
 12: # Resolve project root so the script works from any directory
 13: SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
 14: 
 15: FRONT_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Front.template.anki")
 16: BACK_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Back.template.anki")
 17: CSS_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Style.css")
 18: 
 19: # Pre-sync snapshots of the live Anki state (gitignored safety net)
 20: BACKUP_DIR = os.path.join(SCRIPT_DIR, "backups")
 21: 
 22: 
 23: def _read_file(path: str) -> str:
 24:     """Read a UTF-8 file from the project directory."""
 25:     try:
 26:         with open(path, "r", encoding="utf-8") as f:
 27:             return f.read()
 28:     except FileNotFoundError:
 29:         print(f"ERROR: Template file not found: {path}")
 30:         sys.exit(1)
 31:     except OSError as e:
 32:         print(f"ERROR: Could not read {path}: {e}")
 33:         sys.exit(1)
 34: 
 35: 
 36: def _send_payload(action: str, params: dict = None) -> dict:
 37:     """Send a payload to Anki-Connect and return the parsed response."""
 38:     payload = {
 39:         "action": action,
 40:         "version": 6,
 41:         "params": params or {},
 42:     }
 43:     req = urllib.request.Request(
 44:         ANKI_CONNECT_URL,
 45:         data=json.dumps(payload).encode("utf-8"),
 46:         headers={"Content-Type": "application/json"},
 47:     )
 48:     try:
 49:         with urllib.request.urlopen(req, timeout=10) as response:
 50:             result = json.loads(response.read().decode("utf-8"))
 51:     except urllib.error.URLError as e:
 52:         print(f"ERROR: Could not connect to Anki-Connect. Is Anki running with the add-on installed? {e}")
 53:         sys.exit(1)
 54:     except Exception as e:
 55:         print(f"ERROR: Anki-Connect request failed: {e}")
 56:         sys.exit(1)
 57: 
 58:     if result.get("error"):
 59:         print(f"ERROR: Anki-Connect returned: {result['error']}")
 60:         sys.exit(1)
 61:     return result
 62: 
 63: 
 64: def snapshot_live_state():
 65:     """Pull the live model from Anki into backups/<timestamp>/ before pushing.
 66: 
 67:     Guard against clobbering unnoticed Anki-side edits: the snapshot keeps the
 68:     exact state that is about to be overwritten, so any manual change made in
 69:     the Anki UI stays recoverable. Failures here abort the sync (never push
 70:     over a state we failed to back up).
 71:     """
 72:     templates = _send_payload("modelTemplates", {"modelName": MODEL_NAME})
 73:     styling = _send_payload("modelStyling", {"modelName": MODEL_NAME})
 74: 
 75:     tpls = templates.get("result") or {}
 76:     sty = styling.get("result") or {}
 77:     if not tpls or not isinstance(tpls, dict) or not sty.get("css"):
 78:         print("ERROR: live Anki state looks empty (model missing?) — aborting sync")
 79:         sys.exit(1)
 80: 
 81:     stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
 82:     dest = os.path.join(BACKUP_DIR, stamp)
 83:     os.makedirs(dest, exist_ok=True)
 84:     try:
 85:         os.chmod(dest, 0o700)
 86:     except OSError:
 87:         pass
 88:     # Retention: keep the newest 20 snapshots (unbounded growth guard).
 89:     try:
 90:         for old in sorted(os.listdir(BACKUP_DIR))[:-20]:
 91:             shutil.rmtree(os.path.join(BACKUP_DIR, old), ignore_errors=True)
 92:     except OSError:
 93:         pass
 94:     for card_name, pair in tpls.items():
 95:         safe = card_name.replace(os.sep, "_")
 96:         with open(os.path.join(dest, f"{safe}.front.anki"), "w", encoding="utf-8") as f:
 97:             f.write(pair.get("Front", ""))
 98:         with open(os.path.join(dest, f"{safe}.back.anki"), "w", encoding="utf-8") as f:
 99:             f.write(pair.get("Back", ""))
100:     with open(os.path.join(dest, "style.css"), "w", encoding="utf-8") as f:
101:         f.write(sty.get("css", ""))
102:     print(f"Backup:        {os.path.relpath(dest, SCRIPT_DIR)}/")
103:     return dest
104: 
105: 
106: def sync_to_anki():
107:     """
108:     Reads local template files and pushes them to Anki via Anki-Connect.
109:     This automates the manual copy-paste process for faster iteration.
110:     """
111:     # 1. Read local files (UTF-8 for proper Japanese text handling)
112:     front_html = _read_file(FRONT_FILE)
113:     back_html = _read_file(BACK_FILE)
114:     css_content = _read_file(CSS_FILE)
115: 
116:     # 2. Snapshot the live Anki state we are about to overwrite
117:     snapshot_live_state()
118: 
119:     # 3. Update Templates (Front/Back HTML)
120:     _send_payload("updateModelTemplates", {
121:         "model": {
122:             "name": MODEL_NAME,
123:             "templates": {
124:                 "Card 1": {
125:                     "Front": front_html,
126:                     "Back": back_html
127:                 }
128:             }
129:         }
130:     })
131:     print("Template Sync: Success")
132: 
133:     # 4. Update Styling (CSS)
134:     _send_payload("updateModelStyling", {
135:         "model": {
136:             "name": MODEL_NAME,
137:             "css": css_content
138:         }
139:     })
140:     print("Styling Sync:  Success")
141: 
142: 
143: if __name__ == "__main__":
144:     sync_to_anki()
````

## File: .gitignore
````
1: __pycache__/
2: *.apkg
3: backups/
4: dist/
5: .anki_fields.json
6: conversations/
7: reports/
````

## File: fetch_anki_fields.py
````python
 1: #!/usr/bin/env python3
 2: """Fetch live note-type field names + descriptions from Anki (read-only).
 3: 
 4: Fields are managed EXCLUSIVELY inside the Anki UI — this repo keeps no
 5: static field list. Agents must run this script at session start (see
 6: AGENTS.md rule 0) and read the generated `.anki_fields.json` snapshot
 7: instead of guessing field names.
 8: 
 9: Usage:  python3 fetch_anki_fields.py
10: Output: .anki_fields.json (gitignored) + the field list on stdout.
11: 
12: Requires: Anki running with the Anki-Connect add-on.
13: Standard library only (mirrors sync_to_anki.py).
14: """
15: 
16: import json
17: import os
18: import sys
19: import urllib.request
20: 
21: # Keep in sync with sync_to_anki.py
22: ANKI_CONNECT_URL = "http://127.0.0.1:8765"
23: MODEL_NAME = "Japanese Note type (Sentence card by Default)"
24: 
25: SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
26: OUT_FILE = os.path.join(SCRIPT_DIR, ".anki_fields.json")
27: 
28: 
29: def _anki(action, **params):
30:     req = urllib.request.Request(
31:         ANKI_CONNECT_URL,
32:         data=json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
33:         headers={"Content-Type": "application/json"},
34:     )
35:     try:
36:         with urllib.request.urlopen(req, timeout=10) as response:
37:             result = json.loads(response.read().decode("utf-8"))
38:     except Exception as e:
39:         print(f"ERROR: Could not reach Anki-Connect at {ANKI_CONNECT_URL}. "
40:               f"Is Anki running with the add-on installed? ({e})")
41:         sys.exit(1)
42:     if result.get("error"):
43:         print(f"ERROR: Anki-Connect returned: {result['error']}")
44:         sys.exit(1)
45:     return result.get("result")
46: 
47: 
48: def _anki_soft(action, **params):
49:     """Like _anki but returns None instead of exiting (optional data)."""
50:     req = urllib.request.Request(
51:         ANKI_CONNECT_URL,
52:         data=json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
53:         headers={"Content-Type": "application/json"},
54:     )
55:     try:
56:         with urllib.request.urlopen(req, timeout=10) as response:
57:             result = json.loads(response.read().decode("utf-8"))
58:     except Exception:
59:         return None
60:     return result.get("result") if not result.get("error") else None
61: 
62: 
63: def main():
64:     fields = _anki("modelFieldNames", modelName=MODEL_NAME)
65:     if not isinstance(fields, list) or not fields:
66:         print(f"ERROR: no fields returned for model '{MODEL_NAME}' — does it still exist?")
67:         sys.exit(1)
68:     # Descriptions are typed by the user in Anki (Fields dialog). Older
69:     # Anki-Connect builds lack this action — degrade to names only.
70:     descriptions = _anki_soft("modelFieldDescriptions", modelName=MODEL_NAME)
71:     if not isinstance(descriptions, list) or len(descriptions) != len(fields):
72:         descriptions = [""] * len(fields)
73:     entries = [
74:         {"name": name, "description": desc or ""}
75:         for name, desc in zip(fields, descriptions)
76:     ]
77:     with open(OUT_FILE, "w", encoding="utf-8") as f:
78:         json.dump({"model": MODEL_NAME, "fields": entries}, f, ensure_ascii=False, indent=2)
79:         f.write("\n")
80:     print(f"Model: {MODEL_NAME} ({len(entries)} fields) -> .anki_fields.json")
81:     for i, entry in enumerate(entries):
82:         line = f"  {i:2d}. {entry['name']}"
83:         if entry["description"]:
84:             line += f" — {entry['description']}"
85:         print(line)
86: 
87: 
88: if __name__ == "__main__":
89:     main()
````

## File: fix_summary.md
````markdown
 1: ## Task Completed: Fix false "Card Content Error: Failed to load ''" on AnkiDroid
 2: 
 3: ### Problem
 4: - On AnkiDroid 2.24.0, Mature Word Mode requested the card interval through
 5:   the AnkiDroid JS API (`AnkiDroidJS` → `ankiGetCardInterval()` →
 6:   `/jsapi/cardInterval`).
 7: - AnkiDroid routes WebView resource/load errors through its media-error
 8:   handler, so those calls surfaced natively as
 9:   `Card Content Error: Failed to load ''` in the reviewer.
10: - The error is native/WebView-side, not a catchable JS exception: try/catch,
11:   `Promise.catch()`, timeouts, and stub detection could not reliably prevent
12:   it.
13: 
14: ### Solution Implemented
15: - Removed the entire mobile interval-retrieval path from
16:   `Card 1 - Front.template.anki`: no `AnkiDroidJS`, no
17:   `ankiGetCardInterval`, no `/jsapi/` request, no bridge helpers, no polling.
18: - Mature Word Mode is now **desktop-only** via AnkiConnect
19:   (`guiCurrentCard` → `cardsInfo`).
20: - On Android/mobile the template deliberately makes no interval request:
21:   interval stays `null`, so `wordMode` is `false` and the ordinary sentence
22:   front is shown (graceful degradation).
23: 
24: ### Verification Results
25: - `./verify`: all suites green.
26: - Static search confirms no executable AnkiDroid JS API code remains in the
27:   front template; external `AnkiDroidJS` hits are only in gitignored
28:   `backups/`.
29: 
30: ### Impact
31: - Eliminates the false media error at its source (the request is never made).
32: - Desktop Mature Word Mode is unchanged and fully functional.
33: - No visual, audio, listening, cloze, or layout behavior changes.
````

## File: docs/adr/001-mature-word-mode-interval.md
````markdown
 1: # ADR 001 — Mature Word Mode interval retrieval
 2: 
 3: Date: 2026-09 (records the as-built decision; amended after the
 4: AnkiDroid "downloadfile.bin" debugging — the live reviewer read was
 5: removed in favour of a fallback-only content search).
 6: 
 7: ## Context
 8: 
 9: Anti-overlearning requires the front to show only the Expression once a
10: card is mature (interval ≥ `LONG_INTERVAL_DAYS`). No `{{Interval}}` marker
11: exists, and new fields / add-ons / review-time Python are all rejected.
12: 
13: ## Options considered
14: 
15: 1. Bake the interval into a field at mining time — stale the next day.
16: 2. Guess the card id from the URL — no stable id is exposed.
17: 3. Live read during review (`guiCurrentCard`→`cardsInfo`) on desktop,
18:    content-search fallback for the previewer — was the original design,
19:    **removed**: `guiCurrentCard` only works during active review, it
20:    duplicated a second retrieval path for marginal identity gain, and the
21:    associated debugging cycle repeatedly resurfaced AnkiDroid false
22:    media-load errors.
23: 4. Mobile read via the AnkiDroid JS API (`ankiGetCardInterval()`) — calls
24:    can surface natively as false `Card Content Error: Failed to load ''`
25:    media warnings in the reviewer, even when wrapped in try/catch. Not
26:    reliable from a card template.
27: 5. **Desktop-only fallback content search (chosen).**
28: 
29: ## Decision
30: 
31: Desktop resolves the interval via a single AnkiConnect **content search**:
32: `findCards` by Expression, then Sentence and cloze-body discriminators
33: narrow to exactly one candidate (never candidate 0 blindly; ambiguity
34: fails safely to the sentence front). Reviewer and Browse previewer share
35: this one identical path. The `post` helper **UA-guards every AnkiConnect
36: call before any fetch**: on Android/iOS it rejects immediately, so mobile
37: makes no network request at all — Mature Word Mode is intentionally
38: disabled there and the ordinary sentence front is shown. Listening fronts
39: skip all retrieval. Any failure degrades to the sentence front behind an
40: anti-flash gate.
41: 
42: ## Consequences
43: 
44: Mature Word Mode is a desktop-only presentation feature; on Android users
45: see the normal sentence front. This is an accepted reliability trade-off —
46: the reviewer must never surface false media-load errors. On desktop the
47: mode is heuristic: duplicate mined sentences that survive both
48: discriminators stay on the sentence front instead of guessing. The
49: content-search path is covered by `test_templates.py` §8b and
50: `test_mature_content.py` on every change.
````

## File: verify
````
 1: #!/usr/bin/env bash
 2: # verify — repository's complete mandatory LOCAL quality gate.
 3: #
 4: # Side-effect free: runs checks only. Never touches Anki, never exports,
 5: # never commits, never releases. Run it before declaring any task complete:
 6: #
 7: #   ./verify
 8: #
 9: # finish.sh step 0 delegates to this script, and CI re-runs it on every
10: # push — the three can never disagree. See TEST_STRATEGY.md for the
11: # layering (tiny test → targeted suite → ./verify → CI).
12: set -euo pipefail
13: 
14: cd "$(dirname "$0")"
15: 
16: if [ ! -d tests ]; then
17:   echo "(no tests/ directory — nothing to verify)"
18:   exit 0
19: fi
20: 
21: echo "==> verify: compactor regression tests"
22: python3 tests/test_compactor.py
23: echo "==> verify: template structural invariants"
24: python3 tests/test_templates.py
25: echo "==> verify: front-mode resolver behavior (listening semantics)"
26: python3 tests/test_front_modes.py
27: echo "==> verify: mature content-search fallback (duplicate cards / ambiguity)"
28: python3 tests/test_mature_content.py
29: echo "==> verify: back More lazy-load + prune behavior (headless Chrome, skipped gracefully without Chrome)"
30: python3 tests/test_back_more.py
31: echo "==> verify: headless layout checks (skipped gracefully without Chrome)"
32: python3 tests/test_layout.py
33: echo "verify: OK"
````

## File: TEST_STRATEGY.md
````markdown
 1: # TEST_STRATEGY.md — how QUALITY.md is mechanically verified
 2: 
 3: ```text
 4: QUALITY.md (WHAT must remain true)
 5:   → TEST_STRATEGY.md (HOW it is verified)
 6:     → tests / linters / headless checks / CI
 7: ```
 8: 
 9: ## Layers (narrow → broad)
10: 
11: ```text
12: tiny brick test → targeted suite → ./verify → CI (clean env)
13: ```
14: 
15: While iterating, run the targeted suite; before declaring a task complete,
16: run `./verify`; CI re-runs `./verify` after every push.
17: 
18: ## Enforcement map
19: 
20: | Requirement (QUALITY.md) | Enforcement |
21: | --- | --- |
22: | Compactor keeps 1st dictionary, ≤2 senses, no appendices; extended definition untouched; rules scoped to `.primary-definition` | `tests/test_compactor.py` — extracts real `display:none` rules from CSS §6b, applies to `tests/fixtures/*.html` (bs4 + soupsieve) |
23: | Front furigana ban; raw Sentence/Expression present | `tests/test_templates.py` §1 |
24: | Audio aria-labels; native-only controller; sibling replay source; debounce; restart-only | `tests/test_templates.py` §§2–3b |
25: | Cloze probe shape, trio gate, `<b>` rebuild, bold guard | `tests/test_templates.py` §2c |
26: | Lightbox backdrop-only close, dialog semantics, alt | `tests/test_templates.py` §4 |
27: | Balanced Anki conditionals | `tests/test_templates.py` §5 |
28: | Minimal redesign: no tags bar / frequency badges; More collapse; state label; F/T shortcuts; listening resolver wiring | `tests/test_templates.py` §§6b–6c |
29: | `:focus-visible`, reduced motion, content-driven sizing, context-grid fallback, clamp() authority, no JS font override | `tests/test_templates.py` §§6–7 |
30: | Mature Word Mode: const, desktop-only retrieval, no executable AnkiDroid JS API / bridge code, mobile degrades to sentence, no `note:` clause, anti-flash gate, word-mode CSS | `tests/test_templates.py` §8b |
31: | Mature content-search fallback: never picks candidate 0, Sentence + cloze-body discriminators, fails safely on ambiguity, exact-card resolution | `tests/test_mature_content.py` — extracts the content-search block verbatim, runs 6 headless Chrome cases with mocked AnkiConnect (skipped gracefully without Chrome) |
32: | Listening Policy B + exactly-one-button: `#listening` without audio → sentence front; `#listening` with audio → listening front; both-views markup → exactly one active; dead/duplicate views removed | `tests/test_front_modes.py` — 8 state harnesses in headless Chrome (skipped gracefully without Chrome) |
33: | Listening audio source: tag-listening-view binds to `{{Sentence Audio}}` (not `play:a:0`), Word Audio fallback, label matches | `tests/test_templates.py` §6d |
34: | R shortcut is Anki-owned (never in template shortcut UI); playback indicator terminology | `tests/test_templates.py` §§6e–6f |
35: | finish.sh deterministic ordering (push main before release, `--target main`), no-op protection | `tests/test_templates.py` §9 |
36: | Stdlib-only sync, microsecond backups, finish.sh no-op guard | `tests/test_templates.py` §9 |
37: | Content-driven height, no h-overflow, furigana containment, type hierarchy, 3-line clamp + one-way expand, listening target size, context grid, More collapsed by default, footer containment | `tests/test_layout.py` — headless Chrome on the **real** stylesheet; skipped gracefully when Chrome is absent |
38: | Listening resolver behavior: classic audio-only fields and `#listening` tag activate the audio front; gloss/no-tag, no-audio, and Frequency-legacy shapes keep the sentence front | `tests/test_front_modes.py` — extracts the real resolver from the front template and runs 6 state harnesses in headless Chrome; skipped gracefully when Chrome is absent |
39: | Clean-environment pass, no forgotten files/deps | CI (`.github/workflows/verify.yml`) runs `./verify` |
40: | Every UI element collapses when its field is empty | `tests/test_templates.py` §10 — conditional-enclosure parser over Front/Back, `:has()` shell-guard checks, JS self-removal checks |
41: 
42: ## The gate
43: 
44: `./verify` = the repository's complete mandatory **local** quality gate.
45: Side-effect free: it never touches Anki, never writes releases, never
46: commits. `finish.sh` step 0 delegates to it, so the gate and the release
47: pipeline can never disagree.
48: 
49: ## Regression rule (inside the dev loop, not a separate phase)
50: 
51: ```text
52: bug → diagnose → fix → add regression test → verify → commit
53: ```
54: 
55: Every escaped bug earns a permanent test: compactor regressions → new
56: fixture/assertion; template/CSS regressions → new `test_templates.py`
57: check; layout regressions → new `test_layout.py` probe assertion.
58: 
59: ## Dependencies
60: 
61: - `test_compactor.py`: `beautifulsoup4` + `soupsieve` (test-only).
62: - `test_templates.py`: stdlib only (node optional for JS syntax checks).
63: - `test_front_modes.py`: headless Chrome if present, else skip (pass).
64: - `test_mature_content.py`: headless Chrome if present, else skip (pass).
65: - `test_layout.py`: headless Chrome if present, else skip (pass).
````

## File: finish.sh
````bash
  1: #!/usr/bin/env bash
  2: # =============================================================================
  3: # finish.sh — single-command post-change routine.
  4: #
  5: # Run this at the end of ANY template change instead of remembering 5 steps:
  6: #   ./finish.sh "<commit message>"
  7: #
  8: # Flags:
  9: #   --local          Review mode: sync + export + commit only. Skips push and
 10: #                    GitHub release. Use while iterating; finish the batch with
 11: #                    a full run (no flag) to publish.
 12: #   --minor          Bump the MINOR version segment (v1.x.0) instead of the
 13: #                    patch segment. Use for multi-feature releases.
 14: #   --prompt "text"  Append the user prompt to chat_history/opencode_prompts.txt
 15: #                    BEFORE anything else runs (AGENTS.md rule 3), so the log
 16: #                    lands in the same commit.
 17: #
 18: #   It executes, in order:
 19: #   0. ./verify — local quality gate (compactor CSS + template invariants
 20: #                 + layout; skipped silently when tests/ is absent)
 21: #   1. version stamp  — compute the next release tag and rewrite the CSS
 22: #                        header Version: line (full runs only; the stamp is
 23: #                        what Anki receives in step 2, so it never lags)
 24: #   2. sync_to_anki.py — push templates+CSS into Anki via Anki-Connect
 25: #                        (also snapshots live Anki state into backups/)
 26: #   3. release_apkg.py — export sample deck to dist/*.apkg via Anki-Connect
 27: #   4. git commit     — stage everything (incl. chat_history log) & commit
 28: #   5. git push main  — push the commit to origin/main FIRST so the tag
 29: #                        points at the exact pushed release commit
 30: #   6. GitHub release — gh release create --target main (auto-bump tag + apkg)
 31: #                        → fetch the remote tag for the next version bump
 32: #
 33: # Any failure stops the chain with a clear message (set -e). Requires: Anki
 34: # running with Anki-Connect, gh CLI authenticated (full mode only).
 35: # =============================================================================
 36: set -euo pipefail
 37: 
 38: cd "$(dirname "$0")"
 39: 
 40: # ---------- flag parsing ----------
 41: LOCAL=0
 42: BUMP_KIND=patch
 43: PROMPT_TEXT=""
 44: COMMIT_MSG=""
 45: 
 46: while [ $# -gt 0 ]; do
 47:   case "$1" in
 48:     --local)  LOCAL=1 ;;
 49:     --minor)  BUMP_KIND=minor ;;
 50:     --prompt) shift; PROMPT_TEXT="${1:?--prompt requires a text argument}" ;;
 51:     -h|--help)
 52:       sed -n '2,30p' "$0"; exit 0 ;;
 53:     *)
 54:       if [ -z "$COMMIT_MSG" ]; then
 55:         COMMIT_MSG="$1"
 56:       else
 57:         echo "ERROR: unexpected extra argument: $1 (commit message already set)" >&2
 58:         exit 1
 59:       fi ;;
 60:   esac
 61:   shift
 62: done
 63: 
 64: [ -n "$COMMIT_MSG" ] || { echo 'Usage: ./finish.sh "<commit message>" [--local] [--minor] [--prompt "text"]' >&2; exit 1; }
 65: 
 66: # ---------- optional prompt archiving (before anything else) ----------
 67: if [ -n "$PROMPT_TEXT" ]; then
 68:   if printf '%s' "$PROMPT_TEXT" | grep -Ei -q 'api[_-]?key|token|passwd|password|secret|BEGIN .*PRIVATE KEY'; then
 69:     echo "Refusing: --prompt text looks like it contains a secret; archive it manually after redacting." >&2
 70:     exit 1
 71:   fi
 72:   printf '\n---\n\n%s\n' "$PROMPT_TEXT" >> chat_history/opencode_prompts.txt
 73:   echo "    (prompt archived to chat_history/opencode_prompts.txt)"
 74: fi
 75: 
 76: # ---------- step 0: regression tests (delegates to ./verify, the local gate) ----------
 77: if [ -d tests ]; then
 78:   echo "==> [0/6] Running regression tests (./verify)"
 79:   ./verify
 80: fi
 81: 
 82: # ---------- step 1: version stamp (BEFORE the sync so Anki gets the new tag) ----------
 83: # Local runs skip it: no release is published, so the stamp stays at the
 84: # last released version and the working tree is not polluted.
 85: NEW_TAG=""
 86: if [ "$LOCAL" -eq 0 ]; then
 87:   git fetch origin "refs/tags/*:refs/tags/*" --quiet
 88:   # Auto-bump version from the latest existing tag (v<major>.<minor>.<patch>)
 89:   LATEST_TAG="$(git tag --sort=-v:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -1 || true)"
 90:   if [ -z "$LATEST_TAG" ]; then
 91:     NEW_TAG="v1.0.1"
 92:   else
 93:     NEW_TAG="$(python3 - "$LATEST_TAG" "$BUMP_KIND" <<'PY'
 94: import sys
 95: major, minor, patch = sys.argv[1][1:].split(".")
 96: if sys.argv[2] == "minor":
 97:     print(f"v{major}.{int(minor) + 1}.0")
 98: else:
 99:     print(f"v{major}.{minor}.{int(patch) + 1}")
100: PY
101: )"
102:   fi
103:   # Rewrite the Version: line in the CSS header comment. The stamp is what
104:   # step 2 pushes to Anki and what step 4 commits — tag, tree and the live
105:   # template can never disagree.
106:   python3 - "$NEW_TAG" <<'PY'
107: import re, sys
108: tag = sys.argv[1]
109: path = "Card 1 - Style.css"
110: css = open(path, encoding="utf-8").read()
111: new, n = re.subn(
112:     r"( \* Version: )v[0-9]+\.[0-9]+\.[0-9]+[^\n]*",
113:     rf"\g<1>{tag} — auto-bumped by finish.sh; matches the GitHub release tag",
114:     css, count=1)
115: if n and new != css:
116:     open(path, "w", encoding="utf-8").write(new)
117:     print(f"    (stamped {tag} into Card 1 - Style.css header)")
118: PY
119: fi
120: 
121: echo "==> [1/6] Syncing templates to Anki (Anki-Connect)"
122: python3 sync_to_anki.py
123: 
124: echo "==> [2/6] Exporting sample deck to dist/"
125: python3 release_apkg.py
126: 
127: echo "==> [3/6] Committing changes"
128: git add -A
129: CHANGED=0
130: if git diff --cached --quiet; then
131:   echo "    (nothing to commit)"
132: else
133:   git commit -m "$COMMIT_MSG"
134:   CHANGED=1
135: fi
136: 
137: if [ "$LOCAL" -eq 1 ]; then
138:   echo ""
139:   echo "Local run complete (synced, exported, committed)."
140:   exit 0
141: fi
142: 
143: if [ "$CHANGED" -eq 0 ]; then
144:   echo "    No changes detected. Nothing to push or release."
145:   exit 0
146: fi
147: 
148: echo "==> [4/6] Pushing to origin/main"
149: git push origin main
150: 
151: echo "==> [5/6] Creating GitHub release (--target main: tag points at the pushed commit)"
152: NOTES="Automated release from commit: $COMMIT_MSG
153: 
154: Install: import the .apkg in Anki, then delete the sample cards — the note type is retained."
155: gh release create "$NEW_TAG" dist/anki-japanese-template.apkg \
156:   --target main \
157:   --title "$NEW_TAG" \
158:   --notes "$NOTES" \
159:   --latest
160: 
161: # The release tag was created on the REMOTE by gh above; fetch it so local
162: # tag bookkeeping stays in sync for the next run's version bump.
163: git fetch origin "refs/tags/*:refs/tags/*" --quiet
164: 
165: echo "==> [6/6] Done"
166: echo ""
167: echo "All done: synced, exported, committed, pushed, released as $NEW_TAG"
````

## File: IMPLEMENTATION_PLAN.md
````markdown
  1: # IMPLEMENTATION_PLAN.md — task graph + status
  2: 
  3: The graph is part of the plan (not a substitute): the graph says *what
  4: depends on what*, the task entries say *what each node means*. This is a
  5: task/slice graph, not a todo list (`Build frontend` would not qualify).
  6: 
  7: ## Dependency graph
  8: 
  9: ```text
 10:                     ┌───────────────────┐
 11:                     │ T1 fields bootstrap│
 12:                     └─────────┬─────────┘
 13:                               │
 14:                     ┌─────────┴─────────┐
 15:                     ↓                   ↓
 16:             ┌───────────────┐   ┌───────────────┐
 17:             │ T2 front modes │   │ T3 back grid  │
 18:             └───────┬───────┘   └───────┬───────┘
 19:                     │                   │
 20:                     ↓                   ↓
 21:             ┌───────────────┐   ┌───────────────┐
 22:             │ T4 mature mode │   │ T5 compactor  │
 23:             └───────┬───────┘   └───────┬───────┘
 24:                     │                   │
 25:                     └─────────┬─────────┘
 26:                               ↓
 27:                     ┌───────────────────┐
 28:                     │ T6 audio/lightbox │
 29:                     └─────────┬─────────┘
 30:                               │
 31:                               ↓
 32:                     ┌───────────────────┐
 33:                     │ T7 responsive/    │
 34:                     │ themes/density    │
 35:                     └─────────┬─────────┘
 36:                               │
 37:                               ↓
 38:                     ┌───────────────────┐
 39:                     │ T8 verify gate +  │
 40:                     │ regression tests  │
 41:                     └─────────┬─────────┘
 42:                               │
 43:                               ↓
 44:                     ┌───────────────────┐
 45:                     │ T9 release loop   │
 46:                     │ (sync/export/tag) │
 47:                     └─────────┬─────────┘
 48:                               │
 49:                               ↓
 50:                     ┌───────────────────┐
 51:                     │ T10 methodology   │
 52:                     │ refactor (this)   │
 53:                     └─────────┬─────────┘
 54:                               │
 55:                               ↓
 56:                     ┌───────────────────┐
 57:                     │ T11 empty-field   │
 58:                     │ collapse          │
 59:                     └─────────┬─────────┘
 60:                               │
 61:                               ↓
 62:                     ┌───────────────────┐
 63:                     │ T12 minimal-       │
 64:                     │ interface redesign │
 65:                     └─────────┬─────────┘
 66:                               │
 67:                               ↓
 68:                     ┌───────────────────┐
 69:                     │ T13 editorial     │
 70:                     │ redesign & polish │
 71:                     └───────────────────┘
 72: ```
 73: 
 74: Dependencies: `T1 → {T2, T3} → {T4, T5} → T6 → T7 → T8 → T9 → T10 → T11 → T12 → T13`.
 75: T2/T3 are parallelizable; T4 needs T2; T5 needs T3.
 76: 
 77: ## Tasks
 78: 
 79: - **T1 — Field bootstrap.** `fetch_anki_fields.py` + gitignored
 80:   `.anki_fields.json`; agents read exact names per session. Status: COMPLETE.
 81: - **T2 — Front modes.** Sentence/Expression, listening button,
 82:   Frequency-legacy path, fallback, cloze-trio rebuild. Status: COMPLETE.
 83: - **T3 — Back grid.** Tags, word header, sentence/translation/context, side
 84:   column, footer; DOM-reuse-safe controllers. Status: COMPLETE.
 85: - **T4 — Mature Word Mode.** `LONG_INTERVAL_DAYS` gate, desktop-only
 86:   AnkiConnect interval retrieval (mobile intentionally degrades to the
 87:   sentence front), fallbacks, anti-flash reveal. Status: COMPLETE.
 88: - **T5 — Definition Compactor + truncator.** CSS §6b structural scoping +
 89:   §6c 3-line one-way expand. Status: COMPLETE.
 90: - **T6 — Audio + lightbox.** Native delegation, debounce, sibling source;
 91:   backdrop/`Escape` close. Status: COMPLETE.
 92: - **T7 — Responsive/themes/density.** Clamps, container queries + fallback,
 93:   zero-reflow ruby, Tokyo Night / Aki Paper, backdrop, reduced motion.
 94:   Status: COMPLETE.
 95: - **T8 — Verify gate + regression tests.** `verify`, `test_compactor.py`,
 96:   `test_templates.py`, `test_layout.py`, CI. Status: COMPLETE (this refactor
 97:   introduces `verify` + CI; suites pre-exist).
 98: - **T9 — Release loop.** `sync_to_anki.py` (pre-sync snapshots),
 99:   `release_apkg.py` (`exportPackage`), `finish.sh` one-command flow, apkg as
100:   Release asset only. Status: COMPLETE.
101: - **T10 — Methodology refactor.** Adopt PRODUCT/MVP/ARCHITECTURE/QUALITY/
102:   TEST_STRATEGY/PLAN + slim AGENTS.md + `verify`/CI without changing card
103:   behavior. Status: COMPLETE (`./verify` 129/129 green; released with this
104:   commit).
105: - **T11 — Empty-field collapse.** QUALITY rule + `:has()` shell guards +
106:   degenerate-content self-removal + enclosure parser test (§10). Turns the
107:   standing conditional coverage into a total, mechanically enforced
108:   guarantee. Status: COMPLETE (`./verify` 135/135 green; released with this
109:   commit).
110: - **T12 — Minimal-interface redesign.** Front = pure retrieval surface
111:   (hidden behavioral probes; listening as a hidden-by-default resolver:
112:   classic audio-only fields OR `#listening` tag; sentence front as the
113:   universal fallback). Back = typography hierarchy (word → pitch quiet →
114:   compacted meaning → context grid sentence+picture → secondary collapsed
115:   behind `More ▾`), discreet Context/Word/Listening state label,
116:   `F` full-card furigana + `T` translation shortcuts, tags/frequency
117:   badges removed (tags are behavioral metadata). Bug fixes: `{{Type}}`/
118:   `note:` search clause removed (wrong value), mobile `.word-meta-row`
119:   specificity, JS syntax gate added after an unbalanced-brace regression
120:   was caught by visual QA. Status: COMPLETE (`./verify` 168/168 green).
121: - **T13 — Editorial redesign & aesthetic polish.** Visual transformation from
122:   sterile dashboard to refined Japanese editorial reading interface. Removal of
123:   retrieval-state UI (`.retrieval-state`, "Context"/"Word"/"Listening") in favor
124:   of pure content hierarchy. Refined typography scale: restrained hero headword
125:   `clamp()`, editorial definition with no harsh dividing lines or boxes,
126:   quiet audio affordances (34px/30px buttons with subtle borders), and an
127:   asymmetric context grid balancing the Japanese sentence against intentional
128:   media proportions. Fixed empty-shell collapse bug for `.context-grid` and
129:   `.context-main`. Verified across 10 visual regression scenarios.
130:   Status: COMPLETE.
131: - **T14 — Listening Policy B + audio source fix + mature exact-card.**
132:   Listening Policy B: `#listening` activates the listening front only when
133:   usable audio exists (`hasUsableAudio` on `.raw-audio-source`); `#listening`
134:   + no audio falls back to the normal sentence front. Dead/duplicate views
135:   removed so exactly one listening button is ever visible. Listening audio
136:   source fix: the tag-listening-view binds to the actual `{{Sentence Audio}}`
137:   field (label 文), falling back to `{{Word Audio}}` (label 言葉) — never the
138:   hardcoded `play:a:0` (which plays the first audio field = Word Audio on
139:   listening cards). Mature exact-card: content-search fallback uses Sentence
140:   then cloze-body discriminators, never picks candidate 0, fails safely on
141:   ambiguity. R shortcut is Anki-owned (removed from the back's shortcut UI).
142:   Audio terminology: "progress ring" → "playback indicator". finish.sh
143:   ordering: push main before `gh release create --target main`. Tests:
144:   `test_front_modes.py` (8 cases), `test_mature_content.py` (6 cases),
145:   structural invariants in `test_templates.py` (§§6d–6f, 8c, 9). Docs audit
146:   across all methodology files. Status: COMPLETE.
147: 
148: - **T15 — Hero single-row density (R2).** Back `hero-header`: word + freq/
149:   pitch/audio share one flex row on wide screens (container + media fallback),
150:   tight stacked column on phones; vertical rhythm tightened (`--gap-section`,
151:   definition/separator/context gaps, quieter shortcut hints); picture fills the
152:   parallel row (44vh / 46vw-640px desktop, compact mobile cap unchanged).
153:   Empty-collapse + hierarchy + touch targets preserved; layout-probe proof in
154:   `test_layout.py` (shared-row desktop, stacked mobile), structural guards in
155:   `test_templates.py`. Status: COMPLETE.
156: 
157: ## Roadmap (evolution loop input, not committed scope)
158: 
159: - R1: extra compactor fixtures if Yomitan markup drifts.
160: - R2: further density tuning only with layout-probe proof.
161: - R3: new ADRs only for decisions with alternatives + consequences.
162: 
163: ## State updates
164: 
165: Mark a task COMPLETE only after targeted checks + `./verify` + (for
166: template/CSS changes) the `finish.sh` release run. Update technical docs
167: only when something actually changed — no churn.
````

## File: tests/test_layout.py
````python
  1: #!/usr/bin/env python3
  2: """Headless layout verification for the density pass.
  3: 
  4: Renders the REAL stylesheet plus template-shaped HTML in Chrome headless
  5: (google-chrome-stable is available on this machine) and asserts layout
  6: invariants that pure text tests cannot catch:
  7: 
  8:   - card height is content-driven (back card < 90% of viewport height
  9:     on a rich desktop card, i.e. no viewport fill)
 10:   - no horizontal overflow / clipping
 11:   - furigana (rt) never overlaps the line above it
 12:   - hierarchy: headword font > sentence font > definition font > notes
 13:   - truncator: a long definition clamps at 3 lines until expanded
 14:   - listening front keeps the audio button a comfortable target
 15:   - definition expand still works (JS one-way expand)
 16: 
 17: Usage: python3 tests/test_layout.py
 18: Requires: google-chrome-stable on PATH. Skipped gracefully if absent
 19:         (finish.sh runs it as part of step 0 when present).
 20: """
 21: import json
 22: import os
 23: import re
 24: import shutil
 25: import subprocess
 26: import sys
 27: import tempfile
 28: 
 29: HERE = os.path.dirname(os.path.abspath(__file__))
 30: ROOT = os.path.dirname(HERE)
 31: CSS = os.path.join(ROOT, "Card 1 - Style.css")
 32: CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")
 33: 
 34: PASS = 0
 35: FAIL = 0
 36: 
 37: 
 38: def check(name, cond, detail=""):
 39:     global PASS, FAIL
 40:     tag = "PASS" if cond else "FAIL"
 41:     print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
 42:     if cond:
 43:         PASS += 1
 44:     else:
 45:         FAIL += 1
 46: 
 47: 
 48: # ---------------------------------------------------------------- HTML fixture
 49: # Back card with every block populated: furigana headword, pitch, audio,
 50: # long definition, furigana sentence, picture, More section (translation,
 51: # extended definition, notes), source footer. New minimal hierarchy:
 52: # word → meaning → context (sentence + picture) → More ▾.
 53: BACK_CARD = """<!doctype html><html><head><meta charset="utf-8">
 54: <style>
 55: html,body{margin:0;padding:0;}
 56: /* minimal Anki stand-ins: replay link + fonts so JS runs like in Anki */
 57: </style>
 58: <style>
 59: __CSS__
 60: </style></head><body>
 61: <div class="card back-card">
 62: <div class="card-wrapper back-card">
 63:   <div class="card-container">
 64:     <div class="hero-header">
 65:       <div class="hero-side hero-side-left">
 66:         <div class="frequency-badge"><span class="frequency-stars">★★★★☆</span></div>
 67:         <div class="audio-row">
 68:           <span class="audio-btn-wrapper">
 69:             <button type="button" class="circular-audio-btn small-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">言葉</span></span></button>
 70:             <span class="raw-audio-source"><a class="replay-button" href="#">replay</a></span>
 71:           </span>
 72:         </div>
 73:       </div>
 74:       <div class="hero-word-wrap"><div class="word-display" id="word"><ruby>澄<rt>す</rt></ruby>ます</div></div>
 75:       <div class="hero-side hero-side-right">
 76:         <div class="pitch-quiet">[0]</div>
 77:         <div class="audio-row">
 78:           <span class="audio-btn-wrapper">
 79:             <button type="button" class="circular-audio-btn small-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">文</span></span></button>
 80:             <span class="raw-audio-source"><a class="replay-button" href="#">replay</a></span>
 81:           </span>
 82:         </div>
 83:       </div>
 84:     </div>
 85:     <div class="definition-box primary-definition" id="def">
 86:       <div class="yomitan-glossary"><ol>
 87:         <li><div data-sc-name="語義G">水などを濁りのない状態にする。とても長い定義のテキストで、三行を超えることを保証するためにさらに文字を追加している。三行目に入ってもまだ続くほど十分に長い定義であることを確認するための文です。全幅レイアウトでも確実に三行を超えるように、さらに追加の検証用テキストをここに置く。この文が折り返して四行目に達すれば、切り詰め機能が正しく発動するはずである。</div>
 88:         <div data-sc-name="語義G">雑念を払って、心を落ち着かせる。二番目の語義。</div>
 89:         <div data-sc-name="語義G">一つのことに注意を向ける。三番目の語義（隠れるはず）。</div>
 90:         <div data-sc-name="補説G">supplementary (hidden)</div></li>
 91:       </ol></div>
 92:       <!-- Font-independent overflow guarantee: CI runners have Chrome but
 93:            no CJK fonts, so the Japanese text above renders with fallback
 94:            tofu metrics and may fit within the 3-line cap. The fixed-height
 95:            spacer makes scrollHeight > clientHeight true in EVERY
 96:            environment, so the truncator checks never depend on font
 97:            availability. -->
 98:       <div style="height:140px"></div>
 99:     </div>
100:     <div class="context-grid">
101:       <div class="context-main">
102:         <div class="sentence-japanese" id="sentence"><ruby>心<rt>こころ</rt></ruby>を<ruby>澄<rt>す</rt></ruby>ませて、<b>音楽</b>を聴く。長い文章が二行に折り返される場合の検証も兼ねている。</div>
103:       </div>
104:       <div class="context-picture">
105:         <div class="picture-container"><img id="pic" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E"></div>
106:       </div>
107:     </div>
108:     <div class="more-section" hidden>
109:       <div class="translation-box"><div class="translation-hint">Translation</div>
110:         <div class="translation-text">To clear one's mind and listen to music.</div></div>
111:       <div class="html-content secondary-block">Additional context paragraph.</div>
112:       <div class="html-content secondary-block">漢字のメモ: 澗 — radical 水.</div>
113:       <div class="html-content secondary-block extended-full">Full extended definition text that stays untruncated.</div>
114:     </div>
115:     <button type="button" class="more-toggle" aria-expanded="false">More <span class="more-caret">▾</span></button>
116:     <div class="shortcut-hints"><span class="shortcut-item"><kbd>Z</kbd> hints</span></div>
117:     <div class="source-footer">SOURCE — some novel</div>
118:   </div>
119: </div>
120: </div>
121: <script>
122: window.expandDefinition = function(element) {
123:   if (element.classList.contains('is-expanded')) return;
124:   element.classList.add('is-expanded');
125: };
126: window.initDefinitionTruncation = function() {
127:   document.querySelectorAll('.primary-definition').forEach(function(box) {
128:     const overflows = box.scrollHeight > box.clientHeight + 2;
129:     box.classList.toggle('is-truncated', overflows);
130:   });
131: };
132: window.initDefinitionTruncation();
133: </script>
134: </body></html>"""
135: 
136: FRONT_SENTENCE = """<!doctype html><html><head><meta charset="utf-8">
137: <style>__CSS__</style></head><body>
138: <div class="card"><div class="card-wrapper">
139:   <div class="card-container">
140:     <div class="sentence-display" id="sent">彼は<b>約束</b>を<ruby>守<rt>まも</rt></ruby>らなかった。</div>
141:   </div>
142: </div></div>
143: </body></html>"""
144: 
145: FRONT_LISTENING = """<!doctype html><html><head><meta charset="utf-8">
146: <style>__CSS__</style></head><body>
147: <div class="card"><div class="card-wrapper listening-mode">
148:   <div class="card-container">
149:     <div class="listening-view" id="listening">
150:       <div class="audio-btn-wrapper">
151:         <button type="button" class="circular-audio-btn large-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">文</span></span></button>
152:       </div>
153:     </div>
154:   </div>
155: </div></div>
156: </body></html>"""
157: 
158: 
159: # ---------------------------------------------------------------- probing JS
160: PROBE = """(() => {
161:   const r = {};
162:   const wrapper = document.querySelector('.card-wrapper');
163:   const card = document.querySelector('.card');
164:   r.wrapperH = wrapper.getBoundingClientRect().height;
165:   r.viewportH = window.innerHeight;
166:   r.docScrollW = document.documentElement.scrollWidth;
167:   r.docClientW = document.documentElement.clientWidth;
168:   // overflow-x anywhere?
169:   r.hOverflow = r.docScrollW > r.docClientW + 1;
170:   // furigana overlap: rt boxes vs previous line — collect any rt whose
171:   // top is above the previous sibling line's bottom is hard generically;
172:   // instead verify every rt's top >= its ruby's parent's top (rt never
173:   // escapes the container) AND that rt boxes do not overlap the element
174:   // above: compare first rt top vs sentence/word container top.
175:   const word = document.querySelector('.word-display');
176:   if (word) {
177:     const rb = word.getBoundingClientRect();
178:     const rt = word.querySelector('rt');
179:     r.wordFont = parseFloat(getComputedStyle(word).fontSize);
180:     if (rt) { const rtb = rt.getBoundingClientRect();
181:       r.wordRtInside = rtb.top >= rb.top - 0.5 && rtb.bottom <= rb.bottom + 0.5; }
182:   }
183:   const sent = document.querySelector('#sentence, .sentence-japanese');
184:   if (sent) {
185:     r.sentFont = parseFloat(getComputedStyle(sent).fontSize);
186:     const rt = sent.querySelector('rt');
187:     const sb = sent.getBoundingClientRect();
188:     if (rt) { const rtb = rt.getBoundingClientRect();
189:       r.sentRtInside = rtb.top >= sb.top - 0.5; }
190:     r.sentH = sb.height;
191:   }
192:     const def = document.querySelector('#def');
193:   if (def) {
194:     r.defFont = parseFloat(getComputedStyle(def).fontSize);
195:     const cs = getComputedStyle(def);
196:     r.defLineH = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.5;
197:     r.defPadTop = parseFloat(cs.paddingTop) || 0;
198:     r.defClampedH = def.getBoundingClientRect().height;
199:     r.defScrollH = def.scrollHeight;
200:     r.defTruncated = def.classList.contains('is-truncated');
201:     // expand and re-measure
202:     window.expandDefinition(def);
203:     r.defExpandedH = def.getBoundingClientRect().height;
204:   }
205:   const notes = document.querySelector('.secondary-block');
206:   if (notes && def) {
207:     r.notesFont = parseFloat(getComputedStyle(notes).fontSize);
208:     r.hierarchy = r.wordFont > r.sentFont && r.sentFont > r.defFont && r.defFont >= r.notesFont;
209:   }
210:   const pic = document.querySelector('#pic');
211:   if (pic) { const pb = pic.getBoundingClientRect(); r.picH = pb.height; r.picW = pb.width; }
212:   const listening = document.querySelector('#listening');
213:   if (listening) {
214:     const lb = listening.getBoundingClientRect();
215:     const btn = listening.querySelector('.circular-audio-btn');
216:     r.listenH = lb.height;
217:     r.listenBtn = btn.getBoundingClientRect().height;
218:   }
219:   // Context grid: picture beside the sentence on wide screens.
220:   const ctxPic = document.querySelector('.context-picture');
221:   const ctxMain = document.querySelector('.context-main');
222:   if (ctxPic && ctxMain && innerWidth >= 768) {
223:     r.twoCol = ctxPic.getBoundingClientRect().left > ctxMain.getBoundingClientRect().right;
224:     r.sideW = ctxPic.getBoundingClientRect().width;
225:     r.mainW = ctxMain.getBoundingClientRect().width;
226:   }
227:   // Secondary info collapsed by default; More toggle present.
228:   const more = document.querySelector('.more-section');
229:   const moreBtn = document.querySelector('.more-toggle');
230:   if (more && moreBtn) {
231:     r.moreCollapsed = more.hidden === true
232:       && moreBtn.getAttribute('aria-expanded') === 'false';
233:     r.moreBelowFold = more.getBoundingClientRect().height;
234:   }
235:   const footer = document.querySelector('.source-footer');
236:   if (footer && wrapper) {
237:     r.footerInside = footer.getBoundingClientRect().bottom <= wrapper.getBoundingClientRect().bottom + 1;
238:   }
239:   // Keyboard hints: visible on desktop, hidden on touch phones (dead weight).
240:   const hints = document.querySelector('.shortcut-hints');
241:   if (hints) { r.hintsDisplay = getComputedStyle(hints).display; }
242:   // Hero header: 3-column grid (left | word | right) on wide screens,
243:   // word stacked on its own row with sides below on narrow phones.
244:   // The word must stay truly centered: |wordCenter - headerCenter| ≈ 0.
245:   const hero = document.querySelector('.hero-header');
246:   const heroWord = document.querySelector('.hero-word-wrap');
247:   const heroLeft = document.querySelector('.hero-side-left');
248:   const heroRight = document.querySelector('.hero-side-right');
249:   const heroAudio = document.querySelector('.hero-side .circular-audio-btn');
250:   if (hero && heroWord && heroLeft && heroRight && word) {
251:     r.heroDisplay = getComputedStyle(hero).display;
252:     r.heroAreas = getComputedStyle(hero).gridTemplateAreas || '';
253:     const hb = hero.getBoundingClientRect();
254:     const wb = word.getBoundingClientRect();
255:     r.heroCenterOff = Math.abs((wb.left + wb.width / 2) - (hb.left + hb.width / 2));
256:     const lb = heroLeft.getBoundingClientRect();
257:     const rb = heroRight.getBoundingClientRect();
258:     // split check: left cell ends at/before word start, right starts at/after word end (wide)
259:     // stacked check (narrow): word bottom above both sides' tops
260:     r.heroSplit = (lb.right <= wb.left + 2) && (rb.left >= wb.right - 2);
261:     r.heroStacked = (wb.bottom <= lb.top + 1) && (wb.bottom <= rb.top + 1);
262:     if (heroAudio) r.heroAudioSize = heroAudio.getBoundingClientRect().width;
263:   }
264:   // Context grid top-anchor: the picture must sit at the grid top no
265:   // matter how long the sentence grows (never vertically centered).
266:   const ctxGrid = document.querySelector('.context-grid');
267:   const ctxPicBox = document.querySelector('.context-picture');
268:   if (ctxGrid && ctxPicBox) {
269:     r.picTopOff = ctxPicBox.getBoundingClientRect().top - ctxGrid.getBoundingClientRect().top;
270:   }
271:   return r;
272: })()"""
273: 
274: 
275: def render(html, width, height):
276:     """Chrome headless screenshot + JS probe via --dump-dom is awkward;
277:     use the DevTools-free trick: virtual-time + console.log of the probe,
278:     captured from chrome's stderr? No — instead write the probe result
279:     into the DOM title and read it from the dumped DOM."""
280:     probe_html = html.replace(
281:         "</body>",
282:         f"<script>document.title = JSON.stringify({PROBE});</script></body>",
283:     )
284:     with tempfile.TemporaryDirectory() as td:
285:         path = os.path.join(td, "card.html")
286:         with open(path, "w", encoding="utf-8") as f:
287:             f.write(probe_html)
288:         try:
289:             out = subprocess.run(
290:                 [CHROME, "--headless=new", "--disable-gpu",
291:                  "--no-sandbox", "--hide-scrollbars",
292:                  f"--window-size={width},{height}",
293:                  "--virtual-time-budget=2000",
294:                  "--dump-dom", f"file://{path}"],
295:                 capture_output=True, text=True, timeout=60,
296:             ).stdout
297:         except subprocess.TimeoutExpired:
298:             return None
299:     import re
300:     m = re.search(r"<title>(.*?)</title>", out, re.S)
301:     if not m:
302:         return None
303:     try:
304:         return json.loads(m.group(1))
305:     except json.JSONDecodeError:
306:         return None
307: 
308: 
309: def main():
310:     if not CHROME:
311:         print("[SKIP] no headless Chrome found — layout checks skipped")
312:         return 0
313:     css = open(CSS, encoding="utf-8").read()
314:     # Headless virtual-time freezes the card entrance animations
315:     # (fadeInUp `both` fill) mid-flight, shifting measured Y positions by
316:     # up to 10px. Kill animations/transitions in the harness only so probes
317:     # measure final layout; the product animations are untouched.
318:     css += "\n*,*::before,*::after{animation:none!important;transition:none!important;}\n"
319: 
320:     # ---- Desktop back card (1440x900, rich card) ----
321:     back = render(BACK_CARD.replace("__CSS__", css), 1440, 900)
322:     check("desktop back: probe returned", back is not None)
323:     if back:
324:         check("desktop back: content-driven card (rich card < 100% viewport)",
325:               back["wrapperH"] < back["viewportH"],
326:               f"wrapper={back['wrapperH']:.0f} viewport={back['viewportH']}")
327:         check("desktop back: no horizontal overflow", not back["hOverflow"])
328:         check("desktop back: word furigana stays inside its line box",
329:               back.get("wordRtInside", True))
330:         check("desktop back: sentence furigana stays inside its block",
331:               back.get("sentRtInside", True))
332:         check("desktop back: hierarchy word > sentence > definition > notes",
333:               back.get("hierarchy", False),
334:               f"word={back.get('wordFont')} sent={back.get('sentFont')} "
335:               f"def={back.get('defFont')} notes={back.get('notesFont')}")
336:         check("desktop back: long definition IS truncated by JS",
337:               back.get("defTruncated", False))
338:         check("desktop back: clamped height ≈ pad + 3 line-heights",
339:               abs(back["defClampedH"] - (back["defPadTop"] + 3 * back["defLineH"])) <= 8,
340:               f"clamped={back['defClampedH']:.0f} expected={back['defPadTop'] + 3*back['defLineH']:.0f}")
341:         check("desktop back: expand grows the definition (one-way)",
342:               back.get("defExpandedH", 0) > back.get("defClampedH", 0) + 4)
343:         check("desktop back: image height capped (<= 45vh, fills parallel row)",
344:               back.get("picH", 0) <= 0.45 * back["viewportH"] + 2,
345:               f"picH={back.get('picH', 0):.0f}")
346:         check("desktop back: hero is a 3-col grid with meta split left/right",
347:               back.get("heroDisplay", "") == "grid"
348:               and "left" in back.get("heroAreas", "")
349:               and back.get("heroSplit", False) is True,
350:               f"display={back.get('heroDisplay')} areas={back.get('heroAreas')} split={back.get('heroSplit')}")
351:         check("desktop back: word truly centered (off-center <= 8px)",
352:               back.get("heroCenterOff", 999) <= 8,
353:               f"off={back.get('heroCenterOff', 999):.1f}px")
354:         check("desktop back: hero audio stays tappable (>= 32px)",
355:               back.get("heroAudioSize", 0) >= 32,
356:               f"audio={back.get('heroAudioSize', 0):.0f}")
357:         check("desktop back: context grid engaged (picture beside sentence)",
358:               back.get("twoCol", False),
359:               f"main={back.get('mainW', 0):.0f} pic-col={back.get('sideW', 0):.0f}")
360:         check("desktop back: picture column is the minority width",
361:               back.get("sideW", 1) < back.get("mainW", 0))
362:         check("desktop back: secondary info collapsed behind More by default",
363:               back.get("moreCollapsed", False))
364:         check("desktop back: footer inside the card wrapper",
365:               back.get("footerInside", False))
366:         check("desktop back: keyboard hints visible (physical keyboard)",
367:               back.get("hintsDisplay", "none") != "none",
368:               f"display={back.get('hintsDisplay')}")
369: 
370:     # ---- Back card without picture (single column) ----
371:     nopic_html = re.sub(r'<div class="context-picture">[\s\S]*?</div>\s*</div>', '</div>', BACK_CARD)
372:     nopic = render(nopic_html.replace("__CSS__", css), 1440, 900)
373:     check("desktop back (no picture): probe returned", nopic is not None)
374:     if nopic:
375:         check("desktop back (no picture): single column (no twoCol)", not nopic.get("twoCol", False))
376:         check("desktop back (no picture): no horizontal overflow", not nopic["hOverflow"])
377: 
378:     # ---- Long sentence: picture stays top-anchored, never dragged down ----
379:     long_html = BACK_CARD.replace(
380:         "長い文章が二行に折り返される場合の検証も兼ねている。",
381:         "長い文章が二行に折り返される場合の検証も兼ねている。" * 30)
382:     longcard = render(long_html.replace("__CSS__", css), 1440, 900)
383:     check("desktop back (long sentence): probe returned", longcard is not None)
384:     if longcard:
385:         check("desktop back (long sentence): no horizontal overflow", not longcard["hOverflow"])
386:         check("desktop back (long sentence): picture top-anchored (top offset <= 12px)",
387:               longcard.get("picTopOff", 999) <= 12,
388:               f"picTopOff={longcard.get('picTopOff', 999):.0f}")
389: 
390:     # ---- Mobile back card (A50-ish 412x892) ----
391:     mob = render(BACK_CARD.replace("__CSS__", css), 412, 892)
392:     check("mobile back: probe returned", mob is not None)
393:     if mob:
394:         check("mobile back: no horizontal overflow", not mob["hOverflow"])
395:         check("mobile back: hero stacks word above sides", mob.get("heroStacked", False) is True)
396:         check("mobile back: word stays centered (off-center <= 8px)",
397:               mob.get("heroCenterOff", 999) <= 8,
398:               f"off={mob.get('heroCenterOff', 999):.1f}px")
399:         check("mobile back: hero audio stays tappable (>= 32px)",
400:               mob.get("heroAudioSize", 0) >= 32,
401:               f"audio={mob.get('heroAudioSize', 0):.0f}")
402:         check("mobile back: stacked (no context-grid columns)", not mob.get("twoCol", False))
403:         check("mobile back: no forced viewport fill",
404:               mob["wrapperH"] < 0.95 * mob["viewportH"],
405:               f"wrapper={mob['wrapperH']:.0f} viewport={mob['viewportH']}")
406:         check("mobile back: sentence font stays >= 1rem", mob.get("sentFont", 1) >= 16)
407:         check("mobile back: keyboard hints hidden (no physical keyboard)",
408:               mob.get("hintsDisplay", "") == "none",
409:               f"display={mob.get('hintsDisplay')}")
410: 
411:     # ---- Front sentence card ----
412:     fr = render(FRONT_SENTENCE.replace("__CSS__", css), 1440, 900)
413:     check("front sentence: probe returned", fr is not None)
414:     if fr:
415:         check("front sentence: no horizontal overflow", not fr["hOverflow"])
416:         check("front sentence: content-driven (wrapper < 50% viewport)",
417:               fr["wrapperH"] < 0.5 * fr["viewportH"],
418:               f"wrapper={fr['wrapperH']:.0f}")
419: 
420:     # ---- Front listening card ----
421:     fl = render(FRONT_LISTENING.replace("__CSS__", css), 1440, 900)
422:     check("front listening: probe returned", fl is not None)
423:     if fl:
424:         check("front listening: button is a comfortable target (>= 64px)",
425:               fl.get("listenBtn", 0) >= 64, f"btn={fl.get('listenBtn')}")
426:         check("front listening: view height in 20-35vh band",
427:               0.20 * fl["viewportH"] <= fl.get("listenH", 0) <= 0.36 * fl["viewportH"],
428:               f"listenH={fl.get('listenH', 0):.0f}")
429: 
430:     print()
431:     print(f"{PASS} passed, {FAIL} failed")
432:     return 1 if FAIL else 0
433: 
434: 
435: if __name__ == "__main__":
436:     sys.exit(main())
````

## File: AGENTS.md
````markdown
  1: # AGENTS.md — agent entry point
  2: 
  3: Modern, ultra-compact Japanese sentence-mining note type for Anki.
  4: Desktop: Arch Linux Qt6 WebEngine (widescreen, dense). Mobile: Galaxy A50
  5: AnkiDroid WebKit (ultra-compact). This file is the entry point — the
  6: methodology lives in the repository structure, not in this file.
  7: 
  8: ## Authority hierarchy
  9: 
 10: ```text
 11: PRODUCT.md             → what the product must do
 12: MVP.md                 → current scope (agents never widen it unasked)
 13: ARCHITECTURE.md        → technical structure (+ docs/adr/ for lasting decisions)
 14: QUALITY.md             → properties that must remain true
 15: TEST_STRATEGY.md       → how those properties are verified
 16: IMPLEMENTATION_PLAN.md → task graph + status (work the next READY task)
 17: AGENTS.md (this file)  → how to navigate and operate within all of the above
 18: ```
 19: 
 20: `CODE ≠ specification.` Code implements the specs; tests enforce them.
 21: 
 22: ## Read order
 23: 
 24: 1. `PRODUCT.md` + `MVP.md` — what and what-now.
 25: 2. `ARCHITECTURE.md` (+ relevant `docs/adr/`) — how it is structured.
 26: 3. `QUALITY.md` + `TEST_STRATEGY.md` — invariants + enforcement.
 27: 4. `IMPLEMENTATION_PLAN.md` — current work and dependencies.
 28: 5. Session bootstrap below, then the existing code.
 29: 
 30: ## Development loop (the repeating unit)
 31: 
 32: ```text
 33: SELECT READY TASK → UNDERSTAND → SMALL CONTRACT → TEST/CHECK → IMPLEMENT
 34:   → TARGETED CHECKS → ./verify → UPDATE STATE/DOCS (only if changed)
 35:   → COMMIT → CI → NEXT READY TASK
 36: ```
 37: 
 38: - Work the next task whose dependencies are COMPLETE; never `Build the MVP`.
 39: - Split the task into the smallest meaningful contracts (validated bricks);
 40:   write the test/check before or alongside each brick, then implement only
 41:   enough to satisfy it.
 42: - Targeted suites while iterating, `./verify` before declaring done.
 43: - Bugs branch inside the loop: diagnose → fix → **add regression test** →
 44:   verify → continue. After ~3 blind retries, stop and diagnose root cause
 45:   (stronger model, then human); fix the cause class (spec, invariant, test,
 46:   architecture, tooling) so the system gets stronger.
 47: - MVP completion adds an end-to-end validation (real user journey in
 48:   `MVP.md`) before release; post-MVP changes go product decision →
 49:   architecture reassessment → tasks → loop → release.
 50: 
 51: ## Operating rules
 52: 
 53: ### 0. Field-Name Bootstrap (fields live in Anki, never in the repo)
 54: 
 55: Note-type fields are managed **exclusively inside the Anki UI**. At session
 56: start, **before** any template work, run `python3 fetch_anki_fields.py` and
 57: read the gitignored `.anki_fields.json` for exact names/descriptions. If
 58: Anki/Anki-Connect is unreachable, **stop and ask the user to start Anki** —
 59: never guess, invent, or reuse field names from memory or chat history.
 60: 
 61: ### 1. Local files are the single source of truth
 62: 
 63: All edits happen in the local `.template.anki` / `.css` files. Never instruct
 64: edits inside the Anki UI. Tooling is stdlib-only Python.
 65: 
 66: ### 2. Release workflow (one command, not five)
 67: 
 68: After **every** template/CSS modification, finish with exactly one command:
 69: 
 70: ```bash
 71: ./finish.sh "<semantic commit message>"
 72: # --local: sync + export + commit only · --minor: bump v1.x.0
 73: # --prompt "text": archive prompt (rule 3) before anything runs
 74: ```
 75: 
 76: Chain (stops on first failure): `0.` `./verify` (side-effect-free gate) →
 77: `1.` version stamp → `2.` `sync_to_anki.py` (pre-sync snapshot to gitignored
 78: `backups/<timestamp>/`) → `3.` `release_apkg.py` (deck
 79: `My Life Decks::Japanese::anki-japanese-template` via `exportPackage` to
 80: gitignored `dist/*.apkg`) → `4.` commit → `5.` push main → `6.`
 81: `gh release create --target main` (tag points at the pushed commit) →
 82: fetch the remote tag. The apkg ships as a Release asset, never in the repo.
 83: Do not skip, reorder, or substitute steps.
 84: 
 85: ### 3. Prompt archiving
 86: 
 87: Archive every new user prompt to `chat_history/opencode_prompts.txt`
 88: (prompt text + `---` separator) before/with its commit — preferably via
 89: `./finish.sh --prompt "<user prompt>" "<message>"`.
 90: 
 91: ### 4. Technical constraints (summaries; full rules in QUALITY.md)
 92: 
 93: Zero-reflow furigana (hidden, hover/tap reveal, absolute ruby) · native-only
 94: circular audio (`文`/`言葉`, sibling replay link, debounce, playback
 95: indicator — not true progress) · `R` is Anki-owned (never a template
 96: shortcut) · Mature Word Mode (`LONG_INTERVAL_DAYS = 365`,
 97: desktop-only AnkiConnect content search — one fallback-only path for
 98: reviewer and Browse previewer (live `guiCurrentCard` read removed),
 99: never picks
100: candidate 0, sentence fallback, mobile intentionally degrades to the
101: sentence front and makes no network request (`post` UA-guard), listening
102: untouched,
103: anti-flash gate) · `#listening` requires usable audio (Policy B: falls back
104: to sentence without it) · `:has()` is intentional architecture · no debug
105: badges or verbose labels · vanilla scoped JS resilient to WebView DOM re-use.
106: 
107: ## File map
108: 
109: `Card 1 - Front.template.anki` (front modes + Mature Word Mode) ·
110: `Card 1 - Back.template.anki` (grid, audio, lightbox) ·
111: `Card 1 - Style.css` (themes, layout, compactor §6b, truncator §6c) ·
112: `fetch_anki_fields.py` · `sync_to_anki.py` · `release_apkg.py` · `verify` ·
113: `finish.sh` · `tests/` (compactor + templates + front_modes +
114: mature_content + layout) · `docs/adr/` · `chat_history/` · `dist/` +
115: `backups/` (gitignored).
````

## File: MVP.md
````markdown
 1: # MVP.md — current scope
 2: 
 3: `PRODUCT.md` answers *what is this product?* This file answers *what are we
 4: actually building right now?* Agents must not independently widen this scope
 5: while coding.
 6: 
 7: ## MVP goal
 8: 
 9: A shippable, review-ready Japanese sentence-mining note type: dense on
10: desktop, usable on a small phone, with sentence/word/listening fronts, a
11: compact informative back, and a one-command sync → export → release loop.
12: 
13: ## Core user journey(s)
14: 
15: 1. Import the release `.apkg` → review mined cards daily on desktop and phone.
16: 2. Mature cards automatically test the word, not the memorized sentence.
17: 3. Edit templates/CSS locally → `./finish.sh` → cards updated in Anki and a
18:    new tagged release published.
19: 
20: ## Included capabilities
21: 
22: - Front: pure retrieval surface — sentence / Expression fallback,
23:   Frequency-legacy sentence path, cloze-trio rebuild, pure audio-only listening
24:   cards (usable audio required; `#listening` without audio falls back to
25:   sentence), Mature Word Mode (interval-gated, desktop-only AnkiConnect
26:   content search — one fallback-only path for reviewer and Browse
27:   previewer (live `guiCurrentCard` read removed), mobile intentionally
28:   degrades
29:   to the sentence front, never picks candidate 0, sentence fallback).
30: - Back: typography-driven hierarchy — word+furigana target, quiet pitch
31:   text, Definition Compactor (CSS §6b), 3-line truncator with one-way
32:   expand (§6c), context (sentence + picture as core information,
33:   responsive grid), native circular audio (playback indicator, not true
34:   progress), secondary information collapsed behind `More ▾` (translation,
35:   context, kanji notes, notes, full extended definition), source footer.
36:   Custom shortcuts: `Z` furigana, `X`/`T` translation, `C` expanded-info;
37:   `R` is Anki-owned (never in the template's shortcut UI). Content
38:   hierarchy communicates card mode directly.
39: - Styling: Tokyo Night + Aki Paper themes, fluid clamps, container-query
40:   context grid with media fallback, zero-reflow furigana + `F`
41:   full-card furigana mode (back only), Fuji backdrop, reduced-motion
42:   support.
43: - Empty-field collapse everywhere: no padding, border, or margin survives an
44:   empty field; the More section and its toggle self-remove when empty.
45: - Tooling: field bootstrap (`fetch_anki_fields.py`), snapshotted sync
46:   (`sync_to_anki.py`), apkg export (`release_apkg.py`), `verify` gate,
47:   `finish.sh` release loop, regression tests (compactor + templates +
48:   front-modes + layout).
49: 
50: ## Excluded capabilities
51: 
52: - New fields, add-ons, or review-time Python.
53: - Additional card types or note types.
54: - Cloud sync / collaboration / analytics.
55: - Mandatory per-project doc/diagram checklists beyond `ARCHITECTURE.md`.
56: 
57: ## Acceptance criteria
58: 
59: - `./verify` passes (compactor + template invariants; layout checks when
60:   Chrome is present).
61: - A real user can complete: import → review sentence card → review mature
62:   word card → review listening card → expand definition/translation/image →
63:   edit locally → `./finish.sh` → updated cards + tagged release.
64: - No horizontal overflow, no viewport-fill dead space, furigana never shifts
65:   layout, audio never overlaps, failures always degrade to the sentence front.
66: 
67: ## Known limitations
68: 
69: - Mature interval needs AnkiConnect (desktop); Browse/template previews without
70:   it correctly fall back to the sentence front.
71: - Mature Word Mode is **intentionally unavailable on Android/mobile** (safe
72:   sentence fallback). The template makes no AnkiDroid JS API interval request,
73:   because those calls can surface natively as false "Card Content Error:
74:   Failed to load" media warnings in the reviewer.
75: - Headless layout checks skip gracefully when Chrome is absent.
76: 
77: ## Deferred features
78: 
79: - Further density passes beyond the current clamp/container-query system.
80: - A reliable mobile interval source that does not trigger AnkiDroid's false
81:   media-load error (revisit if AnkiDroid stabilises its JS API).
82: - Extra dictionaries/markup variants beyond current compactor fixtures.
83: - Any `docs/adr/` entries beyond decided items (added only when a decision
84:   has alternatives + consequences + long-term relevance).
````

## File: PRODUCT.md
````markdown
  1: # PRODUCT.md — Japanese sentence-mining note type
  2: 
  3: Authoritative source for **what the product is supposed to do**.
  4: Architecture, plans, and agent instructions all defer to this file.
  5: 
  6: ## Problem
  7: 
  8: Yomitan sentence-mining cards are verbose and ergonomically poor out of the
  9: box: oversized headwords, full multi-dictionary glosses, dead screen space,
 10: clunky audio controls, and a familiar sentence that becomes the retrieval cue
 11: once a card is mature (overlearning). Review on a small phone (Galaxy A50) is
 12: especially wasteful.
 13: 
 14: ## Target users
 15: 
 16: - Solo learner (the maintainer) mining Japanese sentences via Yomitan /
 17:   jidoujisho into Anki.
 18: - Review contexts: Anki Desktop Qt6 WebEngine (Arch Linux, widescreen) and
 19:   AnkiDroid WebView (Samsung Galaxy A50, small screen).
 20: - Installs via the released `.apkg` (GitHub Release asset), or syncs from
 21:   source with Anki-Connect.
 22: 
 23: ## Core design philosophy
 24: 
 25: > **Every visible element must justify its existence and its screen space.**
 26: 
 27: The card is a **minimal Japanese-reading interface**, not a dashboard,
 28: dictionary UI, or mini-SRS. Anki is the SRS: it handles scheduling and
 29: grading. The template's only job is to present the Japanese item clearly,
 30: provide the necessary context for retrieval, and get out of the way.
 31: 
 32: - The fundamental learning task is: **Japanese word → reading + meaning.**
 33:   No English→Japanese production, no custom grading or confidence buttons,
 34:   no additional learning-mode systems.
 35: - The front is a pure retrieval surface: it contains ONLY the thing being
 36:   tested (sentence with target, mature word, or listening audio button).
 37: - The back establishes hierarchy through typography — target → reading →
 38:   meaning → context — with everything secondary collapsed by default.
 39: - Removal beats addition: when uncertain between adding UI and removing
 40:   it, remove; between always-visible and collapsed/hover, prefer
 41:   collapsed.
 42: 
 43: ## Mining / card-quality invariant
 44: 
 45: > **The mined sentence shown on the front must be independently
 46: > understandable enough to solve the card.** Additional surrounding
 47: > context (previous/next paragraph, dialogue) is supplementary reference
 48:   material and must never be required for the card to be intelligible.
 49: 
 50: ```
 51: Front sentence = self-contained learning unit
 52: Additional surrounding context = optional reference material
 53: ```
 54: 
 55: This is a mining invariant, not a UI preference: a card whose front needs
 56: off-screen context to be solvable is a bad mine and should be re-mined.
 57: 
 58: ## Core user journeys
 59: 
 60: 1. **Mine → review sentence card.** Yomitan fills Expression / Sentence /
 61:    Definition / audio / Frequency; the front tests sentence recognition, the
 62:    back shows the hierarchy: target+reading, compacted meaning, context.
 63: 2. **Review mature card as word card.** Cards with interval ≥
 64:    `LONG_INTERVAL_DAYS` show only the Expression on the front
 65:    (anti-overlearning), with silent fallback to the sentence front. The
 66:    familiar sentence must never become the retrieval cue.
 67: 3. **Review listening card.** Cards whose audio is the test (pure audio-only
 68:    fields: no definitions, no frequency) show a single large audio
 69:    button; `#listening` activates the listening front **only when usable
 70:    audio exists** (Sentence Audio, or Word Audio fallback) — without
 71:    usable audio it falls back to the normal sentence front. Normal cards
 72:    are completely unaffected and have zero audio on front.
 73: 4. **Expand information on demand.** Secondary info (translation,
 74:    extended definition, additional context, kanji/general notes) sits
 75:    behind one quiet `More ▾` toggle; `T` reveals the translation, `F`
 76:    toggles full-card furigana on the back, picture opens the lightbox.
 77: 5. **Install / update.** Import the release `.apkg`, or push local
 78:    templates/CSS to the live profile and re-export via `finish.sh`.
 79: 
 80: ## Functional requirements
 81: 
 82: - Front modes (in priority order): Definition/Extended-definition →
 83:   sentence; legacy Frequency-only → sentence; pure listening cards (no
 84:   Definition, no Extended-definition, no Frequency, usable audio present)
 85:   → large circular audio button; `#listening` + no usable audio falls
 86:   back to sentence; cloze trio rebuild when Sentence lacks `<b>`; mature
 87:   interval-gated word-only front. Normal cards NEVER render or play audio
 88:   on the front. The sentence front is the universal fallback for every
 89:   failure path.
 90: - Back hierarchy: word/furigana target with Japanese seal, 5-star frequency
 91:   visualizer and pitch accent, compacted primary definition (§6b), context
 92:   (sentence + picture as core information), native circular audio (`文`/`言葉`),
 93:   secondary information toggleable behind `More ▾` / `Less ▴` (translation,
 94:   context, kanji notes, notes, full extended definition), keyboard shortcuts
 95:   hints, source footer. Content hierarchy communicates card structure directly.
 96: - Mature Word Mode (desktop only): interval resolved at render time via a
 97:   fallback-only AnkiConnect content search (Expression → Sentence →
 98:   cloze-body discriminators) — reviewer and Browse previewer share the
 99:   one identical path (the live `guiCurrentCard` read was removed), it
100:   never picks candidate 0 blindly, and any failure → sentence front;
101:   listening fronts untouched.
102:   On Android/mobile Mature Word Mode is **intentionally disabled** and the
103:   ordinary sentence front is shown: the template makes no AnkiDroid JS API
104:   interval request, because those calls can surface natively as false
105:   "Card Content Error: Failed to load" media warnings in the reviewer.
106: - Tags are behavioral metadata, never decoration: hidden probes only;
107:   `#listening` forces listening behavior (requires usable audio, else
108:   falls back to sentence); extensible for future behavior-related tags
109:   without card redesign.
110: - Tooling: `sync_to_anki.py` pushes Front/Back/CSS with a pre-sync snapshot
111:   to `backups/<timestamp>/`; `release_apkg.py` exports deck
112:   `My Life Decks::Japanese::anki-japanese-template` via `exportPackage`;
113:   `finish.sh` runs tests → sync → export → commit → push → release.
114: 
115: ## UX requirements
116: 
117: - Ultra-compact, content-driven height (no viewport fill, no dead space);
118:   empty space on the front is acceptable — never filled with UI.
119: - Fluid `clamp()` sizing phone → 4K; sentence+picture context grid on
120:   desktop (container queries + media-query fallback), single column on
121:   phones.
122: - Zero-reflow furigana (hidden, hover/tap reveal, absolute ruby); `F`
123:   toggles full-card furigana on the back.
124: - Native-only audio (delegate to Anki replay link, re-tap debounce,
125:   playback indicator pulse — never HTML5 `Audio`); `R` is Anki-owned
126:   (native replay), never a template shortcut. `:has()` is intentional
127:   architecture for empty-shell collapse.
128: - Dual themes (Tokyo Night dark / Aki Paper light, follows Anki Night Mode),
129:   accent color reserved for target highlighting and interactive states,
130:   `prefers-reduced-motion` support, keyboard focus indicators, aria
131:   labels/roles.
132: - Japanese remains the dominant visual language: English typography never
133:   competes with it.
134: 
135: ## Constraints
136: 
137: - Vanilla JS/CSS only, scoped, resilient to Anki WebView DOM re-use.
138: - Fields live **exclusively in the Anki UI**; repo keeps no static field
139:   list (`fetch_anki_fields.py` → gitignored `.anki_fields.json` is the only
140:   source).
141: - Local `.template.anki` / `.css` files are the single source of truth —
142:   never edit inside the Anki UI.
143: - Screen real estate is precious: no debug badges or verbose header labels.
144: - Stdlib-only Python tooling (no third-party runtime deps; test-only deps
145:   allowed).
146: 
147: ## Non-goals
148: 
149: - New Anki note-type fields, add-ons, or Python-at-review solutions.
150: - Multi-note-type theming system or generic card framework.
151: - Enterprise release management (solo `finish.sh` flow is enough).
152: - Server/cloud sync, collaboration, analytics.
153: - English→Japanese production mode, custom grading UI, confidence
154:   buttons, learning-mode systems beyond context/word/listening.
155: 
156: ## Important assumptions
157: 
158: - Yomitan markup shape (`.yomitan-glossary`, `data-sc-*` attributes) is
159:   stable enough for structural CSS scoping; drift is caught by fixtures.
160: - AnkiConnect on `127.0.0.1:8765` (desktop) remains the interval source; it
161:   can be absent. The AnkiDroid JS bridge is deliberately **not** used
162:   (its calls can trigger the reviewer's false media-load error).
163: - One card type ("Card 1"); model name
164:   `Japanese Note type (Sentence card by Default)` is stable.
165: 
166: ## Open questions
167: 
168: - None blocking. Candidate evolution items live in `MVP.md` (Deferred) and
169:   `IMPLEMENTATION_PLAN.md` (roadmap).
````

## File: tests/test_front_modes.py
````python
  1: #!/usr/bin/env python3
  2: """Front-mode resolver behavioral tests (listening semantics).
  3: 
  4: Extracts the LISTENING RESOLVER block verbatim from the real
  5: `Card 1 - Front.template.anki` and runs it in headless Chrome against
  6: six front-state harnesses, asserting the resolved mode:
  7: 
  8:   1. classic audio-only (no Definition/Extended/Frequency + audio)
  9:      -> listening front: sentence removed, listening-view visible
 10:   2. #listening tag + glosses -> listening front (deliberate exercise)
 11:   3. sentence audio + glosses, no tag -> sentence front (regular card)
 12:   4. no audio at all -> sentence front
 13:   5. Frequency legacy probe -> sentence front (never the audio button)
 14:   6. tag but no Sentence Audio -> sentence front (markup is gated on
 15:      Sentence Audio existing)
 16: 
 17: Run directly:  python3 tests/test_front_modes.py
 18: Wired into ./verify alongside the other suites. Skipped gracefully
 19: without Chrome.
 20: 
 21: Dependencies: headless Chrome only (same as test_layout.py).
 22: """
 23: import json
 24: import os
 25: import re
 26: import shutil
 27: import subprocess
 28: import sys
 29: import tempfile
 30: 
 31: HERE = os.path.dirname(os.path.abspath(__file__))
 32: ROOT = os.path.dirname(HERE)
 33: FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
 34: CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")
 35: 
 36: PASS = 0
 37: FAIL = 0
 38: 
 39: 
 40: def check(name, cond, detail=""):
 41:     global PASS, FAIL
 42:     tag = "PASS" if cond else "FAIL"
 43:     print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
 44:     if cond:
 45:         PASS += 1
 46:     else:
 47:         FAIL += 1
 48: 
 49: 
 50: def load_resolver():
 51:     """Extract the resolver block verbatim from the real front template."""
 52:     with open(FRONT, encoding="utf-8") as f:
 53:         front = f.read()
 54:     m = re.search(
 55:         r"/\* --- LISTENING RESOLVER.*?"
 56:         r"container\.querySelectorAll\('\.listening-view'\)\.forEach\(\(v\) => v\.remove\(\)\);\s*\}\n",
 57:         front, re.S)
 58:     if not m:
 59:         raise RuntimeError("listening resolver block not found in front template")
 60:     return m.group(0)
 61: 
 62: 
 63: # (name, has_audio_card, tags_text, tag_audio_source)
 64: # tag_audio_source: content placed inside .raw-audio-source for the tag view.
 65: #   Empty string = no audio field rendered (Policy B fallback test).
 66: CASES = [
 67:     ("classic audio-only (listening-view present)", True, "", None),
 68:     ("normal card (glosses, no listening-view)", False, "", None),
 69:     ("word card (no audio on front)", False, "", None),
 70:     ("#listening tag with Sentence Audio", False, "listening", "[sound:sentence.mp3]"),
 71:     ("#listening tag with Word Audio only", False, "listening", "[sound:word.mp3]"),
 72:     ("#listening tag WITHOUT audio (Policy B fallback)", False, "listening", ""),
 73:     ("non-listening tag (vocab tag with glosses)", False, "vocab n3", "[sound:x.mp3]"),
 74:     # Exactly-one-button invariant: a pure #listening audio card renders BOTH
 75:     # a tag-listening-view and a classic-listening-view in the markup. The
 76:     # resolver must keep only the active one (tag-listening-view wins) and
 77:     # remove the dead/duplicate classic view.
 78:     ("#listening + audio card (both views in markup)", True, "listening", "[sound:sentence.mp3]"),
 79: ]
 80: 
 81: 
 82: def build_html(resolver, is_listening_card, tags_text="", tag_audio_source=None):
 83:     sent_html = '<div class="sentence-display">世の中って<b>不公平</b>よね</div>'
 84:     if tags_text is not None and tags_text != "":
 85:         # When tag_audio_source is None, no tag-listening-view is rendered
 86:         # (tag without audio fields); when it's a string, the view carries
 87:         # that audio source — mirroring the real template's Policy B markup.
 88:         if tag_audio_source is not None:
 89:             audio_inner = tag_audio_source
 90:             tag_view_html = (
 91:                 '<div class="listening-view tag-listening-view" style="display: none;">'
 92:                 '<div class="audio-btn-wrapper">'
 93:                 '<button type="button" class="circular-audio-btn large-audio-btn">文</button>'
 94:                 f'<span class="raw-audio-source" aria-hidden="true">{audio_inner}</span>'
 95:                 '</div></div>'
 96:             )
 97:         else:
 98:             tag_view_html = ""
 99:         tags_html = (
100:             f'<div class="tags-probe" hidden>{tags_text}</div>'
101:             + tag_view_html
102:         )
103:     else:
104:         tags_html = ""
105:     classic_audio = (
106:         '<div class="listening-view classic-listening-view">'
107:         '<div class="audio-btn-wrapper">'
108:         '<button type="button" class="circular-audio-btn large-audio-btn">文</button>'
109:         '<span class="raw-audio-source" aria-hidden="true">[sound:test.mp3]</span>'
110:         '</div>'
111:         '</div>'
112:     ) if is_listening_card else ""
113:     return f"""<!doctype html><html><head><meta charset="utf-8">
114: <style>.front-word-display{{display:none}}</style></head><body>
115: <div class="card"><div class="card-wrapper"><div class="card-container">
116: <div class="front-word-display">不公平</div>
117: {tags_html}{sent_html}{classic_audio}
118: </div></div></div>
119: <script>
120: var report = {{}};
121: try {{
122:   var container = document.querySelector('.card-container');
123:   var wrapper = document.querySelector('.card-wrapper');
124: {resolver}
125: report.listening = isListening;
126: report.cls = wrapper.className;
127: report.sentences = container.querySelectorAll('.sentence-display').length;
128: var lv = container.querySelector('.listening-view');
129: report.viewVisible = !!lv && getComputedStyle(lv).display !== 'none';
130: report.listeningViews = container.querySelectorAll('.listening-view').length;
131: }} catch(e) {{ report.err = String(e && e.stack || e); }}
132: document.title = JSON.stringify(report);
133: </script>
134: </body></html>"""
135: 
136: 
137: def render(html):
138:     with tempfile.TemporaryDirectory() as td:
139:         path = os.path.join(td, "front.html")
140:         with open(path, "w", encoding="utf-8") as f:
141:             f.write(html)
142:         try:
143:             out = subprocess.run(
144:                 [CHROME, "--headless=new", "--disable-gpu",
145:                  "--no-sandbox", "--hide-scrollbars",
146:                  "--window-size=1440,900",
147:                  "--virtual-time-budget=1500",
148:                  "--dump-dom", f"file://{path}"],
149:                 capture_output=True, text=True, timeout=60,
150:             ).stdout
151:         except subprocess.TimeoutExpired:
152:             return None
153:     m = re.search(r"<title>(.*?)</title>", out, re.S)
154:     if not m:
155:         return None
156:     try:
157:         return json.loads(m.group(1))
158:     except json.JSONDecodeError:
159:         return None
160: 
161: 
162: def main():
163:     if not CHROME:
164:         print("[SKIP] no headless Chrome found — front-mode checks skipped")
165:         return 0
166:     resolver = load_resolver()
167: 
168:     for case in CASES:
169:         name, is_listening, tags_text, tag_audio = case
170:         r = render(build_html(resolver, is_listening, tags_text, tag_audio))
171:         check(f"{name}: probe returned", r is not None)
172:         if not r:
173:             continue
174:         if "err" in r:
175:             check(f"{name}: resolver ran without errors", False, r["err"])
176:             continue
177:         check(f"{name}: resolver ran without errors", True)
178: 
179:         # Policy B: #listening without usable audio falls back to sentence front.
180:         # A classic audio-only card (is_listening_card=True) always has a real
181:         # audio source in its classic-listening-view, so it activates listening.
182:         is_policy_b_fallback = (
183:             tags_text and "listening" in tags_text
184:             and tag_audio == ""
185:         )
186:         has_tag_audio = tag_audio is not None and tag_audio != ""
187:         expected_listening = is_listening or (
188:             tags_text and "listening" in tags_text and has_tag_audio
189:         )
190:         # Policy B: tag without audio → sentence front
191:         if is_policy_b_fallback:
192:             expected_listening = False
193: 
194:         if expected_listening:
195:             check(f"{name}: listening front active (view visible, sentence removed, exactly 1 view)",
196:                   r["listening"] is True and r["viewVisible"] and r["sentences"] == 0
197:                   and r["listeningViews"] == 1,
198:                   json.dumps(r))
199:         else:
200:             check(f"{name}: sentence front active (listening false, sentence intact, 0 listening views)",
201:                   r["listening"] is False and not r["viewVisible"] and r["sentences"] == 1
202:                   and r["listeningViews"] == 0,
203:                   json.dumps(r))
204: 
205:     print()
206:     print(f"{PASS} passed, {FAIL} failed")
207:     return 1 if FAIL else 0
208: 
209: 
210: if __name__ == "__main__":
211:     sys.exit(main())
````

## File: QUALITY.md
````markdown
  1: # QUALITY.md — properties that must remain true
  2: 
  3: Answers *what must remain true*. `TEST_STRATEGY.md` answers *how it is
  4: mechanically verified*. Code implements; tests enforce.
  5: 
  6: ## Architecture invariants
  7: 
  8: - Local `.template.anki` / `.css` files are the single source of truth;
  9:   never instruct edits inside the Anki UI.
 10: - Fields live in the Anki UI only; the repo keeps no static field list.
 11: - Vanilla JS/CSS only, scoped, DOM-reuse safe (idempotent init, no globals
 12:   beyond the documented `window.*` controllers).
 13: - Single `LONG_INTERVAL_DAYS = 365` const; no hard-coded `>= 365` elsewhere.
 14: - CSS section numbers (§6b compactor, §6c truncator, §14 backdrop) are stable
 15:   contracts referenced by tests and docs.
 16: 
 17: ## Front invariants
 18: 
 19: - Front renders **no** furigana filter/field (`Sentence (furigana)` ban);
 20:   raw `{{edit:Sentence}}` / `{{edit:Expression}}` only.
 21: - Front shows **no UI** beyond the tested Japanese: no tags, badges,
 22:   metadata, labels, or controls (hidden behavioral probes only: cloze trio).
 23:   Normal cards NEVER render or play audio on the front.
 24: - `R` shortcut is **Anki-owned** (native replay); the template never adds
 25:   or modifies an `R` shortcut. Custom template shortcuts are `Z`
 26:   (furigana), `X` (translation), `C` (expanded-info) — never `R`.
 27: - Balanced `{{#field}}` / `{{^field}}` / `{{/field}}` conditionals.
 28: - The sentence front is the **universal fallback**: every pathological /
 29:   mature failure path degrades to it, never to a blank or hung card.
 30: - Pure listening cards: `listening-view` renders only under
 31:   `{{^Definition}}{{^Extended definition}}{{^Frequency}}{{#Sentence Audio}}`.
 32:   Normal study cards never include `{{Sentence Audio}}` on front, guaranteeing
 33:   zero audio autoplay on front.
 34: - **Listening Policy B**: `#listening` activates the listening front **only
 35:   when usable audio exists** (the tag-listening-view must have a real
 36:   `.raw-audio-source` — `{{Sentence Audio}}`, or `{{Word Audio}}` as
 37:   fallback). `#listening` + no usable audio falls back safely to the normal
 38:   sentence front. The resolver removes every dead/duplicate listening view
 39:   so exactly one listening sound button is ever visible.
 40: - **Listening audio source**: the tag-listening-view binds to the actual
 41:   `{{Sentence Audio}}` field (not the hardcoded `play:a:0` which plays the
 42:   first audio field = Word Audio on listening cards). Word Audio is the
 43:   fallback when Sentence Audio is absent. The label matches what plays
 44:   (文 for sentence audio, 言葉 for word audio).
 45: - Listening cards never enter Mature Word Mode and skip all interval
 46:   retrieval.
 47: - Interval has no `{{Interval}}` marker and no `note:` search clause
 48:   (`{{Type}}` is the scheduling type, not the model): desktop uses
 49:   AnkiConnect only; the mobile path makes **no interval request at all** —
 50:   the AnkiDroid JS API is deliberately never called (it can trigger false
 51:   "Card Content Error: Failed to load" media warnings), and mobile never
 52:   fetches `127.0.0.1:8765`.
 53: - **Mature mode interval retrieval** is desktop-only fallback content
 54:   search (`findCards` by Expression → Sentence/cloze-body discriminators →
 55:   `cardsInfo`). The live reviewer read (`guiCurrentCard`) was REMOVED —
 56:   one identical path for reviewer and Browse previewer. Android/mobile
 57:   intentionally degrades to the sentence front (`post` UA-guards every
 58:   AnkiConnect call before any fetch); if ambiguity remains, retrieval
 59:   fails safely to the sentence front. It never picks candidate 0
 60:   blindly.
 61: - Any retrieval failure degrades to the sentence front; anti-flash
 62:   `visibility:hidden` gate with a bounded reveal cap. The gate is
 63:   deterministic and safe: it must never depend on a single async path or
 64:   timer that can be throttled, and it must never leave a blank/hung card.
 65: - Cloze rebuild fires only when Sentence lacks `<b>`/`<strong>` **and** the
 66:   full prefix/body/suffix trio is non-empty; rebuild uses `<b>`.
 67: - The template contains **no executable AnkiDroid JS API code** and makes no
 68:   `/jsapi/` request; mobile Mature Word Mode is intentionally disabled and
 69:   degrades to the sentence front.
 70: - `:has()` is intentional architecture for empty-shell collapse; it is not
 71:   removed for theoretical portability.
 72: - Front template size is not a defect; correctness is prioritized over line
 73:   count. The front is not aggressively split/refactored.
 74: 
 75: ## Back invariants
 76: 
 77: - Back hierarchy is typography-driven: word-display (largest, with Japanese seal) → metadata bar (5-star frequency visualizer & pitch accent & audio) → primary meaning → context → secondary collapsed behind More. Features discoverable via shortcut hints.
 78: - Secondary information (translation, context, kanji notes, notes,
 79:   full extended definition) lives inside `.more-section`, toggleable via
 80:   `More ▾` / `Less ▴`; the toggle and section self-remove when no secondary
 81:   content exists.
 82: - Content hierarchy communicates card mode directly: no retrieval-state
 83:   badges, captions, or dashboard metadata.
 84: - Keyboard shortcuts on the back: `F` toggles full-card furigana
 85:   (`.furigana-mode`), `T` reveals the translation (opening More first),
 86:   `X` toggles translation (alias for `T`), `C` toggles expanded-info;
 87:   shortcuts never fire in inputs/contentEditable. **`R` is Anki-owned**
 88:   (native replay) and never appears in the template's shortcut UI.
 89: - Every circular audio button has an `aria-label`; replay source is a
 90:   **sibling** `.raw-audio-source` (never inside `<button>`, never
 91:   `display:none`); playback delegates to the native replay link; re-tap is
 92:   debounced; `playCircularAudio` starts with `resetAudioState`; no `new
 93:   Audio()`, no `is-paused` remnants, no `div`-inside-`button`. The ring is
 94:   a **playback indicator** (a decorative play-pulse), not true progress —
 95:   native audio remains the authority (ADR 003).
 96: - Lightbox closes only on backdrop click (`e.target === overlay`) or
 97:   `Escape`; overlay carries dialog semantics; cloned image preserves `alt`.
 98: - Definition expand is one-way (never re-collapses); `.is-truncated` is set
 99:   only on real overflow; no-JS still shows the full definition.
100: - No JS font-scaler overrides CSS (`.sentence-japanese` `clamp()` is the
101:   sizing authority).
102: 
103: ## CSS invariants
104: 
105: - Zero-reflow furigana: absolute `ruby rt`, hidden until
106:   `:hover`/`:active`/`:focus`; `F` mode pins all rt visible with no
107:   reflow (same geometry).
108: - Content-driven card height (no `100vh`/`100dvh` fill); `container-type:
109:   inline-size` present; the context grid (sentence + picture) has a
110:   media-query fallback.
111: - Compactor hide rules all scoped to `.primary-definition`; the full
112:   extended definition (`.extended-full` inside More) stays untouched.
113: - Word-mode swap rules exist and never touch `.listening-view`; the
114:   listening-view is inert until `.listening-mode` activates it.
115: - `:focus-visible` indicators and `prefers-reduced-motion` present.
116: - Accent color is reserved for target highlighting and interactive
117:   states; frequency indicator uses semantic tier colors (--freq-*).
118: 
119: ## Empty-field collapse (space discipline)
120: 
121: - Every rendered field is enclosed in an Anki `{{#field}}` conditional —
122:   except the hidden cloze-probe trio, the hidden behavioral probes
123:   (`tags-probe`, field-presence markers), and the front word probe
124:   (`display:none` default, word-mode gate only).
125: - Unconditionally rendered shells collapse when all conditional children are
126:   absent: `.audio-row`, `.context-grid`, and `.context-main` via `:has()` guards;
127:   `.more-section` + `.more-toggle` self-remove via JS cleanup.
128: - Degenerate content removes itself instead of leaving chrome behind:
129:   blank definition/sentence blocks are removed (front runs after the cloze
130:   fixup, before the reveal); empty secondary blocks inside More are
131:   stripped.
132: - Net rule: no padding, border, or margin may survive an empty field.
133: 
134: ## Tooling / process invariants
135: 
136: - Python tooling stays stdlib-only; backups use microsecond timestamps;
137:   snapshots happen **before** any overwrite; empty live state aborts sync.
138: - `finish.sh` no-op runs never publish a release.
139: - Every user prompt is archived to `chat_history/opencode_prompts.txt`
140:   before/with the commit that follows it.
````

## File: README.md
````markdown
  1: # 🎴 Japanese Anki Note Template (Ergonomic & Responsive)
  2: 
  3: A modern, ultra-compact Japanese sentence-mining note type for Anki. Built for dense, information-efficient review on **Desktop (Arch Linux, Qt6)** and **Mobile (AnkiDroid, small screens)**.
  4: 
  5: ---
  6: 
  7: ## 🎥 Demo
  8: 
  9: [Screencast_20260903_034628.webm](https://github.com/user-attachments/assets/c3021cdb-7cfd-4cb1-b1a7-ff52a990e305)
 10: 
 11: ---
 12: 
 13: ## ✨ Features
 14: 
 15: - **🌙 Dual themes** — Tokyo Night dark (default) and Aki Paper light, following Anki's Night Mode.
 16: - **🔢 Minimal by design** — every visible element must justify its screen space. The front is a pure retrieval surface (just the Japanese); the back is a quiet reading interface: target → reading → meaning → context, with secondary info collapsed behind `More ▾`. Anki is the SRS — no badges, dashboards, or grading UI.
 17: - **📱 Fluid responsive layout** — `clamp()` sizing with no breakpoint jumps; sentence + picture context grid on desktop, single column on phones; container queries with a media-query fallback for old WebViews. Cards size to their content (no forced viewport fill).
 18: - **🔤 Zero-reflow furigana** — hidden by default, revealed on hover (desktop) / tap (mobile); **`F`** pins full-card furigana on the back. Nothing ever shifts.
 19: - **🔊 Native audio** — `文` / `言葉` buttons delegate to Anki's replay link (never HTML5 audio), with re-tap debounce so audio can't overlap on AnkiDroid. The ring is a playback indicator (a decorative play-pulse), not true progress. **`R`** is Anki's own shortcut (native replay) — the template never adds it. Custom template shortcuts: `Z` (furigana), `X` (translation), `C` (expanded-info).
 20: - **👁️ On-demand secondary info** — `T`/`X` reveals the translation; `More ▾` exposes the full Yomitan definition, extra context, kanji and general notes. `C` toggles expanded-info. Quiet by default.
 21: - **🖼️ Lightbox** — tap any image for a full-screen overlay; closes on backdrop click or <kbd>Escape</kbd>.
 22: - **🏷️ Behavioral tags** — tags drive card behavior (e.g. `#listening` forces the listening front) and are never rendered as decoration.
 23: 
 24: ---
 25: 
 26: ## 🃏 Front Card Modes
 27: 
 28: The front contains ONLY the thing being tested — the sentence itself is the retrieval prompt.
 29: 
 30: | Situation | Front shows |
 31: | :--- | :--- |
 32: | Definition present | Sentence (or Expression if no Sentence) |
 33: | No definitions, but `Frequency` set (legacy cards) | Usual sentence — never the audio button |
 34: | No definitions, no Frequency, `Sentence Audio` set | Listening-mode audio button |
 35: | Card tagged `#listening` | Listening-mode audio button — **only when usable audio exists** (Sentence Audio, or Word Audio fallback); without audio, falls back to the sentence front |
 36: | Nothing available | Sentence / Expression fallback |
 37: | Sentence has no bold term + cloze trio complete | Rebuilt `prefix + `<b>`body`</b>` + suffix`, styled identically to a Yomitan sentence |
 38: | Review interval ≥ 365 days (desktop only) | Word only (Mature Word Mode, see below); Android keeps the sentence front |
 39: 
 40: **Cloze fallback** (jidoushio mobile exports): when `Sentence` lacks its `<b>` target word, JS rebuilds it from `cloze-prefix` / `cloze-body` / `cloze-suffix` — but only if all three are non-empty, otherwise the sentence is kept as-is.
 41: 
 42: **Mature Word Mode** (anti-overlearning, desktop only): old cards stop testing the word and start testing sentence recognition, so at `interval ≥ LONG_INTERVAL_DAYS` (default `365`, one constant in `Card 1 - Front.template.anki`) the front shows only the `Expression`. The interval is resolved at render time via AnkiConnect **content search** (`findCards` by Expression, then Sentence → cloze-body discriminators — reviewer and Browse previewer share the one identical fallback-only path; the live `guiCurrentCard` exact-card read was removed). On Android/mobile this mode is **intentionally disabled** and the ordinary sentence front is shown: the `post` helper UA-guards every AnkiConnect call before any fetch, because refused localhost requests can surface natively as false "Card Content Error: Failed to load" media warnings in the reviewer. The search **never picks candidate 0** blindly; if ambiguity remains, it fails safely to the sentence front. Any failure degrades to the normal sentence front; listening cards are never touched; an anti-flash gate keeps the card hidden until the decision is made (500 ms fetch timeout, 1200 ms reveal cap). The gate is deterministic and safe — it never depends on a single async path that can be throttled into a blank front.
 43: 
 44: **Listening semantics (Policy B)**: the audio button markup is gated on `Sentence Audio` and inert until a synchronous resolver confirms the listening condition — the classic audio-only field shape OR the `#listening` tag — **with usable audio**. The tag-listening-view binds to the actual `{{Sentence Audio}}` field (not the hardcoded `play:a:0` which plays the first audio field = Word Audio); Word Audio is the fallback, and the label matches what plays (文 for sentence, 言葉 for word). `#listening` + no usable audio falls back to the normal sentence front. The resolver removes every dead/duplicate view so exactly one listening sound button is ever visible. Every other card (and every failure path, including no-JS) keeps the sentence front.
 45: 
 46: ---
 47: 
 48: ## 📖 Back Card
 49: 
 50: Typography does the work — no dashboard chrome:
 51: 
 52: 1. **Target + reading** — the headword with hover furigana, the hero element; pitch accent as quiet muted text.
 53: 2. **Primary meaning** — **Definition Compactor** (CSS §6b) trims the Yomitan glossary to the first dictionary, max 2 senses, no appendices; **Definition Truncator** (§6c) caps it at 3 lines with a fade + `▼`, click expands and stays open.
 54: 3. **Context** — the sentence (with hover furigana) plus the picture when present, side by side on wide screens.
 55: 4. **Secondary info** — collapsed behind a quiet `More ▾`: translation (`T`), additional context, kanji notes, general notes, and the **full extended definition** (the compactor never touches it).
 56: 5. **Source footer** — quietly identifies the material. Content hierarchy communicates the card mode directly without labels.
 57: 
 58: ---
 59: 
 60: ## 🗂️ Fields
 61: 
 62: Fields are managed **exclusively inside the Anki UI** — the repo keeps no static list. For the live names + descriptions, run:
 63: 
 64: ```bash
 65: python3 fetch_anki_fields.py   # dumps gitignored .anki_fields.json
 66: ```
 67: 
 68: Current set (20): `Expression`, `Definition`, `Kanji Notes`, `Source`, `Sentence`, `Sentence (furigana)`, `Sentence Audio`, `Translation`, `Picture`, `context`, `Notes`, `Word Audio`, `Pitch Accent`, `furigana`, `reading`, `cloze-prefix`, `cloze-body`, `cloze-suffix`, `Frequency`, `Extended definition`. Yomitan-mining compatible.
 69: 
 70: ---
 71: 
 72: ## 🚀 Installation
 73: 
 74: **Option 1 — Quick install (recommended):** download `anki-japanese-template.apkg` from [Releases](https://github.com/mansourvery-hub/anki-japanese-template/releases), import via **File → Import**, then delete the sample cards (the note type is retained).
 75: 
 76: **Option 2 — Sync from source** (needs Anki + [Anki-Connect](https://ankiweb.net/shared/info/2055492159), Python 3 stdlib only):
 77: ```bash
 78: git clone https://github.com/mansourvery-hub/anki-japanese-template.git
 79: cd anki-japanese-template
 80: python3 sync_to_anki.py    # snapshots live state to backups/, then pushes Front/Back/CSS
 81: python3 release_apkg.py    # exports sample deck to dist/*.apkg
 82: ```
 83: 
 84: **Option 3 — Manual:** paste `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, and `Card 1 - Style.css` into the card template editor (**Tools → Manage Note Types → Cards**).
 85: 
 86: ---
 87: 
 88: ## 🛠️ Project Structure
 89: 
 90: ```
 91: ├── Card 1 - Front.template.anki   # Front HTML: modes, cloze fallback, Mature Word Mode
 92: ├── Card 1 - Back.template.anki    # Back HTML: header, definition, sentence, side column
 93: ├── Card 1 - Style.css             # Themes, layout, compactor (§6b), truncator (§6c)
 94: ├── fetch_anki_fields.py           # Read-only dump of live Anki fields (see above)
 95: ├── sync_to_anki.py                # Push templates/CSS to Anki (pre-sync backup)
 96: ├── release_apkg.py                # Export sample deck to dist/*.apkg
 97: ├── verify                         # Local quality gate (tests only, no side effects)
 98: ├── finish.sh                      # One command: verify + sync + export + commit + push + release
 99: ├── PRODUCT.md / MVP.md            # Product intent / current scope
100: ├── ARCHITECTURE.md + docs/adr/    # Technical structure / lasting decisions
101: ├── QUALITY.md / TEST_STRATEGY.md  # Invariants / how they are verified
102: ├── IMPLEMENTATION_PLAN.md         # Task graph + status
103: ├── tests/                         # test_compactor.py + test_templates.py + test_front_modes.py + test_mature_content.py + test_layout.py (run by ./verify)
104: ├── chat_history/                  # Archived agent prompts
105: ├── dist/                          # Exported .apkg (gitignored, GitHub Release asset)
106: ├── backups/                       # Pre-sync Anki snapshots (gitignored)
107: ├── AGENTS.md                      # Agent operating rules
108: └── README.md                      # This file
109: ```
110: 
111: ---
112: 
113: ## 🔄 Development Workflow
114: 
115: Edit the local `.template.anki` / `.css` files (never inside Anki's UI), then run one command:
116: 
117: ```bash
118: ./finish.sh "scope: what changed"
119: # --local: sync + export + commit only · --minor: bump v1.x.0 · --prompt "text": archive prompt
120: ```
121: 
122: This runs tests, syncs to Anki, exports the apkg, commits, pushes, and publishes a tagged release. `tests/` covers the compactor selectors, template invariants (furigana ban on front, audio/lightbox semantics, balanced conditionals, listening Policy B, R-is-Anki-owned, playback indicator terminology, finish.sh ordering), front-mode resolver behavior, mature content-search fallback (duplicate cards / ambiguity), and headless layout checks.
123: 
124: ---
125: 
126: Built with Opencode and Gemini CLI. MIT License.
````

## File: ARCHITECTURE.md
````markdown
  1: # ARCHITECTURE.md — authoritative technical structure
  2: 
  3: Covers *how the software is structured* for the `MVP.md` scope. Additional
  4: documents are created only where they would otherwise make this file unwieldy
  5: or where a domain needs an independently maintained contract. Current extras:
  6: `docs/adr/` (decisions with lasting consequences); no separate
  7: `DATA_MODEL.md` / `API_CONTRACTS.md` / `STATE_MODEL.md` — the project is too
  8: small to justify them.
  9: 
 10: ## System map
 11: 
 12: ```text
 13: Anki note fields (live in Anki UI, never in repo)
 14:   │  Yomitan / jidoujisho mining
 15:   ↓
 16: Card 1 - Front.template.anki ──→ review front (sentence / word / listening)
 17: Card 1 - Back.template.anki  ──→ review back (grid: main + side columns)
 18: Card 1 - Style.css           ──→ themes, layout, compactor, truncator
 19:   │  vanilla JS (scoped, DOM-reuse safe), no libraries
 20:   ↓
 21: Anki renderers: Desktop Qt6 WebEngine · AnkiDroid WebView
 22:   │  live services at render time: AnkiConnect :8765 (desktop only)
 23:   ↓
 24: Tooling (stdlib-only): fetch_anki_fields.py · sync_to_anki.py ·
 25:                        release_apkg.py · verify · finish.sh
 26: ```
 27: 
 28: ## Components
 29: 
 30: ### Front (`Card 1 - Front.template.anki`)
 31: 
 32: A pure retrieval surface: only the tested Japanese renders. HTML
 33: conditionals pick the branch; a synchronous JS resolver finalizes the
 34: listening decision (Policy B: usable audio required); async JS finalizes
 35: Mature Word Mode:
 36: 
 37: ```text
 38: Definition / Extended definition? ──yes──→ sentence-display (zero audio)
 39:         │ no
 40: Frequency (legacy)? ──yes──→ sentence-display (zero audio)
 41:         │ no
 42: Sentence Audio? ──yes──→ listening-view (audio-only card)
 43:         │ no
 44: sentence-display fallback
 45:         │
 46: cloze fixup: Sentence has no <b> AND cloze trio complete?
 47:         │ yes → prefix + <b>body</b> + suffix
 48:         │
 49: Mature check (desktop only; not listening, Expression non-empty,
 50:               interval ≥ LONG_INTERVAL_DAYS=365)?
 51:         │ yes → .word-mode: front-word-display only
 52:         │ no  → sentence front (also the universal fallback)
 53: ```
 54: 
 55: Mature Word Mode is **desktop-only by design**: on Android/mobile the
 56: template deliberately makes no interval request at all (no AnkiDroid JS API
 57: call), because those calls can surface natively as false "Card Content
 58: Error: Failed to load" media warnings in the reviewer. Mobile always keeps
 59: the sentence front; reliability of the reviewer beats this optional
 60: presentation feature.
 61: 
 62: Hidden behavioral probes never render visibly: the cloze trio and the
 63: tags probe. Normal cards never evaluate `{{Sentence Audio}}` on the front,
 64: guaranteeing zero audio autoplay and zero audio controls on normal cards.
 65: **Listening Policy B**: `#listening` (or the legacy audio-only shape)
 66: activates the listening front **only when usable audio exists**
 67: (`hasUsableAudio` check on the `.raw-audio-source`). The tag-listening-view
 68: binds to `{{Sentence Audio}}` (label 文), falling back to `{{Word Audio}}`
 69: (label 言葉) — never the hardcoded `play:a:0`. `#listening` + no usable
 70: audio falls back to the normal sentence front; dead/duplicate views are
 71: removed so exactly one listening button is ever visible.
 72: Interval retrieval is **desktop-only** via a single **content-search**
 73: path (the live `guiCurrentCard` reviewer read was removed — reviewer and
 74: Browse previewer now share the identical code path):
 75: - Content search (only path): `findCards` by Expression, then Sentence
 76:   and cloze-body discriminators narrow to exactly one candidate. **Never
 77:   picks candidate 0**; if ambiguity remains, fails safely to the sentence
 78:   front.
 79: - Mobile: **no retrieval** — `post` UA-guards every AnkiConnect call
 80:   before any fetch (refused localhost requests surface natively as false
 81:   "Failed to load" media warnings); interval stays null → sentence front.
 82: Anti-flash gate (`visibility:hidden` → reveal, 1200 ms safety cap); blank
 83: sentence blocks are removed after the cloze fixup. The gate is
 84: deterministic and safe: it never depends on a single async path or timer
 85: that can be throttled. See `docs/adr/001-*`.
 86: 
 87: `:has()` is intentional architecture for empty-shell collapse (§6b, §10);
 88: it is not removed for theoretical portability. Front template size is not
 89: a defect — correctness is prioritized over line count.
 90: 
 91: ### Back (`Card 1 - Back.template.anki`)
 92: 
 93: Single quiet column with typography-driven hierarchy:
 94: 
 95: ```text
 96: card-container
 97:  ├── .hero-header (3-col grid: left meta | centered word | right meta;
 98:  │    │  stacked word-over-sides on phones)
 99:  │    ├── .hero-side-left (freq visualizer + 言葉 audio)
100:  │    ├── .hero-word-wrap > .word-display (target + furigana hover — hero element)
101:  │    └── .hero-side-right (.pitch-quiet + 文 audio)
102:  ├── definition-box.primary-definition (compacted §6b, 3-line §6c)
103:  ├── .context-grid (sentence + picture; row on wide screens, stacked on phones)
104:  ├── .more-section (hidden) + .more-toggle "More ▾"
105:  │    └── translation (click/T) · context · kanji notes · notes · full
106:  │        extended definition (.extended-full — compactor never touches it)
107:  └── .source-footer
108: ```
109: 
110: JS controllers (all idempotent under WebView DOM re-use): More toggle (one-way reveal;
111: section+button self-remove when secondary content is absent),
112: native-only circular audio (`playCircularAudio` → sibling replay link
113: click, re-tap debounce, playback indicator pulse), definition truncator (blank boxes
114: removed, then measure → `.is-truncated` → one-way `.is-expanded`),
115: lightbox (backdrop-click / `Escape` close, alt preserved), back-only
116: keyboard shortcuts (`F` full-card furigana, `T`/`X` translation reveal,
117: `C` expanded-info toggle; `R` is Anki-owned, never listed).
118: 
119: ### Style (`Card 1 - Style.css`)
120: 
121: Numbered sections are the contract: §1 tokens/themes (no `--freq-*`:
122: accent is reserved for the target and interactive states), §2 containers,
123: §3 More toggle, §4 context grid + desktop overrides, §5 front type,
124: §5b word-mode swap, §6 back hierarchy (hero-header 3-col grid: left meta |
125: centered word | right meta; stacked on narrow; freq/pitch/audio split sides), **§6b Definition Compactor**
126: (first dictionary, ≤2 senses, no appendices, `.primary-definition`-scoped),
127: §6c truncator (3-line cap + fade + chevron), §7 audio rings (playback indicator, not true progress),
128: §8 sentence/translation + secondary blocks, §9 zero-reflow ruby +
129: §9b full-card furigana mode, §10 media/lightbox, §11 footer,
130: §12 listening (inert until `.listening-mode`), §13 mobile,
131: §14 deletable Fuji backdrop, §15 reduced motion (+ blur kill),
132: §16 card entrance (single 0.15s settle, no stagger; killed by §15).
133: 
134: ### Tooling
135: 
136: ```text
137: fetch_anki_fields.py → .anki_fields.json (gitignored, read-only dump)
138: sync_to_anki.py      → snapshot backups/<ts>/, push Front/Back/CSS
139: release_apkg.py      → exportPackage deck → dist/*.apkg (gitignored)
140: verify               → local quality gate (tests only, no side effects)
141: finish.sh            → verify → stamp → sync → export → commit → push main → release (--target main) → fetch tag
142: tests/               → test_compactor.py + test_templates.py
143:                          + test_front_modes.py + test_mature_content.py
144:                          + test_layout.py
145: ```
146: 
147: Fields are **not** a repo artifact: the Anki UI owns them; agents bootstrap
148: via `fetch_anki_fields.py` every session.
149: 
150: ## Diagrams
151: 
152: Produced only where prose is ambiguous. The two graphs above (front-mode
153: decision, back grid) are the standing set; sequence/state/entity diagrams
154: are omitted — no complex async choreography, state machine, or persistent
155: entity graph exists beyond what is shown.
156: 
157: ## Key decisions (summaries; full records in `docs/adr/`)
158: 
159: - **001** Mature interval via desktop-only content search (no
160:   `{{Interval}}`, no new fields/add-ons; `guiCurrentCard` live read
161:   removed after AnkiDroid false-media-warning debugging; mobile makes no
162:   network request at all and degrades to the sentence front).
163: - **002** Definition Compactor as structural CSS (dictionary-agnostic,
164:   `.primary-definition`-scoped; extended definition untouched).
165: - **003** Native-only audio delegation (no `new Audio()`; sibling replay
166:   link; debounce; visually-hidden-not-`display:none` source).
167: - **004** Single-command release (`finish.sh`; `verify` as the side-effect-free
168:   subset; snapshots before overwrite).
169: 
170: ## Evolution rule
171: 
172: Small change → implement normally. Moderate change → update this file
173: (+ ADR when justified) first, then add tasks. Major change → stop feature
174: work, run an explicit architecture-change effort with a migration plan.
````

## File: Card 1 - Back.template.anki
````
  1: <!-- BACK CARD TEMPLATE
  2:      Minimal Japanese Back Card — strong information hierarchy.
  3: 
  4:      Hierarchy (PRODUCT.md redesign):
  5:        Level 1  Target word + reading (furigana hover)   — largest
  6:        Level 2  Primary meaning (compacted definition)    — §6b CSS
  7:        Level 3  Context (sentence + picture when present) — core info
  8:        Level 4  Secondary info — collapsed behind "More ▾":
  9:                 translation (click/T/X), extended definition,
 10:                 additional context, kanji notes, notes, source.
 11: 
 12:       Removed vs the old layout: sticky tags bar (tags are behavioral
 13:       metadata now, never decoration), frequency/pitch badges (visual
 14:       noise without retrieval value), the two-column side dashboard.
 15: 
 16:       Preserved subsystems: Definition Compactor (§6b), truncator (§6c),
 17:       native-delegating audio buttons (文/言葉 — playback indicator, not
 18:       true progress). R is Anki's own shortcut (native replay); the
 19:       template's custom shortcuts are Z/X/C only — R is never added or
 20:       listed. Lightbox, empty-field collapse.
 21: -->
 22: 
 23: <div class="card-wrapper back-card">
 24:   <div class="card-container">
 25: 
 26:     <!-- LEVEL 1: TARGET + META — 3-column grid on wide screens
 27:          (left meta | centered word | right meta; see Style §6 hero-header).
 28:          The word stays truly centered: equal 1fr side columns absorb any
 29:          asymmetry. Narrow phones stack the word on its own row with the
 30:          two sides sharing one tight row below it. -->
 31:     <div class="hero-header">
 32:       <div class="hero-side hero-side-left">
 33:         {{#Frequency}}
 34:           <div class="frequency-badge" data-freq="{{text:Frequency}}">
 35:             <div class="frequency-bar-track">
 36:               <div class="frequency-bar-fill"></div>
 37:             </div>
 38:             <span class="frequency-stars"></span>
 39:           </div>
 40:         {{/Frequency}}
 41: 
 42:         <div class="audio-row">
 43:           {{#Word Audio}}
 44:             <span class="audio-btn-wrapper">
 45:               <button type="button" class="circular-audio-btn small-audio-btn" title="単語音声を再生" aria-label="単語音声を再生" onclick="playCircularAudio(this)">
 46:                 <svg class="audio-progress-ring" viewBox="0 0 44 44">
 47:                   <circle class="ring-bg" cx="22" cy="22" r="19" />
 48:                   <circle class="ring-fill" cx="22" cy="22" r="19" stroke-dasharray="119.38" stroke-dashoffset="119.38" />
 49:                 </svg>
 50:                 <span class="audio-btn-content">
 51:                   <span class="audio-btn-label">言葉</span>
 52:                 </span>
 53:               </button>
 54:               <span class="raw-audio-source" aria-hidden="true">{{Word Audio}}</span>
 55:             </span>
 56:           {{/Word Audio}}
 57:         </div>
 58:       </div>
 59: 
 60:       <div class="hero-word-wrap">
 61:         {{#furigana}}
 62:           <div class="word-display">{{edit:furigana:furigana}}</div>
 63:         {{/furigana}}
 64:         {{^furigana}}
 65:           {{#Expression}}
 66:             <div class="word-display">{{edit:furigana:Expression}}</div>
 67:           {{/Expression}}
 68:         {{/furigana}}
 69:       </div>
 70: 
 71:       <div class="hero-side hero-side-right">
 72:         {{#Pitch Accent}}
 73:           <div class="pitch-quiet">{{edit:Pitch Accent}}</div>
 74:         {{/Pitch Accent}}
 75: 
 76:         <div class="audio-row">
 77:           {{#Sentence Audio}}
 78:             <span class="audio-btn-wrapper">
 79:               <button type="button" class="circular-audio-btn small-audio-btn" title="例文音声を再生" aria-label="例文音声を再生" onclick="playCircularAudio(this)">
 80:                 <svg class="audio-progress-ring" viewBox="0 0 44 44">
 81:                   <circle class="ring-bg" cx="22" cy="22" r="19" />
 82:                   <circle class="ring-fill" cx="22" cy="22" r="19" stroke-dasharray="119.38" stroke-dashoffset="119.38" />
 83:                 </svg>
 84:                 <span class="audio-btn-content">
 85:                   <span class="audio-btn-label">文</span>
 86:                 </span>
 87:               </button>
 88:               <span class="raw-audio-source" aria-hidden="true">{{Sentence Audio}}</span>
 89:             </span>
 90:           {{/Sentence Audio}}
 91:         </div>
 92:       </div>
 93:     </div>
 94: 
 95:     <!-- Decorative separator: seigaiha-inspired arc motif between
 96:          hero header and primary meaning. Matches the one below the
 97:          definition — pure decorative, same as its twin. -->
 98:     <div class="card-separator" aria-hidden="true"><span class="sep-motif"></span></div>
 99: 
100:     <!-- LEVEL 2: PRIMARY MEANING (compact: see Definition Compactor §6b) -->
101:     {{#Definition}}
102:       <div class="definition-box primary-definition" tabindex="0" role="button" aria-expanded="false" onclick="expandDefinition(this)" onkeydown="handleDefinitionKey(event, this)">
103:         {{edit:furigana:Definition}}
104:       </div>
105:     {{/Definition}}
106:     {{^Definition}}
107:       {{#Extended definition}}
108:         <div class="definition-box primary-definition" tabindex="0" role="button" aria-expanded="false" onclick="expandDefinition(this)" onkeydown="handleDefinitionKey(event, this)">
109:           {{Extended definition}}
110:         </div>
111:       {{/Extended definition}}
112:     {{/Definition}}
113: 
114:     <!-- Decorative separator: seigaiha-inspired arc motif between
115:          hero section (word/definition/audio) and context area.
116:          Pure decorative — CSS collapses it to nothing if absent. -->
117:     <div class="card-separator" aria-hidden="true"><span class="sep-motif"></span></div>
118: 
119:     <!-- LEVEL 3: CONTEXT (sentence + picture; core information) -->
120:     <div class="context-grid">
121:       <div class="context-main">
122:         {{#Sentence}}
123:           <div class="sentence-japanese">
124:             {{#Sentence (furigana)}}
125:               {{edit:furigana:Sentence (furigana)}}
126:             {{/Sentence (furigana)}}
127:             {{^Sentence (furigana)}}
128:               {{edit:Sentence}}
129:             {{/Sentence (furigana)}}
130:           </div>
131:         {{/Sentence}}
132: 
133:         <!-- Orphan context (When Sentence is empty) -->
134:         {{^Sentence}}
135:           {{#context}}
136:             <div class="html-content context-only">{{edit:context}}</div>
137:           {{/context}}
138:         {{/Sentence}}
139:       </div>
140: 
141:       {{#Picture}}
142:         <div class="context-picture">
143:           <div class="picture-container" onclick="openLightbox(this)" role="button" tabindex="0" aria-label="画像を拡大" onkeydown="if(event.key==='Enter'){event.preventDefault(); this.click()}">
144:             {{Picture}}
145:           </div>
146:         </div>
147:       {{/Picture}}
148:     </div>
149: 
150:     <!-- TRANSLATION — independent toggle (X/T, click), not part of More -->
151:     {{#Sentence}}
152:       {{#Translation}}
153:         <div class="translation-box"
154:              role="button"
155:              tabindex="0"
156:              aria-expanded="false"
157:               onclick="if(event.target.closest('.translation-text')) return; this.classList.toggle('revealed'); this.setAttribute('aria-expanded', this.classList.contains('revealed'))"
158:               onkeydown="if(event.key==='Enter'){event.preventDefault();this.click()}">
159:           <div class="translation-hint">訳 ▾</div>
160:           <div class="translation-text">{{edit:Translation}}</div>
161:         </div>
162:       {{/Translation}}
163:     {{/Sentence}}
164:     {{^Sentence}}
165:       {{#Translation}}
166:         <div class="translation-text revealed-static">{{edit:Translation}}</div>
167:       {{/Translation}}
168:     {{/Sentence}}
169: 
170:     <!-- LEVEL 4: SECONDARY INFORMATION — collapsed behind "詳細 ▾" -->
171:     <div class="more-section" hidden>
172:       {{#Sentence}}
173:         {{#context}}
174:           <div class="html-content secondary-block">{{edit:context}}</div>
175:         {{/context}}
176:       {{/Sentence}}
177: 
178:       {{#Kanji Notes}}
179:         <div class="html-content secondary-block">{{edit:Kanji Notes}}</div>
180:       {{/Kanji Notes}}
181: 
182:       {{#Notes}}
183:         <div class="html-content secondary-block">{{edit:furigana:Notes}}</div>
184:       {{/Notes}}
185: 
186:       <!-- Full Yomitan definition (only when the compact one exists too).
187:            Inert <template>: up to ~13KB of glossary is parsed but never
188:            rendered, styled, or laid out until More is first opened. -->
189:       {{#Definition}}
190:         {{#Extended definition}}
191:           <div class="extended-def-wrapper">
192:             <div class="extended-def-header">詳細辞書</div>
193:             <template class="extended-full-tpl">{{Extended definition}}</template>
194:             <div class="html-content secondary-block extended-full" data-lazy hidden></div>
195:           </div>
196:         {{/Extended definition}}
197:       {{/Definition}}
198: 
199:       <!-- Tags display inside More section -->
200:       {{#Tags}}
201:         <div class="tags-block secondary-block">{{Tags}}</div>
202:       {{/Tags}}
203:     </div>
204: 
205:     <!-- Two-way "詳細 ▾" / "閉じる ▴" toggle -->
206:     <button type="button" class="more-toggle" aria-expanded="false" onclick="toggleMore(this)">
207:       <span class="more-text">詳細</span> <span class="more-caret">▾</span>
208:     </button>
209: 
210:     <!-- SHORTCUT / FEATURE DISCOVERABILITY BAR
211:          R is Anki-owned (native replay) — never listed here as a template
212:          shortcut. Custom template shortcuts only: Z (furigana), X
213:          (translation), C (expanded-info toggle). -->
214:     <div class="shortcut-hints" aria-label="ショートカット">
215:       <span class="shortcut-item"><kbd>Z</kbd> 振仮名</span>
216:       <span class="shortcut-item"><kbd>X</kbd> 訳</span>
217:       <span class="shortcut-item"><kbd>C</kbd> 展開</span>
218:     </div>
219: 
220:     <!-- Source footer (secondary; stays outside More as a one-line
221:          quiet caption — it identifies the material, not a UI panel) -->
222:     {{#Source}}
223:       <div class="source-footer">{{edit:Source}}</div>
224:     {{/Source}}
225: 
226:   </div> <!-- End card-container -->
227: </div>
228: 
229: <!-- Lightbox, Audio, Frequency & Secondary-Section Scripts -->
230: <script>
231:   (function() {
232:     /* --- SECONDARY SECTION ("詳細 ▾" / "閉じる ▴" Two-way Toggle) --- */
233:     window.toggleMore = function(btn) {
234:       var section = document.querySelector('.more-section');
235:       if (!section) return;
236:       /* Lazy extended definition: stamp the inert template into its host
237:          once, on first open. Until then it costs no style/layout/paint. */
238:       section.querySelectorAll('template.extended-full-tpl').forEach(function(t) {
239:         var host = t.parentNode.querySelector('.extended-full');
240:         if (host && !host.hasChildNodes()) {
241:           host.appendChild(t.content.cloneNode(true));
242:           host.removeAttribute('hidden');
243:         }
244:         t.remove();
245:       });
246:       var isExpanded = btn.getAttribute('aria-expanded') === 'true';
247:       section.hidden = isExpanded;
248:       btn.setAttribute('aria-expanded', String(!isExpanded));
249:       btn.classList.toggle('is-open', !isExpanded);
250:       var textSpan = btn.querySelector('.more-text');
251:       if (textSpan) {
252:         textSpan.textContent = !isExpanded ? '閉じる' : '詳細';
253:       }
254:     };
255: 
256:     /* --- FREQUENCY VISUALIZER (5-Star Scale + Tier Theming) ---
257:        Single table: one edit point for thresholds, labels, fills. */
258:     const FREQ_TIERS = [
259:       { max: 500,   stars: 5, cls: 'freq-very-common', label: '最頻出 (上位500)',  fill: 95 },
260:       { max: 2500,  stars: 4, cls: 'freq-common',      label: '頻出 (上位2,500)',  fill: 75 },
261:       { max: 7000,  stars: 3, cls: 'freq-medium',      label: '常用 (上位7,000)',  fill: 55 },
262:       { max: 18000, stars: 2, cls: 'freq-uncommon',    label: '上級 (上位1.8万)',  fill: 35 },
263:       { max: Infinity, stars: 1, cls: 'freq-rare',     label: '稀少 (1.8万超)',    fill: 15 },
264:     ];
265:     window.renderFrequencyIndicator = function() {
266:       const badges = document.querySelectorAll('.frequency-badge[data-freq]');
267:       badges.forEach(badge => {
268:         const raw = badge.getAttribute('data-freq') || '';
269:         const match = raw.replace(/,/g, '').match(/\d+(?:\.\d+)?/);
270:         if (!match) return;
271: 
272:         const val = parseFloat(match[0]);
273:         if (isNaN(val) || val <= 0) return;
274: 
275:         // Japanese Frequency Tiers (Top 500 / 2.5k / 7k / 18k / Rare)
276:         let tier = FREQ_TIERS[FREQ_TIERS.length - 1];
277:         for (const t of FREQ_TIERS) { if (val <= t.max) { tier = t; break; } }
278:         const stars = tier.stars;
279:         const tierClass = tier.cls;
280:         const tierLabel = tier.label;
281:         const fillPercent = tier.fill;
282: 
283:         badge.classList.add(tierClass);
284:         badge.setAttribute('title', '語彙頻度: ' + raw.trim() + ' • ' + tierLabel);
285:         badge.setAttribute('aria-label', '語彙頻度: ' + tierLabel);
286: 
287:         const fill = badge.querySelector('.frequency-bar-fill');
288:         if (fill) fill.style.width = fillPercent + '%';
289: 
290:         const starContainer = badge.querySelector('.frequency-stars');
291:         if (starContainer) {
292:           starContainer.textContent = '★'.repeat(stars) + '☆'.repeat(5 - stars);
293:         }
294:       });
295:     };
296: 
297:     /* --- LIGHTBOX CONTROLLER (click to expand / click outside to close) --- */
298:     window.openLightbox = function(target) {
299:       const img = target.querySelector('img') || (target.tagName === 'IMG' ? target : null);
300:       if (!img || !img.getAttribute('src')) return;
301:       /* Only local Anki media: refuse remote/file URLs that would leak
302:          (IP/DNS) or fail outside the media dir. Relative paths pass. */
303:       if (/^(https?:|file:|javascript:|data:text\/html)/i.test(img.getAttribute('src'))) return;
304:       if (document.querySelector('.lightbox-overlay')) return;
305: 
306:       const overlay = document.createElement('div');
307:       overlay.className = 'lightbox-overlay';
308:       overlay.setAttribute('role', 'dialog');
309:       overlay.setAttribute('aria-modal', 'true');
310: 
311:       const clone = document.createElement('img');
312:       clone.src = img.src;
313:       clone.className = 'expanded-img';
314:       clone.referrerPolicy = 'no-referrer';
315:       clone.alt = img.alt || '';
316: 
317:       overlay.appendChild(clone);
318:       document.body.appendChild(overlay);
319: 
320:       const closeOverlay = () => {
321:         if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
322:         document.removeEventListener('keydown', handleKey);
323:         if (img.focus) img.focus();
324:       };
325: 
326:       const handleKey = (e) => {
327:         if (e.key === 'Escape') closeOverlay();
328:       };
329: 
330:       overlay.onclick = (e) => {
331:         if (e.target === overlay) closeOverlay();
332:       };
333:       document.addEventListener('keydown', handleKey);
334:     };
335: 
336:     /* Card flip with lightbox open: never orphan the overlay in a re-used DOM. */
337:     if (typeof window.addEventListener === 'function') {
338:       window.addEventListener('pagehide', () => {
339:         const ov = document.querySelector('.lightbox-overlay');
340:         if (ov && ov.parentNode) ov.parentNode.removeChild(ov);
341:       });
342:     }
343: 
344:     /* --- CIRCULAR AUDIO CONTROLLER (native-only) --- */
345:     window.currentActiveBtn = window.currentActiveBtn || null;
346:     window.currentActiveTimer = window.currentActiveTimer || null;
347:     /* WebView DOM re-use: never pin a detached button across card flips. */
348:     if (typeof window.addEventListener === 'function') {
349:         window.addEventListener('pagehide', () => { try { window.resetAudioState(); } catch (_) {} });
350:     }
351: 
352:     window.resetAudioState = function() {
353:         if (window.currentActiveTimer) {
354:             clearTimeout(window.currentActiveTimer);
355:             window.currentActiveTimer = null;
356:         }
357:         if (window.currentActiveBtn) {
358:             window.currentActiveBtn.classList.remove('is-playing');
359:             const ring = window.currentActiveBtn.querySelector('.ring-fill');
360:             if (ring) {
361:                 const circ = parseFloat(ring.getAttribute('stroke-dasharray')) || 119.38;
362:                 ring.style.transition = '';
363:                 ring.style.strokeDashoffset = circ;
364:             }
365:             window.currentActiveBtn = null;
366:         }
367:     };
368: 
369:     window.playCircularAudio = function(btn) {
370:         if (window.currentActiveBtn === btn) return;
371:         window.resetAudioState();
372:         const ringFill = btn.querySelector('.ring-fill');
373: 
374:         const scope = (btn.closest && btn.closest('.audio-btn-wrapper')) || document;
375:         const nativeReplay = scope.querySelector('.replaybutton, .replay-button, a.sound, .soundLink')
376:           || btn.querySelector('.replaybutton, .replay-button, a.sound, .soundLink');
377:         if (nativeReplay) {
378:             try { nativeReplay.click(); } catch (e) { return; }
379:             btn.classList.add('is-playing');
380:             if (ringFill) {
381:                 ringFill.style.transition = 'stroke-dashoffset 0.8s ease-in-out';
382:                 ringFill.style.strokeDashoffset = '0';
383:             }
384:             window.currentActiveBtn = btn;
385:             window.currentActiveTimer = setTimeout(() => {
386:                 if (window.currentActiveBtn === btn) {
387:                     window.resetAudioState();
388:                 }
389:             }, 800);
390:         }
391:     };
392: 
393:     /* --- DEFINITION TRUNCATOR (3-line cap + click to expand, stays open) --- */
394:     window.expandDefinition = function(element) {
395:       if (element.classList.contains('is-expanded')) return;
396:       element.classList.add('is-expanded');
397:       element.setAttribute('aria-expanded', 'true');
398:     };
399: 
400:     window.handleDefinitionKey = function(evt, element) {
401:       if (evt.key === 'Enter') {
402:         evt.preventDefault();
403:         window.expandDefinition(element);
404:       }
405:     };
406: 
407:     window.initDefinitionTruncation = function(root) {
408:       const scope = root || document;
409:       /* Subpixel rounding tolerance for scrollHeight vs clientHeight. */
410:       const TRUNC_SLACK_PX = 2;
411:       scope.querySelectorAll('.primary-definition').forEach(function(box) {
412:         if (!box.textContent || !box.textContent.trim()) { box.remove(); return; }
413:         box.classList.remove('is-expanded');
414:         box.setAttribute('aria-expanded', 'false');
415:         const overflows = box.scrollHeight > box.clientHeight + TRUNC_SLACK_PX;
416:         box.classList.toggle('is-truncated', overflows);
417:       });
418:     };
419: 
420:     /* --- GLOSSARY PRUNE (live-DOM twin of CSS §6b) ---
421:        §6b hides overflow dictionaries/senses/appendices with display:none,
422:        but hidden nodes still cost parse + style-match + layout. Removing
423:        exactly what §6b hides is rendering-identical and shrinks every
424:        later pass (including the truncation measure). Each removal mirrors
425:        one §6b rule 1:1 — keep them paired; test_compactor.py enforces the
426:        mirror on fixtures (prune ⇒ hide rules match nothing, text equal). */
427:     window.pruneCompactedGlossary = function(root) {
428:       const scope = root || document;
429:       /* CSS `A ~ A` counts preceding same-parent siblings: group matches
430:          by parent, drop from index `keep` on. Mirrors §6b keep-counts:
431:          dictionaries 1, senses 2 (l3-a keeps 1), plain glosses 2. */
432:       const dropFrom = (box, sel, keep) => {
433:         const byParent = new Map();
434:         box.querySelectorAll(sel).forEach(function(el) {
435:           const p = el.parentNode;
436:           if (!byParent.has(p)) byParent.set(p, []);
437:           byParent.get(p).push(el);
438:         });
439:         byParent.forEach(function(list) {
440:           for (let i = keep; i < list.length; i++) list[i].remove();
441:         });
442:       };
443:       scope.querySelectorAll('.primary-definition').forEach(function(box) {
444:         dropFrom(box, '.yomitan-glossary > ol > li', 1);
445:         dropFrom(box, 'div[data-sc-name="語義G"]', 2);
446:         dropFrom(box, 'div[data-sc-l3]', 2);
447:         dropFrom(box, 'div[data-sc-l3-a]', 1);
448:         dropFrom(box, '[data-sc-content="glossary"] > li', 2);
449:         box.querySelectorAll(
450:           'div[data-sc-name="補説G"], span[data-sc-name="可能形"], ' +
451:           'span[data-sc-name="歴史仮名"], span[data-sc-name="アクセントG"], ' +
452:           'li[data-sc-content="forms"], div[data-sc-content="attribution"], i'
453:         ).forEach(function(n) { n.remove(); });
454:       });
455:     };
456: 
457:     /* --- SECONDARY SECTION CLEANUP + KEYBOARD SHORTCUTS --- */
458:     window.initSecondarySection = function() {
459:       try {
460:         var section = document.querySelector('.more-section');
461:         var btn = document.querySelector('.more-toggle');
462:         if (section && btn) {
463:           section.querySelectorAll('.secondary-block, .extended-full').forEach(function(el) {
464:             /* Lazy host: content lives in the sibling template until first
465:                open — never strip it here. */
466:             if (el.hasAttribute('data-lazy')) return;
467:             if (!el.textContent || !el.textContent.trim()) el.remove();
468:           });
469:           if (!section.querySelector('.secondary-block, .extended-full, template.extended-full-tpl')) {
470:             btn.remove();
471:             section.remove();
472:           }
473:         }
474:       } catch (e) { /* keep default rendering */ }
475:       try {
476:         document.querySelectorAll('.translation-box, .revealed-static').forEach(function(el) {
477:           if (!el.textContent || !el.textContent.trim()) el.remove();
478:         });
479:       } catch (e) { /* keep default rendering */ }
480:     };
481: 
482:     window.initCardShortcuts = function() {
483:       var wrapper = document.querySelector('.card-wrapper.back-card');
484:       if (!wrapper || wrapper.dataset.shortcutsBound) return;
485:       wrapper.dataset.shortcutsBound = '1';
486:       document.addEventListener('keydown', function(e) {
487:         if (e.altKey || e.ctrlKey || e.metaKey) return;
488:         var tag = (e.target && e.target.tagName) || '';
489:         if (tag === 'INPUT' || tag === 'TEXTAREA' || (e.target && e.target.isContentEditable)) return;
490:         var key = (e.key || '').toLowerCase();
491:         if (key === 'z' || key === 'f') {
492:           e.preventDefault();
493:           e.stopPropagation();
494:           wrapper.classList.toggle('furigana-mode');
495:         } else if (key === 'x' || key === 't') {
496:           e.preventDefault();
497:           e.stopPropagation();
498:           var box = wrapper.querySelector('.translation-box');
499:           if (!box) return;
500:           var isRevealed = box.classList.contains('revealed');
501:           if (isRevealed) {
502:             box.classList.remove('revealed');
503:             box.setAttribute('aria-expanded', 'false');
504:           } else {
505:             box.classList.add('revealed');
506:             box.setAttribute('aria-expanded', 'true');
507:           }
508:         } else if (key === 'c') {
509:           e.preventDefault();
510:           e.stopPropagation();
511:           /* C toggles More + definitions (isolated: never touches translation) */
512:           var moreBtn = wrapper.querySelector('.more-toggle');
513:           var isCurrentlyOpen = moreBtn && moreBtn.getAttribute('aria-expanded') === 'true';
514: 
515:           if (!isCurrentlyOpen) {
516:             if (moreBtn) window.toggleMore(moreBtn);
517:             wrapper.querySelectorAll('.primary-definition').forEach(function(d) {
518:               window.expandDefinition(d);
519:             });
520:           } else {
521:             if (moreBtn) window.toggleMore(moreBtn);
522:           }
523:         }
524:       });
525:     };
526: 
527:     /* Prune first: the truncation measure below then runs over the small
528:        live DOM instead of the full hidden glossary. */
529:     window.pruneCompactedGlossary();
530:     window.renderFrequencyIndicator();
531:     window.initSecondarySection();
532:     window.initCardShortcuts();
533: 
534:     /* Truncation is measured ONCE, after fonts settle: the boot-time measure
535:        forced a full sync layout over the glossary, then fonts.ready forced
536:        it again (the early result can be wrong once webfonts arrive, so it
537:        was partly thrown away). Local fonts resolve pre-paint, so the
538:        chevron timing is unchanged in practice. */
539:     window.__truncQueued = false;
540:     window.queueTruncation = function() {
541:       if (window.__truncQueued) return;
542:       window.__truncQueued = true;
543:       var run = function() {
544:         window.__truncQueued = false;
545:         window.initDefinitionTruncation();
546:       };
547:       try {
548:         if (document.fonts && document.fonts.ready) document.fonts.ready.then(function() {
549:           window.renderFrequencyIndicator();
550:           run();
551:         });
552:         else if (typeof requestAnimationFrame === 'function') requestAnimationFrame(run);
553:         else setTimeout(run, 0);
554:       } catch (e) { run(); }
555:     };
556:     window.queueTruncation();
557:   })();
558: </script>
````

## File: tests/test_templates.py
````python
  1: #!/usr/bin/env python3
  2: """Template & CSS structural invariant tests.
  3: 
  4: Verifies the source files BEFORE they are pushed to Anki:
  5:   - Front card never renders a furigana-bearing field (back-card-only rule)
  6:   - Front is a pure retrieval surface (no tags/badges/metadata UI)
  7:   - Listening is a hidden-by-default resolver: #listening tag or classic
  8:     audio-only fields activate it; the sentence front is the fallback
  9:   - Secondary back information is collapsed behind "More ▾"
 10:   - Audio buttons carry aria-labels; controller is restart-only
 11:   - Lightbox closes only on backdrop clicks (not on the enlarged image)
 12:   - Anki template conditionals are balanced
 13:   - CSS contains the accessibility/portability rules
 14: 
 15: Run directly:  python3 tests/test_templates.py
 16: Wired into finish.sh step 0 alongside test_compactor.py.
 17: 
 18: Pure standard library — no dependencies.
 19: """
 20: import os
 21: import re
 22: import shutil
 23: import subprocess
 24: import sys
 25: 
 26: HERE = os.path.dirname(os.path.abspath(__file__))
 27: ROOT = os.path.dirname(HERE)
 28: 
 29: FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
 30: BACK = os.path.join(ROOT, "Card 1 - Back.template.anki")
 31: CSS = os.path.join(ROOT, "Card 1 - Style.css")
 32: 
 33: PASS = 0
 34: FAIL = 0
 35: 
 36: 
 37: def check(name, cond):
 38:     global PASS, FAIL
 39:     tag = "PASS" if cond else "FAIL"
 40:     print(f"[{tag}] {name}")
 41:     if cond:
 42:         PASS += 1
 43:     else:
 44:         FAIL += 1
 45: 
 46: 
 47: def main():
 48:     front = open(FRONT, encoding="utf-8").read()
 49:     back = open(BACK, encoding="utf-8").read()
 50:     css = open(CSS, encoding="utf-8").read()
 51: 
 52:     # --- 1. Front card: furigana is back-card only ---
 53:     furigana_fields = re.findall(r"\{\{[^}]*furigana[^\d}][^}]*\}\}", front)
 54:     # allowed: none. Front uses plain Sentence/Expression only.
 55:     check("Front renders no furigana: filter or furigana-bearing field",
 56:           not furigana_fields and "Sentence (furigana)" not in front)
 57:     check("Front renders the raw Sentence/Expression fields",
 58:           "{{edit:Sentence}}" in front and "{{edit:Expression}}" in front)
 59: 
 60:     # --- 1b. Template scripts must be syntactically valid JavaScript ---
 61:     # A SyntaxError in a card script kills the WHOLE script block: no
 62:     # reveal, no mature mode, no listening resolver — the card hangs
 63:     # hidden. Structural string checks cannot catch an unbalanced brace,
 64:     # so parse every <script> body with node (skipped if node absent).
 65:     node = shutil.which("node")
 66:     if node:
 67:         import tempfile as _tempfile
 68:         for name, src in (("Front", front), ("Back", back)):
 69:             bodies = re.findall(r"<script>(.*?)</script>", src, re.S)
 70:             all_ok = True
 71:             for body in bodies:
 72:                 with _tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
 73:                     tf.write(body)
 74:                     tmp_path = tf.name
 75:                 try:
 76:                     rc = subprocess.run([node, "--check", tmp_path],
 77:                                         capture_output=True, timeout=30).returncode
 78:                     if rc != 0:
 79:                         all_ok = False
 80:                 finally:
 81:                     os.unlink(tmp_path)
 82:             check(f"{name}: all {len(bodies)} script block(s) parse as valid JavaScript", all_ok)
 83:     else:
 84:         print("[SKIP] node not found — template script syntax check skipped")
 85: 
 86:     # --- 2. Audio buttons: aria-labels present ---
 87:     # Front is sentence-audio-only (1) + Back has word + sentence (2) = 3 total.
 88:     # (Word-audio fallback was removed from the front listening mode.)
 89:     buttons = re.findall(r"<button[^>]*circular-audio-btn[^>]*>", front + back)
 90:     check(f"all {len(buttons)} audio buttons have aria-label",
 91:           len(buttons) >= 3 and all("aria-label" in b for b in buttons))
 92: 
 93:     # --- 3. Audio controller: native-only (no HTML5 Audio path) ---
 94:     for name, src in (("Front", front), ("Back", back)):
 95:         check(f"{name}: no is-paused state remnants",
 96:               "is-paused" not in src)
 97:         check(f"{name}: resetAudioState defined",
 98:               "window.resetAudioState = function" in src)
 99:         check(f"{name}: native-only playback (no new Audio garbage-loads on AnkiDroid)",
100:               "new Audio(" not in src)
101:         check(f"{name}: delegates to Anki replay link",
102:               "nativeReplay.click()" in src)
103:         check(f"{name}: replay link resolved via wrapper scope (not nested in button)",
104:               "closest('.audio-btn-wrapper')" in src)
105:         check(f"{name}: re-tap debounce (native audio can't be stopped)",
106:               "window.currentActiveBtn === btn" in src)
107:         # restart-only: every click path goes through resetAudioState first
108:         check(f"{name}: playCircularAudio starts with resetAudioState",
109:               re.search(r"window\.playCircularAudio = function\(btn\) \{\s*(/\*.*?\*/\s*)*if \(window\.currentActiveBtn === btn\) return;\s*window\.resetAudioState\(\);", src, re.S) is not None)
110: 
111:     # --- 3b. Audio markup: valid + clickable on AnkiDroid ---
112:     for name, src in (("Front", front), ("Back", back)):
113:         check(f"{name}: replay source lives OUTSIDE the button (sibling span)",
114:               re.search(r"</button>\s*<span class=\"raw-audio-source\"", src) is not None)
115:         check(f"{name}: no display:none audio source (breaks .click() playback)",
116:               "raw-audio-source\" style=\"display:none" not in src)
117:         check(f"{name}: no div-inside-button (invalid HTML, breaks AnkiDroid taps)",
118:               '<div class="audio-btn-content">' not in src)
119:     check("CSS: raw-audio-source visually hidden but present (no display:none)",
120:           re.search(r"\.raw-audio-source\s*\{[^}]*position:\s*absolute", css) is not None
121:           and ".raw-audio-source" in css)
122: 
123:     # --- 2c. Cloze fallback: bold-less Sentence rebuilt from cloze trio ---
124:     check("Front: hidden cloze probe with plain prefix/body/suffix fields",
125:           'class="cloze-probe"' in front
126:           and "{{cloze-prefix}}" in front and "{{cloze-body}}" in front
127:           and "{{cloze-suffix}}" in front)
128:     check("Front: probe uses plain fields (no edit: filter, stays furigana-free)",
129:           "edit:cloze" not in front)
130:     check("Front: reconstruction only fires when sentence lacks bold",
131:           "querySelector('b, strong')" in front)
132:     check("Front: reconstruction requires the complete trio (no partial rebuild)",
133:           "clozePre && clozeMid && clozeSuf" in front)
134:     check("Front: rebuilt term uses <b> (inherits sentence-display styling)",
135:           "createElement('b')" in front)
136: 
137:     # --- 4. Lightbox: backdrop-only close ---
138:     check("lightbox closes only on backdrop click (e.target === overlay)",
139:           "if (e.target === overlay) closeOverlay()" in back)
140:     check("lightbox overlay has dialog semantics",
141:           "setAttribute('role', 'dialog')" in back and "setAttribute('aria-modal', 'true')" in back)
142:     check("lightbox clone preserves alt text", "img.alt" in back)
143: 
144:     # --- 5. Anki conditionals balanced ({{#field}} and {{^field}} both open) ---
145:     for name, src in (("Front", front), ("Back", back)):
146:         opens = len(re.findall(r"\{\{[#^][A-Za-z]", src))
147:         closes = len(re.findall(r"\{\{/[A-Za-z]", src))
148:         check(f"{name}: balanced field conditionals ({opens} open / {closes} close)",
149:               opens == closes)
150: 
151:     # --- 6. CSS invariants ---
152:     check("CSS: :focus-visible keyboard indicator present",
153:           ":focus-visible" in css)
154:     check("CSS: prefers-reduced-motion present",
155:           "prefers-reduced-motion: reduce" in css)
156:     check("CSS: content-driven card sizing (no forced viewport fill)",
157:           "min-height: 100vh" not in css and "min-height: 100dvh" not in css
158:           and "container-type: inline-size" in css)
159:     check("CSS: container-query media fallback for the context grid",
160:           re.search(r"@media \(min-width: 768px\)[\s\S]{0,200}\.context-grid", css) is not None)
161: 
162:     # --- 6b. Redesign: hierarchy with frequency visualizer ---
163:     check("Back: no sticky tags bar (tags are behavioral metadata)",
164:           "tags-container" not in back and "tags-list" not in back
165:           and "tag-pill" not in back)
166:     check("Back: frequency visualizer present",
167:           "frequency-badge" in back and "renderFrequencyIndicator" in back)
168:     check("CSS: frequency badge styling present",
169:           "frequency-badge" in css and "--freq-" in css)
170:     check("Back: secondary info is collapsed behind More by default",
171:           'class="more-section" hidden' in back
172:           and "more-toggle" in back)
173:     check("Back: More toggle has aria state + toggle behavior",
174:           'aria-expanded="false"' in back
175:           and "toggleMore" in back)
176:     check("Back: no retrieval-state label UI (content hierarchy replaces captions)",
177:           "retrieval-state" not in back and "__ajtFrontState" not in back)
178:     check("Front: no front-state store written",
179:           "__ajtFrontState" not in front)
180:     check("CSS: no retrieval-state styling remains",
181:           "retrieval-state" not in css)
182:     check("Back: keyboard F toggles full-card furigana (back only)",
183:           "furigana-mode" in back and "'f'" in back)
184:     check("Back: keyboard T reveals the translation",
185:           "'t'" in back and "translation-box" in back)
186:     check("CSS: full-card furigana mode rule exists",
187:           ".card-wrapper.furigana-mode ruby rt" in css)
188:     # --- 6c. Listening mode invariants ---
189:     check("Front: listening markup gated behind Definition/Extended/Frequency absence",
190:           re.search(r"\{\{\^Frequency\}\}[\s\S]*?\{\{#Sentence Audio\}\}\s*<div class=\"listening-view", front) is not None)
191:     check("Front: listening resolver checks for rendered listening view",
192:           "LISTENING RESOLVER" in front and ("querySelector('.listening-view')" in front or "querySelector('.classic-listening-view')" in front))
193:     check("Front: sentence front is the universal fallback",
194:           re.search(r"\{\{#Definition\}\}\s*<div class=\"sentence-display\">", front) is not None)
195:     check("CSS: listening-view flex styled",
196:           ".listening-view" in css and re.search(r"\.listening-view\s*\{[^}]*display:\s*flex", css) is not None)
197:     check("CSS: listening mode hides the sentence/word fronts",
198:           ".card-wrapper.listening-mode .sentence-display" in css)
199: 
200:     # --- 6d. Listening audio source + Policy B (Features 2, 3) ---
201:     # The tag-listening-view delegates to Anki's answer-side audio (play:a:N /
202:     # playsound:a:N) to avoid Anki's C++/Python reviewer auto-playing audio on
203:     # every tagged normal card on load (which happens whenever [sound:...] is
204:     # in the front HTML regardless of CSS display:none).
205:     # On the back card, Word Audio is first (a:0) and Sentence Audio is second (a:1):
206:     # - Both exist: Sentence Audio is a:1 (label 文)
207:     # - Only Sentence Audio exists: Sentence Audio is a:0 (label 文)
208:     # - Only Word Audio exists: Word Audio is a:0 (label 言葉)
209:     tag_block = re.search(r'<!-- Behavioral tag probe.*?\{\{/Tags\}\}', front, re.S)
210:     check("Front: tag-listening-view block present",
211:           tag_block is not None)
212:     if tag_block:
213:         tag_src = tag_block.group(0)
214:         # Binds to Sentence Audio: plays a:1 when Word Audio is also present,
215:         # and a:0 when Word Audio is absent. Never plays Word Audio (a:0) when
216:         # Sentence Audio is present and labelled 文.
217:         check("Front: tag-listening-view plays Sentence Audio (a:1 when Word Audio also present)",
218:               "pycmd('play:a:1')" in tag_src
219:               and "playsound:a:1" in tag_src
220:               and "文" in tag_src)
221:         check("Front: tag-listening-view plays Sentence Audio (a:0 when Word Audio absent)",
222:               re.search(r'\{\{\^Word Audio\}\}[\s\S]*?文[\s\S]*?pycmd\(\'play:a:0\'\)', tag_src) is not None)
223:         check("Front: tag-listening-view falls back to Word Audio (a:0) with 言葉 label",
224:               re.search(r'\{\{\^Sentence Audio\}\}[\s\S]*?\{\{#Word Audio\}\}[\s\S]*?言葉[\s\S]*?pycmd\(\'play:a:0\'\)', tag_src) is not None)
225:         # CRITICAL: raw {{Sentence Audio}} must NOT appear inside {{#Tags}} on
226:         # front — otherwise Anki auto-plays audio on every tagged normal card.
227:         check("Front: no raw audio fields inside {{#Tags}} (prevents auto-play on normal cards)",
228:               re.search(r'\{\{#Tags\}\}[\s\S]*?\{\{Sentence Audio\}\}[\s\S]*?\{\{/Tags\}\}', front) is None
229:               and re.search(r'\{\{#Tags\}\}[\s\S]*?\{\{Word Audio\}\}[\s\S]*?\{\{/Tags\}\}', front) is None)
230:     check("Front: Policy B — #listening without usable audio falls back to sentence front",
231:           "hasUsableAudio" in front and "Policy B" in front)
232:     check("Front: exactly-one-listening-button cleanup removes dead/duplicate views",
233:           "Dead/duplicate view cleanup" in front
234:           and "container.querySelectorAll('.listening-view').forEach" in front)
235:     check("Front: last-resort pycmd fallback is documented (not the primary path)",
236:           "Last-resort fallback" in front)
237: 
238:     # --- 6e. R shortcut is Anki-owned, never template-owned (Feature 1) ---
239:     check("Back: R shortcut hint removed from shortcut UI (Anki-owned)",
240:           '<kbd>R</kbd>' not in back)
241:     check("Back: custom template shortcuts are Z, X, C only",
242:           all(k in back for k in ['<kbd>Z</kbd>', '<kbd>X</kbd>', '<kbd>C</kbd>']))
243: 
244:     # --- 6f. Audio terminology: playback indicator, not progress ring (Feature 4) ---
245:     check("Front: ring described as playback indicator (not true progress)",
246:           "playback indicator" in front.lower())
247:     check("CSS: ring described as playback indicator",
248:           "playback indicator" in css.lower())
249: 
250:     # --- 7. Font sizing source-of-truth ---
251:     check("Back: no JS font-scaler overriding CSS (inline fontSize ban)",
252:           "el.style.fontSize" not in back and "autoScaleBackSentence" not in back)
253:     check("CSS: .sentence-japanese clamp() is the sizing authority",
254:           re.search(r"\.sentence-japanese\s*\{[^}]*font-size:\s*clamp\(", css) is not None)
255: 
256:     # --- 8. (removed) Frequency visualizer retired with the minimal redesign ---
257: 
258:     # --- 8b. Mature Word Mode invariants (interval-gated front) ---
259:     check("Front: LONG_INTERVAL_DAYS threshold constant defined",
260:           re.search(r"const\s+LONG_INTERVAL_DAYS\s*=\s*365", front) is not None
261:           and "interval >= LONG_INTERVAL_DAYS" in front)
262:     check("Front: threshold not hard-coded elsewhere (single const definition)",
263:           len(re.findall(r"LONG_INTERVAL_DAYS\s*=\s*365", front)) == 1
264:           and len(re.findall(r">=\s*365", front)) == 0)
265:     check("Front: word probe div present with Expression",
266:           re.search(r'class="front-word-display">\s*\{\{edit:Expression\}\}', front) is not None)
267:     check("Front: no guiCurrentCard call anywhere (fallback-only word mode)",
268:           "'guiCurrentCard'" not in front
269:           and re.search(r"cardsInfo.*?interval", front, re.S) is not None)
270:     check("Front: word-mode interval via content search (findCards)",
271:           "findCards" in front and "content search" in front
272:           and "BROWSE-PREVIEWER CONTENT SEARCH" in front)
273:     check("Front: no nonexistent Anki-Connect actions",
274:           "getCardsInfo" not in front)
275:     check("Front: no card-id-from-URL guess (no URLSearchParams)",
276:           "URLSearchParams" not in front)
277:     check("Front: no executable AnkiDroid JS API code remains",
278:           "AnkiDroidJS" not in front and "ankiGetCardInterval" not in front)
279:     check("Front: no bridge helpers / polling remain",
280:           "safeApiCall" not in front and "withBridgeTimeout" not in front
281:           and "parseDroidInterval" not in front
282:           and "bridgeAvailable" not in front and "waitForBridge" not in front
283:           and "apiKind" not in front
284:           and "signal:jsapi" not in front)
285:     check("Front: post helper UA-guards every AnkiConnect call (mobile rejects before fetch)",
286:           re.search(r"const post = \(action, params\) => \{[\s\S]*?/Android\|iPhone\|iPad\|iPod/i\.test\(ua\)", front) is not None
287:           and "AnkiConnect is desktop-only" in front)
288:     check("Front: mobile never reaches a fetch (guard inside post, before fetch)",
289:           re.search(r"const post = \(action, params\) => \{[\s\S]*?fetch\('http://127\.0\.0\.1:8765'", front, re.S) is not None)
290:     check("Front: retrieval remains platform-exclusive (DESKTOP-ONLY marker)",
291:           "DESKTOP-ONLY" in front)
292:     check("Front: retrieval latency is measured and logged",
293:           "performance.now" in front and "elapsedMs" in front
294:           and "[Mature Word Mode] source=" in front)
295:     check("Front: safety reveal cap bounds worst-case hidden time",
296:           "setTimeout(reveal, 1200)" in front)
297:     check("Front: AnkiConnect calls fail fast when Anki is wedged (safe sentence fallback)",
298:           "AnkiConnect timeout" in front and ", 500)" in front)
299:     check("Front: temporary toast diagnostic removed (no TEMP-DIAG remnants)",
300:           "TEMP-DIAG" not in front and "ankiShowToast" not in front)
301:     check("Front: on-card debug diagnostic present (mwm-debug)",
302:           "DEBUG_MATURE_MODE" in front and "mwm-debug" in front
303:           and "Mature mode: " in front)
304:     check("Front: skips ALL retrieval on listening cards (no needless JS-API calls)",
305:           "isListening" in front)
306:     check("Front: anti-flash visibility gate present",
307:           'style="visibility: hidden;"' in front
308:           and "container.style.visibility = 'visible'" in front)
309:     check("Front: word-mode class applied to card wrapper",
310:           "wrapper.classList.toggle('word-mode'" in front)
311:     check("Front: retrieval failure falls back to sentence (try/catch + typed interval check)",
312:           "catch" in front and "typeof interval === 'number'" in front)
313:     check("CSS: word-mode display rules present",
314:           ".card-wrapper.word-mode .sentence-display" in css
315:           and ".card-wrapper.word-mode .front-word-display" in css)
316:     check("CSS: word mode leaves listening view untouched",
317:           ".listening-view" not in css.split("5b. MATURE-CARD WORD MODE")[1].split("6. BACK CARD")[0]
318:           if "5b. MATURE-CARD WORD MODE" in css else False)
319:     check("Front: no \"note:\" search clause ({{Type}} is scheduling type, not model)",
320:           "NOTE_TYPE" not in front
321:           and re.search(r"findCards[^\n]*note:", front) is None
322:           and 'escQuery(NOTE_TYPE)' not in front)
323: 
324:     # --- 8c. Mature content-search invariants (fallback-only word mode) ---
325:     # Content search is the ONLY retrieval path (guiCurrentCard removed).
326:     # It must:
327:     # - NEVER pick candidate 0 blindly (matches[0] is banned)
328:     # - Use Sentence then cloze-body as discriminators
329:     # - Fail safely to sentence mode when ambiguity remains
330:     check("Front: content search never picks candidate 0 (matches[0] banned)",
331:           "matches[0]" not in front
332:           and re.search(r"candidates\[0\]", front) is not None)  # only after discriminators narrow to 1
333:     check("Front: content search uses Sentence discriminator",
334:           "Discriminator 1: Sentence" in front)
335:     check("Front: content search uses cloze-body discriminator",
336:           "Discriminator 2: cloze-body" in front)
337:     check("Front: content search fails safely on ambiguity (sentence fallback)",
338:           "content-search-ambiguous" in front
339:           and "sentence fallback" in front)
340:     check("Front: content search uses exact-card resolution (length === 1)",
341:           "candidates.length === 1" in front)
342: 
343:     # --- 10. Empty-field collapse (QUALITY.md: no UI survives an empty field) ---
344:     # 10a. Static proof over the raw templates (comments/scripts stripped):
345:     # every rendered field lives inside an Anki conditional, except the
346:     # documented allowlist (attribute / hidden probe / gated probe).
347:     TOKEN = re.compile(r"\{\{\s*([#^/]?)\s*([^}]*?)\s*\}\}")
348:     ALLOW_BARE = {
349:         ("Front", "cloze-prefix"), ("Front", "cloze-body"), ("Front", "cloze-suffix"),  # hidden probe
350:         ("Front", "Expression"),  # front-word-display: display:none default, word-mode gate only (§8b)
351:     }
352:     bare = []
353:     for name, src in (("Front", front), ("Back", back)):
354:         clean = re.sub(r"<!--.*?-->", "", src, flags=re.S)
355:         clean = re.sub(r"<script.*?</script>", "", clean, flags=re.S)
356:         stack = []
357:         for m in TOKEN.finditer(clean):
358:             sig, body = m.group(1), m.group(2).strip()
359:             if sig in ("#", "^"):
360:                 stack.append(body)
361:             elif sig == "/":
362:                 if stack:
363:                     stack.pop()
364:             elif body:
365:                 field = body.split(":")[-1].strip()
366:                 if not stack and (name, field) not in ALLOW_BARE:
367:                     bare.append(f"{name}:{{{{{body}}}}}")
368:     check("every rendered field is conditional (or allowlisted)" + (f" — bare: {bare}" if bare else ""),
369:           not bare)
370: 
371:     # 10b. Unconditional shells collapse when all conditional children absent.
372:     check("CSS: empty .audio-row collapses (no button => gone)",
373:           re.search(r"\.audio-row:not\(:has\(\.circular-audio-btn\)\)\s*\{\s*display:\s*none", css) is not None)
374:     check("CSS: empty .context-grid collapses (no sentence/context/picture => gone)",
375:           re.search(r"\.context-grid:not\(:has\([^)]+\)\)\s*\{\s*display:\s*none", css) is not None)
376:     check("CSS: empty .context-main collapses (no sentence/context => gone)",
377:           re.search(r"\.context-main:not\(:has\([^)]+\)\)\s*\{\s*display:\s*none", css) is not None)
378:     check("CSS: empty .hero-header collapses (no word/meta => gone)",
379:           re.search(r"\.hero-header:not\(:has\([^)]+\)\)\s*\{\s*display:\s*none", css) is not None)
380:     check("Back: hero-header splits meta left/right around a centered word",
381:           'class="hero-header"' in back
382:           and 'class="hero-side hero-side-left"' in back
383:           and 'class="hero-side hero-side-right"' in back
384:           and back.index('hero-side-left') < back.index('hero-word-wrap') < back.index('hero-side-right')
385:           and back.index('{{#Frequency}}') < back.index('hero-word-wrap')
386:           and back.index('{{#Word Audio}}') < back.index('hero-word-wrap')
387:           and back.index('hero-word-wrap') < back.index('{{#Pitch Accent}}')
388:           and back.index('hero-word-wrap') < back.index('{{#Sentence Audio}}'))
389:     check("CSS: hero-header is a 3-column grid (left | word | right)",
390:           re.search(r"\.hero-header\s*\{[^}]*display:\s*grid", css) is not None
391:           and '"left word right"' in css)
392:     check("CSS: hero sides hug the word (end/start), narrow stacks word on top",
393:           re.search(r"\.hero-side-left\s*\{[^}]*justify-content:\s*flex-end", css) is not None
394:           and re.search(r"\.hero-side-right\s*\{[^}]*justify-content:\s*flex-start", css) is not None
395:           and '"word word"' in css)
396:     check("CSS: hero word never forces horizontal overflow (min-width + anywhere wrap)",
397:           re.search(r"\.hero-word-wrap\s*\{[^}]*min-width:\s*0", css) is not None
398:           and re.search(r"\.word-display\s*\{[^}]*overflow-wrap:\s*anywhere", css) is not None)
399:     check("CSS: picture fills the parallel row (generous desktop cap, compact mobile cap)",
400:           "max-height: 44vh" in css
401:           and "max-height: clamp(24vh, 22vmin, 32vh)" in css
402:           and "min(46vw, 640px)" in css)
403:     check("Back: stylized separators before AND after the definition",
404:           back.count('class="card-separator"') == 2
405:           and back.index('class="card-separator"') < back.index('primary-definition'))
406:     check("CSS: context-grid row is top-anchored in both container + fallback rules",
407:           len(re.findall(r"\.context-grid:has\(\.context-picture\)\s*\{[^}]*align-items:\s*flex-start", css)) == 2
408:           and len(re.findall(r"\.context-grid:has\(\.context-picture\)\s*\{[^}]*align-items:\s*center", css)) == 0)
409:     check("Back: More section + toggle self-remove when secondary content is absent",
410:           "btn.remove()" in back and "section.remove()" in back)
411: 
412:     # 10c. Degenerate content removes itself instead of leaving chrome behind.
413:     check("Back: blank definition box is removed (no bordered void)",
414:           "box.remove()" in back)
415:     check("Front: blank sentence block is removed after cloze fixup",
416:           "sd.remove()" in front)
417: 
418:     # --- 9. Sync tooling invariants ---
419:     sync = open(os.path.join(ROOT, "sync_to_anki.py"), encoding="utf-8").read()
420:     check("sync_to_anki.py: zero third-party imports (standard lib only)",
421:           "import requests" not in sync and "import urllib.request" in sync)
422:     check("sync_to_anki.py: microsecond backup timestamps",
423:           "%H%M%S-%f" in sync)
424:     finish = open(os.path.join(ROOT, "finish.sh"), encoding="utf-8").read()
425:     check("finish.sh: no-op run cannot publish a release",
426:           "Nothing to push or release" in finish)
427:     # Deterministic release ordering: push main BEFORE gh release create so
428:     # the tag points at the exact pushed commit (--target main).
429:     # Strip comments to check actual command order.
430:     finish_code = re.sub(r"^\s*#[^\n]*\n", "", finish, flags=re.M)
431:     finish_code = re.sub(r"^\s*#[^\n]*$", "", finish_code, flags=re.M)
432:     check("finish.sh: push main before gh release create (--target main)",
433:           "git push origin main" in finish_code
434:           and "gh release create" in finish_code
435:           and finish_code.index("git push origin main") < finish_code.index("gh release create")
436:           and "--target main" in finish_code)
437:     check("finish.sh: fetches the remote tag after release creation",
438:           finish_code.index("gh release create") < finish_code.rindex("git fetch origin \"refs/tags/*:refs/tags/*\""))
439:     check("finish.sh: verify runs before version stamp (step 0 before step 1)",
440:           finish.index("./verify") < finish.index("NEW_TAG="))
441: 
442:     print()
443:     print(f"{PASS} passed, {FAIL} failed")
444:     return 1 if FAIL else 0
445: 
446: 
447: if __name__ == "__main__":
448:     sys.exit(main())
````

## File: Card 1 - Front.template.anki
````
  1: <!-- FRONT CARD TEMPLATE
  2:      Premium Ergonomic Japanese Front Card
  3: 
  4:        Behavior:
  5:        - Standard: Shows Sentence (or Expression) if Definition / Extended definition exists. Zero audio on front.
  6:        - Listening (Policy B): #listening (or the legacy audio-only shape)
  7:          activates the listening front ONLY when usable audio exists.
  8:          The tag-listening-view binds to {{Sentence Audio}} (label 文),
  9:          falling back to {{Word Audio}} (label 言葉) — never the hardcoded
 10:          play:a:0 (which plays the first audio field = Word Audio on
 11:          listening cards). #listening + no usable audio falls back to the
 12:          normal sentence front. The resolver removes every dead/duplicate
 13:          view so exactly one listening button is ever visible.
 14:        - Cloze Fallback: Sentence without a bold term (jidoushio mobile
 15:          exports) is rebuilt in JS from cloze-prefix + <b>cloze-body</b>
 16:          + cloze-suffix when all three are non-empty; otherwise the
 17:          usual sentence is kept untouched.
 18:        - Frequency legacy: No definitions but Frequency present (old cards with deleted glosses) → usual sentence, never the audio button.
 19:        - Fallback: Shows Sentence / Expression if both definitions and audio are missing.
 20: - Mature Word Mode (desktop only): If the card interval >= LONG_INTERVAL_DAYS
 21:           (script constant), the front shows only the Expression instead of the
 22:           sentence (anti-overlearning). The interval comes from a
 23:           fallback-only AnkiConnect content search (Expression → Sentence →
 24:           cloze-body discriminators) — the live guiCurrentCard reviewer read
 25:           was REMOVED so reviewer and Browse previewer share one identical
 26:           path. It never picks candidate 0 blindly and fails safely to the
 27:           sentence front on ambiguity.
 28:           On Android/mobile Mature Word Mode is INTENTIONALLY DISABLED: the
 29:           template makes no AnkiDroid JS API call and no AnkiConnect fetch
 30:           (the fetch is UA-guarded inside `post`), because refused localhost
 31:           requests surface natively as false "Card Content Error: Failed to
 32:           load" media warnings in the reviewer. Mobile always keeps the
 33:           ordinary sentence front. Any failure falls back to the sentence
 34:           front.
 35:          - Front sentence sizing: pure CSS (base clamp + smaller phone
 36:            override in the stylesheet's mobile block). No JS involved.
 37:          - Front reveal is deterministic and safe: the anti-flash
 38:            visibility gate never depends on a single async path or timer
 39:            that can be throttled into a blank front. R shortcut is
 40:            Anki-owned; the template's custom shortcuts are Z/X/C only.
 41: 
 42:          Minimalism (PRODUCT.md): the front shows NO other UI — no tags,
 43:          no badges, no metadata, no labels, NO AUDIO on normal cards.
 44:          Front template size is not a defect; correctness > line count.
 45: -->
 46: 
 47: <div class="card-wrapper">
 48:   <div class="card-container" style="visibility: hidden;">
 49:     <!-- Mature-Card Word Mode probe: shown instead of sentence when interval >= threshold -->
 50:     <div class="front-word-display">{{edit:Expression}}</div>
 51: 
 52:     <!-- Cloze-fallback probe (jidoushio mobile exports): hidden source
 53:          parts for JS sentence reconstruction when Sentence has no bold
 54:          term. Plain filters — never displayed, never edited. -->
 55:     <div class="cloze-probe" hidden>
 56:       <span class="cloze-pre">{{cloze-prefix}}</span>
 57:       <span class="cloze-mid">{{cloze-body}}</span>
 58:       <span class="cloze-suf">{{cloze-suffix}}</span>
 59:     </div>
 60: 
 61:     <!-- Behavioral tag probe: tags are behavioral metadata, never rendered as decoration.
 62:          #listening Policy B: the tag-listening-view activates only when usable
 63:          audio exists. To avoid Anki's C++/Python reviewer auto-playing audio on
 64:          EVERY tagged card on card load (which happens whenever [sound:...] is
 65:          in the front HTML regardless of CSS display:none), the tag-listening-view
 66:          does NOT embed raw {{Sentence Audio}} / {{Word Audio}} fields.
 67:          Instead, it delegates to Anki's Answer-side (Back) audio via replay links
 68:          (play:a:N on desktop, playsound:a:N on AnkiDroid).
 69:          On the back card, Word Audio is first and Sentence Audio is second:
 70:          - Both exist → Sentence Audio is a:1 (label 文)
 71:          - Only Sentence Audio exists → Sentence Audio is a:0 (label 文)
 72:          - Only Word Audio exists (fallback) → Word Audio is a:0 (label 言葉)
 73:          - Neither exists → tag-listening-view is not rendered (Policy B: falls
 74:            back to the normal sentence front).
 75:          This guarantees:
 76:          1. ZERO audio autoplay on normal cards (no [sound:...] on front)
 77:          2. #listening cards WITH definitions can still activate
 78:          3. Button plays Sentence Audio (a:1 when both exist, matching 文 label)
 79:          4. Desktop uses pycmd('play:a:N') with return false (no security block)
 80:          5. AnkiDroid uses href="playsound:a:N" -->
 81:     {{#Tags}}
 82:       <div class="tags-probe" hidden>{{Tags}}</div>
 83:       {{#Sentence Audio}}
 84:         {{#Word Audio}}
 85:           <div class="listening-view tag-listening-view" style="display: none;">
 86:             <div class="audio-btn-wrapper">
 87:               <button type="button" class="circular-audio-btn large-audio-btn" title="例文音声を再生" aria-label="例文音声を再生" onclick="playCircularAudio(this)">
 88:                 <svg class="audio-progress-ring" viewBox="0 0 80 80">
 89:                   <circle class="ring-bg" cx="40" cy="40" r="36" />
 90:                   <circle class="ring-fill" cx="40" cy="40" r="36" stroke-dasharray="226.19" stroke-dashoffset="226.19" />
 91:                 </svg>
 92:                 <span class="audio-btn-content">
 93:                   <span class="audio-btn-label">文</span>
 94:                 </span>
 95:               </button>
 96:               <span class="raw-audio-source" aria-hidden="true"><a class="replay-button soundLink" href="playsound:a:1" onclick="if(typeof pycmd!=='undefined'){pycmd('play:a:1');return false;}"></a></span>
 97:             </div>
 98:           </div>
 99:         {{/Word Audio}}
100:         {{^Word Audio}}
101:           <div class="listening-view tag-listening-view" style="display: none;">
102:             <div class="audio-btn-wrapper">
103:               <button type="button" class="circular-audio-btn large-audio-btn" title="例文音声を再生" aria-label="例文音声を再生" onclick="playCircularAudio(this)">
104:                 <svg class="audio-progress-ring" viewBox="0 0 80 80">
105:                   <circle class="ring-bg" cx="40" cy="40" r="36" />
106:                   <circle class="ring-fill" cx="40" cy="40" r="36" stroke-dasharray="226.19" stroke-dashoffset="226.19" />
107:                 </svg>
108:                 <span class="audio-btn-content">
109:                   <span class="audio-btn-label">文</span>
110:                 </span>
111:               </button>
112:               <span class="raw-audio-source" aria-hidden="true"><a class="replay-button soundLink" href="playsound:a:0" onclick="if(typeof pycmd!=='undefined'){pycmd('play:a:0');return false;}"></a></span>
113:             </div>
114:           </div>
115:         {{/Word Audio}}
116:       {{/Sentence Audio}}
117:       {{^Sentence Audio}}
118:       {{#Word Audio}}
119:         <div class="listening-view tag-listening-view" style="display: none;">
120:           <div class="audio-btn-wrapper">
121:             <button type="button" class="circular-audio-btn large-audio-btn" title="単語音声を再生" aria-label="単語音声を再生" onclick="playCircularAudio(this)">
122:               <svg class="audio-progress-ring" viewBox="0 0 80 80">
123:                 <circle class="ring-bg" cx="40" cy="40" r="36" />
124:                 <circle class="ring-fill" cx="40" cy="40" r="36" stroke-dasharray="226.19" stroke-dashoffset="226.19" />
125:               </svg>
126:               <span class="audio-btn-content">
127:                 <span class="audio-btn-label">言葉</span>
128:               </span>
129:             </button>
130:             <span class="raw-audio-source" aria-hidden="true"><a class="replay-button soundLink" href="playsound:a:0" onclick="if(typeof pycmd!=='undefined'){pycmd('play:a:0');return false;}"></a></span>
131:           </div>
132:         </div>
133:       {{/Word Audio}}
134:       {{/Sentence Audio}}
135:     {{/Tags}}
136: 
137:     <!-- Standard Study View -->
138:     {{#Definition}}
139:       <div class="sentence-display">
140:         {{#Sentence}}
141:           {{edit:Sentence}}
142:         {{/Sentence}}
143:         {{^Sentence}}
144:           {{edit:Expression}}
145:         {{/Sentence}}
146:       </div>
147:     {{/Definition}}
148: 
149:     <!-- Fallback Standard View (When only Extended definition is present) -->
150:     {{^Definition}}
151:       {{#Extended definition}}
152:         <div class="sentence-display">
153:           {{#Sentence}}
154:             {{edit:Sentence}}
155:           {{/Sentence}}
156:           {{^Sentence}}
157:             {{edit:Expression}}
158:           {{/Sentence}}
159:         </div>
160:       {{/Extended definition}}
161:     {{/Definition}}
162: 
163:     <!-- Listening Mode / Pathological Fallback -->
164:     {{^Definition}}
165:       {{^Extended definition}}
166: 
167:         <!-- Frequency present but definitions missing (legacy cards with
168:              deleted English glosses): NOT a listening card — show the
169:              usual sentence instead of the audio button. -->
170:         {{#Frequency}}
171:             <div class="sentence-display">
172:               {{#Sentence}}
173:                 {{edit:Sentence}}
174:               {{/Sentence}}
175:               {{^Sentence}}
176:                 {{edit:Expression}}
177:               {{/Sentence}}
178:             </div>
179:         {{/Frequency}}
180: 
181:         {{^Frequency}}
182:         <!-- Sentence Audio available: only rendered on pure listening cards (no glosses, no frequency) -->
183:         {{#Sentence Audio}}
184:           <div class="listening-view classic-listening-view">
185:             <div class="audio-btn-wrapper">
186:               <button type="button" class="circular-audio-btn large-audio-btn" title="音声再生" aria-label="音声再生" onclick="playCircularAudio(this)">
187:                 <svg class="audio-progress-ring" viewBox="0 0 80 80">
188:                   <circle class="ring-bg" cx="40" cy="40" r="36" />
189:                   <circle class="ring-fill" cx="40" cy="40" r="36" stroke-dasharray="226.19" stroke-dashoffset="226.19" />
190:                 </svg>
191:                 <span class="audio-btn-content">
192:                   <span class="audio-btn-label">文</span>
193:                 </span>
194:               </button>
195:               <span class="raw-audio-source" aria-hidden="true">{{Sentence Audio}}</span>
196:             </div>
197:           </div>
198:         {{/Sentence Audio}}
199: 
200:         {{^Sentence Audio}}
201:         {{#Word Audio}}
202:           <div class="listening-view classic-listening-view">
203:             <div class="audio-btn-wrapper">
204:               <button type="button" class="circular-audio-btn large-audio-btn" title="音声再生" aria-label="音声再生" onclick="playCircularAudio(this)">
205:                 <svg class="audio-progress-ring" viewBox="0 0 80 80">
206:                   <circle class="ring-bg" cx="40" cy="40" r="36" />
207:                   <circle class="ring-fill" cx="40" cy="40" r="36" stroke-dasharray="226.19" stroke-dashoffset="226.19" />
208:                 </svg>
209:                 <span class="audio-btn-content">
210:                   <span class="audio-btn-label">言葉</span>
211:                 </span>
212:               </button>
213:               <span class="raw-audio-source" aria-hidden="true">{{Word Audio}}</span>
214:             </div>
215:           </div>
216:         {{/Word Audio}}
217:         {{/Sentence Audio}}
218: 
219:         <!-- Bulletproof Fallback: No Sentence audio -->
220:         {{^Sentence Audio}}
221:             <div class="sentence-display">
222:               {{#Sentence}}
223:                 {{edit:Sentence}}
224:               {{/Sentence}}
225:               {{^Sentence}}
226:                 {{edit:Expression}}
227:               {{/Sentence}}
228:             </div>
229:         {{/Sentence Audio}}
230:         {{/Frequency}}
231:       {{/Extended definition}}
232:     {{/Definition}}
233: 
234:   </div>
235: </div>
236: 
237: <script>
238:   (async function() {
239:     /* --- 1. HOISTED UTILITIES & FUNCTIONS --- */
240: 
241:     /* --- CIRCULAR AUDIO CONTROLLER (native-only) ---
242:        Always delegates to Anki's own replay link (desktop `replay-button`,
243:        AnkiDroid `replaybutton`). Never constructs an HTML5 audio element:
244:        on AnkiDroid the rendered link carries no usable filename (old builds
245:        emit `playsound:q:0`, which would be loaded as a bogus file and fail).
246:        The ring is a playback indicator (a decorative play-pulse), not true
247:        progress — native audio remains the authority (ADR 003). */
248:     window.currentActiveBtn = window.currentActiveBtn || null;
249:     window.currentActiveTimer = window.currentActiveTimer || null;
250:     /* WebView DOM re-use: never pin a detached button across card flips. */
251:     if (typeof window.addEventListener === 'function') {
252:         window.addEventListener('pagehide', () => { try { window.resetAudioState(); } catch (_) {} });
253:     }
254: 
255:     window.resetAudioState = function() {
256:         if (window.currentActiveTimer) {
257:             clearTimeout(window.currentActiveTimer);
258:             window.currentActiveTimer = null;
259:         }
260:         if (window.currentActiveBtn) {
261:             window.currentActiveBtn.classList.remove('is-playing');
262:             const ring = window.currentActiveBtn.querySelector('.ring-fill');
263:             if (ring) {
264:                 const circ = parseFloat(ring.getAttribute('stroke-dasharray')) || 226.19;
265:                 ring.style.transition = '';
266:                 ring.style.strokeDashoffset = circ;
267:             }
268:             window.currentActiveBtn = null;
269:         }
270:     };
271: 
272:     window.playCircularAudio = function(btn) {
273:         /* Debounce: native playback can't be stopped programmatically, so
274:            ignore rapid re-taps on the already-playing button (prevents
275:            overlapping audio on AnkiDroid). */
276:         if (window.currentActiveBtn === btn) return;
277:         window.resetAudioState();
278:         const ringFill = btn.querySelector('.ring-fill');
279: 
280:         /* The replay link lives in the sibling .raw-audio-source (kept OUT
281:            of the <button>: <a> inside <button> is invalid HTML and Android
282:            WebView mishandles taps on it). */
283:         const scope = (btn.closest && btn.closest('.audio-btn-wrapper')) || document;
284:         const nativeReplay = scope.querySelector('.replaybutton, .replay-button, a.sound, .soundLink')
285:           || btn.querySelector('.replaybutton, .replay-button, a.sound, .soundLink');
286:         let played = false;
287:         if (nativeReplay) {
288:             try { nativeReplay.click(); played = true; } catch (e) {}
289:         }
290:         /* Last-resort fallback (removed): every listening view now carries
291:            a real .raw-audio-source (the actual audio field), so the
292:            nativeReplay.click() path above is the only path — it plays the
293:            field the button is labelled with. A hardcoded pycmd('play:a:0')
294:            would play the first audio field regardless of label, so silent
295:            no-op is safer than the wrong audio. */
296:         if (played || nativeReplay) {
297:             btn.classList.add('is-playing');
298:             if (ringFill) {
299:                 ringFill.style.transition = 'stroke-dashoffset 0.8s ease-in-out';
300:                 ringFill.style.strokeDashoffset = '0';
301:             }
302:             window.currentActiveBtn = btn;
303:             window.currentActiveTimer = setTimeout(() => {
304:                 if (window.currentActiveBtn === btn) {
305:                     window.resetAudioState();
306:                 }
307:             }, 800);
308:         }
309:     };
310: 
311:     /* --- 2. MAIN EXECUTION BLOCK --- */
312:     const container = document.querySelector('.card-container');
313:     const wrapper = document.querySelector('.card-wrapper');
314: 
315:     if (container && wrapper) {
316:       let wordMode = false;
317:       let interval = null;
318:       let source = 'unavailable';
319:       /* Latency probe: t0 at script start; elapsed retrieval time is
320:          logged with the decision, so AnkiConnect (desktop) cost can be
321:          measured per card. */
322:       const nowMs = () => (
323:         (typeof performance !== 'undefined' && performance.now)
324:           ? performance.now()
325:           : Date.now()
326:       );
327:       const t0 = nowMs();
328: 
329:       /* Safety Reveal: Ensure card shows even if async calls hang.
330:          Timing budget: 500ms AnkiConnect race / 1200ms reveal cap. The
331:          cap only binds failure paths; the word-mode toggle runs before
332:          reveal. Mobile skips retrieval entirely, so it reveals at once. */
333:       const reveal = () => {
334:         container.style.visibility = 'visible';
335:       };
336:       const safetyTimeout = setTimeout(reveal, 1200);
337: 
338:       /* --- CLOZE FALLBACK (BEGIN — headless check extracts this block verbatim) ---
339:          jidoujisho mobile exports often carry a Sentence with no <b>
340:          target term. When the rendered sentence has no bold element but
341:          the cloze trio (prefix/body/suffix) is complete, rebuild it as
342:          prefix + <b>body</b> + suffix so the front is indistinguishable
343:          from a proper Yomitan sentence (same .sentence-display b styling).
344:          Any gap or failure keeps the original sentence untouched. */
345:       try {
346:         const probe = container.querySelector('.cloze-probe');
347:         const probeText = (sel) => {
348:           const el = probe && probe.querySelector(sel);
349:           return el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : '';
350:         };
351:         const clozePre = probeText('.cloze-pre');
352:         const clozeMid = probeText('.cloze-mid');
353:         const clozeSuf = probeText('.cloze-suf');
354:         if (clozePre && clozeMid && clozeSuf) {
355:           container.querySelectorAll('.sentence-display').forEach((sd) => {
356:             if (!sd.querySelector('b, strong')) {
357:               sd.textContent = '';
358:               const bold = document.createElement('b');
359:               bold.textContent = clozeMid;
360:               sd.append(
361:                 document.createTextNode(clozePre),
362:                 bold,
363:                 document.createTextNode(clozeSuf)
364:               );
365:             }
366:           });
367:         }
368:       } catch (clozeErr) {
369:         console.warn('[Cloze Fallback]', clozeErr);
370:       }
371:       /* --- CLOZE FALLBACK (END) --- */
372: 
373:       /* Empty-field collapse (QUALITY.md): after the cloze rebuild, a
374:          sentence block with no text at all (neither Sentence nor
375:          Expression) leaves no padded void. Runs before the reveal. */
376:       try {
377:         container.querySelectorAll('.sentence-display').forEach((sd) => {
378:           if (!sd.textContent || !sd.textContent.trim()) sd.remove();
379:         });
380:       } catch (blankErr) {
381:         console.warn('[Blank Collapse]', blankErr);
382:       }
383: 
384:       /* --- LISTENING RESOLVER (Policy B) ---
385:          A card activates the listening front ONLY when usable audio exists:
386:          1. #listening tag (deliberate exercise): the tag-listening-view must
387:             have a real .raw-audio-source (Sentence Audio, or Word Audio as
388:             fallback). #listening + no usable audio → fall back to the normal
389:             sentence front. Never leave a dead/empty listening UI.
390:          2. Classic audio-only / pathological legacy card: Definition, Extended
391:             definition, and Frequency are absent and audio is present
392:             (classic-listening-view).
393:          Normal study cards without #listening tag never show audio on front.
394: 
395:          Exactly-one-listening-button invariant: the markup may render both a
396:          tag-listening-view and a classic-listening-view for the same audio;
397:          the resolver keeps only the active one and removes every dead/
398:          duplicate view, plus strips any listening view whose audio source
399:          is empty (missing field). */
400:       const tagsProbe = container.querySelector('.tags-probe');
401:       const tagText = tagsProbe ? (tagsProbe.textContent || '') : '';
402:       const hasListeningTag = /(^|[\s:#])listening([\s:#]|$)/i.test(tagText);
403:       const tagView = container.querySelector('.tag-listening-view');
404:       const classicView = container.querySelector('.classic-listening-view');
405: 
406:       const hasUsableAudio = (view) => {
407:         if (!view) return false;
408:         const src = view.querySelector('.raw-audio-source');
409:         if (!src) return false;
410:         const hasLink = !!src.querySelector('a, .replaybutton, .replay-button, .soundLink');
411:         const hasText = !!(src.textContent || '').replace(/\s+/g, ' ').trim();
412:         return hasLink || hasText;
413:       };
414: 
415:       let isListening = false;
416:       if (hasListeningTag && hasUsableAudio(tagView)) {
417:         isListening = true;
418:         tagView.style.display = '';
419:         wrapper.classList.add('listening-mode');
420:         container.querySelectorAll('.sentence-display').forEach((sd) => sd.remove());
421:         if (classicView) classicView.remove();
422:         setTimeout(function() {
423:           const btn = tagView.querySelector('.circular-audio-btn');
424:           if (btn && window.playCircularAudio) window.playCircularAudio(btn);
425:         }, 120);
426:       } else if (classicView && hasUsableAudio(classicView)) {
427:         isListening = true;
428:         wrapper.classList.add('listening-mode');
429:         container.querySelectorAll('.sentence-display').forEach((sd) => sd.remove());
430:         if (tagView) tagView.remove();
431:       }
432:       /* Dead/duplicate view cleanup: any listening-view that was not activated
433:          is removed so it never leaves a silent/empty audio button behind. */
434:       if (!isListening) {
435:         container.querySelectorAll('.listening-view').forEach((v) => v.remove());
436:       }
437: 
438:       /* Static early-exit: with no Expression, word mode is impossible (the
439:          hasExpression gate below), so the whole retrieval chain —
440:          AnkiConnect content search — is skipped and the sentence front
441:          reveals now.
442:          Failure-identical to the universal fallback, ~50ms faster per such
443:          card on desktop. The class toggle is explicit because WebView DOM
444:          re-use can carry word-mode over from the previous card. */
445:       var wordProbeEarly = container.querySelector('.front-word-display');
446:       if (!isListening && wordProbeEarly && !(wordProbeEarly.textContent || '').trim()) {
447:         clearTimeout(safetyTimeout);
448:         wrapper.classList.toggle('word-mode', false);
449:         reveal();
450:         return;
451:       }
452: 
453:       /* Anki-Connect helper with timeout + platform guard. 500ms is ~15x
454:          the measured healthy localhost latency (~25ms/call), so it only
455:          ever binds a wedged/busy Anki — and the fallback is always the
456:          safe sentence front, never a hang.
457: 
458:          PLATFORM GUARD — DESKTOP-ONLY (this is the downloadfile.bin fix):
459:          fetch() only
460:          runs on desktop Anki (QtWebEngine). On AnkiDroid the WebView has
461:          no AnkiConnect, the request 404s into a media download, and
462:          Android surfaces it natively as "Card Content Error: Failed to
463:          load 'downloadfile.bin'". Mobile never reaches any fetch; word
464:          mode simply stays off (sentence front), by design. */
465:       const post = (action, params) => {
466:         if (typeof fetch !== 'function') {
467:           return Promise.reject(new Error('fetch unavailable (mobile)'));
468:         }
469:         const ua = (typeof navigator !== 'undefined' && navigator.userAgent) || '';
470:         if (/Android|iPhone|iPad|iPod/i.test(ua)) {
471:           return Promise.reject(new Error('AnkiConnect is desktop-only'));
472:         }
473:         const ctl = (typeof AbortController !== 'undefined') ? new AbortController() : null;
474:         const timeout = new Promise((_, rej) =>
475:           setTimeout(() => { try { ctl && ctl.abort(); } catch (_) {} rej(new Error('AnkiConnect timeout')); }, 500)
476:         );
477:         const fetchPromise = fetch('http://127.0.0.1:8765', {
478:           method: 'POST',
479:           ...(ctl ? { signal: ctl.signal } : {}),
480:           body: JSON.stringify({ action: action, version: 6, params: params })
481:         }).then(r => r.json()).then(data => {
482:           if (data.error) throw new Error(data.error);
483:           return data.result;
484:         });
485:         return Promise.race([fetchPromise, timeout]);
486:       };
487: 
488:       const escQuery = (s) => s.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/([*_():-])/g, '\\$1');
489:       const normText = (s) => s
490:         .replace(/<br\s*\/?>/gi, ' ')
491:         .replace(/<[^>]+>/g, ' ')
492:         .replace(/&nbsp;/gi, ' ')
493:         .replace(/\s+/g, ' ')
494:         .trim();
495: 
496:       try {
497:         /* Fallback-only word mode: no AnkiConnect fetch in this branch —
498:            the content search below IS the primary path now. */
499:         if (!isListening) {
500:           /* BROWSE-PREVIEWER CONTENT SEARCH.
501:              Identity is reconstructed from field content. NEVER pick
502:              candidate 0 blindly — duplicates are common (same Expression
503:              across many notes). Use Sentence then cloze-body as
504:              discriminators; if ambiguity remains after both, fail safely
505:              to the sentence front (interval stays null → no word mode). */
506:           const wordEl = document.querySelector('.front-word-display');
507:           const sentEl = document.querySelector('.sentence-display');
508:           if (wordEl) {
509:             const exprDom = normText(wordEl.innerText || wordEl.textContent || '');
510:             if (exprDom) {
511:               /* No "note:" clause: the note type name is not exposed to
512:                  templates ({{Type}} is the scheduling type, not the
513:                  model name), and the exact Expression field match below
514:                  already restricts results to this note type's cards. */
515:               const query = '"Expression:' + escQuery(exprDom) + '"';
516:               let ids = await post('findCards', { query: query });
517:               /* Bound: a common Expression can match hundreds of notes;
518:                  materialising every cardsInfo would jank the previewer.
519:                  Over-broad → sentence fallback (same safe default). */
520:               if (ids && ids.length > 50) {
521:                 source = 'content-search-too-broad → sentence fallback';
522:                 ids = [];
523:               }
524:               if (ids && ids.length) {
525:                 const infos = await post('cardsInfo', { cards: ids });
526:                 const fieldText = (info, name) =>
527:                   normText((info.fields && info.fields[name] && info.fields[name].value) || '');
528:                 let candidates = infos.filter(i => fieldText(i, 'Expression') === exprDom);
529:                 if (candidates.length > 1 && sentEl) {
530:                   /* Discriminator 1: Sentence. The front sentence is
531:                      the strongest content signal — it is unique per
532:                      mined note in practice. */
533:                   const sentDom = normText(sentEl.innerText || sentEl.textContent || '');
534:                   if (sentDom) {
535:                     const withSent = candidates.filter(i => fieldText(i, 'Sentence') === sentDom);
536:                     if (withSent.length) candidates = withSent;
537:                   }
538:                 }
539:                 if (candidates.length > 1) {
540:                   /* Discriminator 2: cloze-body. The cloze trio is
541:                      rendered on the front (hidden probe), so its body
542:                      text is available as a second identity signal. */
543:                   const clozeProbe = container.querySelector('.cloze-probe .cloze-mid');
544:                   const clozeDom = clozeProbe
545:                     ? normText(clozeProbe.innerText || clozeProbe.textContent || '')
546:                     : '';
547:                   if (clozeDom) {
548:                     const withCloze = candidates.filter(i =>
549:                       fieldText(i, 'cloze-body') === clozeDom);
550:                     if (withCloze.length) candidates = withCloze;
551:                   }
552:                 }
553:                 /* Exact-card resolution: only one candidate remains after
554:                    discriminators → use its interval. Multiple candidates
555:                    (ambiguous) → fail safely to the sentence front. Never
556:                    pick candidate 0. */
557:                 if (candidates.length === 1) {
558:                   interval = candidates[0].interval;
559:                   source = 'content-search';
560:                 } else if (candidates.length > 1) {
561:                   source = 'content-search-ambiguous → sentence fallback';
562:                 }
563:               }
564:             }
565:           }
566:         }
567:       } catch (e) {
568:         source = 'error: ' + (e && e.message ? e.message : String(e));
569:         console.warn('[Mature Word Mode]', e);
570:       } finally {
571:         clearTimeout(safetyTimeout);
572:         const elapsedMs = Math.round(nowMs() - t0);
573:         console.log('[Mature Word Mode] source=' + source +
574:           ' ivl=' + String(interval) + ' in ' + elapsedMs + 'ms');
575: 
576:         const LONG_INTERVAL_DAYS = 365;
577: 
578:         // Set to false after confirming that Android works.
579:         const DEBUG_MATURE_MODE = false;
580: 
581:         const wordEl = container.querySelector('.front-word-display');
582:         const hasExpression = !!(
583:           wordEl && (wordEl.textContent || '').trim()
584:         );
585: 
586:         wordMode =
587:           typeof interval === 'number' &&
588:           Number.isFinite(interval) &&
589:           interval >= LONG_INTERVAL_DAYS &&
590:           !isListening &&
591:           hasExpression;
592: 
593:         // Explicitly reset the class as well as enabling it.
594:         wrapper.classList.toggle('word-mode', wordMode);
595: 
596:         if (DEBUG_MATURE_MODE) {
597:           let diagnostic = wrapper.querySelector('.mwm-debug');
598: 
599:           if (!diagnostic) {
600:             diagnostic = document.createElement('div');
601:             diagnostic.className = 'mwm-debug';
602:             diagnostic.style.cssText =
603:               'padding:6px 10px;' +
604:               'font:12px/1.4 sans-serif;' +
605:               'color:var(--text-secondary,#888);' +
606:               'overflow-wrap:anywhere;' +
607:               'text-align:left;';
608:             wrapper.appendChild(diagnostic);
609:           }
610: 
611:           diagnostic.textContent =
612:             'Mature mode: ' + (wordMode ? 'ON' : 'OFF') +
613:             ' | interval=' + String(interval) +
614:             ' | threshold=' + LONG_INTERVAL_DAYS +
615:             ' | source=' + source +
616:             ' | ' + elapsedMs + 'ms';
617:         }
618: 
619:         reveal();
620:       }
621:     }
622:   })();
623: </script>
````

## File: Card 1 - Style.css
````css
   1: /**
   2:  * ==============================================================================
   3:  * Japanese Note Type — Minimal Japanese Reading Interface
   4:  * (Tokyo Night Dark / Aki Paper Light)
   5:  *
   6:  * Source & documentation: https://github.com/mansourvery-hub/anki-japanese-template
   7:  * Version: v1.8.33 — auto-bumped by finish.sh; matches the GitHub release tag
   8:  *
   9:  * Front = pure retrieval surface (sentence / word / audio only).
  10:  * Back = strong hierarchy: target → reading → meaning → context →
  11:  * secondary (collapsed behind "More ▾"). Anki is the SRS; this
  12:  * template is presentation only — every visible element must justify
  13:  * its screen space.
  14:  *
  15:  * Audio: the circular ring is a playback indicator (a decorative
  16:  * play-pulse), not true progress — native Anki/AnkiDroid audio
  17:  * delegation is the authority (ADR 003). R shortcut is Anki-owned.
  18:  * :has() is intentional architecture for empty-shell collapse.
  19:  *
  20:  * Optimized for Arch Linux Desktop (Anki Qt6) and Samsung Galaxy A50
  21:  * (AnkiDroid): cards size to their content; fluid clamp() tokens,
  22:  * container queries with media-query fallback.
  23:  * ==============================================================================
  24:  */
  25: 
  26: /* ==============================================================================
  27:    1. COLOR SYSTEM & CSS VARIABLES
  28:    ============================================================================== */
  29: :root {
  30:   /* --- TOKYO NIGHT DARK (Default: Japanese Midnight Sumi) --- */
  31:   --bg-color: #0d1117;
  32:   --card-bg: #151b28;
  33:   --card-bg-elevated: #1a2233;
  34:   --card-border: rgba(255, 255, 255, 0.06);
  35:   --text-primary: #e8edf5;
  36:   --text-secondary: #8b99b0;
  37:   --text-muted: #5a687d;
  38:   
  39:   --accent-color: #e07a5f;
  40:   --accent-light: rgba(224, 122, 95, 0.10);
  41:   --accent-soft: rgba(224, 122, 95, 0.20);
  42:   --accent-glow: 0 0 20px rgba(224, 122, 95, 0.25);
  43: 
  44:   /* Frequency Tier Colors */
  45:   --freq-very-common: #10b981;
  46:   --freq-common: #22c55e;
  47:   --freq-medium: #eab308;
  48:   --freq-uncommon: #f97316;
  49:   --freq-rare: #ef4444;
  50: 
  51:   /* Warm accent: subtle seasonal warmth for decorative elements */
  52:   --warm-accent: rgba(255, 183, 120, 0.06);
  53:   --warm-accent-border: rgba(255, 183, 120, 0.08);
  54: 
  55:   --shadow-premium: 0 8px 32px -6px rgba(0, 0, 0, 0.5),
  56:                     0 2px 8px -2px rgba(0, 0, 0, 0.25);
  57:   --shadow-soft: 0 2px 12px -4px rgba(0, 0, 0, 0.3);
  58:   --border-radius-lg: 16px;
  59:   --border-radius-md: 10px;
  60:   --border-radius-sm: 6px;
  61: 
  62:   /* Spacing Tokens - Fluid viewport-based (tightened density pass:
  63:      hero-header single row saves one full-width row, so section gaps
  64:      can stay compact without feeling cramped) */
  65:   --gap-section: clamp(8px, 1.2vh, 14px);
  66:   --gap-block: clamp(6px, 1.2vmin, 12px);
  67:   --block-pad-y: clamp(2px, 0.4vmin, 6px);
  68:   --block-pad-x: clamp(10px, 1.8vmin, 18px);
  69:   --container-pad-y: clamp(12px, 2vh, 24px);
  70:   --container-pad-x: clamp(16px, 2.5vw, 36px);
  71: 
  72:   /* Furigana clearance: rt height (0.55em of parent font) + 2px hover gap.
  73:      em-based so it scales with font size across viewports. */
  74:   --furigana-headroom: calc(0.55em + 2px);
  75:   
  76:   /* Fonts */
  77:   --font-japanese-serif: "Yu Mincho", "Hiragino Mincho ProN", "YuMincho", "Noto Serif JP", "MS Mincho", serif;
  78:   --font-japanese-sans: "Inter", "Hiragino Sans", "Meiryo", "Noto Sans JP", sans-serif;
  79:   --font-interface: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  80:   
  81:   --max-content-width: 1360px;
  82: 
  83:   /* Decorative: separator motif (seigaiha-inspired wave) */
  84:   --separator-color: rgba(255, 255, 255, 0.05);
  85:   --separator-accent: rgba(224, 122, 95, 0.20);
  86: }
  87: 
  88: /* --- AKI PAPER LIGHT THEME (Warm Washi) --- */
  89: .card:not(.nightMode):not(.night_mode) {
  90:   --bg-color: #faf8f5;
  91:   --card-bg: #ffffff;
  92:   --card-bg-elevated: #fefefe;
  93:   --card-border: rgba(0, 0, 0, 0.06);
  94:   --text-primary: #1a1c20;
  95:   --text-secondary: #515a6b;
  96:   --text-muted: #8a909d;
  97:   
  98:   --accent-color: #b84a39;
  99:   --accent-light: rgba(184, 74, 57, 0.08);
 100:   --accent-soft: rgba(184, 74, 57, 0.16);
 101:   --accent-glow: 0 0 20px rgba(184, 74, 57, 0.20);
 102: 
 103:   --freq-very-common: #059669;
 104:   --freq-common: #16a34a;
 105:   --freq-medium: #ca8a04;
 106:   --freq-uncommon: #ea580c;
 107:   --freq-rare: #dc2626;
 108: 
 109:   --warm-accent: rgba(184, 74, 57, 0.04);
 110:   --warm-accent-border: rgba(184, 74, 57, 0.08);
 111: 
 112:   --shadow-premium: 0 4px 20px rgba(0, 0, 0, 0.06),
 113:                     0 1px 4px rgba(0, 0, 0, 0.04);
 114:   --shadow-soft: 0 2px 8px rgba(0, 0, 0, 0.04);
 115: 
 116:   --separator-color: rgba(0, 0, 0, 0.04);
 117:   --separator-accent: rgba(184, 74, 57, 0.18);
 118: }
 119: 
 120: .card.nightMode,
 121: .card.night_mode {
 122:   --bg-color: #0d1117;
 123:   --card-bg: #151b28;
 124:   --card-bg-elevated: #1a2233;
 125:   --card-border: rgba(255, 255, 255, 0.06);
 126:   --text-primary: #e8edf5;
 127:   --text-secondary: #8b99b0;
 128:   --text-muted: #5a687d;
 129:   --accent-color: #e07a5f;
 130:   --accent-light: rgba(224, 122, 95, 0.10);
 131:   --accent-soft: rgba(224, 122, 95, 0.20);
 132:   --warm-accent: rgba(255, 183, 120, 0.06);
 133:   --warm-accent-border: rgba(255, 183, 120, 0.08);
 134:   --separator-color: rgba(255, 255, 255, 0.05);
 135:   --separator-accent: rgba(224, 122, 95, 0.20);
 136: }
 137: 
 138: 
 139: /* ==============================================================================
 140:    2. BASE CARD LAYOUT & CONTAINER
 141:    ============================================================================== */
 142: .card {
 143:   background-color: var(--bg-color);
 144:   color: var(--text-primary);
 145:   font-family: var(--font-interface);
 146:   margin: 0;
 147:   padding: 0;
 148:   text-align: center;
 149:   -webkit-font-smoothing: antialiased;
 150:   -moz-osx-font-smoothing: grayscale;
 151:   line-height: 1.5;
 152:   -webkit-tap-highlight-color: transparent;
 153: }
 154: 
 155: .card-wrapper {
 156:   display: flex;
 157:   flex-direction: column;
 158:   align-items: center;
 159:   width: 100%;
 160:   margin: 0;
 161:   padding: 0;
 162:   container-type: inline-size;
 163:   container-name: anki-card;
 164: }
 165: 
 166: .card-container {
 167:   width: 100%;
 168:   max-width: min(96vw, var(--max-content-width, 1360px));
 169:   margin: 0 auto;
 170:   padding: var(--container-pad-y) var(--container-pad-x);
 171:   box-sizing: border-box;
 172: }
 173: 
 174: .back-card .card-container {
 175:   background: rgba(19, 24, 34, 0.78);
 176:   /* 8px, not 18px: fullscreen blur is the top repaint cost on scroll;
 177:      the frosted look survives, the offscreen surface gets ~2x cheaper. */
 178:   backdrop-filter: blur(8px);
 179:   -webkit-backdrop-filter: blur(8px);
 180:   border: 1px solid var(--card-border);
 181:   border-radius: var(--border-radius-lg);
 182:   box-shadow: var(--shadow-premium);
 183:   margin-top: clamp(4px, 0.8vh, 10px);
 184:   margin-bottom: clamp(4px, 0.8vh, 10px);
 185: }
 186: 
 187: .card:not(.nightMode):not(.night_mode) .back-card .card-container {
 188:   background: rgba(255, 255, 255, 0.85);
 189:   border-color: rgba(0, 0, 0, 0.08);
 190:   box-shadow: 0 8px 28px rgba(0, 0, 0, 0.06);
 191: }
 192: 
 193: 
 194: /* ==============================================================================
 195:    3. SECONDARY-INFO TOGGLE ("More ▾")
 196:    ============================================================================== */
 197: /* "More ▾" — a quiet, elegant editorial disclosure */
 198: .more-toggle {
 199:   font-family: var(--font-interface);
 200:   font-size: 0.78rem;
 201:   font-weight: 500;
 202:   letter-spacing: 0.08em;
 203:   text-transform: uppercase;
 204:   color: var(--text-muted);
 205:   background: var(--accent-light);
 206:   border: 1px solid var(--card-border);
 207:   padding: 6px 16px;
 208:   margin: clamp(8px, 1.4vh, 16px) auto 4px auto;
 209:   display: inline-flex;
 210:   align-items: center;
 211:   gap: 5px;
 212:   cursor: pointer;
 213:   border-radius: 9999px;
 214:   transition: color 0.2s ease, background-color 0.2s ease,
 215:               border-color 0.2s ease, transform 0.15s ease;
 216:   user-select: none;
 217:   -webkit-tap-highlight-color: transparent;
 218: }
 219: 
 220: .more-toggle:hover,
 221: .more-toggle:focus-visible {
 222:   color: var(--accent-color);
 223:   background-color: var(--accent-soft);
 224:   border-color: var(--accent-color);
 225:   transform: translateY(-1px);
 226:   outline: none;
 227: }
 228: 
 229: .card:not(.nightMode):not(.night_mode) .more-toggle:hover,
 230: .card:not(.nightMode):not(.night_mode) .more-toggle:focus-visible {
 231:   background-color: var(--accent-soft);
 232: }
 233: 
 234: .more-toggle:focus-visible {
 235:   outline: 2px solid var(--accent-color);
 236:   outline-offset: 1px;
 237: }
 238: 
 239: .more-toggle .more-caret {
 240:   display: inline-block;
 241:   font-size: 0.7rem;
 242:   margin-left: 2px;
 243:   transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
 244: }
 245: 
 246: .more-toggle.is-open .more-caret {
 247:   transform: rotate(180deg);
 248: }
 249: 
 250: .more-section {
 251:   margin-top: 8px;
 252:   width: 100%;
 253: }
 254: 
 255: 
 256: /* ==============================================================================
 257:    4. CONTEXT GRID (core info: sentence + picture)
 258:    ============================================================================== */
 259: .context-grid {
 260:   display: flex;
 261:   flex-direction: column;
 262:   gap: clamp(10px, 1.5vh, 18px);
 263:   align-items: center;
 264:   width: 100%;
 265:   margin-top: var(--gap-section);
 266: }
 267: 
 268: /* Empty-shell guard (QUALITY.md): collapse when neither sentence nor picture exists */
 269: .context-grid:not(:has(.sentence-japanese, .context-only, .context-picture)) {
 270:   display: none;
 271: }
 272: 
 273: .context-main {
 274:   width: 100%;
 275:   min-width: 0;
 276:   text-align: center;
 277: }
 278: 
 279: .context-main:not(:has(.sentence-japanese, .context-only)) {
 280:   display: none;
 281: }
 282: 
 283: .context-picture {
 284:   width: 100%;
 285:   text-align: center;
 286: }
 287: 
 288: @container anki-card (min-width: 580px) {
 289:   /* Editorial balance: sentence left/center, picture right, both
 290:      top-anchored — the picture stays just below the definition no matter
 291:      how long the sentence grows (never dragged down by it). */
 292:   .context-grid:has(.context-picture) {
 293:     flex-direction: row;
 294:     align-items: flex-start;
 295:     justify-content: center;
 296:     gap: clamp(20px, 3.5vw, 48px);
 297:   }
 298: 
 299:   .context-grid:has(.context-picture) .context-main {
 300:     flex: 1 1 54%;
 301:     min-width: 0;
 302:     text-align: center;
 303:   }
 304: 
 305:   .context-grid:has(.context-picture) .sentence-japanese {
 306:     text-align: center;
 307:   }
 308: 
 309:   .context-picture {
 310:     flex: 0 1 46%;
 311:     width: auto;
 312:     max-width: min(46vw, 640px);
 313:   }
 314: 
 315:   .small-audio-btn {
 316:     width: 36px;
 317:     height: 36px;
 318:   }
 319: }
 320: 
 321: /* Portability fallback for WebViews without container-query support */
 322: @media (min-width: 580px) {
 323:   .context-grid:has(.context-picture) {
 324:     flex-direction: row;
 325:     align-items: flex-start;
 326:     justify-content: center;
 327:     gap: clamp(20px, 3.5vw, 48px);
 328:   }
 329: 
 330:   .context-grid:has(.context-picture) .context-main {
 331:     flex: 1 1 54%;
 332:     min-width: 0;
 333:     text-align: center;
 334:   }
 335: 
 336:   .context-grid:has(.context-picture) .sentence-japanese {
 337:     text-align: center;
 338:   }
 339: 
 340:   .context-picture {
 341:     flex: 0 1 46%;
 342:     width: auto;
 343:     max-width: min(46vw, 640px);
 344:   }
 345: }
 346: 
 347: @media (min-width: 768px) {
 348:   .context-grid:has(.context-picture) {
 349:     gap: clamp(24px, 3.5vw, 48px);
 350:   }
 351: }
 352: 
 353: 
 354: 
 355: 
 356: /* ==============================================================================
 357:     5. FRONT CARD TYPOGRAPHY - Fluid Sizing
 358:        One base clamp for all screens (vmin respects height too), plus a
 359:        smaller override in the mobile block (section 13) for phones.
 360:     ============================================================================== */
 361: .sentence-display,
 362: .front-word-display {
 363:   font-family: var(--font-japanese-serif);
 364:   /* Refined, authoritative scale: dominant without visual shouting */
 365:   font-size: clamp(1.8rem, 4.2vmin + 0.75rem, 4.2rem);
 366:   line-height: 1.4;
 367:   padding: 12px 16px;
 368:   text-align: center;
 369:   width: 100%;
 370:   box-sizing: border-box;
 371:   margin: 0 auto;
 372:   font-weight: 400;
 373:   overflow-wrap: anywhere;
 374:   letter-spacing: 0.02em;
 375: }
 376: 
 377: /* Front: Yomitan wraps the target word in <b> even for word-only fronts
 378:    (Sentence field = "<b>word</b>"). Force it light — color + underline
 379:    still mark it without the heavy stroke. */
 380: .sentence-display b,
 381: .sentence-display strong,
 382: .front-word-display b,
 383: .front-word-display strong {
 384:   color: var(--accent-color);
 385:   font-weight: 400;
 386:   /* Brushstroke-inspired underline: a warm gradient that tapers like ink */
 387:   background: linear-gradient(transparent 76%, var(--accent-soft) 76%, var(--accent-light) 94%);
 388:   padding: 0 5px;
 389:   border-radius: 3px;
 390: }
 391: 
 392: /* Back sentence target matches surrounding weight — color + underline mark it. */
 393: .sentence-japanese b,
 394: .sentence-japanese strong {
 395:   color: var(--accent-color);
 396:   font-weight: 400;
 397:   background: linear-gradient(transparent 76%, var(--accent-soft) 76%, var(--accent-light) 94%);
 398:   padding: 0 5px;
 399:   border-radius: 3px;
 400: }
 401: 
 402: /* Back headword: never bold, even if Yomitan injects <b>/<strong>. */
 403: .word-display b,
 404: .word-display strong {
 405:   font-weight: 400;
 406: }
 407: 
 408: /* 5b. MATURE-CARD WORD MODE
 409:    Used when card interval >= LONG_INTERVAL_DAYS.
 410:    Swaps the sentence display for the bare expression. */
 411: .front-word-display {
 412:   display: none;
 413:   font-weight: 400;
 414: }
 415: 
 416: .card-wrapper.word-mode .sentence-display {
 417:   display: none;
 418: }
 419: 
 420: .card-wrapper.word-mode .front-word-display {
 421:   display: block;
 422: }
 423: 
 424: 
 425: /* ==============================================================================
 426:     6. BACK CARD HIERARCHY — target, reading, meaning (Fluid Typography)
 427:     ============================================================================== */
 428: /* Target + reading form ONE conceptual unit, centered, the hero element.
 429:    The word display now occupies more visual space with generous sizing
 430:    and a subtle warm glow backdrop. */
 431: 
 432: .hero-header {
 433:   display: grid;
 434:   grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);
 435:   grid-template-areas: "left word right";
 436:   align-items: center;
 437:   column-gap: clamp(8px, 1.5vw, 18px);
 438:   row-gap: 2px;
 439:   width: 100%;
 440:   margin: 0 auto;
 441: }
 442: 
 443: /* Empty-shell guard: collapse when neither word nor meta exists */
 444: .hero-header:not(:has(.word-display, .frequency-badge, .pitch-quiet, .circular-audio-btn)) {
 445:   display: none;
 446: }
 447: 
 448: .hero-word-wrap {
 449:   grid-area: word;
 450:   display: flex;
 451:   align-items: center;
 452:   justify-content: center;
 453:   justify-self: center;
 454:   position: relative;
 455:   min-width: 0;
 456: }
 457: 
 458: /* Side cells hug the word (end/start) so buttons sit beside the
 459:    expression, not at the far card edges. They stay in the grid even
 460:    when empty — that is what keeps the word truly centered. Zero
 461:    margin/padding here, so empty sides leave no chrome behind. */
 462: .hero-side {
 463:   display: flex;
 464:   align-items: center;
 465:   gap: 10px;
 466:   flex-wrap: wrap;
 467:   min-width: 0;
 468: }
 469: 
 470: .hero-side-left {
 471:   grid-area: left;
 472:   justify-self: end;
 473:   justify-content: flex-end;
 474: }
 475: 
 476: .hero-side-right {
 477:   grid-area: right;
 478:   justify-self: start;
 479:   justify-content: flex-start;
 480: }
 481: 
 482: .hero-side .audio-row {
 483:   margin: 0;
 484: }
 485: 
 486: /* Furigana headroom: ruby rt renders 0.55em above the text with a 2px gap.
 487:    Fields that use {{furigana:...}} get exactly that clearance as top padding
 488:    (plus the base pad), so hover furigana never clips or overlaps neighbors.
 489:    em-based => scales continuously with font size across all screen sizes. */
 490: .word-display {
 491:   font-family: var(--font-japanese-serif);
 492:   /* Hero target: unmistakably dominant, commanding, and present */
 493:   font-size: clamp(3.0rem, 5.2vw + 1.2rem, 5.2rem);
 494:   font-weight: 400;
 495:   line-height: 1.15;
 496:   letter-spacing: 0.06em;
 497:   padding-top: calc(var(--block-pad-y, 0px) + var(--furigana-headroom));
 498:   padding-bottom: clamp(2px, 0.5vh, 6px);
 499:   margin: 0;
 500:   text-align: center;
 501:   min-width: 0;
 502:   overflow-wrap: anywhere;
 503: }
 504: 
 505: /* Furigana on Back Card: shown by default on the hero expression */
 506: .word-display ruby rt {
 507:   visibility: visible;
 508:   opacity: 1;
 509: }
 510: 
 511: /* Frequency badge: 5-star scale & progress track */
 512: .frequency-badge {
 513:   display: inline-flex;
 514:   align-items: center;
 515:   gap: 6px;
 516:   font-size: 0.82rem;
 517:   font-weight: 600;
 518:   color: var(--accent-color);
 519:   background-color: var(--accent-light);
 520:   border: 1px solid var(--accent-soft);
 521:   padding: 3px 10px;
 522:   border-radius: 9999px;
 523:   line-height: 1;
 524:   cursor: default;
 525:   transition: all 0.2s ease;
 526:   user-select: none;
 527: }
 528: 
 529: .frequency-bar-track {
 530:   width: 32px;
 531:   height: 4px;
 532:   border-radius: 2px;
 533:   background-color: rgba(255, 255, 255, 0.12);
 534:   overflow: hidden;
 535: }
 536: 
 537: .card:not(.nightMode):not(.night_mode) .frequency-bar-track {
 538:   background-color: rgba(0, 0, 0, 0.1);
 539: }
 540: 
 541: .frequency-bar-fill {
 542:   height: 100%;
 543:   width: 0%;
 544:   border-radius: 2px;
 545:   transition: width 0.3s ease;
 546: }
 547: 
 548: .frequency-stars {
 549:   font-size: 0.7rem;
 550:   letter-spacing: 0.05em;
 551:   line-height: 1;
 552: }
 553: 
 554: /* Frequency Tier Theming */
 555: .frequency-badge.freq-very-common {
 556:   color: var(--freq-very-common);
 557:   border-color: rgba(16, 185, 129, 0.3);
 558:   background-color: rgba(16, 185, 129, 0.1);
 559: }
 560: .frequency-badge.freq-very-common .frequency-bar-fill {
 561:   background-color: var(--freq-very-common);
 562: }
 563: 
 564: .frequency-badge.freq-common {
 565:   color: var(--freq-common);
 566:   border-color: rgba(34, 197, 94, 0.3);
 567:   background-color: rgba(34, 197, 94, 0.1);
 568: }
 569: .frequency-badge.freq-common .frequency-bar-fill {
 570:   background-color: var(--freq-common);
 571: }
 572: 
 573: .frequency-badge.freq-medium {
 574:   color: var(--freq-medium);
 575:   border-color: rgba(234, 179, 8, 0.3);
 576:   background-color: rgba(234, 179, 8, 0.1);
 577: }
 578: .frequency-badge.freq-medium .frequency-bar-fill {
 579:   background-color: var(--freq-medium);
 580: }
 581: 
 582: .frequency-badge.freq-uncommon {
 583:   color: var(--freq-uncommon);
 584:   border-color: rgba(249, 115, 22, 0.3);
 585:   background-color: rgba(249, 115, 22, 0.1);
 586: }
 587: .frequency-badge.freq-uncommon .frequency-bar-fill {
 588:   background-color: var(--freq-uncommon);
 589: }
 590: 
 591: .frequency-badge.freq-rare {
 592:   color: var(--freq-rare);
 593:   border-color: rgba(239, 68, 68, 0.3);
 594:   background-color: rgba(239, 68, 68, 0.1);
 595: }
 596: .frequency-badge.freq-rare .frequency-bar-fill {
 597:   background-color: var(--freq-rare);
 598: }
 599: 
 600: /* Pitch accent: quiet muted supplement to the reading */
 601: .pitch-quiet {
 602:   font-size: clamp(0.88rem, 0.6vw + 0.72rem, 1.08rem);
 603:   color: var(--text-muted);
 604:   line-height: 1.4;
 605:   margin: 0;
 606:   text-align: center;
 607: }
 608: 
 609: .pitch-quiet svg {
 610:   max-height: 2.2em;
 611:   width: auto;
 612:   vertical-align: middle;
 613:   filter: opacity(0.85);
 614: }
 615: 
 616: /* --- Decorative separator: seigaiha-inspired arc motif ---
 617:    A tiny wave pattern between the hero word/meaning and the context area.
 618:    Pure CSS, no images. Adds visual rhythm without distraction. */
 619: .card-separator {
 620:   display: flex;
 621:   align-items: center;
 622:   justify-content: center;
 623:   gap: 0;
 624:   margin: clamp(4px, 0.8vh, 8px) auto;
 625:   width: 100%;
 626:   max-width: 280px;
 627:   height: 12px;
 628:   opacity: 0.7;
 629: }
 630: 
 631: .card-separator::before,
 632: .card-separator::after {
 633:   content: "";
 634:   flex: 1;
 635:   height: 1px;
 636:   background: linear-gradient(to var(--sep-dir, right),
 637:     transparent, var(--separator-color) 40%, var(--separator-accent) 100%);
 638: }
 639: 
 640: .card-separator::after {
 641:   --sep-dir: left;
 642: }
 643: 
 644: .card-separator .sep-motif {
 645:   flex-shrink: 0;
 646:   width: 8px;
 647:   height: 8px;
 648:   border-radius: 50%;
 649:   background: var(--separator-accent);
 650:   margin: 0 10px;
 651:   position: relative;
 652: }
 653: 
 654: /* Small decorative arcs flanking the dot — evoke seigaiha wave crests */
 655: .card-separator .sep-motif::before,
 656: .card-separator .sep-motif::after {
 657:   content: "";
 658:   position: absolute;
 659:   top: 50%;
 660:   width: 14px;
 661:   height: 14px;
 662:   border-radius: 50%;
 663:   border: 1px solid var(--separator-color);
 664:   transform: translateY(-50%);
 665: }
 666: 
 667: .card-separator .sep-motif::before {
 668:   right: 100%;
 669:   margin-right: 4px;
 670: }
 671: 
 672: .card-separator .sep-motif::after {
 673:   left: 100%;
 674:   margin-left: 4px;
 675: }
 676: 
 677: /* Audio row: quiet affordances under the target & meaning. */
 678: .audio-row {
 679:   display: flex;
 680:   align-items: center;
 681:   justify-content: center;
 682:   flex-wrap: wrap;
 683:   gap: 10px;
 684:   margin: clamp(10px, 1.6vh, 18px) auto 6px auto;
 685: }
 686: 
 687: /* Empty-shell guard (QUALITY.md "Empty-field collapse"): .audio-row
 688:    renders unconditionally while its buttons are conditional — collapse
 689:    the shell when every child is absent so no margin/gap survives an
 690:    empty field. */
 691: .audio-row:not(:has(.circular-audio-btn)) {
 692:   display: none;
 693: }
 694: 
 695: .definition-box {
 696:   /* Editorial typography: no harsh dividing lines, optimal reading measure */
 697:   font-family: var(--font-interface);
 698:   font-size: clamp(1.04rem, 0.45vw + 0.84rem, 1.38rem);
 699:   line-height: calc(var(--furigana-headroom) + 1em + 0.15em);
 700:   color: var(--text-primary);
 701:   max-width: 68ch;
 702:   margin: clamp(4px, 0.8vh, 10px) auto 0 auto;
 703:   padding-top: var(--furigana-headroom);
 704:   width: 100%;
 705:   text-align: center;
 706: }
 707: 
 708: 
 709: /* ==============================================================================
 710:    6b. DEFINITION COMPACTOR (scope: .primary-definition ONLY)
 711:    ==============================================================================
 712:    Yomitan mines the full Definition field as a .yomitan-glossary containing
 713:    one <li data-dictionary="..."> per dictionary plus embedded <style> blocks.
 714:    That is far too verbose for the main card. Rules below collapse it to:
 715:      - 1 dictionary entry (the first)
 716:      - at most 2 numbered senses within it
 717:      - no appendices (possible-forms / synonym / supplementary blocks)
 718:    Dictionary-agnostic: matches structural attributes, never dictionary
 719:     names. Deliberately does NOT touch .extended-full (the full Yomitan
 720:     definition inside the More section stays full) or any other field.
 721:    ============================================================================== */
 722: 
 723: /* --- Collapse all dictionary entries after the first --- */
 724: /* List markers: Yomitan emits <ol><li> per dictionary; suppress the "1."
 725:    numbering and the ol indent so the kept entry reads as plain text. */
 726: .primary-definition .yomitan-glossary > ol {
 727:   list-style: none;
 728:   margin: 0;
 729:   padding-left: 0;
 730: }
 731: /* Dictionary name labels and metadata <i>(...)</i> are noise. */
 732: .primary-definition i {
 733:   display: none;
 734: }
 735: .primary-definition .yomitan-glossary > ol > li ~ li {
 736:   display: none;
 737: }
 738: 
 739: /* --- Keep at most 2 numbered senses per dictionary --- */
 740: /* Structured dictionaries (data-sc-name variants: 語義G sense blocks in
 741:    大辞林-style SC markup, data-sc-l3* sense wrappers in 大辞泉-style SC
 742:    markup). Sibling chains select everything from the 3rd occurrence on. */
 743: .primary-definition div[data-sc-name="語義G"] ~ div[data-sc-name="語義G"] ~ div[data-sc-name="語義G"],
 744: .primary-definition div[data-sc-l3] ~ div[data-sc-l3] ~ div[data-sc-l3],
 745: .primary-definition div[data-sc-l3-a] ~ div[data-sc-l3-a] {
 746:   display: none;
 747: }
 748: 
 749: /* Simple merged dictionaries: plain gloss <li> lists — keep max 2 glosses */
 750: .primary-definition [data-sc-content="glossary"] > li ~ li ~ li {
 751:   display: none;
 752: }
 753: 
 754: /* --- Hide sense appendices (any dictionary, structural match) --- */
 755: /* 補説G = supplementary note; 可能形 = possible-form line;
 756:    歴史仮名 = historical kana reading; アクセントG = accent [n] notation
 757:    (hiding the group also hides its nested [n] number) */
 758: .primary-definition div[data-sc-name="補説G"],
 759: .primary-definition span[data-sc-name="可能形"],
 760: .primary-definition span[data-sc-name="歴史仮名"],
 761: .primary-definition span[data-sc-name="アクセントG"],
 762: .primary-definition li[data-sc-content="forms"] {
 763:   display: none;
 764: }
 765: 
 766: /* Hide attribution (JMdict | Tatoeba) */
 767: .primary-definition div[data-sc-content="attribution"] {
 768:   display: none;
 769: }
 770: 
 771: /* Yomitan inline <style> blocks inside the glossary leak their own rules
 772:    (list display modes, per-dictionary colors). Neutralize styling that
 773:    fights the card theme; keep size/margins untouched so SC layouts hold.
 774:    background-image is killed outright: hide-only compactor must never let
 775:    mined CSS exfiltrate via url() or overlay UI. */
 776: .primary-definition .yomitan-glossary * {
 777:   background-image: none !important;
 778: }
 779: .primary-definition .yomitan-glossary ul[data-sc-content="glossary"] {
 780:   display: inline;
 781:   list-style: none;
 782:   padding-left: 0;
 783: }
 784: .primary-definition .yomitan-glossary ul[data-sc-content="glossary"] > li {
 785:   display: inline;
 786: }
 787: .primary-definition .yomitan-glossary ul[data-sc-content="glossary"] > li:not(:first-child)::before {
 788:   content: " | ";
 789:   white-space: pre-wrap;
 790:   display: inline;
 791:   color: var(--text-muted);
 792: }
 793: 
 794: /* ==============================================================================
 795:     6c. DEFINITION TRUNCATOR & EXPANDABLE UI
 796:     ==============================================================================
 797:     Primary definition shows THREE lines by default (line-height computed
 798:     from --furigana-headroom + 1em + 0.05em). Longer content clips and
 799:     gets a progressive fade + one small ▼ chevron (no text label). Click,
 800:     tap, Enter or Space expands to the full text and STAYS expanded
 801:     (one-way: a second click never re-collapses it).
 802: 
 803:     Mechanics are deliberately boring so they hold for ANY nested Yomitan
 804:     markup on every client (Qt6 WebEngine + AnkiDroid WebKit):
 805:       - display:block + max-height + overflow:hidden clips everything.
 806:         (-webkit-line-clamp was tried and reverted: it needs -webkit-box,
 807:         miscounts nested block children, and silently kept .is-expanded
 808:         clamped because the clamp was never unset on expand.)
 809:       - .is-truncated is added by JS only when content truly overflows
 810:         (scrollHeight > clientHeight), so short glosses never show a
 811:         misleading fade/chevron. Without JS the box is just a plain full
 812:         definition — never broken, never misleading.
 813:     ============================================================================== */
 814: 
 815: /* Collapsed cap = 3 lines. Line-height is the furigana-headroom formula
 816:    from .definition-box; max-height applies to the CONTENT box (no
 817:    box-sizing override here), so the top headroom padding sits outside
 818:    the cap — no extra term needed. */
 819: .definition-box.primary-definition {
 820:   position: relative;
 821:   overflow: hidden;
 822:   max-height: calc((var(--furigana-headroom) + 1em + 0.05em) * 3);
 823:   cursor: default;
 824: }
 825: 
 826: /* Expanded: cap removed entirely, stays expanded (no re-collapse) */
 827: .definition-box.primary-definition.is-expanded {
 828:   max-height: none;
 829:   cursor: default;
 830: }
 831: 
 832: /* Overflow confirmed by JS: clickable affordance */
 833: .definition-box.primary-definition.is-truncated {
 834:   cursor: pointer;
 835: }
 836: 
 837: /* Progressive fade: line bottom dissolves into the card => "there's more" */
 838: .definition-box.primary-definition.is-truncated:not(.is-expanded)::after {
 839:   content: "";
 840:   position: absolute;
 841:   bottom: 0;
 842:   left: 0;
 843:   right: 0;
 844:   height: 1.2em;
 845:   background: linear-gradient(to bottom,
 846:     transparent 0%,
 847:     var(--bg-color) 100%
 848:   );
 849:   pointer-events: none;
 850: }
 851: 
 852: /* Collapsed indicator: one small chevron, no text */
 853: .definition-box.primary-definition.is-truncated:not(.is-expanded)::before {
 854:   content: "▼";
 855:   position: absolute;
 856:   bottom: 0;
 857:   left: 50%;
 858:   transform: translateX(-50%);
 859:   color: var(--text-muted);
 860:   font-size: 0.62rem;
 861:   line-height: 1;
 862:   pointer-events: none;
 863: }
 864: 
 865: .definition-box.primary-definition.is-truncated:not(.is-expanded):hover::before,
 866: .definition-box.primary-definition.is-truncated:not(.is-expanded):focus-visible::before {
 867:   color: var(--accent-color);
 868: }
 869: 
 870: /* ==============================================================================
 871:    7. CIRCULAR AUDIO BUTTON WITH SVG PROGRESS RING
 872:    ============================================================================== */
 873: /* Ring geometry: stroke-dasharray 226.19 (large, r=36) / 119.38 (small,
 874:    r=19) = 2πr. The same constants live in the SVG markup and the JS
 875:    resetAudioState fallbacks — update all three together if r changes. */
 876: .audio-row {
 877:   display: inline-flex;
 878:   align-items: center;
 879:   gap: 10px;
 880: }
 881: 
 882: .circular-audio-btn {
 883:   position: relative;
 884:   display: inline-flex;
 885:   align-items: center;
 886:   justify-content: center;
 887:   background-color: var(--accent-light);
 888:   border: 1px solid var(--card-border);
 889:   border-radius: 50%;
 890:   cursor: pointer;
 891:   padding: 0;
 892:   margin: 0;
 893:   outline: none;
 894:   transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1),
 895:               border-color 0.2s ease,
 896:               background-color 0.2s ease,
 897:               box-shadow 0.2s ease;
 898:   user-select: none;
 899:   -webkit-tap-highlight-color: transparent;
 900: }
 901: 
 902: .small-audio-btn {
 903:   width: 36px;
 904:   height: 36px;
 905: }
 906: 
 907: /* Keyboard focus indicator (outline: none above only affects mouse clicks;
 908:    :focus-visible restores a compact accent ring for keyboard navigation) */
 909: .circular-audio-btn:focus-visible,
 910: .translation-box:focus-visible,
 911: .picture-container:focus-visible {
 912:   outline: 2px solid var(--accent-color);
 913:   outline-offset: 2px;
 914: }
 915: 
 916: .large-audio-btn {
 917:   width: 84px;
 918:   height: 84px;
 919:   background-color: var(--card-bg-elevated);
 920:   box-shadow: var(--shadow-premium);
 921: }
 922: 
 923: .circular-audio-btn:hover,
 924: .circular-audio-btn:active {
 925:   transform: scale(1.08);
 926:   border-color: var(--accent-color);
 927:   background-color: var(--accent-soft);
 928:   box-shadow: var(--accent-glow);
 929: }
 930: 
 931: .circular-audio-btn.is-playing {
 932:   border-color: var(--accent-color);
 933:   box-shadow: var(--accent-glow);
 934:   background-color: var(--accent-soft);
 935: }
 936: 
 937: .audio-progress-ring {
 938:   /* Playback indicator: a decorative play-pulse, not true progress.
 939:      Native audio is the authority (ADR 003); this ring only signals that
 940:      a play was triggered and re-tap debounce is active. */
 941:   position: absolute;
 942:   top: 0;
 943:   left: 0;
 944:   width: 100%;
 945:   height: 100%;
 946:   transform: rotate(-90deg);
 947:   pointer-events: none;
 948: }
 949: 
 950: .audio-progress-ring .ring-bg {
 951:   fill: none;
 952:   stroke: var(--accent-light);
 953:   stroke-width: 2px;
 954: }
 955: 
 956: .audio-progress-ring .ring-fill {
 957:   fill: none;
 958:   stroke: var(--accent-color);
 959:   stroke-width: 2px;
 960:   stroke-linecap: round;
 961:   transition: stroke-dashoffset 0.08s linear;
 962: }
 963: 
 964: .audio-btn-content {
 965:   display: flex;
 966:   align-items: center;
 967:   justify-content: center;
 968:   z-index: 2;
 969: }
 970: 
 971: .small-audio-btn .audio-btn-label {
 972:   font-family: var(--font-japanese-serif);
 973:   font-size: 0.75rem;
 974:   font-weight: 500;
 975:   color: var(--text-muted);
 976:   letter-spacing: 0.02em;
 977:   line-height: 1;
 978:   transition: color 0.15s ease;
 979: }
 980: 
 981: .small-audio-btn:hover .audio-btn-label {
 982:   color: var(--accent-color);
 983: }
 984: 
 985: .large-audio-btn .audio-btn-label {
 986:   font-family: var(--font-japanese-serif);
 987:   font-size: 1.5rem;
 988:   font-weight: 700;
 989:   color: var(--accent-color);
 990:   letter-spacing: 0.04em;
 991:   line-height: 1;
 992: }
 993: 
 994: .circular-audio-btn.is-playing .audio-btn-label {
 995:   color: var(--text-primary);
 996: }
 997: 
 998: 
 999: /* ==============================================================================
1000:     8. SENTENCE & TRANSLATION - Fluid Typography
1001:     ============================================================================== */
1002: /* Level 3 (context): the sentence supports the target; it reads as
1003:    context, not as the loudest element (that is the headword). */
1004: .sentence-japanese {
1005:   font-family: var(--font-japanese-serif);
1006:   /* Supporting context: distinctly smaller than the hero headword */
1007:   font-size: clamp(1.2rem, 1.5vw + 0.6rem, 1.85rem);
1008:   /* Multi-line clearance: each wrapped line needs room for hover furigana
1009:      above it (rt height + gap), delivered via line-height. Final line is
1010:      covered by --furigana-headroom on top padding below. */
1011:   line-height: calc(var(--furigana-headroom) + 1.3em);
1012:   padding-top: calc(var(--block-pad-y, 0px) + var(--furigana-headroom));
1013:   margin-bottom: clamp(8px, 1.5vmin, 14px);
1014:   color: var(--text-primary);
1015:   text-align: center;
1016:   letter-spacing: 0.03em;
1017: }
1018: 
1019: .sentence-japanese,
1020: .sentence-japanese * {
1021:   text-align: center;
1022: }
1023: 
1024: /* Secondary blocks inside the More section: quiet, no card-in-card. */
1025: .secondary-block {
1026:   font-size: clamp(0.98rem, 0.35vw + 0.78rem, 1.28rem);
1027:   line-height: 1.6;
1028:   color: var(--text-secondary);
1029:   text-align: left;
1030:   margin-top: 10px;
1031:   padding: clamp(6px, 1vh, 12px) var(--block-pad-x);
1032:   background: var(--warm-accent);
1033:   border-radius: var(--border-radius-sm);
1034:   border-left: 2px solid var(--separator-accent);
1035: }
1036: 
1037: .translation-box {
1038:   background-color: var(--accent-light);
1039:   border: 1px solid var(--card-border);
1040:   border-radius: var(--border-radius-md);
1041:   padding: 10px 16px;
1042:   cursor: pointer;
1043:   transition: background-color 0.2s ease, border-color 0.2s ease,
1044:               transform 0.15s ease;
1045:   width: 100%;
1046:   max-width: 68ch;
1047:   margin: 8px auto;
1048:   box-sizing: border-box;
1049: }
1050: 
1051: .translation-box:hover {
1052:   background-color: var(--accent-soft);
1053:   border-color: var(--accent-color);
1054:   transform: translateY(-1px);
1055: }
1056: 
1057: .card:not(.nightMode):not(.night_mode) .translation-box {
1058:   background-color: var(--accent-light);
1059:   border-color: rgba(0, 0, 0, 0.06);
1060: }
1061: 
1062: .card:not(.nightMode):not(.night_mode) .translation-box:hover {
1063:   background-color: var(--accent-soft);
1064:   border-color: var(--accent-color);
1065: }
1066: 
1067: .translation-hint {
1068:   font-size: 0.82rem;
1069:   font-weight: 500;
1070:   letter-spacing: 0.06em;
1071:   text-transform: uppercase;
1072:   color: var(--text-muted);
1073:   user-select: none;
1074:   text-align: center;
1075: }
1076: 
1077: .translation-text {
1078:   display: none;
1079:   /* Lower emphasis tier: floor sits below the definition's floor
1080:      so revealed translations read as secondary. */
1081:   font-size: clamp(0.98rem, 0.35vw + 0.78rem, 1.28rem);
1082:   color: var(--text-secondary);
1083:   line-height: 1.55;
1084:   text-align: center;
1085: }
1086: 
1087: .translation-box.revealed .translation-text { display: block; }
1088: .translation-box.revealed .translation-hint { display: none; }
1089: 
1090: /* Orphan translation (no Sentence): rendered statically, same tier. */
1091: .revealed-static.translation-text {
1092:   display: block;
1093:   font-size: clamp(0.98rem, 0.35vw + 0.78rem, 1.28rem);
1094:   color: var(--text-secondary);
1095:   line-height: 1.55;
1096:   text-align: center;
1097: }
1098: 
1099: .context-block {
1100:   margin-top: 8px;
1101: }
1102: 
1103: .html-content {
1104:   /* Lower emphasis tier: notes/context are support material, quieter
1105:      than the definition (and floor-below it, unlike before). */
1106:   font-size: clamp(0.98rem, 0.35vw + 0.78rem, 1.28rem);
1107:   line-height: 1.6;
1108: }
1109: 
1110: 
1111: /* ==============================================================================
1112:    9. FURIGANA HOVER & TOUCH ERGONOMICS (Zero-Reflow / Zero-Shift)
1113:    ============================================================================== */
1114: ruby {
1115:   position: relative;
1116:   display: inline-block;
1117:   line-height: 1;
1118: }
1119: 
1120: ruby rt {
1121:   position: absolute;
1122:   left: 50%;
1123:   transform: translateX(-50%);
1124:   bottom: 100%;
1125:   font-size: 0.55em;
1126:   line-height: 1;
1127:   white-space: nowrap;
1128:   visibility: hidden;
1129:   opacity: 0;
1130:   color: var(--accent-color);
1131:   transition: opacity 0.15s ease-out;
1132:   pointer-events: none;
1133:   user-select: none;
1134:   /* Gap above the base text — part of the reserved headroom */
1135:   margin-bottom: 2px;
1136: }
1137: 
1138: /* Mouse Hover & Mobile Tap Active - 100% Shift-free */
1139: ruby:hover rt,
1140: ruby:active rt,
1141: ruby:focus rt,
1142: ruby:focus-within rt {
1143:   visibility: visible;
1144:   opacity: 1;
1145: }
1146: 
1147: /* 9b. FULL-CARD FURIGANA MODE (back only; F toggles).
1148:    Pins every rt visible at once — same absolute geometry, so nothing
1149:    reflows. .furigana-mode lives on the back card wrapper only; the
1150:    front is a retrieval surface and stays furigana-free. */
1151: .card-wrapper.furigana-mode ruby rt {
1152:   visibility: visible;
1153:   opacity: 1;
1154: }
1155: 
1156: 
1157: /* ==============================================================================
1158:    10. MEDIA & LIGHTBOX MODAL
1159:    ============================================================================== */
1160: .picture-container img {
1161:   /* Block-level: kills the inline-baseline descender gap that left loose pixels.
1162:      Desktop cap is generous (44vh) so the parallel picture fills the row
1163:      height beside the sentence instead of leaving empty space; mobile
1164:      override (§13) stays compact for no-scroll. */
1165:   display: block;
1166:   margin-inline: auto;
1167:   max-width: 100%;
1168:   max-height: 44vh;
1169:   height: auto;
1170:   object-fit: contain;
1171:   border-radius: var(--border-radius-md);
1172:   border: 1px solid var(--card-border);
1173:   box-shadow: var(--shadow-premium);
1174:   cursor: zoom-in;
1175:   transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
1176:               box-shadow 0.3s ease;
1177: }
1178: 
1179: .card:not(.nightMode):not(.night_mode) .picture-container img {
1180:   border-color: rgba(0, 0, 0, 0.07);
1181:   box-shadow: var(--shadow-soft);
1182: }
1183: 
1184: .picture-container img:hover {
1185:   transform: scale(1.02);
1186:   box-shadow: var(--shadow-premium), var(--accent-glow);
1187: }
1188: 
1189: .lightbox-overlay {
1190:   position: fixed;
1191:   top: 0;
1192:   left: 0;
1193:   width: 100%;
1194:   height: 100%;
1195:   background: rgba(0, 0, 0, 0.78);
1196:   z-index: 2000;
1197:   backdrop-filter: blur(14px) saturate(0.8);
1198:   -webkit-backdrop-filter: blur(14px) saturate(0.8);
1199:   display: flex;
1200:   align-items: center;
1201:   justify-content: center;
1202:   cursor: zoom-out;
1203: }
1204: 
1205: .expanded-img {
1206:   position: fixed;
1207:   top: 50%;
1208:   left: 50%;
1209:   transform: translate(-50%, -50%) scale(1);
1210:   max-width: 96vw;
1211:   max-height: 96vh;
1212:   z-index: 2001;
1213:   border-radius: var(--border-radius-md);
1214:   box-shadow: 0 20px 60px rgba(0, 0, 0, 0.88);
1215:   animation: lightboxIn 0.18s cubic-bezier(0.34, 1.56, 0.64, 1);
1216: }
1217: 
1218: @keyframes lightboxIn {
1219:   from {
1220:     transform: translate(-50%, -50%) scale(0.92);
1221:     opacity: 0;
1222:   }
1223:   to {
1224:     transform: translate(-50%, -50%) scale(1);
1225:     opacity: 1;
1226:   }
1227: }
1228: 
1229: 
1230: /* ==============================================================================
1231:    11. FOOTER & SHORTCUT HINTS
1232:    ============================================================================== */
1233: .extended-def-wrapper {
1234:   margin-top: 12px;
1235:   padding-top: 8px;
1236:   border-top: 1px dashed var(--card-border);
1237: }
1238: 
1239: .extended-def-header {
1240:   font-size: 0.72rem;
1241:   font-weight: 600;
1242:   letter-spacing: 0.08em;
1243:   text-transform: uppercase;
1244:   color: var(--text-muted);
1245:   margin-bottom: 6px;
1246:   text-align: left;
1247: }
1248: 
1249: .shortcut-hints {
1250:   display: flex;
1251:   align-items: center;
1252:   justify-content: center;
1253:   flex-wrap: wrap;
1254:   gap: 12px;
1255:   margin: clamp(6px, 1vh, 12px) auto 4px auto;
1256:   padding: 6px 12px;
1257:   opacity: 0.55;
1258:   transition: opacity 0.2s ease;
1259:   user-select: none;
1260: }
1261: 
1262: .shortcut-hints:hover {
1263:   opacity: 0.95;
1264: }
1265: 
1266: .shortcut-item {
1267:   display: inline-flex;
1268:   align-items: center;
1269:   gap: 4px;
1270:   font-size: 0.72rem;
1271:   color: var(--text-muted);
1272:   font-weight: 500;
1273:   letter-spacing: 0.02em;
1274: }
1275: 
1276: .shortcut-item kbd {
1277:   display: inline-block;
1278:   padding: 1px 5px;
1279:   font-family: var(--font-interface);
1280:   font-size: 0.68rem;
1281:   font-weight: 600;
1282:   line-height: 1.2;
1283:   color: var(--text-primary);
1284:   background-color: var(--card-bg-elevated);
1285:   border: 1px solid var(--card-border);
1286:   border-radius: 4px;
1287:   box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
1288: }
1289: 
1290: .card:not(.nightMode):not(.night_mode) .shortcut-item kbd {
1291:   background-color: #f0ede6;
1292:   border-color: rgba(0, 0, 0, 0.12);
1293:   box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
1294: }
1295: 
1296: .source-footer {
1297:   text-align: center;
1298:   padding: 8px 0 4px;
1299:   font-size: 0.72rem;
1300:   font-weight: 500;
1301:   color: var(--text-muted);
1302:   letter-spacing: 0.06em;
1303:   text-transform: uppercase;
1304:   opacity: 0.7;
1305: }
1306: 
1307: 
1308: /* ==============================================================================
1309:     12. LISTENING MODE FRONT
1310:     ============================================================================== */
1311: /* Listening cards (audio-only: no definitions, no frequency, has Sentence Audio).
1312:    The template only renders .listening-view on pure listening cards. */
1313: .listening-view {
1314:   display: flex;
1315:   align-items: center;
1316:   justify-content: center;
1317:   /* Deliberate presence: enough height that the lone audio button reads
1318:       as THE card, not an accident */
1319:   min-height: 30vh;
1320:   padding: 16px;
1321: }
1322: 
1323: .card-wrapper.listening-mode .listening-view {
1324:   display: flex;
1325: }
1326: 
1327: /* Listening mode is exclusive with the sentence/word fronts. */
1328: .card-wrapper.listening-mode .sentence-display,
1329: .card-wrapper.listening-mode .front-word-display {
1330:   display: none;
1331: }
1332: 
1333: .audio-btn-wrapper {
1334:   display: inline-flex;
1335:   align-items: center;
1336:   justify-content: center;
1337:   position: relative;
1338: }
1339: 
1340: /* Holds Anki's own replay link. Visually hidden but KEPT in layout:
1341:    display:none breaks programmatic .click() playback on some clients,
1342:    and the link must not live inside the <button> (invalid HTML that
1343:    Android WebView mishandles). */
1344: .raw-audio-source {
1345:   position: absolute;
1346:   width: 1px;
1347:   height: 1px;
1348:   margin: -1px;
1349:   padding: 0;
1350:   overflow: hidden;
1351:   clip: rect(0 0 0 0);
1352:   white-space: nowrap;
1353:   opacity: 0;
1354:   pointer-events: none;
1355: }
1356: 
1357: 
1358: /* ==============================================================================
1359:     13. MOBILE SPECIFIC OPTIMIZATIONS (< 600px / Samsung Galaxy A50)
1360:     Density, hierarchy, furigana, and JS interactions stay intact on the
1361:     narrow screen.
1362:     ============================================================================== */
1363: @media (max-width: 600px) {
1364:   .back-card .card-container {
1365:     margin: 0 auto;
1366:     padding: 8px 6px;
1367:     border-radius: var(--border-radius-md);
1368:     /* A50 fast-path: stacked layout hides the backdrop anyway; skip the
1369:        offscreen blur surface on the weakest GPU. */
1370:     backdrop-filter: none;
1371:     -webkit-backdrop-filter: none;
1372:   }
1373: 
1374:   .sentence-display,
1375:   .front-word-display {
1376:     font-size: clamp(1.1rem, 3.8vmin + 0.5rem, 1.85rem);
1377:     padding: 4px 6px;
1378:   }
1379:   .sentence-japanese {
1380:     font-size: clamp(1.1rem, 3.5vmin + 0.5rem, 1.85rem);
1381:   }
1382:   .word-display {
1383:     font-size: clamp(1.9rem, 4.5vmin + 1rem, 2.7rem);
1384:   }
1385: 
1386:   /* Narrow phones: word on its own centered row, the two sides share
1387:      one tight row below it (left cell right-aligned, right cell
1388:      left-aligned, so the pair stays jointly centered). */
1389:   .hero-header {
1390:     grid-template-columns: 1fr 1fr;
1391:     grid-template-areas:
1392:       "word word"
1393:       "left right";
1394:     row-gap: 1px;
1395:     column-gap: 8px;
1396:   }
1397: 
1398:   .hero-side {
1399:     gap: 8px;
1400:   }
1401: 
1402:   .frequency-badge {
1403:     padding: 2px 7px;
1404:     font-size: 0.74rem;
1405:     gap: 4px;
1406:   }
1407: 
1408:   .frequency-bar-track {
1409:     width: 24px;
1410:   }
1411: 
1412:   .frequency-stars {
1413:     font-size: 0.62rem;
1414:   }
1415: 
1416:   .context-grid:has(.context-picture) {
1417:     flex-direction: column;
1418:     gap: 8px;
1419:   }
1420: 
1421:   .context-grid:has(.context-picture) .context-picture {
1422:     order: -1;
1423:   }
1424: 
1425:   .picture-container img {
1426:     max-height: clamp(24vh, 22vmin, 32vh);
1427:     border-radius: var(--border-radius-sm);
1428:   }
1429: 
1430:   .audio-row {
1431:     gap: 8px;
1432:   }
1433: 
1434:   .small-audio-btn {
1435:     width: 32px;
1436:     height: 32px;
1437:   }
1438: 
1439:   .small-audio-btn .audio-btn-label {
1440:     font-size: 0.66rem;
1441:   }
1442: 
1443:   .more-toggle {
1444:     font-size: 0.72rem;
1445:     padding: 5px 12px;
1446:     margin-top: 8px;
1447:   }
1448: 
1449:   .card-separator {
1450:     max-width: 180px;
1451:     margin: 4px auto;
1452:   }
1453: 
1454:   .secondary-block {
1455:     padding: 6px 10px;
1456:   }
1457: 
1458:   /* No physical keyboard on phones: the Z/X/C hints are dead weight
1459:      that costs scroll space on every card. Desktop keeps them. */
1460:   .shortcut-hints {
1461:     display: none;
1462:   }
1463: 
1464:   .shortcut-item {
1465:     font-size: 0.65rem;
1466:   }
1467: }
1468: 
1469: 
1470: /* ==============================================================================
1471:     14. BACKDROP SYSTEM (Back card only)
1472:     ==============================================================================
1473:     Full-card decorative background: fully isolated and swappable.
1474:     inspired  by thttps://miaai-lab.github.io/Fable-5.1-100-HTML-Files/
1475:     ENABLE / DISABLE THE BACKDROP
1476:       Delete or comment out everything between the two marker lines
1477:       ".backdrop-block-start" and ".backdrop-block-end" below. The rules
1478:       between the markers contain no comments of their own, so the whole
1479:       region can also be wrapped in a single block comment, or each rule
1480:       deleted individually. Nothing else in this stylesheet depends on
1481:       this block; the Back card then renders exactly as before this
1482:       section existed.
1483: 
1484:     SWAP THE BACKGROUND (any future scene)
1485:       Edit ONLY the two --backdrop-image lines (rule 3 = dark theme,
1486:       rule 4 = Aki Paper light theme). Any CSS background value works:
1487:       a data-URI SVG, url(...), a gradient... The other rules are
1488:       art-agnostic plumbing:
1489: 
1490:       Block contents, in order:
1491:         1. strength dial: --backdrop-opacity (currently 0.45)
1492:         2. generic placement: fixed full-viewport, bottom-anchored, cover
1493:         3. dark-theme scene: --backdrop-image (paper-cut Fuji)
1494:         4. light-theme scene: --backdrop-image (washi-tone variant)
1495:         5. z-index plumbing: keeps card content above the scene
1496:     ============================================================================== */
1497: 
1498: /* ================= .backdrop-block-start =================
1499:    (delete or comment everything from here...
1500: */
1501: 
1502: .card.back-card {
1503:   --backdrop-opacity: 0.45;
1504: }
1505: 
1506: .card.back-card::before {
1507:   content: "";
1508:   position: fixed;
1509:   top: 0;
1510:   left: 0;
1511:   right: 0;
1512:   bottom: 0;
1513:   z-index: 0;
1514:   pointer-events: none;
1515:   background-image: var(--backdrop-image);
1516:   background-repeat: no-repeat;
1517:   background-size: cover;
1518:   background-position: bottom center;
1519:   opacity: var(--backdrop-opacity, 0.45);
1520: }
1521: 
1522: .back-card::before {
1523:   --backdrop-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201600%20900'%20preserveAspectRatio='xMidYMax%20slice'%3E%3Ccircle%20cx='730'%20cy='380'%20r='140'%20fill='%23c9575f'/%3E%3Cpath%20d='M400%20900%20L400%20780%20C600%20620%20720%20460%20790%20335%20L815%20300%20C835%20285%20885%20285%20905%20300%20L930%20335%20C1000%20460%201120%20620%201280%20780%20L1280%20900%20Z'%20fill='%232e3a5c'/%3E%3Cpath%20d='M772%20362%20L815%20300%20C835%20285%20885%20285%20905%20300%20L948%20362%20C920%20370%20895%20358%20868%20364%20C840%20370%20815%20358%20795%20364%20C786%20366%20778%20364%20772%20362%20Z'%20fill='%23d8dde8'/%3E%3Cpath%20d='M-40%20900%20L-40%20812%20C240%20762%20480%20792%20720%20776%20C960%20760%201180%20724%201400%20748%20C1480%20756%201560%20772%201640%20782%20L1640%20900%20Z'%20fill='%23232f4d'/%3E%3Cpath%20d='M-40%20900%20L-40%20852%20C280%20812%20540%20842%20800%20828%20C1040%20816%201260%20786%201460%20818%20C1520%20828%201600%20844%201640%20838%20L1640%20900%20Z'%20fill='%231b2440'/%3E%3Cpath%20d='M-40%20900%20L-40%20880%20C320%20854%20620%20872%20900%20864%20C1140%20858%201390%20840%201640%20866%20L1640%20900%20Z'%20fill='%23151d33'/%3E%3C/svg%3E");
1524: }
1525: 
1526: .card:not(.nightMode):not(.night_mode) .card.back-card::before {
1527:   --backdrop-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201600%20900'%20preserveAspectRatio='xMidYMax%20slice'%3E%3Ccircle%20cx='730'%20cy='380'%20r='140'%20fill='%23cc5f43'/%3E%3Cpath%20d='M400%20900%20L400%20780%20C600%20620%20720%20460%20790%20335%20L815%20300%20C835%20285%20885%20285%20905%20300%20L930%20335%20C1000%20460%201120%20620%201280%20780%20L1280%20900%20Z'%20fill='%23d8bd96'/%3E%3Cpath%20d='M772%20362%20L815%20300%20C835%20285%20885%20285%20905%20300%20L948%20362%20C920%20370%20895%20358%20868%20364%20C840%20370%20815%20358%20795%20364%20C786%20366%20778%20364%20772%20362%20Z'%20fill='%23fbf7ee'/%3E%3Cpath%20d='M-40%20900%20L-40%20812%20C240%20762%20480%20792%20720%20776%20C960%20760%201180%20724%201400%20748%20C1480%20756%201560%20772%201640%20782%20L1640%20900%20Z'%20fill='%23e8dcc6'/%3E%3Cpath%20d='M-40%20900%20L-40%20852%20C280%20812%20540%20842%20800%20828%20C1040%20816%201260%20786%201460%20818%20C1520%20828%201600%20844%201640%20838%20L1640%20900%20Z'%20fill='%23dcc8a6'/%3E%3Cpath%20d='M-40%20900%20L-40%20880%20C320%20854%20620%20872%20900%20864%20C1140%20858%201390%20840%201640%20866%20L1640%20900%20Z'%20fill='%23cfb390'/%3E%3C/svg%3E");
1528: }
1529: 
1530: .back-card .card-container {
1531:   position: relative;
1532:   z-index: 1;
1533: }
1534: 
1535: /* ...to here) ================== .backdrop-block-end ================= */
1536: 
1537: 
1538: /* ==============================================================================
1539:     15. REDUCED MOTION
1540:     ============================================================================== */
1541: 
1542: @media (prefers-reduced-motion: reduce) {
1543:   *,
1544:   *::before,
1545:   *::after {
1546:     transition-duration: 0.01ms !important;
1547:     animation-duration: 0.01ms !important;
1548:     animation-iteration-count: 1 !important;
1549:   }
1550:   /* Static blurs repaint on scroll; cheapest paint for reduced-motion. */
1551:   .back-card .card-container,
1552:   .lightbox-overlay {
1553:     backdrop-filter: none !important;
1554:     -webkit-backdrop-filter: none !important;
1555:   }
1556: }
1557: 
1558: 
1559: /* ==============================================================================
1560:     16. CARD ENTRANCE & VISUAL POLISH
1561:     ==============================================================================
1562:     One quick settle, no stagger: the old per-element delays (up to 0.14s +
1563:     0.35s durations) kept every card visibly in flight for ~half a second,
1564:     which reads as load lag by review #200. A single 0.15s fade keeps a
1565:     whisper of motion; delete the block for instant cards. All animations
1566:     respect prefers-reduced-motion (section 15 kills durations). */
1567: 
1568: /* Back card entrance: everything settles together, once */
1569: .back-card .word-display,
1570: .back-card .definition-box,
1571: .back-card .audio-row,
1572: .back-card .context-grid,
1573: .back-card .card-separator {
1574:   animation: fadeInUp 0.15s ease-out both;
1575: }
1576: 
1577: @keyframes fadeInUp {
1578:   from {
1579:     opacity: 0;
1580:     transform: translateY(10px);
1581:   }
1582:   to {
1583:     opacity: 1;
1584:     transform: translateY(0);
1585:   }
1586: }
1587: 
1588: /* Front card: single quick entrance */
1589: .card-container .sentence-display,
1590: .card-container .front-word-display,
1591: .card-container .listening-view {
1592:   animation: fadeIn 0.15s ease-out both;
1593: }
1594: 
1595: @keyframes fadeIn {
1596:   from { opacity: 0; }
1597:   to { opacity: 1; }
1598: }
1599: 
1600: /* --- Selection styling: accent-tinted highlights --- */
1601: ::selection {
1602:   background: var(--accent-soft);
1603:   color: var(--text-primary);
1604: }
1605: 
1606: ::-moz-selection {
1607:   background: var(--accent-soft);
1608:   color: var(--text-primary);
1609: }
````
