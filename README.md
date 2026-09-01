# 🎴 Japanese Anki Note Template (Ergonomic & Responsive)

A modern, refined, and ergonomic Japanese sentence-mining note type for Anki. Designed for maximum screen utilization on **Desktop (Arch Linux / Windows / macOS)** and **Mobile (Samsung Galaxy A50 / Android / iOS)**.

---

## 🎥 Demo in Action

https://github.com/mansourvery-hub/anki-japanese-template/assets/demo.webm

*(Watch the template in action with zero-reflow furigana hover, circular SVG audio progress rings, lightbox image zoom, and fluid responsive scaling)*

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

### Option 1: Quick Install (Recommended)
1. Download the latest `anki-japanese-template.apkg` file from the [Releases](https://github.com/mansourvery-hub/anki-japanese-template/releases) page.
2. In Anki, go to **File** $\rightarrow$ **Import...** and select the `.apkg` file.
3. Once imported, you can delete the sample cards. Anki will retain the newly created Note Type, which you can now use for your own cards.

### Option 2: Automatic Sync via Anki-Connect
1. Make sure [Anki](https://apps.ankiweb.net/) is open with the [Anki-Connect](https://ankiweb.net/shared/info/2055492159) add-on installed.
2. In your terminal, run the sync script:
   ```bash
   python3 sync_to_anki.py
   ```
3. The script will automatically update the Front Template, Back Template, and CSS styling directly inside your Anki profile.

### Option 3: Manual Installation
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

## 🔄 Development & Synchronization Workflow

To ensure changes are tracked in Git and never overwritten accidentally, follow the **Local-First Workflow**:

1. **Edit Local Files:** Always edit `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, or `Card 1 - Style.css` directly in your code editor. *Never edit templates inside Anki's UI.*
2. **Push to Anki:** Run `python3 sync_to_anki.py` to push changes to your active Anki collection.
3. **Commit to Git:** Save a version snapshot:
   ```bash
   git add . && git commit -m "style: update layout"
   ```
4. **Backup to GitHub:** Push your commits to GitHub:
   ```bash
   git push origin main
   ```

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
