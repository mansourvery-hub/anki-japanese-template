# MVP.md — current scope

`PRODUCT.md` answers *what is this product?* This file answers *what are we
actually building right now?* Agents must not independently widen this scope
while coding.

## MVP goal

A shippable, review-ready Japanese sentence-mining note type: dense on
desktop, usable on a small phone, with sentence/word/listening fronts, a
compact informative back, and a one-command sync → export → release loop.

## Core user journey(s)

1. Import the release `.apkg` → review mined cards daily on desktop and phone.
2. Mature cards automatically test the word, not the memorized sentence.
3. Edit templates/CSS locally → `./finish.sh` → cards updated in Anki and a
   new tagged release published.

## Included capabilities

- Front: sentence / Expression fallback, listening-mode audio button,
  Frequency-legacy sentence path, cloze-trio rebuild, Mature Word Mode
  (interval-gated, platform-exclusive retrieval, sentence fallback).
- Back: sticky tags, word + furigana header, frequency/pitch badges, native
  circular audio, Definition Compactor (CSS §6b), 3-line truncator with
  one-way expand (§6c), sentence + translation toggle, picture lightbox,
  kanji/general notes, extended-definition accordion, source footer.
- Styling: Tokyo Night + Aki Paper themes, fluid clamps, container-query
  2-column grid with media fallback, zero-reflow furigana, Fuji backdrop,
  reduced-motion support.
- Empty-field collapse everywhere: no padding, border, or margin survives an
  empty field.
- Tooling: field bootstrap (`fetch_anki_fields.py`), snapshotted sync
  (`sync_to_anki.py`), apkg export (`release_apkg.py`), `verify` gate,
  `finish.sh` release loop, regression tests.

## Excluded capabilities

- New fields, add-ons, or review-time Python.
- Additional card types or note types.
- Cloud sync / collaboration / analytics.
- Mandatory per-project doc/diagram checklists beyond `ARCHITECTURE.md`.

## Acceptance criteria

- `./verify` passes (compactor + template invariants; layout checks when
  Chrome is present).
- A real user can complete: import → review sentence card → review mature
  word card → review listening card → expand definition/translation/image →
  edit locally → `./finish.sh` → updated cards + tagged release.
- No horizontal overflow, no viewport-fill dead space, furigana never shifts
  layout, audio never overlaps, failures always degrade to the sentence front.

## Known limitations

- Mature interval needs AnkiConnect (desktop) or the AnkiDroid reviewer
  bridge; Browse/template previews without a bridge correctly fall back to
  the sentence front.
- AnkiDroid fragment-reviewer stub bridges (`signal:jsapi`) are detected and
  never invoked.
- Headless layout checks skip gracefully when Chrome is absent.

## Deferred features

- Further density passes beyond the current clamp/container-query system.
- Additional AnkiDroid bridge capabilities (beyond interval read).
- Extra dictionaries/markup variants beyond current compactor fixtures.
- Any `docs/adr/` entries beyond decided items (added only when a decision
  has alternatives + consequences + long-term relevance).
