import json
import os

def get_settings_path():
    app_data_dir = os.path.join(os.getenv('APPDATA'), 'ProTimer')
    os.makedirs(app_data_dir, exist_ok=True)
    return os.path.join(app_data_dir, 'settings.json')

def save_settings(settings):
    if settings is None:
        settings = {}
    with open(get_settings_path(), 'w') as f:
        json.dump(settings, f, indent=4)

def load_settings():
    try:
        with open(get_settings_path(), 'r') as f:
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
