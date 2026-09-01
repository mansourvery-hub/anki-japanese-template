#!/usr/bin/env python3
"""Export the sample deck to dist/anki-japanese-template.apkg via Anki-Connect.

Called by finish.sh; can also be run standalone. The real Anki-Connect action
is `exportPackage` (params: deck, path, includeSched). The apkg is gitignored
(`*.apkg` in .gitignore) — it is distributed via GitHub Releases, never the
repo itself.
"""
import os
import sys

import requests

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
DECK_NAME = "My Life Decks::Japanese::anki-japanese-template"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EXPORT_PATH = os.path.join(SCRIPT_DIR, "dist", "anki-japanese-template.apkg")


def main() -> int:
    os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)
    payload = {
        "action": "exportPackage",
        "version": 6,
        "params": {"deck": DECK_NAME, "path": EXPORT_PATH, "includeSched": False},
    }
    try:
        resp = requests.post(ANKI_CONNECT_URL, json=payload, timeout=180)
        resp.raise_for_status()
        result = resp.json()
    except requests.exceptions.ConnectionError:
        print("ERROR: cannot reach Anki-Connect (is Anki running with the add-on?)")
        return 1
    except requests.exceptions.RequestException as e:
        print(f"ERROR: export request failed: {e}")
        return 1

    if result.get("error") or not result.get("result"):
        print(f"ERROR: Anki-Connect export failed: {result.get('error') or 'unknown error'}")
        return 1

    if not os.path.isfile(EXPORT_PATH) or os.path.getsize(EXPORT_PATH) == 0:
        print(f"ERROR: expected export missing or empty: {EXPORT_PATH}")
        return 1

    print(f"Export OK: {EXPORT_PATH} ({os.path.getsize(EXPORT_PATH) / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
