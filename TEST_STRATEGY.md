# TEST_STRATEGY.md — how QUALITY.md is mechanically verified

```text
QUALITY.md (WHAT must remain true)
  → TEST_STRATEGY.md (HOW it is verified)
    → tests / linters / headless checks / CI
```

## Layers (narrow → broad)

```text
tiny brick test → targeted suite → ./verify → CI (clean env)
```

While iterating, run the targeted suite; before declaring a task complete,
run `./verify`; CI re-runs `./verify` after every push.

## Enforcement map

| Requirement (QUALITY.md) | Enforcement |
| --- | --- |
| Compactor keeps 1st dictionary, ≤2 senses, no appendices; extended definition untouched; rules scoped to `.primary-definition` | `tests/test_compactor.py` — extracts real `display:none` rules from CSS §6b, applies to `tests/fixtures/*.html` (bs4 + soupsieve) |
| Front furigana ban; raw Sentence/Expression present | `tests/test_templates.py` §1 |
| Audio aria-labels; native-only controller; sibling replay source; debounce; restart-only | `tests/test_templates.py` §§2–3b |
| Cloze probe shape, trio gate, `<b>` rebuild, bold guard | `tests/test_templates.py` §2c |
| Lightbox backdrop-only close, dialog semantics, alt | `tests/test_templates.py` §4 |
| Balanced Anki conditionals | `tests/test_templates.py` §5 |
| `:focus-visible`, reduced motion, content-driven sizing, grid fallback, word-header guard, clamp() authority, no JS font override, frequency tiers | `tests/test_templates.py` §§6–8 |
| Mature Word Mode: const, platform-exclusive retrieval, stub/timeout/fallback rules, anti-flash gate, word-mode CSS | `tests/test_templates.py` §8b |
| Stdlib-only sync, microsecond backups, finish.sh no-op guard | `tests/test_templates.py` §9 |
| Content-driven height, no h-overflow, furigana containment, type hierarchy, 3-line clamp + one-way expand, listening target size, 2-col vs stacked grid, footer containment | `tests/test_layout.py` — headless Chrome on the **real** stylesheet; skipped gracefully when Chrome is absent |
| Clean-environment pass, no forgotten files/deps | CI (`.github/workflows/verify.yml`) runs `./verify` |

## The gate

`./verify` = the repository's complete mandatory **local** quality gate.
Side-effect free: it never touches Anki, never writes releases, never
commits. `finish.sh` step 0 delegates to it, so the gate and the release
pipeline can never disagree.

## Regression rule (inside the dev loop, not a separate phase)

```text
bug → diagnose → fix → add regression test → verify → commit
```

Every escaped bug earns a permanent test: compactor regressions → new
fixture/assertion; template/CSS regressions → new `test_templates.py`
check; layout regressions → new `test_layout.py` probe assertion.

## Dependencies

- `test_compactor.py`: `beautifulsoup4` + `soupsieve` (test-only).
- `test_templates.py`: stdlib only.
- `test_layout.py`: headless Chrome if present, else skip (pass).
