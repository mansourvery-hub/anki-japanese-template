# 🎴 Japanese Anki Note Template (Ergonomic & Responsive)

A modern, ultra-compact Japanese sentence-mining note type for Anki. Built for dense, information-efficient review on **Desktop (Arch Linux, Qt6)** and **Mobile (AnkiDroid, small screens)**.

---

## 🎥 Demo

[Screencast_20260903_034628.webm](https://github.com/user-attachments/assets/c3021cdb-7cfd-4cb1-b1a7-ff52a990e305)

---

## ✨ Features

- **🌙 Dual themes** — Tokyo Night dark (default) and Aki Paper light, following Anki's Night Mode.
- **🔢 Minimal by design** — every visible element must justify its screen space. The front is a pure retrieval surface (just the Japanese); the back is a quiet reading interface: target → reading → meaning → context, with secondary info collapsed behind `More ▾`. Anki is the SRS — no badges, dashboards, or grading UI.
- **📱 Fluid responsive layout** — `clamp()` sizing with no breakpoint jumps; sentence + picture context grid on desktop, single column on phones; container queries with a media-query fallback for old WebViews. Cards size to their content (no forced viewport fill).
- **🔤 Zero-reflow furigana** — hidden by default, revealed on hover (desktop) / tap (mobile); **`F`** pins full-card furigana on the back. Nothing ever shifts.
- **🔊 Native audio** — `文` / `言葉` buttons and Anki's own **`R`** shortcut delegate to Anki's replay link (never HTML5 audio), with re-tap debounce so audio can't overlap on AnkiDroid.
- **👁️ On-demand secondary info** — `T` reveals the translation; `More ▾` exposes the full Yomitan definition, extra context, kanji and general notes. Quiet by default.
- **🖼️ Lightbox** — tap any image for a full-screen overlay; closes on backdrop click or <kbd>Escape</kbd>.
- **🏷️ Behavioral tags** — tags drive card behavior (e.g. `#listening` forces the listening front) and are never rendered as decoration.

---

## 🃏 Front Card Modes

The front contains ONLY the thing being tested — the sentence itself is the retrieval prompt.

| Situation | Front shows |
| :--- | :--- |
| Definition present | Sentence (or Expression if no Sentence) |
| No definitions, but `Frequency` set (legacy cards) | Usual sentence — never the audio button |
| No definitions, no Frequency, `Sentence Audio` set | Listening-mode audio button |
| Card tagged `#listening` | Listening-mode audio button (deliberate listening exercise, even with glosses) |
| Nothing available | Sentence / Expression fallback |
| Sentence has no bold term + cloze trio complete | Rebuilt `prefix + `<b>`body`</b>` + suffix`, styled identically to a Yomitan sentence |
| Review interval ≥ 365 days | Word only (Mature Word Mode, see below) |

**Cloze fallback** (jidoushio mobile exports): when `Sentence` lacks its `<b>` target word, JS rebuilds it from `cloze-prefix` / `cloze-body` / `cloze-suffix` — but only if all three are non-empty, otherwise the sentence is kept as-is.

**Mature Word Mode** (anti-overlearning): old cards stop testing the word and start testing sentence recognition, so at `interval ≥ LONG_INTERVAL_DAYS` (default `365`, one constant in `Card 1 - Front.template.anki`) the front shows only the `Expression`. The interval is read live at render time — AnkiConnect (`guiCurrentCard` → `cardsInfo`, with a `findCards` content-search fallback for the Browse previewer) on desktop, the AnkiDroid JS API on mobile. Any failure degrades to the normal sentence front; listening cards are never touched; an anti-flash gate keeps the card hidden until the decision is made (500 ms fetch timeout, 1200 ms reveal cap).

**Listening semantics**: the audio button markup is gated on `Sentence Audio` and inert until a synchronous resolver confirms the listening condition — the classic audio-only field shape OR the `#listening` tag. Every other card (and every failure path, including no-JS) keeps the sentence front.

---

## 📖 Back Card

Typography does the work — no dashboard chrome:

1. **Target + reading** — the headword with hover furigana, the largest element; pitch accent as quiet muted text.
2. **Primary meaning** — **Definition Compactor** (CSS §6b) trims the Yomitan glossary to the first dictionary, max 2 senses, no appendices; **Definition Truncator** (§6c) caps it at 3 lines with a fade + `▼`, click expands and stays open.
3. **Context** — the sentence (with hover furigana) plus the picture when present, side by side on wide screens.
4. **Secondary info** — collapsed behind a quiet `More ▾`: translation (`T`), additional context, kanji notes, general notes, and the **full extended definition** (the compactor never touches it).
5. A discreet **Context / Word / Listening** label explains the retrieval condition on hover; the source footer identifies the material.

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
├── verify                         # Local quality gate (tests only, no side effects)
├── finish.sh                      # One command: verify + sync + export + commit + push + release
├── PRODUCT.md / MVP.md            # Product intent / current scope
├── ARCHITECTURE.md + docs/adr/    # Technical structure / lasting decisions
├── QUALITY.md / TEST_STRATEGY.md  # Invariants / how they are verified
├── IMPLEMENTATION_PLAN.md         # Task graph + status
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
