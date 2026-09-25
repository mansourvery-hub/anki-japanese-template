# HANDOFF — Yūkei (夕景) scenic band: illustration + photo mode + picture consolidation

You are implementing one visual component in two layered decisions
(ADR 005, then ADR 006 on top of it) as a single pass. This is
**presentation-only**: no field changes beyond how `Picture` is displayed,
no changes to Mature Word Mode / listening / audio delegation / the
definition compactor / the translation toggle / `openLightbox` itself. If
implementing this seems to require touching any of those systems, stop and
re-read `design/YUKEI_DESIGN_SPEC.md` §5 and §9 — it shouldn't, and if it
genuinely does, something here is stale relative to the current repo and
is worth flagging before proceeding.

> **Read order first:** `PRODUCT.md` + `MVP.md` → `ARCHITECTURE.md` →
> `QUALITY.md` + `TEST_STRATEGY.md` → `IMPLEMENTATION_PLAN.md` → `AGENTS.md`
> (repo's own order) — **then**, in this order:
> 1. `docs/adr/005-scenic-band-yukei.md` — the band's existence, sizing,
>    the illustrated fallback
> 2. `docs/adr/006-photo-derived-scenic-band.md` — the photo pipeline and
>    why the old picture thumbnail is removed
> 3. `design/YUKEI_DESIGN_SPEC.md` — full spec, read §9 especially closely,
>    it's the amendment layer on top of §1–8
> 4. `snippets/` — the literal CSS and HTML to apply (already merged/final;
>    you do not need to apply an "005 version" and then a separate "006
>    version" — the snippets as given already reflect both decisions
>    together)
>
> Then, per `AGENTS.md` rule 0: run `python3 fetch_anki_fields.py` and read
> the gitignored `.anki_fields.json` before touching either template file.

## What this handoff is (and isn't) based on

Iterated in a separate design-review conversation against a `repomix`
snapshot of this repo, including a live back-and-forth where a first
version of the photo pipeline was tested against real images and found to
be actually broken (not just untuned — see ADR 006). The field names,
class names, JS function signatures (`openLightbox(target)` specifically),
and CSS tokens quoted throughout were read directly from that snapshot's
`Card 1 - Back.template.anki` and `Card 1 - Style.css` — not invented. Per
`AGENTS.md` rule 1, the **live repo is still the source of truth** over
this handoff if anything has drifted.

## What to build

1. **Tokens** — merge `yukei.css` §1a–1c (ADR 005 color/sizing tokens,
   unchanged) and §1d (ADR 006: `--scenic-blur`, `--scenic-sat`,
   `--scenic-tint`, `--scenic-wash`) into `Style.css` §1.

2. **Component CSS** — append `yukei.css` §3 (illustrated fallback) and §4
   (photo mode) as one new section.

3. **Two integration edits to existing rules**:
   - `overflow: hidden` on `.back-card .card-container` (ADR 005).
   - Add `.scenic-photo-trigger` to the existing shared `:focus-visible`
     selector group alongside `.circular-audio-btn` and `.translation-box`
     (ADR 006) — don't write a new rule, extend the existing one.

4. **HTML, part A** — insert the `{{#Picture}}...{{^Picture}}...{{/Picture}}`
   block from `back-template-scenic-band.html` as the first child of
   `.card-container`, before `.hero-header`.

5. **HTML, part B** — remove the old `{{#Picture}}<div class="context-picture">...`
   block from inside `.context-grid` (right after `.context-main`). Exact
   block to delete is quoted verbatim in the snippet file. Leave
   `.context-main` and everything else in `.context-grid` untouched.

6. **Front card** — still not in scope. `front-template-wash.html` remains
   optional/lower-priority per ADR 005; nothing about ADR 006 changes that
   assessment.

## Do NOT do

- Don't reintroduce `grayscale()` + `mix-blend-mode: color` for the photo
  tint — that combination is the specific bug ADR 006 fixes (it replaces
  100% of the source image's color with one fixed hue). Use `saturate()` +
  `mix-blend-mode: overlay` as given.
- Don't delete `.context-grid:has(.context-picture)` or
  `.picture-container` CSS rules in this pass, even though they're now
  dead code. `test_templates.py` asserts on their presence (see ADR 006
  "Consequences"); removing them requires updating that test in the same
  commit, which is out of scope here.
- Don't modify `openLightbox` itself. The consolidation works specifically
  *because* that function clones `img.src`/`alt` into a fresh element
  rather than the styled one — that behavior is what makes the lightbox
  show the unblurred original. If you find yourself wanting to change
  `openLightbox` to make this work, stop — it already works as-is.
- Don't add a second `{{Picture}}` reference anywhere. It should appear
  exactly once in the whole back template, inside the scenic band.
- Don't add JavaScript. Still zero new JS in this change.
- Don't touch `.hero-header`, `.frequency-badge`, `.pitch-quiet`,
  `.word-display`, `.card-separator`/`.sep-motif`, `.definition-box`,
  `.translation-box`, `.more-section`, or any function in the back
  template's `<script>` block other than the two `:focus-visible` and
  `overflow` edits explicitly listed above.
- Don't implement the front sliver in this pass.

## Verification

- Run the existing suite first, unmodified, confirm green baseline.
- After implementing: `./verify`, then a real Anki desktop review session,
  both themes, checking:
  - A card **with** a Picture: scenic band shows the photo treatment;
    clicking it opens the lightbox with the full-quality original (not a
    blurred version); keyboard `Tab` to it + `Enter` does the same;
    `Escape` and backdrop-click both still close it exactly as before.
  - A card **without** a Picture: scenic band shows the Fuji/cloud-sea
    fallback, is not focusable, has no click handler.
  - `.context-grid` on a Picture card no longer shows the old inline
    thumbnail, and `.context-main` (the sentence) reads correctly at full
    width.
  - `prefers-reduced-motion: reduce` still stops the fallback's twinkle/
    glow/drift animations (photo mode has no animation to disable).
- If AnkiDroid is available: repeat the with-Picture check there
  specifically — this is the one part of the change touching real,
  variable-sized image data rather than fixed vector shapes, worth
  confirming on the actual target hardware.
- Spot-check the tuned constants (`16px` blur, `0.8` saturation, `0.25`/
  `0.25` tint/wash) against a few real Night-mode frames — they were only
  tuned in Sunset. If dark frames look wrong, split the four constants
  per-theme the same way the color tokens already are, rather than forcing
  one set of numbers to fit both.

## Release

Same as always, one command:

```bash
./finish.sh --prompt "<paste this handoff's originating user prompt>" "visual: photo-derived scenic band + retire inline picture thumbnail (ADR 005 + 006)"
```

`--local` if you want sync + export + commit only, per `AGENTS.md` §2.
