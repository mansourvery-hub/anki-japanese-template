# Yūkei scenic-band — export for local implementation

Everything needed to implement the approved design (Round 7 — Fuji peak
above a cloud sea, back card only) in your actual repo.

```
HANDOFF_YUKEI.md                     ← give this whole file to your agent to start
docs/adr/005-scenic-band-yukei.md    ← decision record: why, what was rejected
design/YUKEI_DESIGN_SPEC.md          ← full spec: tokens, anatomy, a11y, perf
snippets/back-template-scenic-band.html   ← paste into Card 1 - Back.template.anki
snippets/front-template-wash.html         ← optional, deliberately lower priority
snippets/yukei.css                        ← paste into Card 1 - Style.css
```

**No image assets.** The whole design is inline SVG + CSS — no `.png`/`.svg`
files to add to Anki's media collection, no extra weight in the `.apkg`.

## Fastest path

1. Drop this whole folder into your repo root (or anywhere your agent can
   read it — paths inside the docs are relative to your repo root, e.g.
   `docs/adr/005-...` is meant to land in your existing `docs/adr/`).
2. Open your coding agent in the repo and paste the contents of
   `HANDOFF_YUKEI.md` as your first message.
3. Let it read the repo's own docs first (it's instructed to), then the
   three files above, then implement.

## What this is, precisely

The class names, field names (`{{Frequency}}`, `{{furigana}}`, etc.), JS
function names, and CSS token names referenced throughout were read
directly from your actual `Card 1 - Back.template.anki`,
`Card 1 - Front.template.anki`, and `Card 1 - Style.css` (via the repomix
export you gave me earlier in this conversation) — not invented. That said,
per your own `AGENTS.md`, the live repo is the source of truth, not this
export; the handoff prompt tells the agent that explicitly.

## What changed since the last round you approved

Only the *size* of the scenic band (~65% smaller, cropped to peak + cloud
sea instead of full landscape). Everything else — palette, motion, the
hard separation between decoration and reading surface — is what you saw
in the last preview artifact.
