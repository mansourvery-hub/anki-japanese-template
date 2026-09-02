import urllib.request
import json
import os
import sys
import time

# Configuration for the Japanese Note Type
ANKI_CONNECT_URL = "http://127.0.0.1:8765"
MODEL_NAME = "Japanese Note type (Sentence card by Default)"

# Resolve project root so the script works from any directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

FRONT_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Front.template.anki")
BACK_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Back.template.anki")
CSS_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Style.css")

# Pre-sync snapshots of the live Anki state (gitignored safety net)
BACKUP_DIR = os.path.join(SCRIPT_DIR, "backups")


def _read_file(path: str) -> str:
    """Read a UTF-8 file from the project directory."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: Template file not found: {path}")
        sys.exit(1)
    except OSError as e:
        print(f"ERROR: Could not read {path}: {e}")
        sys.exit(1)


def _send_payload(action: str, params: dict = None) -> dict:
    """Send a payload to Anki-Connect and return the parsed response."""
    payload = {
        "action": action,
        "version": 6,
        "params": params or {},
    }
    req = urllib.request.Request(
        ANKI_CONNECT_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"ERROR: Could not connect to Anki-Connect. Is Anki running with the add-on installed? {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Anki-Connect request failed: {e}")
        sys.exit(1)

    if result.get("error"):
        print(f"ERROR: Anki-Connect returned: {result['error']}")
        sys.exit(1)
    return result


def snapshot_live_state():
    """Pull the live model from Anki into backups/<timestamp>/ before pushing.

    Guard against clobbering unnoticed Anki-side edits: the snapshot keeps the
    exact state that is about to be overwritten, so any manual change made in
    the Anki UI stays recoverable. Failures here abort the sync (never push
    over a state we failed to back up).
    """
    templates = _send_payload("modelTemplates", {"modelName": MODEL_NAME})
    styling = _send_payload("modelStyling", {"modelName": MODEL_NAME})

    tpls = templates.get("result") or {}
    sty = styling.get("result") or {}
    if not tpls or not isinstance(tpls, dict) or not sty.get("css"):
        print("ERROR: live Anki state looks empty (model missing?) — aborting sync")
        sys.exit(1)

    stamp = time.strftime("%Y%m%d-%H%M%S-%f")
    dest = os.path.join(BACKUP_DIR, stamp)
    os.makedirs(dest, exist_ok=True)
    for card_name, pair in tpls.items():
        safe = card_name.replace(os.sep, "_")
        with open(os.path.join(dest, f"{safe}.front.anki"), "w", encoding="utf-8") as f:
            f.write(pair.get("Front", ""))
        with open(os.path.join(dest, f"{safe}.back.anki"), "w", encoding="utf-8") as f:
            f.write(pair.get("Back", ""))
    with open(os.path.join(dest, "style.css"), "w", encoding="utf-8") as f:
        f.write(sty.get("css", ""))
    print(f"Backup:        {os.path.relpath(dest, SCRIPT_DIR)}/")
    return dest


def sync_to_anki():
    """
    Reads local template files and pushes them to Anki via Anki-Connect.
    This automates the manual copy-paste process for faster iteration.
    """
    # 1. Read local files (UTF-8 for proper Japanese text handling)
    front_html = _read_file(FRONT_FILE)
    back_html = _read_file(BACK_FILE)
    css_content = _read_file(CSS_FILE)

    # 2. Snapshot the live Anki state we are about to overwrite
    snapshot_live_state()

    # 3. Update Templates (Front/Back HTML)
    _send_payload("updateModelTemplates", {
        "model": {
            "name": MODEL_NAME,
            "templates": {
                "Card 1": {
                    "Front": front_html,
                    "Back": back_html
                }
            }
        }
    })
    print("Template Sync: Success")

    # 4. Update Styling (CSS)
    _send_payload("updateModelStyling", {
        "model": {
            "name": MODEL_NAME,
            "css": css_content
        }
    })
    print("Styling Sync:  Success")


if __name__ == "__main__":
    sync_to_anki()
