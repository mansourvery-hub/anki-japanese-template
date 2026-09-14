# QUALITY.md — properties that must remain true

Answers *what must remain true*. `TEST_STRATEGY.md` answers *how it is
mechanically verified*. Code implements; tests enforce.

## Architecture invariants

- Local `.template.anki` / `.css` files are the single source of truth;
  never instruct edits inside the Anki UI.
- Fields live in the Anki UI only; the repo keeps no static field list.
- Vanilla JS/CSS only, scoped, DOM-reuse safe (idempotent init, no globals
  beyond the documented `window.*` controllers).
- Single `LONG_INTERVAL_DAYS = 365` const; no hard-coded `>= 365` elsewhere.
- CSS section numbers (§6b compactor, §6c truncator, §14 backdrop) are stable
  contracts referenced by tests and docs.

## Front invariants

- Front renders **no** furigana filter/field (`Sentence (furigana)` ban);
  raw `{{edit:Sentence}}` / `{{edit:Expression}}` only.
- Front shows **no UI** beyond the tested Japanese: no tags, badges,
  metadata, labels, or controls (hidden behavioral probes only: cloze trio).
  Normal cards NEVER render or play audio on the front.
- Balanced `{{#field}}` / `{{^field}}` / `{{/field}}` conditionals.
- The sentence front is the **universal fallback**: every pathological /
  mature failure path degrades to it, never to a blank or hung card.
- Pure listening cards: `listening-view` renders only under
  `{{^Definition}}{{^Extended definition}}{{^Frequency}}{{#Sentence Audio}}`
  (with a `{{Word Audio}}` fallback when Sentence Audio is absent). Listening
  mode activates ONLY when usable audio exists: `#listening` tag + no audio
  falls back safely to the normal sentence front; a dead/empty listening UI
  is never shown. Exactly ONE listening view is ever visible: a pure
  `#listening` audio card renders both the tag and classic views in markup,
  and the resolver removes every non-active view so no duplicate/dead sound
  button lingers when audio or sentence is missing.
- Normal study cards never include `{{Sentence Audio}}` on front, guaranteeing
  zero audio autoplay on front.
- Listening cards never enter Mature Word Mode and skip all interval
  retrieval.
- Interval has no `{{Interval}}` marker and no `note:` search clause
  (`{{Type}}` is the scheduling type, not the model): desktop AnkiConnect
  only, mobile AnkiDroid bridge only; mobile never fetches
  `127.0.0.1:8765`.
- Mature Word Mode reads the interval of the **exact current card** during
  active review (`guiCurrentCard` → `cardsInfo` on desktop, AnkiDroid bridge
  on mobile); heuristic content matching (Expression → Sentence → cloze-body
  discriminators) is only a best-effort preview/browser fallback and never
  the primary review route. Ambiguous duplicates fail safely to the sentence
  front — candidate 0 is never arbitrarily chosen.
- Any retrieval failure degrades to the sentence front; the front is revealed
  **synchronously** on script start (never blank), with the `visibility:hidden`
  markup and a bounded safety reveal cap kept as redundant guards. A mature card
  may briefly show the sentence before word-mode applies — a blank/hung front is
  never possible.
- Cloze rebuild fires only when Sentence lacks `<b>`/`<strong>` **and** the
  full prefix/body/suffix trio is non-empty; rebuild uses `<b>`.
- AnkiDroid stub bridges (`signal:jsapi`) are never invoked;
  `{success:false}` never becomes an interval; numeric strings and
  JSON-encoded responses parse; bridge calls time out.

## Back invariants

- Back hierarchy is typography-driven: word-display (largest, with Japanese seal) → metadata bar (5-star frequency visualizer & pitch accent & audio) → primary meaning → context → secondary collapsed behind More. Features discoverable via shortcut hints.
- Secondary information (translation, context, kanji notes, notes,
  full extended definition) lives inside `.more-section`, toggleable via
  `More ▾` / `Less ▴`; the toggle and section self-remove when no secondary
  content exists.
- Content hierarchy communicates card mode directly: no retrieval-state
  badges, captions, or dashboard metadata.
- Keyboard shortcuts on the back: `Z` toggles full-card furigana
  (`.furigana-mode`, `F` alias), `X` reveals the translation (`T` alias,
  opening More first), `C` toggles expanded information. `R` is **not** a
  template shortcut — Anki owns it for native audio replay. Custom shortcuts
  never fire in inputs/contentEditable.
- Every circular audio button has an `aria-label`; replay source is a
  **sibling** `.raw-audio-source` (never inside `<button>`, never
  `display:none`); playback delegates to the native replay link; re-tap is
  debounced; `playCircularAudio` starts with `resetAudioState`; no `new
  Audio()`, no `is-paused` remnants, no `div`-inside-`button`. The ring is a
  **playback indicator** (decorative play-pulse), not actual audio progress —
  native delegation is preserved and no HTML5 `Audio()` is used for progress.
- Lightbox closes only on backdrop click (`e.target === overlay`) or
  `Escape`; overlay carries dialog semantics; cloned image preserves `alt`.
- Definition expand is one-way (never re-collapses); `.is-truncated` is set
  only on real overflow; no-JS still shows the full definition.
- No JS font-scaler overrides CSS (`.sentence-japanese` `clamp()` is the
  sizing authority).

## CSS invariants

- Zero-reflow furigana: absolute `ruby rt`, hidden until
  `:hover`/`:active`/`:focus`; `F` mode pins all rt visible with no
  reflow (same geometry).
- Content-driven card height (no `100vh`/`100dvh` fill); `container-type:
  inline-size` present; the context grid (sentence + picture) has a
  media-query fallback.
- `:has()` is intentionally accepted architecture for this project (empty
  collapse guards, responsive context grid) and is not removed or redesigned
  purely for theoretical portability.
- Compactor hide rules all scoped to `.primary-definition`; the full
  extended definition (`.extended-full` inside More) stays untouched.
- Word-mode swap rules exist and never touch `.listening-view`; the
  listening-view is inert until `.listening-mode` activates it.
- `:focus-visible` indicators and `prefers-reduced-motion` present.
- Accent color is reserved for target highlighting and interactive
  states; frequency indicator uses semantic tier colors (--freq-*).
- Front template size is not treated as a defect; correctness and
  reliability take precedence over reducing line count.

## Empty-field collapse (space discipline)

- Every rendered field is enclosed in an Anki `{{#field}}` conditional —
  except the hidden cloze-probe trio, the hidden behavioral probes
  (`tags-probe`, field-presence markers), and the front word probe
  (`display:none` default, word-mode gate only).
- Unconditionally rendered shells collapse when all conditional children are
  absent: `.audio-row`, `.context-grid`, and `.context-main` via `:has()` guards;
  `.more-section` + `.more-toggle` self-remove via JS cleanup.
- Degenerate content removes itself instead of leaving chrome behind:
  blank definition/sentence blocks are removed (front runs after the cloze
  fixup, before the reveal); empty secondary blocks inside More are
  stripped.
- Net rule: no padding, border, or margin may survive an empty field.

## Tooling / process invariants

- Python tooling stays stdlib-only; backups use microsecond timestamps;
  snapshots happen **before** any overwrite; empty live state aborts sync.
- `finish.sh` no-op runs never publish a release.
- Every user prompt is archived to `chat_history/opencode_prompts.txt`
  before/with the commit that follows it.
