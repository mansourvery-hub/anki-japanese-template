#!/usr/bin/env python3
"""Template & CSS structural invariant tests.

Verifies the source files BEFORE they are pushed to Anki:
  - Front card never renders a furigana-bearing field (back-card-only rule)
  - Front is a pure retrieval surface (no tags/badges/metadata UI)
  - Listening is a hidden-by-default resolver: #listening tag or classic
    audio-only fields activate it; the sentence front is the fallback
  - Secondary back information is collapsed behind "More ▾"
  - Audio buttons carry aria-labels; controller is restart-only
  - Lightbox closes only on backdrop clicks (not on the enlarged image)
  - Anki template conditionals are balanced
  - CSS contains the accessibility/portability rules

Run directly:  python3 tests/test_templates.py
Wired into finish.sh step 0 alongside test_compactor.py.

Pure standard library — no dependencies.
"""
import os
import re
import shutil
import subprocess
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

    # --- 1b. Template scripts must be syntactically valid JavaScript ---
    # A SyntaxError in a card script kills the WHOLE script block: no
    # reveal, no mature mode, no listening resolver — the card hangs
    # hidden. Structural string checks cannot catch an unbalanced brace,
    # so parse every <script> body with node (skipped if node absent).
    node = shutil.which("node")
    if node:
        import tempfile as _tempfile
        for name, src in (("Front", front), ("Back", back)):
            bodies = re.findall(r"<script>(.*?)</script>", src, re.S)
            all_ok = True
            for body in bodies:
                with _tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
                    tf.write(body)
                    tmp_path = tf.name
                try:
                    rc = subprocess.run([node, "--check", tmp_path],
                                        capture_output=True, timeout=30).returncode
                    if rc != 0:
                        all_ok = False
                finally:
                    os.unlink(tmp_path)
            check(f"{name}: all {len(bodies)} script block(s) parse as valid JavaScript", all_ok)
    else:
        print("[SKIP] node not found — template script syntax check skipped")

    # --- 2. Audio buttons: aria-labels present ---
    # Front is sentence-audio-only (1) + Back has word + sentence (2) = 3 total.
    # (Word-audio fallback was removed from the front listening mode.)
    buttons = re.findall(r"<button[^>]*circular-audio-btn[^>]*>", front + back)
    check(f"all {len(buttons)} audio buttons have aria-label",
          len(buttons) >= 3 and all("aria-label" in b for b in buttons))

    # --- 3. Audio controller: native-only (no HTML5 Audio path) ---
    for name, src in (("Front", front), ("Back", back)):
        check(f"{name}: no is-paused state remnants",
              "is-paused" not in src)
        check(f"{name}: resetAudioState defined",
              "window.resetAudioState = function" in src)
        check(f"{name}: native-only playback (no new Audio garbage-loads on AnkiDroid)",
              "new Audio(" not in src)
        check(f"{name}: delegates to Anki replay link",
              "nativeReplay.click()" in src)
        check(f"{name}: replay link resolved via wrapper scope (not nested in button)",
              "closest('.audio-btn-wrapper')" in src)
        check(f"{name}: re-tap debounce (native audio can't be stopped)",
              "window.currentActiveBtn === btn" in src)
        # restart-only: every click path goes through resetAudioState first
        check(f"{name}: playCircularAudio starts with resetAudioState",
              re.search(r"window\.playCircularAudio = function\(btn\) \{\s*(/\*.*?\*/\s*)*if \(window\.currentActiveBtn === btn\) return;\s*window\.resetAudioState\(\);", src, re.S) is not None)

    # --- 3b. Audio markup: valid + clickable on AnkiDroid ---
    for name, src in (("Front", front), ("Back", back)):
        check(f"{name}: replay source lives OUTSIDE the button (sibling span)",
              re.search(r"</button>\s*<span class=\"raw-audio-source\"", src) is not None)
        check(f"{name}: no display:none audio source (breaks .click() playback)",
              "raw-audio-source\" style=\"display:none" not in src)
        check(f"{name}: no div-inside-button (invalid HTML, breaks AnkiDroid taps)",
              '<div class="audio-btn-content">' not in src)
    check("CSS: raw-audio-source visually hidden but present (no display:none)",
          re.search(r"\.raw-audio-source\s*\{[^}]*position:\s*absolute", css) is not None
          and ".raw-audio-source" in css)

    # --- 2c. Cloze fallback: bold-less Sentence rebuilt from cloze trio ---
    check("Front: hidden cloze probe with plain prefix/body/suffix fields",
          'class="cloze-probe"' in front
          and "{{cloze-prefix}}" in front and "{{cloze-body}}" in front
          and "{{cloze-suffix}}" in front)
    check("Front: probe uses plain fields (no edit: filter, stays furigana-free)",
          "edit:cloze" not in front)
    check("Front: reconstruction only fires when sentence lacks bold",
          "querySelector('b, strong')" in front)
    check("Front: reconstruction requires the complete trio (no partial rebuild)",
          "clozePre && clozeMid && clozeSuf" in front)
    check("Front: rebuilt term uses <b> (inherits sentence-display styling)",
          "createElement('b')" in front)

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
    check("CSS: content-driven card sizing (no forced viewport fill)",
          "min-height: 100vh" not in css and "min-height: 100dvh" not in css
          and "container-type: inline-size" in css)
    check("CSS: container-query media fallback for the context grid",
          re.search(r"@media \(min-width: 768px\)[\s\S]{0,200}\.context-grid", css) is not None)

    # --- 6b. Minimal redesign: noise is gone, hierarchy is present ---
    check("Back: no sticky tags bar (tags are behavioral metadata)",
          "tags-container" not in back and "tags-list" not in back
          and "tag-pill" not in back)
    check("Back: no frequency badge machinery (noise without retrieval value)",
          "frequency-badge" not in back and "renderFrequencyIndicator" not in back)
    check("CSS: no frequency badge styling remains",
          "frequency-badge" not in css and "--freq-" not in css)
    check("Back: secondary info is collapsed behind More by default",
          'class="more-section" hidden' in back
          and "more-toggle" in back)
    check("Back: More toggle has aria state + one-way reveal",
          'aria-expanded="false"' in back
          and "toggleMore" in back)
    check("Back: no retrieval-state label UI (content hierarchy replaces captions)",
          "retrieval-state" not in back and "__ajtFrontState" not in back)
    check("Front: no front-state store written",
          "__ajtFrontState" not in front)
    check("CSS: no retrieval-state styling remains",
          "retrieval-state" not in css)
    check("Back: keyboard F toggles full-card furigana (back only)",
          "furigana-mode" in back and "'f'" in back)
    check("Back: keyboard T reveals the translation",
          "'t'" in back and "translation-box" in back)
    check("CSS: full-card furigana mode rule exists",
          ".card-wrapper.furigana-mode ruby rt" in css)
    check("Front: listening resolver driven by #listening tag probe",
          'class="tags-probe"' in front and "hasListeningTag" in front)
    check("Front: no field-presence probes for classic audio-only check",
          "probe-def" not in front and "probe-ext" not in front and "probe-freq" not in front)

    # --- 6c. Listening mode invariants (triggered only by #listening tag) ---
    check("Front: listening markup present (hidden by default, activated by resolver)",
          '<div class="listening-view" hidden>' in front or 'listening-view" hidden' in front)
    check("Front: listening resolver runs synchronously before the reveal",
          "LISTENING RESOLVER" in front)
    check("Front: sentence front is the universal fallback (renders unless listening active)",
          re.search(r"sd.remove\(\)", front) is not None)
    check("CSS: listening-view inert until .listening-mode activates it",
          ".card-wrapper.listening-mode .listening-view" in css)
    check("CSS: listening mode hides the sentence/word fronts",
          ".card-wrapper.listening-mode .sentence-display" in css)
    check("Front: active listening removes the sentence display",
          "sd.remove()" in front)

    # --- 7. Font sizing source-of-truth ---
    check("Back: no JS font-scaler overriding CSS (inline fontSize ban)",
          "el.style.fontSize" not in back and "autoScaleBackSentence" not in back)
    check("CSS: .sentence-japanese clamp() is the sizing authority",
          re.search(r"\.sentence-japanese\s*\{[^}]*font-size:\s*clamp\(", css) is not None)

    # --- 8. (removed) Frequency visualizer retired with the minimal redesign ---

    # --- 8b. Mature Word Mode invariants (interval-gated front) ---
    check("Front: LONG_INTERVAL_DAYS threshold constant defined",
          re.search(r"const\s+LONG_INTERVAL_DAYS\s*=\s*365", front) is not None
          and "interval >= LONG_INTERVAL_DAYS" in front)
    check("Front: threshold not hard-coded elsewhere (single const definition)",
          len(re.findall(r"LONG_INTERVAL_DAYS\s*=\s*365", front)) == 1
          and len(re.findall(r">=\s*365", front)) == 0)
    check("Front: word probe div present with Expression",
          re.search(r'class="front-word-display">\s*\{\{edit:Expression\}\}', front) is not None)
    check("Front: desktop flow guiCurrentCard -> cardsInfo -> interval",
          "guiCurrentCard" in front and "cardsInfo" in front
          and re.search(r"cardsInfo.*?interval", front, re.S) is not None)
    check("Front: previewer fallback via content search (findCards)",
          "findCards" in front and "content search" in front)
    check("Front: no nonexistent Anki-Connect actions",
          "getCardsInfo" not in front)
    check("Front: no card-id-from-URL guess (no URLSearchParams)",
          "URLSearchParams" not in front)
    check("Front: AnkiDroid JS API with verified contract",
          "ankiGetCardInterval" in front and 'new AnkiDroidJS(' in front)
    check("Front: supports constructor + direct bridge APIs",
          "apiKind" in front and "'constructor'" in front and "'direct'" in front)
    check("Front: never invokes new-reviewer stub bridge (signal:jsapi guard)",
          "signal" in front and "jsapi" in front
          and "ankiDroid-stub" in front)
    check("Front: accepts AnkiDroid {success,value} shape (official wiki contract)",
          "parseDroidInterval" in front
          and "hasOwnProperty" in front
          and "'value'" in front)
    check("Front: rejects {success:false} failure defaults (number => -1)",
          "success === false" in front)
    check("Front: parses numeric strings + JSON-encoded responses",
          "JSON.parse" in front and "Number.isFinite" in front)
    check("Front: bridge call has its own timeout (never hangs the card)",
          "withBridgeTimeout" in front)
    check("Front: never fetches AnkiConnect from mobile WebViews (downloadfile.bin toast)",
          "isMobile" in front and "no-bridge-mobile" in front
          and "127.0.0.1" in front)
    check("Front: one deferred bridge retry on mobile while still hidden",
          "bridgeAvailable" in front)
    check("Front: polls for late-injected bridge with a firm deadline",
          "waitForBridge" in front)
    check("Front: bridge poll capped short (fast preview fallback)",
          "waitForBridge(700" in front)
    check("Front: platform-exclusive retrieval (mobile bridge vs desktop AnkiConnect)",
          "Platform-exclusive retrieval" in front and "DESKTOP-ONLY" in front)
    check("Front: retrieval latency is measured and logged",
          "performance.now" in front and "elapsedMs" in front
          and "[Mature Word Mode] source=" in front)
    check("Front: safety reveal cap bounds worst-case hidden time",
          "setTimeout(reveal, 1200)" in front)
    check("Front: AnkiConnect calls fail fast when Anki is wedged (safe sentence fallback)",
          "AnkiConnect timeout" in front and "')), 500)" in front)
    check("Front: temporary toast diagnostic removed (no TEMP-DIAG remnants)",
          "TEMP-DIAG" not in front and "ankiShowToast" not in front)
    check("Front: on-card debug diagnostic present (mwm-debug)",
          "DEBUG_MATURE_MODE" in front and "mwm-debug" in front
          and "Mature mode: " in front)
    check("Front: skips ALL retrieval on listening cards (no needless JS-API calls)",
          "isListening" in front)
    check("Front: anti-flash visibility gate present",
          'style="visibility: hidden;"' in front
          and "container.style.visibility = 'visible'" in front)
    check("Front: word-mode class applied to card wrapper",
          "wrapper.classList.toggle('word-mode'" in front)
    check("Front: retrieval failure falls back to sentence (try/catch + typed interval check)",
          "catch" in front and "typeof interval === 'number'" in front)
    check("CSS: word-mode display rules present",
          ".card-wrapper.word-mode .sentence-display" in css
          and ".card-wrapper.word-mode .front-word-display" in css)
    check("CSS: word mode leaves listening view untouched",
          ".listening-view" not in css.split("5b. MATURE-CARD WORD MODE")[1].split("6. BACK CARD")[0]
          if "5b. MATURE-CARD WORD MODE" in css else False)
    check("Front: no \"note:\" search clause ({{Type}} is scheduling type, not model)",
          "NOTE_TYPE" not in front
          and re.search(r"findCards[^\n]*note:", front) is None
          and 'escQuery(NOTE_TYPE)' not in front)

    # --- 10. Empty-field collapse (QUALITY.md: no UI survives an empty field) ---
    # 10a. Static proof over the raw templates (comments/scripts stripped):
    # every rendered field lives inside an Anki conditional, except the
    # documented allowlist (attribute / hidden probe / gated probe).
    TOKEN = re.compile(r"\{\{\s*([#^/]?)\s*([^}]*?)\s*\}\}")
    ALLOW_BARE = {
        ("Front", "cloze-prefix"), ("Front", "cloze-body"), ("Front", "cloze-suffix"),  # hidden probe
        ("Front", "Expression"),  # front-word-display: display:none default, word-mode gate only (§8b)
        ("Front", "Sentence Audio"),  # listening-view: hidden by default, rendered when #listening tag active
    }
    bare = []
    for name, src in (("Front", front), ("Back", back)):
        clean = re.sub(r"<!--.*?-->", "", src, flags=re.S)
        clean = re.sub(r"<script.*?</script>", "", clean, flags=re.S)
        stack = []
        for m in TOKEN.finditer(clean):
            sig, body = m.group(1), m.group(2).strip()
            if sig in ("#", "^"):
                stack.append(body)
            elif sig == "/":
                if stack:
                    stack.pop()
            elif body:
                field = body.split(":")[-1].strip()
                if not stack and (name, field) not in ALLOW_BARE:
                    bare.append(f"{name}:{{{{{body}}}}}")
    check("every rendered field is conditional (or allowlisted)" + (f" — bare: {bare}" if bare else ""),
          not bare)

    # 10b. Unconditional shells collapse when all conditional children absent.
    check("CSS: empty .audio-row collapses (no button => gone)",
          re.search(r"\.audio-row:not\(:has\(\.circular-audio-btn\)\)\s*\{\s*display:\s*none", css) is not None)
    check("CSS: empty .context-grid collapses (no sentence/context/picture => gone)",
          re.search(r"\.context-grid:not\(:has\([^)]+\)\)\s*\{\s*display:\s*none", css) is not None)
    check("CSS: empty .context-main collapses (no sentence/context => gone)",
          re.search(r"\.context-main:not\(:has\([^)]+\)\)\s*\{\s*display:\s*none", css) is not None)
    check("Back: More section + toggle self-remove when secondary content is absent",
          "btn.remove()" in back and "section.remove()" in back)

    # 10c. Degenerate content removes itself instead of leaving chrome behind.
    check("Back: blank definition box is removed (no bordered void)",
          "box.remove()" in back)
    check("Front: blank sentence block is removed after cloze fixup",
          "sd.remove()" in front)

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
