#!/usr/bin/env bash
# =============================================================================
# finish.sh — single-command post-change routine.
#
# Run this at the end of ANY template change instead of remembering 5 steps:
#   ./finish.sh "<commit message>"
#
# It executes, in order:
#   1. sync_to_anki.py   — push templates+CSS into Anki via Anki-Connect
#   2. release_apkg.py   — export sample deck to dist/*.apkg via Anki-Connect
#   3. git commit        — stage everything (incl. chat_history log) & commit
#   4. git push          — push to origin/main
#   5. GitHub release    — auto-bump patch tag (v1.x.y) and upload the apkg
#
# Any failure stops the chain with a clear message (set -e). Requires: Anki
# running with Anki-Connect, gh CLI authenticated.
# =============================================================================
set -euo pipefail

cd "$(dirname "$0")"

COMMIT_MSG="${1:?Usage: ./finish.sh \"<commit message>\"}"

echo "==> [1/5] Syncing templates to Anki (Anki-Connect)"
python3 sync_to_anki.py

echo "==> [2/5] Exporting sample deck to dist/"
python3 release_apkg.py

echo "==> [3/5] Committing changes"
git add -A
if git diff --cached --quiet; then
  echo "    (nothing to commit — skipping commit, release will reuse latest)"
else
  git commit -m "$COMMIT_MSG"
fi

echo "==> [4/5] Pushing to origin/main"
git push origin main

echo "==> [5/5] Creating GitHub release"
# Sync remote tags first: gh release create makes tags on the REMOTE only,
# so local tags lag behind and would produce a duplicate version bump.
git fetch origin "refs/tags/*:refs/tags/*" --quiet
# Auto-bump the patch version from the latest existing tag (v<major>.<minor>.<patch>)
LATEST_TAG="$(git tag --sort=-v:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -1 || true)"
if [ -z "$LATEST_TAG" ]; then
  NEW_TAG="v1.0.1"
else
  NEW_TAG="$(python3 - "$LATEST_TAG" <<'PY'
import sys
major, minor, patch = sys.argv[1][1:].split(".")
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
