# Yūkei (夕景) — scenic band design spec

Companion to `docs/adr/005-scenic-band-yukei.md`. That ADR says *why* and
*what*; this document says *exactly how*, at implementation detail. It
assumes the reader has `Card 1 - Back.template.anki`,
`Card 1 - Front.template.anki`, and `Card 1 - Style.css` open.

Six rounds of visual exploration preceded this — see "Rejected directions"
at the end if a future agent is tempted to reintroduce one of them; each was
tried and specifically rejected, not merely unconsidered.

## 1. Core principle

**Decoration that must be looked at and content that must be read never
occupy the same visual layer.** The scenic band is 100% decorative, never
contains a field value, is `aria-hidden="true"`, and sits in its own block
above `.hero-header` with a hard visual seam between it and everything
else. Nothing about the reading surface below it changes.

## 2. Anatomy

```
.card-wrapper.back-card
  .card-container            (existing — add overflow:hidden, see §5)
    .scenic-band             (NEW — first child, back card only)
      svg.scenic-svg
        <defs> softEdge filter </defs>
        stars (×3, .scenic-star)
        glow (sun/moon, .scenic-glow + inner solid circle)
        fuji peak path (.scenic-fuji, filter: softEdge)
        snow-cap path (.scenic-snow, filter: softEdge)
        cloud layer, far (.scenic-cloud.is-far)
        cloud layer, near (.scenic-cloud.is-near)
        seam path (fills to var(--card-bg) / var(--bg-color), see §5)
    .hero-header              (existing, untouched)
    ...everything else (existing, untouched)
```

## 3. Tokens (add to `Card 1 - Style.css` §1)

Add alongside the existing custom properties, following the exact same
three-block pattern already in use (`:root` = dark defaults, then the two
theme overrides). Reuse existing tokens wherever the semantics match —
only genuinely new colors get new names.

| Token | `:root` (dark default) | Aki Paper (light override) | Notes |
|---|---|---|---|
| `--scenic-sky` | `linear-gradient(180deg,#171a33 0%,#23274a 42%,#33284f 72%,#402b46 100%)` | `linear-gradient(180deg,#f6c69b 0%,#f0a08a 42%,#d98a95 72%,#b8879c 100%)` | night vs sunset |
| `--scenic-fuji` | `#100e1c` | `#5b4a6b` | mountain silhouette |
| `--scenic-snow` | `#d8d3e8` | `#fbeadf` | snow-cap highlight |
| `--scenic-cloud` | `#2c2f52` | `#fbe7d8` | cloud sea |
| `--scenic-star-op` | `.8` | `0` | stars invisible in daylight |
| `--scenic-band-h` | `clamp(44px, 12.5vw, 58px)` | *(same, not theme-dependent)* | put once in `:root` only |

Do **not** add a new accent token — the glow reuses `var(--accent-color)`,
which already flips between `#e07a5f` (dark) and `#b84a39` (light)
correctly via the existing rules.

Add the identical dark values again inside `.card.nightMode, .card.night_mode`
for the four theme-dependent rows, matching how every other token in that
block is handled (explicit, not just inherited from `:root`).

## 4. The component CSS

See `snippets/yukei.css` for the literal block to paste in — this section
just explains the non-obvious parts:

- **Sizing**: `.scenic-band { height: var(--scenic-band-h); }`. This is
  deliberately a fixed-height band, not aspect-ratio-based — on a phone
  card that's ~65% smaller than the first full-landscape draft, and it's
  the single biggest lever if it still feels like too much space; shrink
  the clamp values, not the illustration detail.
- **The SVG uses `viewBox="0 0 400 60"` with `preserveAspectRatio="none"`**
  so it stretches to fill whatever width the card renders at (desktop
  Qt6 vs. AnkiDroid phone) without letterboxing.
- **`filter: url(#softEdge)`** is applied to exactly two shapes (the Fuji
  path and the snow-cap path) — a small-scale `feTurbulence` +
  `feDisplacementMap` (scale ≈ 2.6) that softens the vector edge just
  enough to not look like clip art, without the cost of applying it
  everywhere. Do not apply it to more shapes without re-checking paint
  cost on-device.
- **Animations** (`twinkle`, `breathe`, `driftSlow`) are slow on purpose
  (4.5s–240s) — nothing is timed to draw the eye mid-recall. All three are
  disabled under `@media (prefers-reduced-motion: reduce)`.
- **The bottom "seam"**: a wavy path filled with the *panel* background
  color (`var(--card-bg)` inside `.back-card .card-container`, matching
  whatever the surrounding content sits on) sits as the last element in
  the SVG, at the very bottom of the viewBox, creating a soft horizon-line
  cutoff into the panel below instead of a hard rectangular edge.

## 5. Integration changes to existing rules

Two small, additive edits to existing selectors — not rewrites:

1. `.back-card .card-container` needs `overflow: hidden` added. Without it,
   `.scenic-band`'s square top corners will visibly poke past the
   container's existing `border-radius: var(--border-radius-lg)` in both
   themes. This is the only change to an existing rule's *behavior*;
   everything else is purely additive.
2. `.scenic-band` itself needs matching top corners
   (`border-radius: var(--border-radius-lg) var(--border-radius-lg) 0 0`)
   as a belt-and-suspenders match for #1, in case `overflow: hidden`
   interacts with something else already relying on overflow being visible
   (the lightbox does not — it's appended to `document.body`, not clipped
   by any ancestor — but verify).

Nothing else in the existing 1600+ lines of CSS needs to change. In
particular: **do not** touch `.hero-header`, `.frequency-badge`,
`.pitch-quiet`, `.word-display`, `.card-separator`/`.sep-motif`,
`.definition-box`, `.context-grid`, `.translation-box`, or `.more-section`.
They were not the problem being solved here.

## 6. Front card — optional, explicitly lower priority

A thin (`clamp(14px, 4.2vw, 20px)`) flat gradient sliver
(`linear-gradient(180deg, var(--scenic-sky-flat), var(--bg-color))`) at the
very top of the front, for visual continuity with the back, was prototyped
and works. **Recommendation: skip it unless explicitly asked for.**

Reasons this is lower priority, not just "nice to have":

- `HANDOFF.md` documents a real, previously-shipped regression where a
  front-visual change caused **every front to render blank** in real
  AnkiDroid review (not caught by the headless suite). The front has a
  documented history of being the highest-blast-radius surface in this
  codebase for exactly this class of change.
- PRODUCT.md's front contract is "pure retrieval surface" — the sliver adds
  zero retrieval value, purely branding/continuity.
- The back-only change already fully answers the actual product ask.

If it's implemented anyway: it must be tested in a real Anki desktop review
session **and** real AnkiDroid, per `HANDOFF.md`'s explicit warning, not
just `./verify`'s headless suite.

## 7. Accessibility & performance checklist

- [ ] `.scenic-band` and its SVG are `aria-hidden="true"`; no `alt` text
      needed since nothing informational is conveyed.
- [ ] All three animations respect `prefers-reduced-motion: reduce`.
- [ ] No new color combination introduces a text-on-background contrast
      issue — the band never has text on it, so this should be moot, but
      confirm no field can be conditionally rendered into it later without
      re-checking contrast.
- [ ] Confirm on real AnkiDroid (Galaxy A50 baseline per AGENTS.md), not
      just desktop Qt6 WebEngine, that the `feTurbulence`/`feDisplacementMap`
      filter doesn't introduce visible jank on card flip.
- [ ] Confirm `overflow: hidden` on `.card-container` doesn't clip anything
      that currently relies on overflowing (spot-check the lightbox and any
      focus-ring/outline that might extend past the box on keyboard focus).

## 8. Rejected directions (for context, not to be revisited casually)

1. **Ink/paper texture (sumi-e wash, torn-paper edges)** — too abstract to
   read as "Japan" to a general learner; competed with legibility when
   placed near/behind text.
2. **Kintsugi gold-seam framing** — same issue: elegant in isolation,
   didn't register as unmistakably Japanese at a glance, and the "frame
   within a frame" cost real padding on mobile.
3. **Ukiyo-e flat color blocking** — read as a generic academic/history
   template once built, despite being historically well-grounded.
4. **Oversized-kanji poster watermark** — same "template" problem; big pale
   glyphs behind content are a common presentation-software trope and
   didn't read as bespoke or as specifically Japanese.
5. **Full landscape scene (Fuji + torii + foreground leaves + floating
   embers) at full size** — visually the strongest of all the drafts, but
   too large a share of the mobile viewport. The current cropped version
   is a direct descendant of this one, not a different concept.

If the product direction changes enough that one of these is worth
revisiting, treat it as a new decision (new ADR), not a silent CSS edit.

## 9. Amendment — photo mode (ADR 006)

Everything above still holds for cards with no `Picture` (the fallback).
For cards that have one, the band's content changes; read
`docs/adr/006-photo-derived-scenic-band.md` for the full decision. Summary
of what's different from everything written above:

- The band's background is now derived from that specific card's own
  `Picture` field — a frame from the exact timestamp the sentence was
  mined — instead of always showing the same Fuji illustration.
- **The technique is deliberately not canvas-based.** `{{Picture}}` is
  rendered as a plain `<img>`, styled with CSS `filter`
  (`saturate`/`contrast`/`brightness`/`blur`) and `mix-blend-mode`
  (`overlay`, tinting toward `--accent-color`). No pixel data is ever read
  by JS, so there is no cross-origin/"tainted canvas" question to even
  ask.
- **First attempt at this was actually broken, not just too strong**:
  `grayscale(1)` + `mix-blend-mode: color` at 92% opacity is a full hue
  replacement — it throws away the source image's real color entirely,
  which is why every test frame came out looking identical. The fix keeps
  color (`saturate()` instead of `grayscale()`) and uses the much gentler
  `overlay` blend for the tint. This is a correctness fix, not a taste
  preference — do not reintroduce `grayscale()` + `mix-blend-mode: color`
  for this component.
- Final tuned constants (`--scenic-blur: 16px`, `--scenic-sat: 0.8`,
  `--scenic-tint: 0.25`, `--scenic-wash: 0.25`) came from testing against
  real mined frames, not arbitrary defaults — see `snippets/yukei.css` §1d.
  They were tuned in Sunset (light) theme only; spot-check a handful of
  real frames in Night mode too before treating them as final for both.
- **The old inline picture thumbnail is gone.** `.context-picture` /
  `.picture-container` are removed from `.context-grid` entirely — the
  photo now lives only in the scenic band. Click-to-expand is preserved by
  making the scenic band's photo layer itself the `openLightbox` trigger
  (see `snippets/back-template-scenic-band.html`). This works without any
  change to `openLightbox` because that function clones `img.src`/`alt`
  into a fresh, unstyled `<img>` — the lightbox always shows the original
  full-quality frame, never the blurred on-card version.
- The resulting dead CSS (`.context-grid:has(.context-picture)` and
  `.picture-container` rules) is left in place on purpose — see ADR 006's
  "Consequences" for the `test_templates.py` dependency that makes this
  the safer choice for this change specifically.
