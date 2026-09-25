# ADR 006 — Photo-derived scenic band; retire the separate picture thumbnail

Builds on ADR 005 (which shipped the static Fuji/cloud-sea `.scenic-band`).
This ADR replaces that band's *content* on any card that has a `Picture`,
and removes the old inline thumbnail entirely.

## Context

`Picture` on these notes is a frame captured at the exact timestamp a
sentence was mined — not a generic stock photo. The static Fuji illustration
from ADR 005 is identical on every card; using the card's own frame instead
gives each card a genuinely unique, source-derived background instead of one
fixed graphic repeated forever. Two real constraints shaped the
implementation:

1. **No canvas, no server-side processing.** Anki templates are static
   HTML/CSS per render. The chosen technique reuses `{{Picture}}` as a plain
   `<img>` and does all abstraction via CSS `filter`/`mix-blend-mode` — no
   `getImageData`, no cross-origin/tainted-canvas risk, no new JS at all.
2. **The first version of the pipeline was wrong, not just untuned.** It
   converted the image to `grayscale(1)` and then re-painted it with
   `mix-blend-mode: color` at 92% opacity — that combination throws away
   100% of the source image's actual hue and replaces it with one fixed
   color, so every card looked identical regardless of its frame. Blur was
   also sized independently of the element (10–30px on a ~50px-tall band),
   which erased most remaining structure. Both were caught by testing
   against real frames and are fixed below.

## Decision

**Pipeline** (final, tuned interactively against real frames, values below
are the actual shipped constants, not placeholders):

- Keep the image's own color. Use `saturate()` to mute it, never
  `grayscale()`.
- `mix-blend-mode: overlay` for the theme tint, not `color` — this nudges
  hue/contrast toward `--accent-color` without replacing it.
- Tuned constants:

  | Property | Value |
  |---|---|
  | Blur | `16px` |
  | Saturation kept | `0.8` (i.e. `saturate(0.8)`) |
  | Theme tint opacity | `0.25` |
  | Paper wash opacity | `0.25` |

  These were tuned against Sunset (light) theme frames specifically; verify
  they also read correctly in Night mode with a few real dark/bright frames
  before shipping — the mechanism is identical, but no one has yet checked
  whether the same four numbers are right for both themes. If not, split
  them into per-theme values the same way the color tokens already are.

**Picture field consolidation:** the old `.context-picture`/
`.picture-container` inline thumbnail inside `.context-grid` is removed
entirely. `{{Picture}}` is now referenced exactly once, inside the scenic
band. The click-to-expand behavior is **not lost** — it moves to the scenic
band itself, reusing the existing `openLightbox(this)` function completely
unmodified. This works cleanly because `openLightbox` clones `img.src` (and
`img.alt`) into a fresh, unfiltered `<img>` for the overlay — it does not
clone CSS classes or computed styles, so the lightbox shows the original,
full-quality, non-blurred frame even though the on-card `<img>` has
`filter`/blend-mode applied to it. No change to `openLightbox` was needed
or made.

**Fallback:** cards with no `Picture` keep the ADR 005 static Fuji/cloud-sea
illustration exactly as shipped, via `{{^Picture}}`.

## Consequences

- `.context-grid` loses its `.context-picture` child on every card,
  permanently (not conditionally on some cards and not others — Picture is
  never rendered there anymore regardless of whether the field has a
  value). `.context-main` (the sentence) now runs full width in all cases.
- `.context-grid:has(.context-picture)` and
  `.context-grid:has(.context-picture) .context-main` /
  `.sentence-japanese` CSS rules become **dead code** — `.context-picture`
  no longer exists anywhere in the rendered DOM, so these selectors will
  never match again. **Recommendation: leave them in place, do not delete
  them in this change.** `test_templates.py` (per `ARCHITECTURE.md`
  §context-grid tests) asserts on the literal presence/count of
  `.context-grid:has(.context-picture) { ... align-items: flex-start }` —
  deleting the CSS without also updating that assertion will fail the
  suite for reasons unrelated to anything actually broken. Cleaning up both
  the dead CSS and the test that checks for it is reasonable future work,
  but is a separate, deliberate change — not a side effect of this one.
- `.picture-container` and its `:focus-visible`/`:hover`/sizing rules also
  become dead code for the same reason. Same recommendation: leave them.
- New interactive element needs the same keyboard-focus treatment the old
  one had: add `.scenic-photo-trigger` to the existing shared
  `:focus-visible` selector group (currently `.circular-audio-btn,
  .translation-box, .picture-container`) rather than writing a new rule
  from scratch.
- No new JS, no new fields, no change to `openLightbox`, no change to
  Mature Word Mode / audio delegation / definition compactor.
