import json

def save_settings(settings):
    if settings is None:
        settings = {}
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def load_settings():
    try:
        with open('settings.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        save_settings({})
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON. Using default settings.")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
