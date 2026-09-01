# 🎴 Japanese Anki Note Template (Ergonomic & Responsive)

A modern, refined, and ergonomic Japanese sentence-mining note type for Anki. Designed for maximum screen utilization on **Desktop (Arch Linux / Windows / macOS)** and **Mobile (Samsung Galaxy A50 / Android / iOS)**.

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

- **🖼️ Lightbox Image Zoom:**
  - Click or tap any card image to view it full-screen in a hardware-accelerated frosted-glass modal overlay.
  - Close by clicking anywhere on the overlay or pressing the <kbd>Escape</kbd> key.

- **🎧 Intelligent Listening Mode & Fallback Safety:**
  - When both definition fields are absent, the card automatically enters **Listening Mode** (displaying only the audio player).
  - If a card has neither definitions nor audio files attached, it automatically displays the text fallback to prevent "soft-locked" unstudyable cards.

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

### Option A: Automatic Sync via Anki-Connect (Recommended)

1. Make sure [Anki](https://apps.ankiweb.net/) is open with the [Anki-Connect](https://ankiweb.net/shared/info/2055492159) add-on installed.
2. In your terminal, run the sync script:
   ```bash
   python3 sync_to_anki.py
   ```
3. The script will automatically update the Front Template, Back Template, and CSS styling directly inside your Anki profile.

### Option B: Manual Installation

1. In Anki, go to **Tools** $\rightarrow$ **Manage Note Types**.
2. Select or create your Japanese note type.
3. Click **Cards...**:
   - Paste the contents of `Card 1 - Front.template.anki` into **Front Template**.
   - Paste the contents of `Card 1 - Back.template.anki` into **Back Template**.
   - Paste the contents of `Card 1 - Style.css` into **Styling**.

---

## 🛠️ Project Structure

```
├── Card 1 - Front.template.anki   # Front card HTML template & dynamic scaling script
├── Card 1 - Back.template.anki    # Back card HTML template, lightbox & audio controller
├── Card 1 - Style.css             # Tokyo Night & Aki Paper CSS responsive styling
├── JapNoteType.json               # Note type schema export definition
├── sync_to_anki.py                # Python automation script communicating with Anki-Connect
└── README.md                      # Project documentation
```

---

## 🤖 Built With
This template was architected using **Opencode** as the primary agentic builder for iterative refactoring, and **Gemini CLI** for initial project scaffolding and requirements analysis.

### Model Usage Breakdown:
*   **Opencode Agent (`poolside/laguna-s-2.1:free`):** 55%
*   **Gemini CLI (`gemini-3.5-flash`):** 30%
*   **Current Agent (`google/gemini-3.1-flash-lite`):** 15%

---

## 📜 License

MIT License. Free to use, modify, and distribute for your Japanese learning journey.
