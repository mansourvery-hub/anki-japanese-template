# IMPLEMENTATION_PLAN.md — task graph + status

The graph is part of the plan (not a substitute): the graph says *what
depends on what*, the task entries say *what each node means*. This is a
task/slice graph, not a todo list (`Build frontend` would not qualify).

## Dependency graph

```text
                    ┌───────────────────┐
                    │ T1 fields bootstrap│
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
            ┌───────────────┐   ┌───────────────┐
            │ T2 front modes │   │ T3 back grid  │
            └───────┬───────┘   └───────┬───────┘
                    │                   │
                    ↓                   ↓
            ┌───────────────┐   ┌───────────────┐
            │ T4 mature mode │   │ T5 compactor  │
            └───────┬───────┘   └───────┬───────┘
                    │                   │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ T6 audio/lightbox │
                    └─────────┬─────────┘
                              │
                              ↓
                    ┌───────────────────┐
                    │ T7 responsive/    │
                    │ themes/density    │
                    └─────────┬─────────┘
                              │
                              ↓
                    ┌───────────────────┐
                    │ T8 verify gate +  │
                    │ regression tests  │
                    └─────────┬─────────┘
                              │
                              ↓
                    ┌───────────────────┐
                    │ T9 release loop   │
                    │ (sync/export/tag) │
                    └─────────┬─────────┘
                              │
                              ↓
                    ┌───────────────────┐
                    │ T10 methodology   │
                    │ refactor (this)   │
                    └─────────┬─────────┘
                              │
                              ↓
                    ┌───────────────────┐
                    │ T11 empty-field   │
                    │ collapse          │
                    └───────────────────┘
```

Dependencies: `T1 → {T2, T3} → {T4, T5} → T6 → T7 → T8 → T9 → T10 → T11`.
T2/T3 are parallelizable; T4 needs T2; T5 needs T3.

## Tasks

- **T1 — Field bootstrap.** `fetch_anki_fields.py` + gitignored
  `.anki_fields.json`; agents read exact names per session. Status: COMPLETE.
- **T2 — Front modes.** Sentence/Expression, listening button,
  Frequency-legacy path, fallback, cloze-trio rebuild. Status: COMPLETE.
- **T3 — Back grid.** Tags, word header, sentence/translation/context, side
  column, footer; DOM-reuse-safe controllers. Status: COMPLETE.
- **T4 — Mature Word Mode.** `LONG_INTERVAL_DAYS` gate, platform-exclusive
  interval retrieval, fallbacks, anti-flash reveal. Status: COMPLETE.
- **T5 — Definition Compactor + truncator.** CSS §6b structural scoping +
  §6c 3-line one-way expand. Status: COMPLETE.
- **T6 — Audio + lightbox.** Native delegation, debounce, sibling source;
  backdrop/`Escape` close. Status: COMPLETE.
- **T7 — Responsive/themes/density.** Clamps, container queries + fallback,
  zero-reflow ruby, Tokyo Night / Aki Paper, backdrop, reduced motion.
  Status: COMPLETE.
- **T8 — Verify gate + regression tests.** `verify`, `test_compactor.py`,
  `test_templates.py`, `test_layout.py`, CI. Status: COMPLETE (this refactor
  introduces `verify` + CI; suites pre-exist).
- **T9 — Release loop.** `sync_to_anki.py` (pre-sync snapshots),
  `release_apkg.py` (`exportPackage`), `finish.sh` one-command flow, apkg as
  Release asset only. Status: COMPLETE.
- **T10 — Methodology refactor.** Adopt PRODUCT/MVP/ARCHITECTURE/QUALITY/
  TEST_STRATEGY/PLAN + slim AGENTS.md + `verify`/CI without changing card
  behavior. Status: COMPLETE (`./verify` 129/129 green; released with this
  commit).
- **T11 — Empty-field collapse.** QUALITY rule + `:has()` shell guards +
  degenerate-content self-removal + enclosure parser test (§10). Turns the
  standing conditional coverage into a total, mechanically enforced
  guarantee. Status: COMPLETE (`./verify` 135/135 green; released with this
  commit).

## Roadmap (evolution loop input, not committed scope)

- R1: extra compactor fixtures if Yomitan markup drifts.
- R2: further density tuning only with layout-probe proof.
- R3: new ADRs only for decisions with alternatives + consequences.

## State updates

Mark a task COMPLETE only after targeted checks + `./verify` + (for
template/CSS changes) the `finish.sh` release run. Update technical docs
only when something actually changed — no churn.
