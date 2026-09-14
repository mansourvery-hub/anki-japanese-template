# ADR 001 — Mature Word Mode interval retrieval

Date: 2026-09 (records the as-built decision).

## Context

Anti-overlearning requires the front to show only the Expression once a
card is mature (interval ≥ `LONG_INTERVAL_DAYS`). No `{{Interval}}` marker
exists, and new fields / add-ons / review-time Python are all rejected.

## Options considered

1. Bake the interval into a field at mining time — stale the next day.
2. Guess the card id from the URL — no stable id is exposed.
3. Single live-read path for both platforms — mobile has no AnkiConnect and
   the refused fetch surfaces as `Failed to load 'downloadfile.bin'`.
4. **Platform-exclusive live read (chosen).**

## Decision

Desktop reads AnkiConnect only (`guiCurrentCard`→`cardsInfo` reads the
**exact current card's** interval; `findCards` content-search fallback exists
only for the Browse previewer where no active review is available). Mobile
reads the AnkiDroid JS bridge only (`ankiGetCardInterval()`, both constructor
and direct shapes, stub guard, timeouts, short late-injection poll). Listening
fronts skip all retrieval. Any failure degrades to the sentence front behind
an anti-flash gate.

### Exact current-card vs best-effort preview fallback

These two paths are deliberately distinct and never conflated:

- **Exact current-card retrieval (authoritative, review path):** desktop
  `guiCurrentCard` → `cardsInfo`; mobile `ankiGetCardInterval()`. The review
  path never depends on heuristic content matching when exact identity is
  available. A guard confirms the returned card's Expression matches the DOM
  before trusting its interval, so a review-flow race cannot leak another
  duplicate card's interval.
- **Best-effort preview fallback:** only when no active review exists
  (browser/preview). Content matching discriminates by Expression → Sentence →
  cloze-body. If ambiguity remains after all discriminators, it fails safely
  to the sentence front — candidate 0 is never arbitrarily selected.

## Consequences

Preview screens without a bridge correctly show the sentence front. Two
platform paths must both be covered by `test_templates.py` §8b and the
duplicate-card fallback behavior by `tests/test_mature_content.py` on every
change.
