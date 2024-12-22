import tkinter as tk
from timer import CountdownTimer  # type: ignore
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
# Initialize pause time globally
paused_minutes = None
paused_seconds = None
timer = None  # Initialize timer as None to be created dynamically
settings_window_open = False  # Checking if settings window is open

# Initialize default values for work time and window opacity
default_time = 25  # Work session time in minutes
break_time = 5  # Break session time in minutes
window_opacity = 1  # Opacity level for the main window

# Define the main window
window = tk.Tk()
window.geometry("320x320")
window.minsize(200, 300)
window.maxsize(420, 420)
window.title("ProTimer")
window.attributes("-topmost", True, "-alpha", window_opacity)
window.configure(bg="#1a1a1a")  # Dark gray background

# Load icon image if available
try:
    img = PhotoImage(file='logo.png')
    window.iconphoto(False, img)
except Exception as e:
    print(f"Error loading icon: {e}")

# Create a timer label with monospace font
labelTimer = tk.Label(text=f"{default_time:02d}:00", font=("Courier New", 30))
labelTimer.config(fg="#FFD700", bg="#1a1a1a")
labelTimer.pack(pady=20)

# Define a style for the buttons using ttk
style = ttk.Style()
style.theme_use("alt")

# Button styles
style.configure(
    "StartButton.TButton",
    font=("Courier New", 10, "bold"),
    padding=10,
    relief="flat",
    background="#006400",
    foreground="white",
    borderwidth=0,
)
style.map(
    "StartButton.TButton",
    background=[("active", "#228B22")],
    relief=[("pressed", "flat")],
)

style.configure(
    "PauseButton.TButton",
    font=("Courier New", 10, "bold"),
    padding=10,
    relief="flat",
    background="#4682B4",
    foreground="#D3D3D3",
    borderwidth=0,
)
style.map(
    "PauseButton.TButton",
    background=[("active", "#5A9BD5")],
    relief=[("pressed", "flat")],
)

style.configure(
    "ResetButton.TButton",
    font=("Courier New", 10, "bold"),
    padding=10,
    relief="flat",
    background="#FF8C00",
    foreground="white",
    borderwidth=0,
)
style.map(
    "ResetButton.TButton",
    background=[("active", "#FF7F00")],
    relief=[("pressed", "flat")],
)

style.configure(
    "SettingsButton.TButton",
    font=("Courier New", 10, "bold"),
    padding=10,
    relief="flat",
    background="#C0C0C0",
    foreground="#696969",
    borderwidth=0,
)
style.map(
    "SettingsButton.TButton",
    background=[("active", "#A9A9A9")],
    relief=[("pressed", "flat")],
)

# Function to update the label every second
def updateLabel():
    global timer

    if (timer and timer.is_running):
        labelTimer.config(text=timer.timer)
        window.after(1000, updateLabel)
    elif (timer and timer.is_ended):
        labelTimer.config(text="Time is up!")
        timer.is_ended = False  # Reset the flag
        if not timer.is_break:
            start_break()
    else:
        labelTimer.config(text="Paused")

# Function to start the Pomodoro session
def starter(is_break=False):
    global timer, paused_minutes, paused_seconds

    if timer and timer.is_running:
        return

    if is_break:
        start_minutes = break_time
        start_seconds = 0
    else:
        start_minutes = paused_minutes if paused_minutes is not None else default_time
        start_seconds = paused_seconds if paused_seconds is not None else 0

    labelTimer.config(text=f"{start_minutes:02d}:{start_seconds:02d}")

    timer = CountdownTimer(start_minutes, start_seconds)
    timer.is_break = is_break  # Add a flag to indicate if it's a break timer
    timer.start()
    updateLabel()

def start_break():
    messagebox.showinfo("Break Time", "Time for a break!")
    starter(is_break=True)

def end_break():
    global paused_minutes, paused_seconds
    paused_minutes = None
    paused_seconds = None
    labelTimer.config(text=f"{default_time:02d}:00")
    messagebox.showinfo("Work Time", "Break is over! Time to get back to work.")

# Pause button callback
def pause():
    global timer, paused_minutes, paused_seconds

    if timer and timer.is_running:
        timer.stop()
        paused_minutes, paused_seconds = divmod(timer.total_seconds, 60)
    else:
        labelTimer.config(text="Paused")

# Reset button callback
def reset():
    global paused_minutes, paused_seconds
    if timer:
        timer.stop()
    paused_minutes, paused_seconds = None, None  # Reset paused values
    labelTimer.config(text=f"{default_time:02d}:00")  # Display correct default time

# Settings button callback
def openSettings():
    global settings_window_open

    if settings_window_open:  
        return

    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("300x260")
    settings_window.minsize(300, 260)
    settings_window.maxsize(340, 270)
    settings_window.lift()
    settings_window.attributes("-topmost", True)
    settings_window_open = True

    def on_close():
        global settings_window_open
        settings_window_open = False
        settings_window.destroy()

    settings_window.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(settings_window, text="Work Time (minutes):").pack(pady=5)
    entry_default_time = tk.Entry(settings_window)
    entry_default_time.insert(0, str(default_time))
    entry_default_time.pack(pady=5)

    tk.Label(settings_window, text="Break Time (minutes):").pack(pady=5)
    entry_break_time = tk.Entry(settings_window)
    entry_break_time.insert(0, str(break_time))
    entry_break_time.pack(pady=5)

    tk.Label(settings_window, text="Window Opacity (0.1 to 1.0):").pack(pady=5)
    scale_opacity = tk.Scale(settings_window, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
    scale_opacity.set(window.attributes("-alpha"))
    scale_opacity.pack(pady=5)

    def saveSettings():
        global default_time, break_time
        default_time = int(entry_default_time.get())
        break_time = int(entry_break_time.get())
        window.attributes("-alpha", scale_opacity.get())
        labelTimer.config(text=f"{default_time:02d}:00")
        on_close()

    save_button = ttk.Button(settings_window, text="Save", command=saveSettings, style="StartButton.TButton")
    save_button.pack(pady=10)


# Layout for Start, Pause, Reset, and Settings buttons
start_button = ttk.Button(window, text="Start", command=starter, style="StartButton.TButton")
start_button.pack(pady=5)

pause_button = ttk.Button(window, text="Pause", command=pause, style="PauseButton.TButton")
pause_button.pack(pady=5)

reset_button = ttk.Button(window, text="Reset", command=reset, style="ResetButton.TButton")
reset_button.pack(pady=5)

settings_button = ttk.Button(window, text="Settings", command=openSettings, style="SettingsButton.TButton")
settings_button.pack(pady=5)

# Copyright label
copyright_label = tk.Label(window, text="© 2024 TUSI LLC", font=("Courier New", 8), fg="#A9A9A9", bg="#1a1a1a")
copyright_label.pack(side=tk.BOTTOM, pady=5)

# Run the main event loop
window.mainloop()