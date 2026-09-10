# ADR 002 — Definition Compactor as structural CSS

## Context

Yomitan mines the full multi-dictionary gloss into `Definition`, far too
verbose for the main card, while `Extended definition` must stay complete.

## Options considered

1. Trim at mining time (Yomitan settings/handlers) — fragile per-dictionary,
   lost on re-mine.
2. Trim in JS at render time — flash of full text, more failure modes.
3. **Structural CSS hiding (chosen).**

## Decision

CSS §6b collapses to the first dictionary, ≤2 senses, no appendices, matched
on structure (`data-sc-*`, glossary lists) — never dictionary names — and
scoped strictly to `.primary-definition`.

## Consequences

Dictionary-agnostic and flash-free; Yomitan markup drift is caught by
`test_compactor.py` fixtures taken from real mined cards.
