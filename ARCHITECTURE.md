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
listening decision; async JS finalizes Mature Word Mode:

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
Interval retrieval is **platform-exclusive**: mobile uses
only the AnkiDroid bridge (`ankiGetCardInterval()`, constructor + direct
shapes, stub guard, timeouts, 700 ms late-injection poll); desktop uses
only AnkiConnect (`guiCurrentCard`→`cardsInfo`, `findCards`
content-search fallback for the Browse previewer — no `note:` clause,
`{{Type}}` is not the model name, 500 ms fetch timeout). Anti-flash gate
(`visibility:hidden` → reveal, 1200 ms safety cap); blank sentence
blocks are removed after the cloze fixup. See `docs/adr/001-*`.

### Back (`Card 1 - Back.template.anki`)

Single quiet column with typography-driven hierarchy:

```text
card-container
 ├── word-display (target + furigana hover — hero element)
 ├── .pitch-quiet (muted supplement to the reading)
 ├── definition-box.primary-definition (compacted §6b, 3-line §6c)
 ├── .audio-row (文/言葉 native-delegating buttons, :has() empty guard)
 ├── .context-grid (sentence + picture; row on wide screens, stacked on phones)
 ├── .more-section (hidden) + .more-toggle "More ▾"
 │    └── translation (click/T) · context · kanji notes · notes · full
 │        extended definition (.extended-full — compactor never touches it)
 └── .source-footer
```

JS controllers (all idempotent under WebView DOM re-use): More toggle (one-way reveal;
section+button self-remove when secondary content is absent),
native-only circular audio (`playCircularAudio` → sibling replay link
click, re-tap debounce, ring pulse), definition truncator (blank boxes
removed, then measure → `.is-truncated` → one-way `.is-expanded`),
lightbox (backdrop-click / `Escape` close, alt preserved), back-only
keyboard shortcuts (`F` full-card furigana, `T` translation reveal).

### Style (`Card 1 - Style.css`)

Numbered sections are the contract: §1 tokens/themes (no `--freq-*`:
accent is reserved for the target and interactive states), §2 containers,
§3 More toggle, §4 context grid + desktop overrides, §5 front type,
§5b word-mode swap, §6 back hierarchy (word/pitch/audio), **§6b Definition Compactor**
(first dictionary, ≤2 senses, no appendices, `.primary-definition`-scoped),
§6c truncator (3-line cap + fade + chevron), §7 audio rings,
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
finish.sh            → verify → stamp → sync → export → commit → push → release
tests/               → test_compactor.py + test_templates.py
                        + test_front_modes.py + test_layout.py
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
