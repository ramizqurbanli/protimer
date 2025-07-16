# ProTimer v1.3
# Pomodoro Timer

## Overview
The Pomodoro Timer is a productivity application built using Python and Tkinter. It helps users manage their work and break sessions using a countdown timer. The timer can be started, paused, and reset, and it automatically transitions from work time to break time.

## Features
- Start, pause, and reset the timer.
- Automatically transitions from work time to break time.
- Customizable work and break durations.
- **Light and dark themes.**
- **Adjustable window opacity.**
- Plays a sound when the timer ends.
- Simple and intuitive user interface.

## Requirements
- Python 3.x
- Tkinter
- audioplayer

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ramizqurbanli/protimer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd protimer
    ```
3. Install the required packages:
    ```sh
    pip install audioplayer
    ```

## Usage
1. Run the application:
    ```sh
    python main.py
    ```
2. Use the buttons to start, pause, and reset the timer.
3. Configure the work and break durations in the settings window.

## Files
- `main.py`: The main application file that contains the GUI and logic for the Pomodoro Timer.
- `timer.py`: Contains the `CountdownTimer` class that handles the countdown logic.
- `effect_sound.py`: Contains the function to play sound effects when the timer ends.
- `settings_save.py`: Handles saving and loading user settings.

## main.py

### Functions
- `updateLabel()`: Updates the timer label every second and handles the transition from work time to break time.
- `starter(is_break=False)`: Starts the Pomodoro session or break session.
- `start_break()`: Starts the break session.
- `end_break()`: Resets the timer after the break session ends.
- `pause()`: Pauses the timer.
- `reset()`: Resets the timer to the default time.
- `openSettings()`: Opens the settings window to configure work and break times, theme, and opacity.
- `apply_theme(theme_name)`: Applies the selected theme (light or dark) to the application.

### Theming
The application supports both light and dark themes. The theme can be changed in the settings window. The `dark_theme_colors` and `light_theme_colors` dictionaries define the color schemes for the different themes.

### GUI Setup
- Creates the main window and sets its properties.
- Creates a timer label with a monospace font.
- Defines styles for the buttons using `ttk.Style`.

## timer.py
### CountdownTimer Class
Handles the countdown logic for the timer.
- `__init__(self, minutes: int, seconds: int = 0)`: Initializes the timer with the specified minutes and seconds.
- `start(self)`: Starts the countdown timer.
- `_countdown(self)`: The countdown logic that updates the timer every second.
- `stop(self)`: Stops the countdown timer.

## effect_sound.py
### play_sound Function
Plays a sound file for a specified duration (default is 3 seconds).
- `play_sound(file_path, duration=3)`: Plays the sound file at `file_path` for `duration` seconds.

## settings_save.py
The `settings_save.py` script handles saving and loading user settings, such as work/break durations, theme, and window opacity. It stores the settings in a JSON file in the appropriate directory for the user's operating system (`%APPDATA%\\ProTimer` on Windows and `~/.config/ProTimer` on Linux/macOS).

## Acknowledgements
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [audioplayer](https://pypi.org/project/audioplayer/) for playing sound effects.
