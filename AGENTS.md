# 🤖 Agent Operational Guidelines & Architecture

This document defines the strict operational rules, architectural guidelines, and synchronization workflows for any AI coding agent working in this repository.

---

## 🎯 Project Overview & Core Goals
- **Goal:** Modern, refined, ultra-compact, ergonomic Japanese sentence-mining note type for Anki.
- **Target Environments:**
  - **Desktop:** Arch Linux (Anki Desktop Qt6 WebEngine, widescreen 100% fill).
  - **Mobile:** Samsung Galaxy A50 (AnkiDroid / WebKit, small screen, ultra-compact zero-waste vertical spacing).
- **Core Files:**
  - `Card 1 - Front.template.anki` (Front card HTML & dynamic scaling script)
  - `Card 1 - Back.template.anki` (Back card HTML, circular audio & lightbox script)
  - `Card 1 - Style.css` (Tokyo Night & Aki Paper themes, responsive clamps)
  - `JapNoteType.json` (Source of truth for all 18 note field names and configurations)
  - `finish.sh` (⭐ THE post-change routine: sync + export + commit + push + release in one command)
  - `sync_to_anki.py` (Pushes templates & styles to Anki via Anki-Connect; step 1 of finish.sh)
  - `release_apkg.py` (Exports sample deck to `dist/anki-japanese-template.apkg` via Anki-Connect `exportPackage`; step 2 of finish.sh)
  - `chat_history/` (Archived user prompts from Gemini CLI & Opencode)

## 📦 Sample Deck & Release Facts
- Release automation exports the deck **"My Life Decks::Japanese::anki-japanese-template"** via the Anki-Connect `exportPackage` action (the only verified working export action).
- The apkg is **gitignored** (`*.apkg`) — it is distributed exclusively as a **GitHub Release asset** named `anki-japanese-template.apkg`, never committed to the repo.
- Releases are git tags (`v<major>.<minor>.<patch>`); `finish.sh` auto-bumps the patch segment.

---

## 🔒 Mandatory Golden Rules for All Agents

### 1. Local Files are the Single Source of Truth
- **Never** instruct the user to edit HTML/CSS inside the Anki application UI.
- All edits must happen directly in the local `.template.anki` and `.css` files.

### 2. THE Release Workflow (one command, not five)
> **⚠ LLM failure-mode warning:** routine multi-step endings get forgotten late in a session (it already happened once). Never run the steps manually — that is how steps get dropped.

After **every** modification to the note templates/CSS, finish with exactly one command:

```bash
./finish.sh "<semantic commit message>"
```

It runs, in order, and stops on first failure:
1. `sync_to_anki.py` — push Front/Back/CSS into the live Anki profile
2. `release_apkg.py` — export the sample deck to `dist/anki-japanese-template.apkg`
3. `git add -A && git commit` — snapshot (includes the chat_history log)
4. `git push origin main`
5. `gh release create` — auto-bump patch tag and upload the apkg asset

Do not skip, reorder, or substitute steps. The user reviews cards inside Anki after this command.

### 3. Prompt Archiving
- Append every new user prompt to `chat_history/opencode_prompts.txt` **before** running `./finish.sh` (so the log is included in the same commit).
- Format: prompt text, then `---` separator on its own line.

### 4. Technical Constraints
- **Zero-Reflow Furigana:** Furigana must remain hidden by default and reveal on `:hover` (Desktop) / `:active` (Mobile) without shifting surrounding Japanese text by even a single pixel (uses absolute ruby positioning).
- **Audio Buttons:** Uses custom standalone circular SVG progress buttons (`文` for sentence, `言葉` for word). Avoid default browser audio controls.
- **Screen Real Estate:** Screen space is precious. Avoid adding useless debug badges or verbose header labels (`Sentence`, `Listening Card Active`, etc.).
- **Minimal JS Footprint:** Avoid external libraries. All scripts must be vanilla, scoped, and resilient to Anki WebView DOM re-use.
