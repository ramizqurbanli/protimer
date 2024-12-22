# Pomodoro Timer

## Overview
The Pomodoro Timer is a productivity application built using Python and Tkinter. It helps users manage their work and break sessions using a countdown timer. The timer can be started, paused, and reset, and it automatically transitions from work time to break time.

## Features
- Start, pause, and reset the timer.
- Automatically transitions from work time to break time.
- Customizable work and break durations.
- Plays a sound when the timer ends.
- Simple and intuitive user interface.

## Requirements
- Python 3.x
- Tkinter
- audioplayer

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pomodoro-timer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd pomodoro-timer
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
- 

main.py

: The main application file that contains the GUI and logic for the Pomodoro Timer.
- `timer.py`: Contains the `CountdownTimer` class that handles the countdown logic.
- `effect_sound.py`: Contains the function to play sound effects when the timer ends.

## 

main.py


### Functions
- `updateLabel()`: Updates the timer label every second and handles the transition from work time to break time.
- `starter(is_break=False)`: Starts the Pomodoro session or break session.
- `start_break()`: Starts the break session.
- `end_break()`: Resets the timer after the break session ends.
- `pause()`: Pauses the timer.
- `reset()`: Resets the timer to the default time.
- `openSettings()`: Opens the settings window to configure work and break times.

### GUI Setup
- Creates the main window and sets its properties.
- Creates a timer label with a monospace font.
- Defines styles for the buttons using 

`ttk.Style`

.

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


## Acknowledgements
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [audioplayer](https://pypi.org/project/audioplayer/) for playing sound effects.

