# HANDOFF — build these features on top of the reverted baseline

You are continuing on the **reverted working baseline**: commit `59ac56f`
(HEAD, tagged `v1.8.2`, CSS header `v1.7.6`). `main` == `v1.8.2` == `59ac56f`.
The repo's methodology lives in `PRODUCT.md` / `MVP.md` / `ARCHITECTURE.md` /
`QUALITY.md` / `TEST_STRATEGY.md` / `IMPLEMENTATION_PLAN.md` / `AGENTS.md`.

> **Read order first:** `PRODUCT.md` + `MVP.md` → `ARCHITECTURE.md` → `QUALITY.md`
> + `TEST_STRATEGY.md` → `IMPLEMENTATION_PLAN.md`. Then run
> `python3 fetch_anki_fields.py` (field names live in Anki, never in the repo)
> and read the gitignored `.anki_fields.json` **before any template work**.
> Run `./verify` before declaring done; release via `./finish.sh`.

## What happened before you

A previous implementation (now **reverted**) tried to add the features below
as v1.8.0/v1.8.1 but introduced a **blank front in real Anki during review**
(all cards). It was reverted. The headless test suite passed the broken
build, so the bug was environment-specific: **you cannot fully validate the
front by headless Chrome alone.** Verify the front in a REAL Anki review
session on desktop before releasing.

## Features to build (after `59ac56f`)

1. **`R` shortcut is Anki-owned, never template-owned.** Do not add or
   modify an `R` shortcut. Remove the `R` hint from the back's shortcut UI
   if present. Keep custom template shortcuts **`Z`** (furigana toggle),
   **`X`** (translation toggle), **`C`** (expanded-info toggle). Don't
   interfere with Anki's native `R` replay.

2. **Listening mode — Policy B.** `#listening` (or the legacy audio-only
   shape) activates the listening front **only when usable audio exists**.
   `#listening` + no usable audio must fall back safely to the normal
   sentence front. Never leave a dead/empty listening UI.

3. **Listening audio source bug (NEW, confirmed in the live baseline).**
   In `Card 1 - Front.template.anki`, the `tag-listening-view` audio source
   is hardcoded to
   `<a class="replay-button soundLink" href="#" onclick="...pycmd('play:a:0')...">`
   (`play:a:0` = "first audio field"). On listening cards this plays the
   **Word Audio** field instead of the intended **Sentence Audio**, even
   though the button is labelled 文 (sentence). Fix: bind the listening
   button's audio source to the actual `{{Sentence Audio}}` field, falling
   back to `{{Word Audio}}` only when Sentence Audio is absent. The label
   must match what actually plays.

4. **Audio terminology.** The native audio system is intentionally **not a
   real progress indicator**. Rename internal comments/terminology from
   "progress ring" toward **playback indicator** where practical. Do **not**
   recreate playback progress with `new Audio()`; preserve native Anki /
   AnkiDroid audio delegation (sibling replay link, re-tap debounce,
   restart-only).

5. **Front template size is not a problem.** Do not aggressively split /
   refactor the front to reduce line count. Correctness > file size.

6. **Mature Word Mode — exact current-card interval.** During review, select
   the interval of the **exact current card** (`guiCurrentCard` →
   `cardsInfo` on desktop; AnkiDroid bridge `ankiGetCardInterval()` on
   mobile). Content search (Expression → Sentence → cloze-body) is **only** a
   best-effort preview/browser fallback when exact identity is unavailable.
   If content fallback yields multiple candidates, **never pick candidate 0**
   — use Sentence and cloze-body discriminators; if ambiguity remains, fail
   safely to the normal sentence mode. Add regression tests for duplicate
   Expressions / duplicate notes.

7. **`:has()` is accepted architecture.** Do not remove or redesign `:has()`
   usage for theoretical portability.

8. **Deterministic release ordering in `finish.sh`.** Order must be:
   `verify → version stamp → sync to Anki → export apkg → commit → push main
   → create GitHub release/tag (--target main) → fetch tag`. The tag must
   point at the exact pushed release commit. Preserve the existing no-op
   (nothing-to-commit) protection.

9. **Tests** (extend the current architecture: structural + headless
   behavioral + layout + CI). Prioritize behavioral tests for:
   `#listening` without audio; `#listening` with audio; duplicate-Expression
   mature candidates; exact-current-card interval; ambiguous preview fallback
   → safe sentence mode; audio failure/reset; release-script ordering / no-op.
   Add a regression that **exactly one** listening sound button is ever
   visible (a pure `#listening` audio card renders both a tag view and a
   classic view in markup — the resolver must keep only the active one, and
   must remove every dead/duplicate view when audio/sentence is missing).

10. **Docs audit.** `QUALITY.md`, `TEST_STRATEGY.md`, `ARCHITECTURE.md`,
    `PRODUCT.md`, `README.md`, template comments, and CSS comments must
    describe the actual architecture: R is Anki-owned; `#listening` requires
    usable audio; the ring is a playback indicator; mature mode distinguishes
    exact-card retrieval from heuristic preview fallback; `:has()` is
    intentional; front size is not a defect.

## CRITICAL pitfall — do not repeat it

The reverted v1.8.x set `visibility:hidden` on `.card-container` and relied
on an async + `setTimeout` reveal. In real Anki review the async AnkiConnect
round-trip could stall, the reveal timer never fired, and **every front
rendered blank** (back card unaffected — it has no visibility gate). A
synchronous-reveal attempt was also reverted. Whatever you do:

- Keep the front reveal **deterministic and safe**: it must never depend on a
  single async path or timer that can be throttled, and it must never leave a
  blank/hung card.
- Preserve the intended anti-flash behavior for mature cards **without**
  risking a blank front.
- **Test in a real Anki review session on desktop** (and ideally AnkiDroid)
  before releasing, in addition to `./verify`. If you cannot reproduce a real
  review, say so explicitly rather than claiming it is fixed.

## Do NOT do

- No unnecessary frameworks.
- No HTML5 `Audio()` replacing native delegation.
- Don't remove `:has()` for portability.
- Don't arbitrarily pick the first duplicate card in mature mode.
- Don't add a shortcut that conflicts with Anki.
- Don't add visual UI unless it directly improves learning/retrieval.
- Don't refactor the Front just to reduce line count.

## Current test baseline

`./verify` is green on `59ac56f` (compactor 25, template invariants 99,
front-mode 15, layout 28). `tests/` = `test_compactor.py`, `test_templates.py`,
`test_front_modes.py`, `test_layout.py` (+ `test_mature_content.py` existed
only in the reverted branch and is not present on this baseline).