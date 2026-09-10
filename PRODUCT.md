# PRODUCT.md — Japanese sentence-mining note type

Authoritative source for **what the product is supposed to do**.
Architecture, plans, and agent instructions all defer to this file.

## Problem

Yomitan sentence-mining cards are verbose and ergonomically poor out of the
box: oversized headwords, full multi-dictionary glosses, dead screen space,
clunky audio controls, and a familiar sentence that becomes the retrieval cue
once a card is mature (overlearning). Review on a small phone (Galaxy A50) is
especially wasteful.

## Target users

- Solo learner (the maintainer) mining Japanese sentences via Yomitan /
  jidoujisho into Anki.
- Review contexts: Anki Desktop Qt6 WebEngine (Arch Linux, widescreen) and
  AnkiDroid WebView (Samsung Galaxy A50, small screen).
- Installs via the released `.apkg` (GitHub Release asset), or syncs from
  source with Anki-Connect.

## Core user journeys

1. **Mine → review sentence card.** Yomitan fills Expression / Sentence /
   Definition / audio / Frequency; the front tests sentence recognition, the
   back shows word, badges, definition, sentence, translation, media, notes.
2. **Review mature card as word card.** Cards with interval ≥
   `LONG_INTERVAL_DAYS` show only the Expression on the front
   (anti-overlearning), with silent fallback to the sentence front.
3. **Review listening card.** Cards with audio but no definitions test
   recognition via a single large audio button.
4. **Expand media / definition / translation on demand.** Picture lightbox,
   3-line definition truncation with one-way expand, click-to-reveal
   translation, extended-definition accordion.
5. **Install / update.** Import the release `.apkg`, or push local
   templates/CSS to the live profile and re-export via `finish.sh`.

## Functional requirements

- Front modes (in priority order): Definition/Extended-definition →
  sentence; legacy Frequency-only → sentence; audio-only → listening button;
  otherwise sentence/Expression fallback; cloze trio rebuild when Sentence
  lacks `<b>`; mature interval-gated word-only front.
- Back: word/furigana header, frequency + pitch badges, word + sentence
  circular audio, compacted primary definition, sentence + translation +
  context, picture / kanji / general notes, extended-definition accordion,
  source footer, sticky tags bar.
- Mature Word Mode: live interval read at render time (desktop AnkiConnect
  `guiCurrentCard`→`cardsInfo` + `findCards` content-search fallback for the
  Browse previewer; mobile AnkiDroid JS API `ankiGetCardInterval()` only);
  never fetch AnkiConnect from a mobile WebView; any failure → sentence
  front; listening fronts untouched.
- Tooling: `sync_to_anki.py` pushes Front/Back/CSS with a pre-sync snapshot
  to `backups/<timestamp>/`; `release_apkg.py` exports deck
  `My Life Decks::Japanese::anki-japanese-template` via `exportPackage`;
  `finish.sh` runs tests → sync → export → commit → push → release.

## UX requirements

- Ultra-compact, content-driven height (no viewport fill, no dead space).
- Fluid `clamp()` sizing phone → 4K; 2-column back grid on desktop,
  1-column on phones (container queries + media-query fallback).
- Zero-reflow furigana (hidden, hover/tap reveal, absolute ruby).
- Native-only audio (delegate to Anki replay link, re-tap debounce, ring
  pulse — never HTML5 `Audio`).
- Dual themes (Tokyo Night dark / Aki Paper light, follows Anki Night Mode),
  decorative Fuji backdrop (deletable block), `prefers-reduced-motion`
  support, keyboard focus indicators, aria labels/roles.

## Constraints

- Vanilla JS/CSS only, scoped, resilient to Anki WebView DOM re-use.
- Fields live **exclusively in the Anki UI**; repo keeps no static field
  list (`fetch_anki_fields.py` → gitignored `.anki_fields.json` is the only
  source).
- Local `.template.anki` / `.css` files are the single source of truth —
  never edit inside the Anki UI.
- Screen real estate is precious: no debug badges or verbose header labels.
- Stdlib-only Python tooling (no third-party runtime deps; test-only deps
  allowed).

## Non-goals

- New Anki note-type fields, add-ons, or Python-at-review solutions.
- Multi-note-type theming system or generic card framework.
- Enterprise release management (solo `finish.sh` flow is enough).
- Server/cloud sync, collaboration, analytics.

## Important assumptions

- Yomitan markup shape (`.yomitan-glossary`, `data-sc-*` attributes) is
  stable enough for structural CSS scoping; drift is caught by fixtures.
- AnkiConnect on `127.0.0.1:8765` (desktop) and the AnkiDroid JS bridge
  (reviewer only) remain the interval sources; both can be absent.
- One card type ("Card 1"); model name
  `Japanese Note type (Sentence card by Default)` is stable.

## Open questions

- None blocking. Candidate evolution items live in `MVP.md` (Deferred) and
  `IMPLEMENTATION_PLAN.md` (roadmap).
