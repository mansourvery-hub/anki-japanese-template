#!/usr/bin/env bash
# =============================================================================
# finish.sh — single-command post-change routine.
#
# Run this at the end of ANY template change instead of remembering 5 steps:
#   ./finish.sh "<commit message>"
#
# Flags:
#   --local          Review mode: sync + export + commit only. Skips push and
#                    GitHub release. Use while iterating; finish the batch with
#                    a full run (no flag) to publish.
#   --minor          Bump the MINOR version segment (v1.x.0) instead of the
#                    patch segment. Use for multi-feature releases.
#   --prompt "text"  Append the user prompt to chat_history/opencode_prompts.txt
#                    BEFORE anything else runs (AGENTS.md rule 3), so the log
#                    lands in the same commit.
#
# It executes, in order:
#   0. compactor tests — verify the Definition Compactor CSS selectors
#                        (skipped silently when tests/ is absent)
#   1. sync_to_anki.py — push templates+CSS into Anki via Anki-Connect
#                        (also snapshots live Anki state into backups/)
#   2. release_apkg.py — export sample deck to dist/*.apkg via Anki-Connect
#   3. git commit     — stage everything (incl. chat_history log) & commit
#   4. git push       — push to origin/main              (skipped with --local)
#   5. GitHub release — auto-bump tag (v1.x.y) + apkg   (skipped with --local)
#
# Any failure stops the chain with a clear message (set -e). Requires: Anki
# running with Anki-Connect, gh CLI authenticated (full mode only).
# =============================================================================
set -euo pipefail

cd "$(dirname "$0")"

# ---------- flag parsing ----------
LOCAL=0
BUMP_KIND=patch
PROMPT_TEXT=""
COMMIT_MSG=""

while [ $# -gt 0 ]; do
  case "$1" in
    --local)  LOCAL=1 ;;
    --minor)  BUMP_KIND=minor ;;
    --prompt) shift; PROMPT_TEXT="${1:?--prompt requires a text argument}" ;;
    -h|--help)
      sed -n '2,30p' "$0"; exit 0 ;;
    *)
      if [ -z "$COMMIT_MSG" ]; then
        COMMIT_MSG="$1"
      else
        echo "ERROR: unexpected extra argument: $1 (commit message already set)" >&2
        exit 1
      fi ;;
  esac
  shift
done

[ -n "$COMMIT_MSG" ] || { echo 'Usage: ./finish.sh "<commit message>" [--local] [--minor] [--prompt "text"]' >&2; exit 1; }

# ---------- optional prompt archiving (before anything else) ----------
if [ -n "$PROMPT_TEXT" ]; then
  printf '\n---\n\n%s\n' "$PROMPT_TEXT" >> chat_history/opencode_prompts.txt
  echo "    (prompt archived to chat_history/opencode_prompts.txt)"
fi

# ---------- step 0: compactor regression tests ----------
if [ -d tests ]; then
  echo "==> [0/5] Running compactor tests"
  python3 tests/test_compactor.py
fi

echo "==> [1/5] Syncing templates to Anki (Anki-Connect)"
python3 sync_to_anki.py

echo "==> [2/5] Exporting sample deck to dist/"
python3 release_apkg.py

echo "==> [3/5] Committing changes"
git add -A
CHANGED=0
if git diff --cached --quiet; then
  echo "    (nothing to commit)"
else
  git commit -m "$COMMIT_MSG"
  CHANGED=1
fi

if [ "$LOCAL" -eq 1 ]; then
  echo ""
  echo "Local run complete (synced, exported, committed)."
  exit 0
fi

if [ "$CHANGED" -eq 0 ]; then
  echo "    No changes detected. Nothing to push or release."
  exit 0
fi

echo "==> [4/5] Pushing to origin/main"
git push origin main

echo "==> [5/5] Creating GitHub release"
# Sync remote tags first: gh release create makes tags on the REMOTE only,
# so local tags lag behind and would produce a duplicate version bump.
git fetch origin "refs/tags/*:refs/tags/*" --quiet
# Auto-bump version from the latest existing tag (v<major>.<minor>.<patch>)
LATEST_TAG="$(git tag --sort=-v:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -1 || true)"
if [ -z "$LATEST_TAG" ]; then
  NEW_TAG="v1.0.1"
else
  NEW_TAG="$(python3 - "$LATEST_TAG" "$BUMP_KIND" <<'PY'
import sys
major, minor, patch = sys.argv[1][1:].split(".")
if sys.argv[2] == "minor":
    print(f"v{major}.{int(minor) + 1}.0")
else:
    print(f"v{major}.{minor}.{int(patch) + 1}")
PY
)"
fi
NOTES="Automated release from commit: $COMMIT_MSG

Install: import the .apkg in Anki, then delete the sample cards — the note type is retained."
gh release create "$NEW_TAG" dist/anki-japanese-template.apkg \
  --title "$NEW_TAG" \
  --notes "$NOTES" \
  --latest

echo ""
echo "All done: synced, exported, committed, pushed, released as $NEW_TAG"
