# 🎴 Japanese Anki Note Template (Ergonomic & Responsive)

A modern, ultra-compact Japanese sentence-mining note type for Anki. Built for full-screen use on **Desktop (Arch Linux, Qt6)** and **Mobile (AnkiDroid, small screens)**.

---

## 🎥 Demo

[Screencast_20260903_034628.webm](https://github.com/user-attachments/assets/c3021cdb-7cfd-4cb1-b1a7-ff52a990e305)

---

## ✨ Features

- **🌙 Dual themes** — Tokyo Night dark (default) and Aki Paper light, following Anki's Night Mode.
- **📱 Fluid responsive layout** — `clamp()` sizing with no breakpoints jumps; 2-column dashboard on desktop, 1-column on phones; container queries with a media-query fallback for old WebViews.
- **🔤 Zero-reflow furigana** — hidden by default, revealed on hover (desktop) / tap (mobile) via absolute ruby positioning; surrounding text never shifts.
- **🔊 Circular audio buttons** (`文` sentence, `言葉` word) — always delegate to Anki's native replay link (never HTML5 audio), with re-tap debounce so audio can't overlap on AnkiDroid.
- **📊 Frequency & pitch badges** — frequency rank rendered as a tiered bar + 5-star scale (Top 500 → Rare); pitch accent pill.
- **🖼️ Lightbox** — tap any image for a full-screen overlay; closes on backdrop click or <kbd>Escape</kbd>.
- **👁️ Click-to-reveal translation**, sticky tags bar, decorative Fuji backdrop (CSS §14, delete the block to remove it), `prefers-reduced-motion` support.

---

## 🃏 Front Card Modes

| Situation | Front shows |
| :--- | :--- |
| Definition present | Sentence (or Expression if no Sentence) |
| No definitions, but `Frequency` set (legacy cards) | Usual sentence — never the audio button |
| No definitions, no Frequency, `Sentence Audio` set | Listening-mode audio button |
| Nothing available | Sentence / Expression fallback |
| Sentence has no bold term + cloze trio complete | Rebuilt `prefix + `<b>`body`</b>` + suffix`, styled identically to a Yomitan sentence |
| Review interval ≥ 365 days | Word only (Mature Word Mode, see below) |

**Cloze fallback** (jidoushio mobile exports): when `Sentence` lacks its `<b>` target word, JS rebuilds it from `cloze-prefix` / `cloze-body` / `cloze-suffix` — but only if all three are non-empty, otherwise the sentence is kept as-is.

**Mature Word Mode** (anti-overlearning): old cards stop testing the word and start testing sentence recognition, so at `interval ≥ LONG_INTERVAL_DAYS` (default `365`, one constant in `Card 1 - Front.template.anki`) the front shows only the `Expression`. The interval is read live at render time — AnkiConnect (`guiCurrentCard` → `cardsInfo`, with a `findCards` content-search fallback for the Browse previewer) on desktop, the AnkiDroid JS API on mobile. Any failure degrades to the normal sentence front; listening cards are never touched; an anti-flash gate keeps the card hidden until the decision is made (500 ms fetch timeout, 1200 ms reveal cap).

---

## 📖 Back Card

- **Definition Compactor** (CSS §6b): the Yomitan glossary is trimmed to the first dictionary, max 2 senses, no appendices (possible forms, synonyms, supplementary notes, accent numbers). Extended-definition accordion stays full.
- **Definition Truncator** (CSS §6c): 4-line cap with progressive fade + small `▼`; click expands and stays open. Short glosses never show the chevron.
- Word header (furigana, badges, audio), sentence + translation toggle, picture / kanji / general notes, source footer.

---

## 🗂️ Fields

Fields are managed **exclusively inside the Anki UI** — the repo keeps no static list. For the live names + descriptions, run:

```bash
python3 fetch_anki_fields.py   # dumps gitignored .anki_fields.json
```

Current set (20): `Expression`, `Definition`, `Kanji Notes`, `Source`, `Sentence`, `Sentence (furigana)`, `Sentence Audio`, `Translation`, `Picture`, `context`, `Notes`, `Word Audio`, `Pitch Accent`, `furigana`, `reading`, `cloze-prefix`, `cloze-body`, `cloze-suffix`, `Frequency`, `Extended definition`. Yomitan-mining compatible.

---

## 🚀 Installation

**Option 1 — Quick install (recommended):** download `anki-japanese-template.apkg` from [Releases](https://github.com/mansourvery-hub/anki-japanese-template/releases), import via **File → Import**, then delete the sample cards (the note type is retained).

**Option 2 — Sync from source** (needs Anki + [Anki-Connect](https://ankiweb.net/shared/info/2055492159), Python 3 stdlib only):
```bash
git clone https://github.com/mansourvery-hub/anki-japanese-template.git
cd anki-japanese-template
python3 sync_to_anki.py    # snapshots live state to backups/, then pushes Front/Back/CSS
python3 release_apkg.py    # exports sample deck to dist/*.apkg
```

**Option 3 — Manual:** paste `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, and `Card 1 - Style.css` into the card template editor (**Tools → Manage Note Types → Cards**).

---

## 🛠️ Project Structure

```
├── Card 1 - Front.template.anki   # Front HTML: modes, cloze fallback, Mature Word Mode
├── Card 1 - Back.template.anki    # Back HTML: header, definition, sentence, side column
├── Card 1 - Style.css             # Themes, layout, compactor (§6b), truncator (§6c)
├── fetch_anki_fields.py           # Read-only dump of live Anki fields (see above)
├── sync_to_anki.py                # Push templates/CSS to Anki (pre-sync backup)
├── release_apkg.py                # Export sample deck to dist/*.apkg
├── finish.sh                      # One command: tests + sync + export + commit + push + release
├── tests/                         # test_compactor.py + test_templates.py (run by finish.sh)
├── chat_history/                  # Archived agent prompts
├── dist/                          # Exported .apkg (gitignored, GitHub Release asset)
├── backups/                       # Pre-sync Anki snapshots (gitignored)
├── AGENTS.md                      # Agent operating rules
└── README.md                      # This file
```

---

## 🔄 Development Workflow

Edit the local `.template.anki` / `.css` files (never inside Anki's UI), then run one command:

```bash
./finish.sh "scope: what changed"
# --local: sync + export + commit only · --minor: bump v1.x.0 · --prompt "text": archive prompt
```

This runs tests, syncs to Anki, exports the apkg, commits, pushes, and publishes a tagged release. `tests/` covers the compactor selectors and template invariants (furigana ban on front, audio/lightbox semantics, balanced conditionals, Mature Mode + cloze + truncator rules).

---

Built with Opencode and Gemini CLI. MIT License.
