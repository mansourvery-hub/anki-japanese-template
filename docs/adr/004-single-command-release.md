# ADR 004 — Single-command release with pre-sync snapshots

## Context

Multi-step endings (test → sync → export → commit → push → release) were
dropped late in sessions when run manually.

## Decision

`finish.sh` runs the full chain and stops on first failure; `./verify` is
the side-effect-free subset it delegates to. `sync_to_anki.py` snapshots the
live Anki state to `backups/<timestamp>/` (microsecond stamps) before
overwriting and aborts on empty live state. `release_apkg.py` uses the only
verified export action (`exportPackage`) into gitignored `dist/`; the apkg
ships as a GitHub Release asset, never in the repo. No-op runs never publish.

## Consequences

One command to remember; snapshots make Anki-side overwrites recoverable;
tag, tree, and live templates agree (CSS header is stamped before sync).
