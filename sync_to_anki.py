import requests
import os
import sys

# Configuration for the Japanese Note Type
ANKI_CONNECT_URL = "http://127.0.0.1:8765"
MODEL_NAME = "Japanese Note type (Sentence card by Default)"

# Resolve project root so the script works from any directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

FRONT_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Front.template.anki")
BACK_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Back.template.anki")
CSS_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Style.css")


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


def _send_payload(action: str, payload: dict) -> dict:
    """Send a payload to Anki-Connect and return the parsed response."""
    request = {
        "action": action,
        "version": 6,
        "params": payload,
    }
    try:
        resp = requests.post(ANKI_CONNECT_URL, json=request, timeout=10)
        resp.raise_for_status()
        result = resp.json()
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to Anki-Connect. Is Anki running with the add-on installed?")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("ERROR: Anki-Connect request timed out. Is Anki busy?")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Anki-Connect request failed: {e}")
        sys.exit(1)

    if result.get("error"):
        print(f"ERROR: Anki-Connect returned: {result['error']}")
    return result


def sync_to_anki():
    """
    Reads local template files and pushes them to Anki via Anki-Connect.
    This automates the manual copy-paste process for faster iteration.
    """
    # 1. Read local files (UTF-8 for proper Japanese text handling)
    front_html = _read_file(FRONT_FILE)
    back_html = _read_file(BACK_FILE)
    css_content = _read_file(CSS_FILE)

    # 2. Update Templates (Front/Back HTML)
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

    # 3. Update Styling (CSS)
    _send_payload("updateModelStyling", {
        "model": {
            "name": MODEL_NAME,
            "css": css_content
        }
    })
    print("Styling Sync:  Success")


if __name__ == "__main__":
    sync_to_anki()
