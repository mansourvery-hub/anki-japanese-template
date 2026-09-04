# 🎴 Japanese Anki Note Template (Ergonomic & Responsive)

A modern, refined, and ergonomic Japanese sentence-mining note type for Anki. Designed for maximum screen utilization on **Desktop (Arch Linux / Windows / macOS)** and **Mobile (Samsung Galaxy A50 / Android / iOS)**.

---

## 🎥 Demo in Action

[Screencast_20260903_034628.webm](https://github.com/user-attachments/assets/c3021cdb-7cfd-4cb1-b1a7-ff52a990e305)

*(Watch the template in action with zero-reflow furigana hover, circular SVG audio progress rings, click-to-expand lightbox, and fluid responsive scaling)*

---

## ✨ Features

- **🌙 Dual Theme Engine (Tokyo Night & Aki Paper):**
  - **Tokyo Night Dark (Default):** Deep Obsidian (`#0f141c`), Frosted Slate (`#182030`), and Glowing Cyan (`#38bdf8`) accents.
  - **Aki Paper Light:** Warm Cream (`#fcfaf6`), Matte White (`#ffffff`), and Deep Amber (`#d97706`) accents.
  - Automatically switches with Anki's Night Mode or your system's color scheme.

- **📱 Ergonomic Viewport & Screen Utilization:**
  - **Fluid Continuous Sizing:** Eliminates discrete layout jumps using CSS `clamp()`.
  - **Desktop 2-Column Dashboard:** Balanced two-column grid that fills 100% of widescreen desktop displays.
  - **Mobile 1-Column Layout:** Zero wasted padding and margins so complete sentences, definitions, and images fit cleanly without endless vertical scrolling.

- **🔤 Dynamic Text Scaling:**
  - Automatically inspects the length of sentences or expressions on card flip.
  - Short expressions (1–8 characters) automatically scale up (up to `6.8rem`) to prominently fill the screen.
  - Longer sentences gracefully scale down for optimal reading legibility.

- **🔊 Circular Audio Player with SVG Progress Ring:**
  - Custom circular play/pause button with centered Japanese Kanji/labels (`文` for Sentence, `言葉` for Word).
  - Dynamic SVG progress border that fills smoothly as audio plays and resets on completion.
  - Supports native HTML5 `Audio()` playback with automatic fallback to Anki replay buttons.

- **📖 Word-by-Word Furigana (Hover & Touch):**
  - Furigana is hidden by default to test raw kanji recall.
  - **Desktop:** Hover mouse over any word to reveal its furigana.
  - **Mobile:** Tap or hold any word to instantly reveal furigana without double-tap delay.

- **🖼️ Lightbox Image Expansion:**
  - Click or tap any card image to view it full-screen in a frosted-glass modal overlay.
  - Close by clicking the overlay or pressing the <kbd>Escape</kbd> key.

- **🎓 Mature-Card Word Mode (Anti-Overlearning):**
  - Cards with a review interval ≥ 365 days automatically show only the target word on the front instead of the sentence — see the [full section below](#-mature-card-word-mode-anti-overlearning) for how it works and how to configure it.

---

## 🗂️ Note Type Fields

This note type is fully compatible with **Yomitan / Yomichan** mining workflows:

| Field Index | Field Name | Description |
| :--- | :--- | :--- |
| `0` | `Expression` | Dictionary term in kanji form (used for search & deduplication). |
| `1` | `Definition` | Primary definition (bilingual or monolingual). |
| `2` | `Kanji Notes` | Kanji radicals, mnemonics, stroke order, or readings. |
| `3` | `Source` | Media source name, book title, anime episode, or URL. |
| `4` | `Sentence` | Target Japanese context sentence. |
| `5` | `Sentence (furigana)` | Sentence with inline Anki furigana notation (`漢[かん] 字[じ]`). |
| `6` | `Sentence Audio` | Audio file for the sentence (`[sound:xxx.mp3]`). |
| `7` | `Translation` | Toggleable sentence translation. |
| `8` | `Picture` | Screenshot or context image (lightbox enabled). |
| `9` | `context` | Paragraph dialogue or extended context. |
| `10` | `Notes` | Grammar explanations, nuance notes, or extra definitions. |
| `11` | `Word Audio` | Isolated term pronunciation audio (`[sound:xxx.mp3]`). |
| `12` | `Pitch Accent` | Pitch accent notation (graphs or numbers like ⓪, ①). |
| `13` | `furigana` | Term with furigana notation (`単[たん] 語[ご]`). |
| `14` | `reading` | Plain kana reading for the expression. |
| `15` | `cloze-body` | Inflected form of the term as it appeared in the sentence. |
| `16` | `Frequency` | Term frequency rank badge. |
| `17` | `Extended definition` | Full monolingual dictionary definitions (e.g. Daijirin, Koujien). |

---

## 🚀 Installation & Sync

### Option 1: Quick Install (Recommended)
1. Download the latest `anki-japanese-template.apkg` file from the [Releases](https://github.com/mansourvery-hub/anki-japanese-template/releases) page.
2. In Anki, go to **File** $\rightarrow$ **Import...** and select the `.apkg` file.
3. Once imported, you can delete the sample cards. Anki will retain the newly created Note Type, which you can now use for your own cards.

### Option 2: Automatic Sync via Anki-Connect
*Prerequisite: Clone this repository to your local machine. Only Python 3 (standard library) is needed — no `pip install` required.*
```bash
git clone https://github.com/mansourvery-hub/anki-japanese-template.git
cd anki-japanese-template
```
1. Make sure [Anki](https://apps.ankiweb.net/) is open with the [Anki-Connect](https://ankiweb.net/shared/info/2055492159) add-on installed.
2. In your terminal, run the sync script:
   ```bash
   python3 sync_to_anki.py
   ```
   The script snapshots the live Anki template state into `backups/<timestamp>/` first, then updates the Front Template, Back Template, and CSS styling directly inside your Anki profile.
3. To export the sample deck to `dist/anki-japanese-template.apkg` (for local use only — pushing and releasing happen via `finish.sh`):
   ```bash
   python3 release_apkg.py
   ```

### Option 3: Manual Installation
1. *Prerequisite: Clone this repository or copy the contents of the files.*
2. In Anki, go to **Tools** $\rightarrow$ **Manage Note Types**.
3. Select or create your Japanese note type.
4. Click **Cards...**:
   - Paste the contents of `Card 1 - Front.template.anki` into **Front Template**.
   - Paste the contents of `Card 1 - Back.template.anki` into **Back Template**.
   - Paste the contents of `Card 1 - Style.css` into **Styling**.

---

## 🛠️ Project Structure

```
├── Card 1 - Front.template.anki   # Front card HTML, dynamic scaling & Mature Word Mode (interval-gated word-only front)
├── Card 1 - Back.template.anki    # Back card HTML template, audio & lightbox scripts
├── Card 1 - Style.css             # Tokyo Night & Aki Paper CSS responsive styling
├── JapNoteType.json               # Note type schema export definition (18 fields)
├── finish.sh                      # One-command routine: tests + sync + export + commit + push + release
├── sync_to_anki.py                # Push templates to Anki via Anki-Connect (with pre-sync backup)
├── release_apkg.py                # Export sample deck to dist/*.apkg via Anki-Connect
├── tests/                         # Regression tests: compactor CSS + template invariants (run by finish.sh, stdlib only)
├── chat_history/                  # Archived AI-agent conversation logs
├── dist/                          # Exported .apkg (gitignored, released via GitHub)
├── backups/                       # Pre-sync snapshots of live Anki state (gitignored)
├── AGENTS.md                      # Operational guidelines for AI coding agents
├── Design.md                      # Original design goals
└── README.md                      # This file
```

---

## 🗜️ Definition Compaction (Yomitan Glossary)

The **Definition** field usually contains the full Yomitan-mined glossary: every dictionary entry, every numbered sense, plus appendices. On the main card this is collapsed to the essentials, purely via CSS:

- **1 dictionary entry** (the first) — later dictionaries are hidden.
- **Max 2 numbered senses** — sense 3+ hidden (structured SC dictionaries and plain gloss lists alike).
- **Appendices hidden**: possible forms (可能形), synonym lists (類語), supplementary notes (補説G), accent numbers, historical kana readings.

The full, untouched glossary is always available in the **Extended definition** accordion on the back card. Compaction is scoped exclusively to the main definition box (`.primary-definition`) — no other field is affected.

*To disable it:* remove the `6b. DEFINITION COMPACTOR` rules from `Card 1 - Style.css` and the `primary-definition` class from the Definition `<div>` in `Card 1 - Back.template.anki`. The regression suite in `tests/` verifies this behavior (plus template invariants like the front-card furigana ban) — run it with `python3 tests/test_compactor.py && python3 tests/test_templates.py` after any change.

---

## 🎓 Mature-Card Word Mode (Anti-Overlearning)

Sentence cards have a hidden failure mode: once a card is old enough, you stop retrieving the word from memory and instead recognize the *sentence* — its rhythm, its context, even its length become the retrieval cue. Anki's efficiency collapses into passive reading. **Mature Word Mode** breaks that crutch: when a card's review interval reaches a configurable threshold (default: 365 days), the front shows **only the target word**, forcing genuine word-recall. The sentence returns on the back card as usual.

### How the interval is read (no addons, no extra fields)

There is no `{{Interval}}` template marker in Anki, so the front-card script queries the interval live at render time through whichever native bridge the current platform provides:

| Platform | Mechanism | Notes |
| :--- | :--- | :--- |
| **Anki Desktop** (active review) | AnkiConnect `guiCurrentCard` → `cardsInfo` | Exact card ID of the card being reviewed. |
| **Anki Desktop** (Browse previewer) | AnkiConnect `findCards` content search on the `Expression` field → `cardsInfo` | `guiCurrentCard` only works during active review, so in the previewer the script locates the card by its own rendered content (same technique as jp-mining-note), then disambiguates duplicates by Sentence text. |
| **AnkiDroid** | AnkiDroid JS API `ankiGetCardInterval()` | Official in-template JS API (contract version `0.0.3`). |

Requirements: Anki with the [Anki-Connect](https://ankiweb.net/shared/info/2055492159) add-on on desktop (already required by this repo's sync workflow), AnkiDroid ≥ 2.18 on mobile. If the interval cannot be retrieved — AnkiConnect not running, previewer edge cases, old AnkiDroid without the JS API, JavaScript disabled — the card **always degrades gracefully to the normal sentence front**. The feature can never break a card.

### Configuration

The threshold is a single constant at the top of the front-card script in `Card 1 - Front.template.anki`:

```js
const LONG_INTERVAL_DAYS = 365;
```

Change `365` to any number of days (e.g. `180` for half-year), save, and re-run `./finish.sh` to sync. The comparison is `interval >= LONG_INTERVAL_DAYS`, so exactly 365 days triggers word mode at the default value.

### Behavior details

- **Anti-flash:** the front container starts `visibility: hidden` and is revealed only after the interval decision is made — the sentence never visibly flashes before being swapped for the word.
- **Word-only, no scaffolding:** the mature front shows the bare `Expression` (same serif typography and length-based auto-scaling as the sentence view) — no furigana, no audio buttons, no reveal-the-sentence escape hatch. The full back card is unchanged.
- **Listening-mode cards untouched:** audio-only cards (no definition fields) keep their circular audio player front.
- **Diagnostics:** every decision is logged to the console as `[Mature Word Mode] …` (source, interval, threshold, wordMode) — visible in Anki's web console / debug tools.
- **Scope:** applies only to cards of this note type; the swap is done by toggling the `word-mode` class on `.card-wrapper` (CSS section `5b. MATURE-CARD WORD MODE`).

 ---


## 🔄 Development & Synchronization Workflow

To ensure changes are tracked in Git and never overwritten accidentally, follow the **Local-First Workflow**:

1. **Edit Local Files:** Always edit `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, or `Card 1 - Style.css` directly in your code editor. *Never edit templates inside Anki's UI.*
2. **Finish (one command does everything):**
   ```bash
   ./finish.sh "style: update layout"
   ```
   This automatically: syncs templates to your Anki profile (Anki-Connect, with a safety snapshot of the live Anki state into `backups/` first), exports the sample deck *"My Life Decks::Japanese::anki-japanese-template"* to an apkg, commits, pushes to GitHub, and publishes it as a new tagged release with the apkg attached.
   
   **Flags:**
   - `--local` — sync + export + commit only (no push, no release). Use it while iterating; run without the flag to publish the batch.
   - `--minor` — bump the minor version (v1.x.0) instead of the patch version, for multi-feature releases.
   - `--prompt "text"` — archive the prompt to `chat_history/opencode_prompts.txt` before running, so it lands in the same commit.

---

## 🤖 Built With
This template was architected using **Opencode** as the primary agentic builder for iterative refactoring, and **Gemini CLI** for initial project scaffolding and requirements analysis.

### Model Usage Breakdown (Based on Token Consumption):
*   **GLM 4.7 Flash (`zai`):** 53.1%
*   **Gemini 3.1 Flash Lite (`google`):** 39.8%
*   **Gemini 3.6 Flash (`google`):** 7.1%

---

## 📜 License

MIT License. Free to use, modify, and distribute for your Japanese learning journey.
