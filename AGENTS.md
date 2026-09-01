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
  - `sync_to_anki.py` (Local bridge pushing template & styles to Anki via Anki-Connect)
  - `chat_history/` (Archived user prompts from Gemini CLI & Opencode)

---

## 🔒 Mandatory Golden Rules for All Agents

### 1. Local Files are the Single Source of Truth
- **Never** instruct the user to edit HTML/CSS inside the Anki application UI.
- All edits must happen directly in the local `.template.anki` and `.css` files.

### 2. Mandatory 4-Step Release Workflow
Every single modification must strictly execute this complete sequence:
1. **Local Edit:** Apply edits to `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, or `Card 1 - Style.css`.
2. **Anki-Connect Sync:** Execute `python3 sync_to_anki.py` to push changes immediately to the local Anki profile.
3. **Git Snapshot:** Stage files and create a semantic commit (`git add . && git commit -m "..."`).
4. **GitHub Push:** Always push the commit to GitHub remote:
   ```bash
   git push origin main
   ```

### 3. Prompt Archiving
- Whenever interacting with the user, ensure new user prompts are appended to `chat_history/opencode_prompts.txt` so full development history remains transparent and backed up to GitHub.

### 4. Technical Constraints
- **Zero-Reflow Furigana:** Furigana must remain hidden by default and reveal on `:hover` (Desktop) / `:active` (Mobile) without shifting surrounding Japanese text by even a single pixel (uses absolute ruby positioning).
- **Audio Buttons:** Uses custom standalone circular SVG progress buttons (`文` for sentence, `言葉` for word). Avoid default browser audio controls.
- **Screen Real Estate:** Screen space is precious. Avoid adding useless debug badges or verbose header labels (`Sentence`, `Listening Card Active`, etc.).
- **Minimal JS Footprint:** Avoid external libraries. All scripts must be vanilla, scoped, and resilient to Anki WebView DOM re-use.
