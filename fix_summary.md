## Task Completed: Fix false "Card Content Error: Failed to load ''" on AnkiDroid

### Problem
- On AnkiDroid 2.24.0, Mature Word Mode requested the card interval through
  the AnkiDroid JS API (`AnkiDroidJS` → `ankiGetCardInterval()` →
  `/jsapi/cardInterval`).
- AnkiDroid routes WebView resource/load errors through its media-error
  handler, so those calls surfaced natively as
  `Card Content Error: Failed to load ''` in the reviewer.
- The error is native/WebView-side, not a catchable JS exception: try/catch,
  `Promise.catch()`, timeouts, and stub detection could not reliably prevent
  it.

### Solution Implemented
- Removed the entire mobile interval-retrieval path from
  `Card 1 - Front.template.anki`: no `AnkiDroidJS`, no
  `ankiGetCardInterval`, no `/jsapi/` request, no bridge helpers, no polling.
- Mature Word Mode is now **desktop-only** via AnkiConnect
  (`guiCurrentCard` → `cardsInfo`).
- On Android/mobile the template deliberately makes no interval request:
  interval stays `null`, so `wordMode` is `false` and the ordinary sentence
  front is shown (graceful degradation).

### Verification Results
- `./verify`: all suites green.
- Static search confirms no executable AnkiDroid JS API code remains in the
  front template; external `AnkiDroidJS` hits are only in gitignored
  `backups/`.

### Impact
- Eliminates the false media error at its source (the request is never made).
- Desktop Mature Word Mode is unchanged and fully functional.
- No visual, audio, listening, cloze, or layout behavior changes.