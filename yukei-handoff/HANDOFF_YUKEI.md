# HANDOFF — Yūkei (夕景) scenic-band visual addition

You are implementing one visual component on top of the current baseline.
This is a **presentation-only** change: no field changes, no JS behavior
changes, no changes to Mature Word Mode / listening / audio delegation /
the definition compactor / the translation toggle. If implementing this
seems to require touching any of those systems, stop and re-read
`design/YUKEI_DESIGN_SPEC.md` §5 — it almost certainly doesn't, and if it
genuinely does, that's a sign something in this handoff is stale relative
to the current repo and worth flagging before proceeding.

> **Read order first:** `PRODUCT.md` + `MVP.md` → `ARCHITECTURE.md` →
> `QUALITY.md` + `TEST_STRATEGY.md` → `IMPLEMENTATION_PLAN.md` → `AGENTS.md`
> (repo's own order) — **then** the three files that came with this
> handoff, in this order:
> 1. `docs/adr/005-scenic-band-yukei.md` — why, and what was rejected
> 2. `design/YUKEI_DESIGN_SPEC.md` — exact spec, tokens, integration points
> 3. `snippets/` — the literal CSS and HTML to apply
>
> Then, per `AGENTS.md` rule 0: run `python3 fetch_anki_fields.py` and read
> the gitignored `.anki_fields.json` before touching either template file.
> This change references zero `{{Field}}` placeholders, so field names
> shouldn't matter here — but confirm nothing in `Card 1 - Back.template.anki`
> has drifted from what's quoted in the design spec before editing it.

## What this handoff is (and isn't) based on

This design was iterated in a separate design-review conversation against
a `repomix` snapshot of this repo, not against the live repo. The exact
field names, class names, JS function names, and CSS token names quoted in
`YUKEI_DESIGN_SPEC.md` and `snippets/` were read directly from that
snapshot's `Card 1 - Back.template.anki`, `Card 1 - Front.template.anki`,
and `Card 1 - Style.css` — they are not invented or reconstructed from
memory. Treat them as accurate as of that snapshot, but **the live repo,
not this handoff, is the single source of truth** (per `AGENTS.md` rule 1)
— if anything here doesn't match what you find on disk, trust the disk and
adapt accordingly; don't force a mismatch to fit.

## What to build

1. **Tokens** — add the `--scenic-*` custom properties from `yukei.css` §1
   into the three existing token blocks in `Style.css` §1 (COLOR SYSTEM &
   CSS VARIABLES). Do not create new standalone `:root`-like blocks; merge
   into the existing ones, in the existing style.

2. **The `.scenic-band` component** — append the component CSS from
   `yukei.css` §3 as a new section at the end of `Style.css` (pick the next
   free section number; the snippet's own comment suggests §16 but check
   what's actually next).

3. **One integration edit to an existing rule** — add `overflow: hidden` to
   the existing `.back-card .card-container` rule (see `yukei.css` §2 and
   `YUKEI_DESIGN_SPEC.md` §5 for why). This is the only change to
   pre-existing CSS behavior in the whole change.

4. **The HTML fragment** — insert `snippets/back-template-scenic-band.html`
   as the first child of `.card-container` in
   `Card 1 - Back.template.anki`, before the existing `.hero-header` block.
   Exact insertion point and rationale are commented in that file.

5. **Front card** — **do not implement** `snippets/front-template-wash.html`
   unless the user explicitly asks for it in this session. Read
   `YUKEI_DESIGN_SPEC.md` §6 for why it's flagged separately: this repo has
   a documented history (`HANDOFF.md`) of a front-visual change causing a
   blank front in real AnkiDroid review, undetected by the headless suite.

## Do NOT do

- Don't add, rename, or remove any `{{Field}}` reference. This change uses
  none.
- Don't add JavaScript. The entire component is static markup + CSS
  animation; if you find yourself reaching for a `<script>` tag, stop —
  that means the spec is being misread.
- Don't touch `.hero-header`, `.frequency-badge`, `.pitch-quiet`,
  `.word-display`, `.card-separator`/`.sep-motif`, `.definition-box`,
  `.context-grid`, `.translation-box`, `.more-section`, or any JS function
  in the back template's `<script>` block. None of them are in scope.
- Don't weaken or delete an existing test assertion to make new markup
  pass (e.g. if something asserts `.card-container`'s first child or child
  count). Add a new, additive assertion instead; if that's not possible
  without touching an old one, stop and flag it rather than editing the
  old assertion to fit.
- Don't implement the front sliver in the same pass as the back change —
  see item 5 above.
- Don't apply the `feTurbulence`/`feDisplacementMap` filter to anything
  beyond the two shapes it's already scoped to in the snippet.

## Verification

- Run the existing suite first, unmodified, to confirm the baseline is
  green before you start.
- After implementing: `./verify`, then **also** open the back template in
  a real Anki desktop review session in both night mode and day mode, and
  check the top corners of the card aren't clipped oddly by the new
  `overflow: hidden`. If AnkiDroid (or an emulator) is available, check
  there too, specifically for any jank on card flip from the SVG filter —
  this is the one part of the change with a real (if small) paint cost.
- Confirm `prefers-reduced-motion: reduce` actually stops all three
  animations (twinkle, glow breathe, cloud drift) — toggle it in browser
  devtools or OS accessibility settings during the desktop check.

## Release

Same as always — one command, don't reorder or substitute steps:

```bash
./finish.sh --prompt "<paste this handoff's originating user prompt>" "visual: add Yūkei scenic band to back card (ADR 005)"
```

`--local` if you want sync + export + commit only without pushing/tagging
a release yet, per the existing convention in `AGENTS.md` §2.
