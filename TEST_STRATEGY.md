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
| Minimal redesign: no tags bar / frequency badges; More collapse; state label; F/T shortcuts; listening resolver wiring | `tests/test_templates.py` §§6b–6c |
| `:focus-visible`, reduced motion, content-driven sizing, context-grid fallback, clamp() authority, no JS font override | `tests/test_templates.py` §§6–7 |
| Mature Word Mode: const, platform-exclusive retrieval, no `note:` clause, stub/timeout/fallback rules, anti-flash gate, word-mode CSS | `tests/test_templates.py` §8b |
| Stdlib-only sync, microsecond backups, finish.sh no-op guard | `tests/test_templates.py` §9 |
| Content-driven height, no h-overflow, furigana containment, type hierarchy, 3-line clamp + one-way expand, listening target size, context grid, More collapsed by default, footer containment | `tests/test_layout.py` — headless Chrome on the **real** stylesheet; skipped gracefully when Chrome is absent |
| Listening resolver behavior: classic audio-only fields and `#listening` tag activate the audio front; gloss/no-tag, no-audio, and Frequency-legacy shapes keep the sentence front | `tests/test_front_modes.py` — extracts the real resolver from the front template and runs 6 state harnesses in headless Chrome; skipped gracefully when Chrome is absent |
| Clean-environment pass, no forgotten files/deps | CI (`.github/workflows/verify.yml`) runs `./verify` |
| Every UI element collapses when its field is empty | `tests/test_templates.py` §10 — conditional-enclosure parser over Front/Back, `:has()` shell-guard checks, JS self-removal checks |

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
- `test_front_modes.py`: headless Chrome if present, else skip (pass).
- `test_layout.py`: headless Chrome if present, else skip (pass).
