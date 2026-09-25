# Yūkei scenic-band — export for local implementation

Everything needed to implement the approved design — illustrated fallback
(ADR 005) plus the photo-derived band and picture-field consolidation
(ADR 006) — as one implementation pass.

```
HANDOFF_YUKEI.md                          ← give this whole file to your agent to start
docs/adr/005-scenic-band-yukei.md         ← decision record: the band itself, why compact, what was rejected
docs/adr/006-photo-derived-scenic-band.md ← decision record: photo pipeline fix + dropping the old thumbnail
design/YUKEI_DESIGN_SPEC.md               ← full spec — §1–8 is ADR 005, §9 is the ADR 006 amendment
snippets/back-template-scenic-band.html   ← paste into Card 1 - Back.template.anki (insert + one removal)
snippets/front-template-wash.html         ← optional, deliberately lower priority, unchanged by ADR 006
snippets/yukei.css                        ← paste into Card 1 - Style.css
```

**No image assets.** The whole thing is inline SVG + CSS filters/blend
modes on your existing `{{Picture}}` field — nothing new added to Anki's
media collection.

## Fastest path

1. Drop this whole folder into your repo root.
2. Open your coding agent in the repo and paste the contents of
   `HANDOFF_YUKEI.md` as your first message.
3. Let it read the repo's own docs first, then these four files, then
   implement.

## What changed since the last round

Two things, both already folded into the snippets — you don't need to
apply an "005 version" and then a separate "006 version":

1. **The photo pipeline was actually broken, not just untuned.** The first
   attempt converted every image to grayscale and repainted it with one
   fixed color at 92% opacity, so every card looked the same regardless of
   its actual picture. Fixed: color is now kept (muted via `saturate()`,
   never deleted via `grayscale()`), and the theme tint is a much gentler
   `overlay` blend. Final constants (16px blur, 0.8 saturation, 0.25 tint,
   0.25 wash) came from testing against real frames, not guesses.
2. **The old inline picture thumbnail in `.context-grid` is gone.** The
   photo now lives only in the scenic band, and clicking the band opens
   the exact same lightbox the old thumbnail used to — reusing
   `openLightbox` completely unmodified.

## What this is, precisely

Class names, field names, JS function signatures, and CSS tokens
referenced throughout were read directly from your actual
`Card 1 - Back.template.anki` and `Card 1 - Style.css` (via the repomix
export you gave earlier in this conversation) — not invented. Per your own
`AGENTS.md`, the live repo is still the source of truth over this export;
`HANDOFF_YUKEI.md` says so explicitly.
