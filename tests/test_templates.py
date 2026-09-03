#!/usr/bin/env python3
"""Template & CSS structural invariant tests.

Verifies the source files BEFORE they are pushed to Anki:
  - Front card never renders a furigana-bearing field (back-card-only rule)
  - Audio buttons carry aria-labels
  - Audio controller is restart-only (no pause/resume remnants)
  - Lightbox closes only on backdrop clicks (not on the enlarged image)
  - Anki template conditionals are balanced
  - CSS contains the accessibility/portability rules

Run directly:  python3 tests/test_templates.py
Wired into finish.sh step 0 alongside test_compactor.py.

Pure standard library — no dependencies.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
BACK = os.path.join(ROOT, "Card 1 - Back.template.anki")
CSS = os.path.join(ROOT, "Card 1 - Style.css")

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


def main():
    front = open(FRONT, encoding="utf-8").read()
    back = open(BACK, encoding="utf-8").read()
    css = open(CSS, encoding="utf-8").read()

    # --- 1. Front card: furigana is back-card only ---
    furigana_fields = re.findall(r"\{\{[^}]*furigana[^\d}][^}]*\}\}", front)
    # allowed: none. Front uses plain Sentence/Expression only.
    check("Front renders no furigana: filter or furigana-bearing field",
          not furigana_fields and "Sentence (furigana)" not in front)
    check("Front renders the raw Sentence/Expression fields",
          "{{edit:Sentence}}" in front and "{{edit:Expression}}" in front)

    # --- 2. Audio buttons: aria-labels present ---
    buttons = re.findall(r"<button[^>]*circular-audio-btn[^>]*>", front + back)
    check(f"all {len(buttons)} audio buttons have aria-label",
          len(buttons) >= 4 and all("aria-label" in b for b in buttons))

    # --- 3. Audio controller: restart-only (no pause state machine) ---
    for name, src in (("Front", front), ("Back", back)):
        check(f"{name}: no is-paused state remnants",
              "is-paused" not in src)
        check(f"{name}: resetAudioState defined",
              "window.resetAudioState = function" in src)
        check(f"{name}: error/abort/ended cleanup wired",
              "onended" in src and ("onabort" in src and "onerror" in src))
        check(f"{name}: space-tolerant audio regex",
              "sound:)([^\"'>\\]]+)" in src)
        # restart-only: every click path goes through resetAudioState first
        check(f"{name}: playCircularAudio starts with resetAudioState",
              re.search(r"window\.playCircularAudio = function\(btn\) \{\s*window\.resetAudioState\(\);", src) is not None)

    # --- 4. Lightbox: backdrop-only close ---
    check("lightbox closes only on backdrop click (e.target === overlay)",
          "if (e.target === overlay) closeOverlay()" in back)
    check("lightbox overlay has dialog semantics",
          "setAttribute('role', 'dialog')" in back and "setAttribute('aria-modal', 'true')" in back)
    check("lightbox clone preserves alt text", "img.alt" in back)

    # --- 5. Anki conditionals balanced ({{#field}} and {{^field}} both open) ---
    for name, src in (("Front", front), ("Back", back)):
        opens = len(re.findall(r"\{\{[#^][A-Za-z]", src))
        closes = len(re.findall(r"\{\{/[A-Za-z]", src))
        check(f"{name}: balanced field conditionals ({opens} open / {closes} close)",
              opens == closes)

    # --- 6. CSS invariants ---
    check("CSS: :focus-visible keyboard indicator present",
          ":focus-visible" in css)
    check("CSS: prefers-reduced-motion present",
          "prefers-reduced-motion: reduce" in css)
    check("CSS: 100dvh with 100vh fallback",
          "min-height: 100vh" in css and "min-height: 100dvh" in css)
    check("CSS: container-query media fallback for 2-column layout",
          re.search(r"@media \(min-width: 768px\)[\s\S]{0,200}\.back-grid", css) is not None)
    check("CSS: empty word-header guard (:has)",
          ".word-header:not(:has(" in css)

    # --- 7. Font sizing source-of-truth ---
    check("Back: no JS font-scaler overriding CSS (inline fontSize ban)",
          "el.style.fontSize" not in back and "autoScaleBackSentence" not in back)
    check("CSS: .sentence-japanese clamp() is the sizing authority",
          re.search(r"\.sentence-japanese\s*\{[^}]*font-size:\s*clamp\(", css) is not None)

    # --- 8. Frequency visualizer invariants ---
    check("Back: frequency-badge with data-freq attribute present",
          'class="frequency-badge" data-freq="{{Frequency}}"' in back)
    check("Back: frequency visualizer JS function defined",
          "window.renderFrequencyIndicator = function" in back)
    check("CSS: all 5 frequency tier theme variables defined",
          all(f"--freq-{t}:" in css for t in ("very-common", "common", "medium", "uncommon", "rare")))
    check("CSS: frequency bar track & fill styled",
          ".frequency-bar-track" in css and ".frequency-bar-fill" in css)

    # --- 9. Sync tooling invariants ---
    sync = open(os.path.join(ROOT, "sync_to_anki.py"), encoding="utf-8").read()
    check("sync_to_anki.py: zero third-party imports (standard lib only)",
          "import requests" not in sync and "import urllib.request" in sync)
    check("sync_to_anki.py: microsecond backup timestamps",
          "%H%M%S-%f" in sync)
    finish = open(os.path.join(ROOT, "finish.sh"), encoding="utf-8").read()
    check("finish.sh: no-op run cannot publish a release",
          "Nothing to push or release" in finish)

    print()
    print(f"{PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
