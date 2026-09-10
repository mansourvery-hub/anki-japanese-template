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

HTML conditionals select the mode; JS finalizes it at render time:

```text
Definition / Extended definition? ──yes──→ sentence-display
        │ no
Frequency (legacy)? ──yes──→ sentence-display (never audio)
        │ no
Sentence Audio? ──yes──→ listening-view (large 文 button)
        │ no
sentence-display fallback (Sentence → Expression)
        │
cloze fixup: Sentence has no <b> AND cloze trio complete?
        │ yes → prefix + <b>body</b> + suffix
        │
Mature check (not listening, Expression non-empty,
              interval ≥ LONG_INTERVAL_DAYS=365)?
        │ yes → .word-mode: front-word-display only
        │ no  → sentence front (also the universal fallback)
```

Interval retrieval is **platform-exclusive**: mobile uses only the AnkiDroid
bridge (`ankiGetCardInterval()`, constructor + direct shapes, stub guard,
timeouts, 700 ms late-injection poll); desktop uses only AnkiConnect
(`guiCurrentCard`→`cardsInfo`, `findCards` content-search fallback for the
Browse previewer, 500 ms fetch timeout). Anti-flash gate
(`visibility:hidden` → reveal, 1200 ms safety cap); blank sentence blocks
are removed after the cloze fixup. See `docs/adr/001-*`.

### Back (`Card 1 - Back.template.anki`)

Single grid, content-driven height:

```text
tags-container (sticky)
card-container
 └── back-grid (1 col mobile; 2 col desktop via container + media queries)
      ├── main-content: word-header (word-display-row + definition-box)
      │                 sentence-block (sentence-japanese + translation + context)
      └── side-content: picture-block · kanji notes · notes · extended accordion
      └── source-footer
```

JS controllers (all idempotent under WebView DOM re-use): tags renderer,
native-only circular audio (`playCircularAudio` → sibling replay link click,
re-tap debounce, ring pulse), frequency visualizer (tier → bar + stars;
badge removed when the rank is unparseable), definition truncator (blank
boxes removed, then measure → `.is-truncated` → one-way `.is-expanded`),
lightbox (backdrop-click / `Escape` close, alt preserved).

### Style (`Card 1 - Style.css`)

Numbered sections are the contract: §1 tokens/themes, §2 containers, §3
tags, §4 grid + desktop overrides, §5 front type, §5b word-mode swap, §6
header/meta/definition, **§6b Definition Compactor** (first dictionary, ≤2
senses, no appendices, `.primary-definition`-scoped), §6c truncator (3-line
cap + fade + chevron), §7 audio rings, §8 sentence/translation, §9
zero-reflow ruby, §10 media/lightbox, §11 accordion/footer, §12 listening,
§13 mobile, §14 deletable Fuji backdrop, §15 reduced motion.

### Tooling

```text
fetch_anki_fields.py → .anki_fields.json (gitignored, read-only dump)
sync_to_anki.py      → snapshot backups/<ts>/, push Front/Back/CSS
release_apkg.py      → exportPackage deck → dist/*.apkg (gitignored)
verify               → local quality gate (tests only, no side effects)
finish.sh            → verify → stamp → sync → export → commit → push → release
tests/               → test_compactor.py + test_templates.py + test_layout.py
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
