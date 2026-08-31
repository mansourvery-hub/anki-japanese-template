import requests
import os

# Configuration for the Japanese Note Type
ANKI_CONNECT_URL = "http://127.0.0.1:8765"
MODEL_NAME = "Japanese Note type (Sentence card by Default)"

def sync_to_anki():
    """
    Reads local template files and pushes them to Anki via Anki-Connect.
    This automates the manual copy-paste process for faster iteration.
    """
    try:
        # 1. Read local files
        with open("Card 1 - Front.template.anki", "r") as f:
            front_html = f.read()
        with open("Card 1 - Back.template.anki", "r") as f:
            back_html = f.read()
        with open("Card 1 - Style.css", "r") as f:
            css_content = f.read()

        # 2. Update Templates (Front/Back HTML)
        template_payload = {
            "action": "updateModelTemplates",
            "version": 6,
            "params": {
                "model": {
                    "name": MODEL_NAME,
                    "templates": {
                        "Card 1": {
                            "Front": front_html,
                            "Back": back_html
                        }
                    }
                }
            }
        }
        
        # 3. Update Styling (CSS)
        styling_payload = {
            "action": "updateModelStyling",
            "version": 6,
            "params": {
                "model": {
                    "name": MODEL_NAME,
                    "css": css_content
                }
            }
        }

        # Send requests to Anki-Connect
        t_resp = requests.post(ANKI_CONNECT_URL, json=template_payload).json()
        s_resp = requests.post(ANKI_CONNECT_URL, json=styling_payload).json()

        print(f"Template Sync: {'Success' if not t_resp.get('error') else f'Error: {t_resp['error']}'}")
        print(f"Styling Sync:  {'Success' if not s_resp.get('error') else f'Error: {s_resp['error']}'}")

    except Exception as e:
        print(f"Sync failed: {e}")

if __name__ == "__main__":
    sync_to_anki()
