# ADR 001 — Mature Word Mode interval retrieval

Date: 2026-09 (records the as-built decision; amended after the
AnkiDroid "downloadfile.bin" debugging — the live reviewer read was
removed in favour of a fallback-only content search).

## Context

Anti-overlearning requires the front to show only the Expression once a
card is mature (interval ≥ `LONG_INTERVAL_DAYS`). No `{{Interval}}` marker
exists, and new fields / add-ons / review-time Python are all rejected.

## Options considered

1. Bake the interval into a field at mining time — stale the next day.
2. Guess the card id from the URL — no stable id is exposed.
3. Live read during review (`guiCurrentCard`→`cardsInfo`) on desktop,
   content-search fallback for the previewer — was the original design,
   **removed**: `guiCurrentCard` only works during active review, it
   duplicated a second retrieval path for marginal identity gain, and the
   associated debugging cycle repeatedly resurfaced AnkiDroid false
   media-load errors.
4. Mobile read via the AnkiDroid JS API (`ankiGetCardInterval()`) — calls
   can surface natively as false `Card Content Error: Failed to load ''`
   media warnings in the reviewer, even when wrapped in try/catch. Not
   reliable from a card template.
5. **Desktop-only fallback content search (chosen).**

## Decision

Desktop resolves the interval via a single AnkiConnect **content search**:
`findCards` by Expression, then Sentence and cloze-body discriminators
narrow to exactly one candidate (never candidate 0 blindly; ambiguity
fails safely to the sentence front). Reviewer and Browse previewer share
this one identical path. The `post` helper **UA-guards every AnkiConnect
call before any fetch**: on Android/iOS it rejects immediately, so mobile
makes no network request at all — Mature Word Mode is intentionally
disabled there and the ordinary sentence front is shown. Listening fronts
skip all retrieval. Any failure degrades to the sentence front behind an
anti-flash gate.

## Consequences

Mature Word Mode is a desktop-only presentation feature; on Android users
see the normal sentence front. This is an accepted reliability trade-off —
the reviewer must never surface false media-load errors. On desktop the
mode is heuristic: duplicate mined sentences that survive both
discriminators stay on the sentence front instead of guessing. The
content-search path is covered by `test_templates.py` §8b and
`test_mature_content.py` on every change.
