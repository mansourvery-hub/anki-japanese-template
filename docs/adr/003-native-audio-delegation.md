# ADR 003 — Native-only audio delegation

## Context

Custom circular buttons (`文` / `言葉`) must play audio on Desktop and
AnkiDroid without overlapping playback.

## Options considered

1. HTML5 `new Audio(filename)` — AnkiDroid render links carry no usable
   filename (old builds emit `playsound:q:0`), causing bogus-file loads.
2. Nest the replay link inside `<button>` — invalid HTML, Android WebView
   mishandles taps.
3. **`playCircularAudio` delegating to the sibling native replay link
   (chosen).**

## Decision

The `.raw-audio-source` span lives **outside** the button, visually hidden
but kept in layout (never `display:none`, which breaks programmatic
`.click()`). Every play path resets state first; re-taps on the playing
button are ignored (native audio can't be stopped); the ring is a decorative
pulse.

## Consequences

No filenames are ever constructed in JS. Markup/JS contract is pinned by
`test_templates.py` §§2–3b.
