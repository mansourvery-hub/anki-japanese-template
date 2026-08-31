- # Project Architecture & Rules
- **Environment:** Arch Linux, Anki-Connect (127.0.0.1:8765), Python 3.
  **Goal:** Modern, responsive Japanese Anki note type. 
  **Core Files:** `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, `Card 1 - Style.css`, `sync_anki.py`.
- ## Operational Rules
- Never modify `sync_anki.py` during HTML/CSS editing tasks.
  Read `@JapNoteType.json` whenever you need the name of the fields.  
- The use of scripts should be minimal (no script is acceptable), you better have a very good reason for a script
- in general the code should be filled with high signal comments explaining what each part does and behaves
- The code should be crystal clear for any other agent reading it in the futre but also for a good human programmer
- After modifying the local files,  a small python script to talk to anki connect and update the note template in question directly is required
## Git & Safety Rules
- Always check `git status` before editing template files.
- Ask permission or automatically run `git add . && git commit` before applying broad structural refactorings.
