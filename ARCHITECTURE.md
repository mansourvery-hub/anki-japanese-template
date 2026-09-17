# ARCHITECTURE.md — authoritative technical structure

Covers *how the software is structured* for the `MVP.md` scope. Additional
documents are created only where they would otherwise make this file unwieldy
or where a domain needs an independently maintained contract. Current extras:
`docs/adr/` (decisions with lasting consequences); no separate
`DATA_MODEL.md` / `API_CONTRACTS.md` / `STATE_MODEL.md` — the project is too
small to justify them.

## System map

```text
Anki note fields (live in Anki UI, never in repo)
  │  Yomitan / jidoujisho mining
  ↓
Card 1 - Front.template.anki ──→ review front (sentence / word / listening)
Card 1 - Back.template.anki  ──→ review back (grid: main + side columns)
Card 1 - Style.css           ──→ themes, layout, compactor, truncator
  │  vanilla JS (scoped, DOM-reuse safe), no libraries
  ↓
Anki renderers: Desktop Qt6 WebEngine · AnkiDroid WebView
  │  live services at render time: AnkiConnect :8765 (desktop only),
  │  AnkiDroid JS bridge (mobile reviewer only)
  ↓
Tooling (stdlib-only): fetch_anki_fields.py · sync_to_anki.py ·
                       release_apkg.py · verify · finish.sh
```

## Components

### Front (`Card 1 - Front.template.anki`)

A pure retrieval surface: only the tested Japanese renders. HTML
conditionals pick the branch; a synchronous JS resolver finalizes the
listening decision (Policy B: usable audio required); async JS finalizes
Mature Word Mode:

```text
Definition / Extended definition? ──yes──→ sentence-display (zero audio)
        │ no
Frequency (legacy)? ──yes──→ sentence-display (zero audio)
        │ no
Sentence Audio? ──yes──→ listening-view (audio-only card)
        │ no
sentence-display fallback
        │
cloze fixup: Sentence has no <b> AND cloze trio complete?
        │ yes → prefix + <b>body</b> + suffix
        │
Mature check (not listening, Expression non-empty,
              interval ≥ LONG_INTERVAL_DAYS=365)?
        │ yes → .word-mode: front-word-display only
        │ no  → sentence front (also the universal fallback)
```

Hidden behavioral probes never render visibly: the cloze trio and the
tags probe. Normal cards never evaluate `{{Sentence Audio}}` on the front,
guaranteeing zero audio autoplay and zero audio controls on normal cards.
**Listening Policy B**: `#listening` (or the legacy audio-only shape)
activates the listening front **only when usable audio exists**
(`hasUsableAudio` check on the `.raw-audio-source`). The tag-listening-view
binds to `{{Sentence Audio}}` (label 文), falling back to `{{Word Audio}}`
(label 言葉) — never the hardcoded `play:a:0`. `#listening` + no usable
audio falls back to the normal sentence front; dead/duplicate views are
removed so exactly one listening button is ever visible.
Interval retrieval is **platform-exclusive** and distinguishes
**exact-current-card** retrieval from **heuristic content-search fallback**:
- Exact card (primary): mobile uses only the AnkiDroid bridge
  (`ankiGetCardInterval()`, constructor + direct shapes, stub guard,
  timeouts, 700 ms late-injection poll); desktop uses only AnkiConnect
  (`guiCurrentCard`→`cardsInfo` — the exact current review card).
- Content-search fallback (Browse previewer only, when guiCurrentCard
  fails): `findCards` by Expression, then Sentence and cloze-body
  discriminators narrow to exactly one candidate. **Never picks candidate
  0**; if ambiguity remains, fails safely to the sentence front.
Anti-flash gate (`visibility:hidden` → reveal, 1200 ms safety cap); blank
sentence blocks are removed after the cloze fixup. The gate is
deterministic and safe: it never depends on a single async path or timer
that can be throttled. See `docs/adr/001-*`.

`:has()` is intentional architecture for empty-shell collapse (§6b, §10);
it is not removed for theoretical portability. Front template size is not
a defect — correctness is prioritized over line count.

### Back (`Card 1 - Back.template.anki`)

Single quiet column with typography-driven hierarchy:

```text
card-container
 ├── .hero-header (single row on wide: word + meta inline; stacked on phones)
 │    ├── .hero-word-wrap > .word-display (target + furigana hover — hero element)
 │    └── .word-meta-bar (freq visualizer + .pitch-quiet + .audio-row 文/言葉)
 ├── definition-box.primary-definition (compacted §6b, 3-line §6c)
 ├── .context-grid (sentence + picture; row on wide screens, stacked on phones)
 ├── .more-section (hidden) + .more-toggle "More ▾"
 │    └── translation (click/T) · context · kanji notes · notes · full
 │        extended definition (.extended-full — compactor never touches it)
 └── .source-footer
```

JS controllers (all idempotent under WebView DOM re-use): More toggle (one-way reveal;
section+button self-remove when secondary content is absent),
native-only circular audio (`playCircularAudio` → sibling replay link
click, re-tap debounce, playback indicator pulse), definition truncator (blank boxes
removed, then measure → `.is-truncated` → one-way `.is-expanded`),
lightbox (backdrop-click / `Escape` close, alt preserved), back-only
keyboard shortcuts (`F` full-card furigana, `T`/`X` translation reveal,
`C` expanded-info toggle; `R` is Anki-owned, never listed).

### Style (`Card 1 - Style.css`)

Numbered sections are the contract: §1 tokens/themes (no `--freq-*`:
accent is reserved for the target and interactive states), §2 containers,
§3 More toggle, §4 context grid + desktop overrides, §5 front type,
§5b word-mode swap, §6 back hierarchy (hero-header single row: word + meta inline
wide / stacked narrow; word/pitch/audio), **§6b Definition Compactor**
(first dictionary, ≤2 senses, no appendices, `.primary-definition`-scoped),
§6c truncator (3-line cap + fade + chevron), §7 audio rings (playback indicator, not true progress),
§8 sentence/translation + secondary blocks, §9 zero-reflow ruby +
§9b full-card furigana mode, §10 media/lightbox, §11 footer,
§12 listening (inert until `.listening-mode`), §13 mobile,
§14 deletable Fuji backdrop, §15 reduced motion.

### Tooling

```text
fetch_anki_fields.py → .anki_fields.json (gitignored, read-only dump)
sync_to_anki.py      → snapshot backups/<ts>/, push Front/Back/CSS
release_apkg.py      → exportPackage deck → dist/*.apkg (gitignored)
verify               → local quality gate (tests only, no side effects)
finish.sh            → verify → stamp → sync → export → commit → push main → release (--target main) → fetch tag
tests/               → test_compactor.py + test_templates.py
                         + test_front_modes.py + test_mature_content.py
                         + test_layout.py
```

Fields are **not** a repo artifact: the Anki UI owns them; agents bootstrap
via `fetch_anki_fields.py` every session.

## Diagrams

Produced only where prose is ambiguous. The two graphs above (front-mode
decision, back grid) are the standing set; sequence/state/entity diagrams
are omitted — no complex async choreography, state machine, or persistent
entity graph exists beyond what is shown.

## Key decisions (summaries; full records in `docs/adr/`)

- **001** Mature interval via platform-exclusive live read (no
  `{{Interval}}`, no new fields/add-ons; mobile never touches AnkiConnect).
- **002** Definition Compactor as structural CSS (dictionary-agnostic,
  `.primary-definition`-scoped; extended definition untouched).
- **003** Native-only audio delegation (no `new Audio()`; sibling replay
  link; debounce; visually-hidden-not-`display:none` source).
- **004** Single-command release (`finish.sh`; `verify` as the side-effect-free
  subset; snapshots before overwrite).

## Evolution rule

Small change → implement normally. Moderate change → update this file
(+ ADR when justified) first, then add tasks. Major change → stop feature
work, run an explicit architecture-change effort with a migration plan.
