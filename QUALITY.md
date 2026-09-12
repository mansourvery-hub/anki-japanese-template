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
  metadata, labels, or controls (hidden behavioral probes only:
  cloze trio, `#listening` tag probe, field-presence markers).
- Balanced `{{#field}}` / `{{^field}}` / `{{/field}}` conditionals.
- The sentence front is the **universal fallback**: every listening /
  mature failure path degrades to it, never to a blank or hung card.
- Listening activation is a synchronous hidden-by-default resolver:
  the listening markup renders only under `{{#Sentence Audio}}` and is
  inert until the resolver confirms classic audio-only fields OR the
  `#listening` tag; it then removes the sentence display. No JS =>
  sentence front.
- Listening cards never enter Mature Word Mode and skip all interval
  retrieval.
- Interval has no `{{Interval}}` marker and no `note:` search clause
  (`{{Type}}` is the scheduling type, not the model): desktop AnkiConnect
  only, mobile AnkiDroid bridge only; mobile never fetches
  `127.0.0.1:8765`.
- Any retrieval failure degrades to the sentence front; anti-flash
  `visibility:hidden` gate with a bounded reveal cap.
- Cloze rebuild fires only when Sentence lacks `<b>`/`<strong>` **and** the
  full prefix/body/suffix trio is non-empty; rebuild uses `<b>`.
- AnkiDroid stub bridges (`signal:jsapi`) are never invoked;
  `{success:false}` never becomes an interval; numeric strings and
  JSON-encoded responses parse; bridge calls time out.

## Back invariants

- Back hierarchy is typography-driven: word-display (largest) → pitch
  quiet text → definition → sentence context → secondary collapsed.
  No sticky tags bar, no frequency/pitch badges, no oversized controls.
- Secondary information (translation, context, kanji notes, notes,
  full extended definition) lives inside `.more-section`, collapsed by
  default behind one quiet `More ▾` toggle; the toggle and section
  self-remove when no secondary content exists.
- Content hierarchy communicates card mode directly: no retrieval-state
  badges, captions, or dashboard metadata.
- Keyboard shortcuts on the back: `F` toggles full-card furigana
  (`.furigana-mode`), `T` reveals the translation (opening More first);
  shortcuts never fire in inputs/contentEditable.
- Every circular audio button has an `aria-label`; replay source is a
  **sibling** `.raw-audio-source` (never inside `<button>`, never
  `display:none`); playback delegates to the native replay link; re-tap is
  debounced; `playCircularAudio` starts with `resetAudioState`; no `new
  Audio()`, no `is-paused` remnants, no `div`-inside-`button`.
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
- Compactor hide rules all scoped to `.primary-definition`; the full
  extended definition (`.extended-full` inside More) stays untouched.
- Word-mode swap rules exist and never touch `.listening-view`; the
  listening-view is inert until `.listening-mode` activates it.
- `:focus-visible` indicators and `prefers-reduced-motion` present.
- Accent color is reserved for target highlighting and interactive
  states; no per-content-type semantic color palette (no `--freq-*`).

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
