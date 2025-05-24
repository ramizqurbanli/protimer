import json
import os
import platform

def get_settings_path():
    if platform.system() == 'Windows':
        app_data_dir = os.path.join(os.getenv('APPDATA'), 'ProTimer')
    else:  # Linux and other Unix-like systems
        app_data_dir = os.path.join(os.path.expanduser('~'), '.config', 'ProTimer')
    
    os.makedirs(app_data_dir, exist_ok=True)
    return os.path.join(app_data_dir, 'settings.json')

def save_settings(settings):
    if settings is None:
        # This case should ideally not be hit if load_settings always provides defaults.
        # However, keeping it for robustness.
        settings = {'work_time': 25, 'break_time': 5, 'window_opacity': 1.0, 'theme': 'dark'}
    with open(get_settings_path(), 'w') as f:
        json.dump(settings, f, indent=4)

def load_settings():
    default_settings = {
        'work_time': 25,
        'break_time': 5,
        'window_opacity': 1.0,
        'theme': 'dark'
    }
    
    settings_path = get_settings_path()
    
    try:
        with open(settings_path, 'r') as f:
            loaded_settings = json.load(f)
            # Merge defaults with loaded settings. Loaded settings take precedence.
            # Ensure all default keys are present.
            settings = default_settings.copy()
            settings.update(loaded_settings)
            # Explicitly ensure 'theme' is present, defaulting to 'dark' if somehow missing after update
            if 'theme' not in settings:
                settings['theme'] = 'dark'
            return settings
    except FileNotFoundError:
        # If file not found, save default settings and return them
        save_settings(default_settings.copy())
        return default_settings.copy()
    except json.JSONDecodeError:
        print("Error decoding JSON. Using default settings.")
        # If JSON is corrupt, save default settings and return them
        save_settings(default_settings.copy())
        return default_settings.copy()
    except Exception as e:
        print(f"Unexpected error loading settings: {e}. Using default settings.")
        # For any other error, try to save defaults and return them
        # It's possible save_settings might also fail if there are permission issues, etc.
        try:
            save_settings(default_settings.copy())
        except Exception as save_e:
            print(f"Failed to save default settings after error: {save_e}")
        return default_settings.copy()
