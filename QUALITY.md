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
- Balanced `{{#field}}` / `{{^field}}` / `{{/field}}` conditionals.
- Listening cards never enter Mature Word Mode and skip all interval
  retrieval.
- Interval has no `{{Interval}}` marker: desktop AnkiConnect only,
  mobile AnkiDroid bridge only; mobile never fetches `127.0.0.1:8765`.
- Any retrieval failure degrades to the sentence front; anti-flash
  `visibility:hidden` gate with a bounded reveal cap.
- Cloze rebuild fires only when Sentence lacks `<b>`/`<strong>` **and** the
  full prefix/body/suffix trio is non-empty; rebuild uses `<b>`.
- AnkiDroid stub bridges (`signal:jsapi`) are never invoked;
  `{success:false}` never becomes an interval; numeric strings and
  JSON-encoded responses parse; bridge calls time out.

## Back invariants

- Every circular audio button has an `aria-label`; replay source is a
  **sibling** `.raw-audio-source` (never inside `<button>`, never
  `display:none`); playback delegates to the native replay link; re-tap is
  debounced; `playCircularAudio` starts with `resetAudioState`; no `new
  Audio()`, no `is-paused` remnants, no `div`-inside-`button`.
- Lightbox closes only on backdrop click (`e.target === overlay`) or
  `Escape`; overlay carries dialog semantics; cloned image preserves `alt`.
- Definition expand is one-way (never re-collapses); `.is-truncated` is set
  only on real overflow; no-JS still shows the full definition.
- Frequency badge keeps `data-freq="{{text:Frequency}}"` and the tier
  bar + stars renderer; all 5 tier theme variables exist.
- No JS font-scaler overrides CSS (`.sentence-japanese` `clamp()` is the
  sizing authority).

## CSS invariants

- Zero-reflow furigana: absolute `ruby rt`, hidden until
  `:hover`/`:active`/`:focus`.
- Content-driven card height (no `100vh`/`100dvh` fill); `container-type:
  inline-size` present; 2-column grid has a media-query fallback;
  empty `word-header` collapses via `:has()`.
- Compactor hide rules all scoped to `.primary-definition`; extended
  definition stays full.
- Word-mode swap rules exist and never touch `.listening-view`.
- `:focus-visible` indicators and `prefers-reduced-motion` present.

## Empty-field collapse (space discipline)

- Every rendered field is enclosed in an Anki `{{#field}}` conditional —
  except `Type` (element attribute, not UI), the hidden cloze-probe trio,
  and the front word probe (`display:none` default, word-mode gate only).
- Unconditionally rendered shells collapse when all conditional children are
  absent: `.audio-row` / `.word-display-row .word-meta-row` via `:has()`
  guards.
- Degenerate content removes itself instead of leaving chrome behind:
  unparseable Frequency removes its badge; blank definition/sentence blocks
  are removed (front runs after the cloze fixup, before the reveal).
- Net rule: no padding, border, or margin may survive an empty field.

## Tooling / process invariants

- Python tooling stays stdlib-only; backups use microsecond timestamps;
  snapshots happen **before** any overwrite; empty live state aborts sync.
- `finish.sh` no-op runs never publish a release.
- Every user prompt is archived to `chat_history/opencode_prompts.txt`
  before/with the commit that follows it.
