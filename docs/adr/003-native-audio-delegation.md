# ADR 003 — Native-only audio

*Supersedes the 2026-09 "circular button + sibling replay link" delegation
design (previously recorded here).*

## Context

Audio (`文` / `言葉`) must play on Desktop and AnkiDroid. The earlier design
shipped custom circular buttons that delegated clicks to a hidden sibling
replay link (`.raw-audio-source` + `playCircularAudio` + re-tap debounce +
SVG playback-indicator ring).

## Problem with the delegation design

The custom layer carried real cost for behaviour it never owned:

- invalid-HTML pitfalls (link inside `<button>`) and `display:none` quirks
  (breaks programmatic `.click()` on some WebViews);
- a JS controller (`playCircularAudio` / `resetAudioState` /
  `currentActiveBtn`) that duplicated state Anki already tracks;
- an SVG progress ring that could only *suggest* playback (native audio
  cannot be paused or measured), i.e. chrome without authority;
- per-side markup with hand-numbered `playsound:a:N` indices that Anki
  re-numbers whenever fields change.

## Decision

**Render the audio field itself and ship no custom audio machinery.**

- `{{Word Audio}}` / `{{Sentence Audio}}` render inside their own
  conditionals; Anki collects the `[sound:...]` tags and renders its own
  replay links (or autoplays per user settings).
- The template only *styles* the rendered control (`.native-audio` spans,
  `.native-audio-link` on the tag-listening front — the link itself is the
  button).
- No `playCircularAudio`, no `resetAudioState`, no ring, no hidden sibling
  source, no constructed filenames, no `new Audio()`.

## Consequences

- Playback behaviour (debounce, autoplay, replay) is Anki's, consistently
  on Desktop and AnkiDroid.
- Audio markup is field-conditional; the `.audio-row` shell collapses via
  `:has(.native-audio)` when a card has no audio.
- Contract pinned by `test_templates.py` §§2–3 (no controller remnants,
  native field rendering, `:has()` collapse guard).
