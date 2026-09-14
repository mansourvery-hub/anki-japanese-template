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

Desktop reads AnkiConnect only (`guiCurrentCard`→`cardsInfo` — the **exact
current review card**; `findCards` content-search is a best-effort
**heuristic fallback** for the Browse previewer only, using Sentence then
cloze-body as discriminators, never picking candidate 0 blindly, failing
safely on ambiguity). Mobile reads the AnkiDroid JS bridge only
(`ankiGetCardInterval()`, both constructor and direct shapes, stub guard,
timeouts, short late-injection poll). Listening fronts skip all retrieval.
Any failure degrades to the sentence front behind an anti-flash gate.

## Consequences

Preview screens without a bridge correctly show the sentence front. Two
platform paths must both be covered by `test_templates.py` §8b and
`test_mature_content.py` on every change. The content-search fallback is
heuristic, not authoritative — it distinguishes exact-card retrieval (the
primary path) from best-effort preview fallback.
