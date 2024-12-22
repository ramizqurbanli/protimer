Sure! Here is the updated `README.md` file with the company license section added:

---

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

ttk.Style

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

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Tusi LLC Source Code License Agreement

**IMPORTANT**: By accessing, downloading, or using this source code ("Code") in this repository, you agree to be bound by the terms and conditions of this Source Code License Agreement ("Agreement"). If you do not agree to the terms of this Agreement, you should not use the Code.

### 1. License Grant
Tusi LLC ("Licensor") hereby grants you a non-exclusive, non-transferable, revocable license to use, modify, and compile the source code in this repository ("Code") for personal, non-commercial, or internal business purposes only. You may not distribute, sublicense, or otherwise transfer the Code to any third party without prior written permission from Tusi LLC.

### 2. Ownership
The Code is owned by Tusi LLC and is protected by copyright and other intellectual property laws. You acknowledge that you do not acquire any ownership rights in the Code and that the Code remains the exclusive property of Tusi LLC.

### 3. Restrictions
You may not:
- Use the Code for commercial purposes or in a manner that competes with Tusi LLC's business.
- Distribute or sublicense the Code without express written permission from Tusi LLC.
- Reverse engineer, decompile, disassemble, or attempt to derive the source code of the Code, except as permitted by applicable law.
- Use the Code in any way that violates any laws, regulations, or third-party rights.

### 4. Confidential Information
The Code contains proprietary and confidential information of Tusi LLC ("Confidential Information"). You agree not to disclose, distribute, or use the Confidential Information for any purpose other than as expressly permitted under this Agreement.

### 5. No Warranty
The Code is provided "as-is," without any express or implied warranties of any kind, including but not limited to implied warranties of merchantability, fitness for a particular purpose, or non-infringement. Tusi LLC does not warrant that the Code will be error-free or meet your specific requirements.

### 6. Limitation of Liability
In no event shall Tusi LLC be liable for any indirect, incidental, special, or consequential damages arising from your use or inability to use the Code, even if Tusi LLC has been advised of the possibility of such damages. Tusi LLC's liability shall be limited to the amount you paid for the Code, if applicable.

### 7. Term and Termination
This Agreement is effective until terminated. Tusi LLC may terminate this Agreement immediately if you violate any of the terms. Upon termination, you must cease using the Code and destroy all copies in your possession.

### 8. Governing Law
This Agreement shall be governed by the laws of [Your Jurisdiction], without regard to its conflict of law principles.

### 9. Miscellaneous
- This Agreement constitutes the entire agreement between you and Tusi LLC regarding the Code.
- If any provision of this Agreement is found to be invalid or unenforceable, the remaining provisions shall remain in full force and effect.
- You may not assign or transfer your rights or obligations under this Agreement without prior written consent from Tusi LLC.

By accessing or using the Code, you agree to the terms and conditions of this Agreement.


## Acknowledgements
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [audioplayer](https://pypi.org/project/audioplayer/) for playing sound effects.

