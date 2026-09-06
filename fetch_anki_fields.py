#!/usr/bin/env python3
"""Fetch live note-type field names + descriptions from Anki (read-only).

Fields are managed EXCLUSIVELY inside the Anki UI — this repo keeps no
static field list. Agents must run this script at session start (see
AGENTS.md rule 0) and read the generated `.anki_fields.json` snapshot
instead of guessing field names.

Usage:  python3 fetch_anki_fields.py
Output: .anki_fields.json (gitignored) + the field list on stdout.

Requires: Anki running with the Anki-Connect add-on.
Standard library only (mirrors sync_to_anki.py).
"""

import json
import os
import sys
import urllib.request

# Keep in sync with sync_to_anki.py
ANKI_CONNECT_URL = "http://127.0.0.1:8765"
MODEL_NAME = "Japanese Note type (Sentence card by Default)"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(SCRIPT_DIR, ".anki_fields.json")


def _anki(action, **params):
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        data=json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"ERROR: Could not reach Anki-Connect at {ANKI_CONNECT_URL}. "
              f"Is Anki running with the add-on installed? ({e})")
        sys.exit(1)
    if result.get("error"):
        print(f"ERROR: Anki-Connect returned: {result['error']}")
        sys.exit(1)
    return result.get("result")


def _anki_soft(action, **params):
    """Like _anki but returns None instead of exiting (optional data)."""
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        data=json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
    except Exception:
        return None
    return result.get("result") if not result.get("error") else None


def main():
    fields = _anki("modelFieldNames", modelName=MODEL_NAME)
    if not isinstance(fields, list) or not fields:
        print(f"ERROR: no fields returned for model '{MODEL_NAME}' — does it still exist?")
        sys.exit(1)
    # Descriptions are typed by the user in Anki (Fields dialog). Older
    # Anki-Connect builds lack this action — degrade to names only.
    descriptions = _anki_soft("modelFieldDescriptions", modelName=MODEL_NAME)
    if not isinstance(descriptions, list) or len(descriptions) != len(fields):
        descriptions = [""] * len(fields)
    entries = [
        {"name": name, "description": desc or ""}
        for name, desc in zip(fields, descriptions)
    ]
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"model": MODEL_NAME, "fields": entries}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Model: {MODEL_NAME} ({len(entries)} fields) -> .anki_fields.json")
    for i, entry in enumerate(entries):
        line = f"  {i:2d}. {entry['name']}"
        if entry["description"]:
            line += f" — {entry['description']}"
        print(line)


if __name__ == "__main__":
    main()
