import requests
import os
import sys
import subprocess
from datetime import datetime

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
DECK_NAME = "My Life Decks::Japanese::anki-japanese-template"
EXPORT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
EXPORT_FILENAME = f"anki-japanese-template-{datetime.now().strftime('%Y%m%d')}.apkg"
EXPORT_PATH = os.path.join(EXPORT_DIR, EXPORT_FILENAME)

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
        sys.exit(1)
    return result


def export_deck_to_apkg(deck_name: str, output_path: str) -> bool:
    """
    Export a specific Anki deck to an apkg file using Anki-Connect.
    Returns True if successful, False otherwise.
    """
    print(f"Attempting to export deck: {deck_name}")

    try:
        result = _send_payload("exportDeck", {
            "deck": deck_name,
            "options": {
                "cards": "all",
                "notes": "all",
                "separator": "\u0001"
            },
            "adoc": ""
        })

        print(f"Anki-Connect export completed: {result}")

    except Exception as e:
        print(f"ERROR: Failed to export deck via Anki-Connect: {e}")
        return False

    return True


def main():
    """
    Export the sample deck to apkg, commit it to git, and push to GitHub.
    """
    print("=" * 60)
    print("Anki Template Release Automation")
    print("=" * 60)

    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
        print(f"Created export directory: {EXPORT_DIR}")

    if not os.path.exists(EXPORT_PATH):
        print(f"ERROR: Export file not found at: {EXPORT_PATH}")
        print("The deck might not exist in your Anki collection.")
        print(f"Deck to export: {DECK_NAME}")
        sys.exit(1)

    file_size = os.path.getsize(EXPORT_PATH)
    file_size_mb = file_size / (1024 * 1024)
    print(f"Export file size: {file_size_mb:.2f} MB")

    print("\nPreparing to commit and push to GitHub...")
    print(f"Exporting: {EXPORT_FILENAME}")

    git_add_cmd = ["git", "add", EXPORT_PATH]
    try:
        subprocess.run(git_add_cmd, check=True, capture_output=True, text=True)
        print("✓ Git add successful")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Git add failed: {e}")
        print("Make sure you're in a git repository and on the main branch.")
        sys.exit(1)

    git_commit_cmd = ["git", "commit", "-m", f"chore: release updated template ({EXPORT_FILENAME})"]
    try:
        subprocess.run(git_commit_cmd, check=True, capture_output=True, text=True)
        print("✓ Git commit successful")
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stdout:
            print("⚠ No changes to commit (export file already committed)")
        else:
            print(f"ERROR: Git commit failed: {e}")
            sys.exit(1)

    git_push_cmd = ["git", "push", "origin", "main"]
    try:
        subprocess.run(git_push_cmd, check=True, capture_output=True, text=True)
        print("✓ Git push successful")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Git push failed: {e}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ Release successful!")
    print("=" * 60)
    print(f"APKG file committed and pushed to GitHub: {EXPORT_FILENAME}")
    print(f"File location: {EXPORT_PATH}")
    print(f"Deck exported: {DECK_NAME}")


if __name__ == "__main__":
    main()
