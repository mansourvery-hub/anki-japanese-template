# ADR 005 — Scenic band component (Yūkei)

## Context

The back card's visual language was functionally strong (PRODUCT.md hierarchy)
but read as generic — no visual signal that this is specifically a Japanese
study tool. Multiple decorative directions were explored (ink/paper texture,
kintsugi gold-seam framing, ukiyo-e flat color blocking, oversized-kanji
poster treatment, torn-paper ink-bleed) and rejected for one of two opposite
failure modes: either too abstract to read as "Japan" to a general learner,
or too visually busy/large to sit near content that must stay fast to parse
during active recall.

## Options considered

1. Texture/motif applied to or behind the existing content (ink-bleed edges,
   brush dividers, kanji watermark behind the definition, etc.) — rejected:
   anything visible during the actual read/recall moment trades legibility
   for atmosphere, and abstract motifs (ink wash, kintsugi) didn't register
   as identifiably Japanese to a non-specialist at a glance.
2. Full illustrated landscape (mountain, torii, foreground foliage, particle
   effects) as a dedicated section — rejected: at a size where the scene
   reads clearly (~120–156px), it consumed too much of the vertical budget
   on a phone screen, which PRODUCT.md already treats as the scarce resource.
3. **Compact illustrated band, structurally separate from the reading
   surface, cropped to a recognizable fragment rather than a full scene
   (chosen).**

## Decision

Add a `.scenic-band` block as the first child of `.card-container` on the
**back card only**, above `.hero-header`. It never contains text and is
`aria-hidden`, so it carries zero recall/accessibility weight — it is looked
at, never read. Composition is cropped to Mt. Fuji's snow-capped peak
breaking above a drifting cloud sea (a real, named motif — *unkai*, "sea of
clouds" — not an arbitrary crop), rendered as inline SVG, sized via a
`clamp()` token to roughly 44–58px of occupied height (≈⅓ of the first
full-scene attempt). The painted band extends 6px farther downward with an
equal negative bottom margin, using the hero's reserved furigana headroom
without increasing the card's total flow height.
Ambient motion (star twinkle, a slow breathing glow behind the sun/moon,
very slow cloud drift) is pure CSS `@keyframes`, disabled under
`prefers-reduced-motion`. Color tokens follow the existing dual-theme
pattern (`:root` defaults / `.card:not(.nightMode):not(.night_mode)` light
override / `.card.nightMode, .card.night_mode` dark) and reuse
`--accent-color` for the glow so it stays in sync with the existing theme
system rather than introducing a parallel one.

No JavaScript is added. No existing field, class, or JS hook is removed or
renamed. `.hero-header`, `.frequency-badge`, `.pitch-quiet`, `.card-separator`
(×2, per the existing `test_templates.py` invariant), `.definition-box`, and
everything below are untouched.

The front card is intentionally **not** in scope for this ADR beyond an
optional, separately-flagged hairline color accent — see
`design/YUKEI_DESIGN_SPEC.md` §6 and `HANDOFF_YUKEI.md` for why the front is
treated as higher-risk, lower-value for this change.

## Consequences

- Adds one new CSS section (~15 new custom properties + one component) and
  one new inline-SVG block in `Card 1 - Back.template.anki`. No new fields,
  no new JS, no new HTTP/font requests, no raster image assets.
- `test_templates.py` should be re-run as-is first; if any assertion counts
  the direct children of `.card-container` or asserts `.hero-header` is the
  first element inside it, that assertion needs a new sibling case added —
  do not weaken an existing assertion to make the new markup pass.
- The one filter (`feTurbulence` + `feDisplacementMap`, used at small scale
  purely to soften two silhouette edges) is the only non-trivial paint cost
  introduced. It must be checked on a real low-end AnkiDroid device
  (Galaxy A50 per AGENTS.md), not just desktop Qt6 WebEngine, before release.
  If it measurably affects flip latency, drop the filter first — the
  composition still reads fine with crisp vector edges.
- `.card-container` needs `overflow: hidden` added (or the scenic band needs
  matching top corner radius) so the new band's square corners don't poke
  past the card's existing `border-radius`. Verify visually in both themes.
