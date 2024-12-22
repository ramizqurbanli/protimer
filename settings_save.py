import json


def save_settings(settings):
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4)

def load_settings():
        try:
            with open('settings.json', 'r') as f:
                return json.load(f)
        except :
            save_settings(None)
            return False
