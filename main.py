import tkinter as tk
from timer import CountdownTimer  # type: ignore
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from settings_save import save_settings, load_settings # type: ignore

dark_theme_colors = {
    "bg": "#1a1a1a",
    "label_fg": "#FFD700",
    "label_bg": "#1a1a1a",
    # Settings window specific
    "settings_bg": "#2c2c2c",
    "settings_fg": "#e0e0e0",
    "input_bg": "#3c3c3c",
    "input_fg": "#e0e0e0",
    "input_insert_bg": "#e0e0e0", # Cursor color for Entry
    "scale_trough_bg": "#3c3c3c",
    # Main window buttons
    "start_button_bg": "#006400",
    "start_button_fg": "white",
    "start_button_active_bg": "#228B22",
    "pause_button_bg": "#4682B4",
    "pause_button_fg": "#D3D3D3",
    "pause_button_active_bg": "#5A9BD5",
    "reset_button_bg": "#FF8C00",
    "reset_button_fg": "white",
    "reset_button_active_bg": "#FF7F00",
    "settings_button_bg": "#C0C0C0",
    "settings_button_fg": "#696969",
    "settings_button_active_bg": "#A9A9A9",
    "copyright_fg": "#A9A9A9",
    "copyright_bg": "#1a1a1a",
}

light_theme_colors = {
    "bg": "#f0f0f0",
    "label_fg": "#000000",
    "label_bg": "#f0f0f0",
    # Settings window specific
    "settings_bg": "#e0e0e0",
    "settings_fg": "#2c2c2c",
    "input_bg": "#ffffff",
    "input_fg": "#000000",
    "input_insert_bg": "#000000", # Cursor color for Entry
    "scale_trough_bg": "#d3d3d3",
    # Main window buttons
    "start_button_bg": "#28a745",
    "start_button_fg": "white",
    "start_button_active_bg": "#218838",
    "pause_button_bg": "#007bff",
    "pause_button_fg": "white",
    "pause_button_active_bg": "#0069d9",
    "reset_button_bg": "#ffc107",
    "reset_button_fg": "black",
    "reset_button_active_bg": "#e0a800",
    "settings_button_bg": "#6c757d",
    "settings_button_fg": "white",
    "settings_button_active_bg": "#5a6268",
    "copyright_fg": "#333333",
    "copyright_bg": "#f0f0f0",
}

# Initialize pause time globally
paused_minutes = None
paused_seconds = None
timer = None  # Initialize timer as None to be created dynamically
settings_window_open = False  # Checking if settings window is open

# Load settings from the JSON file if available
settings = load_settings()
current_theme = settings.get("theme") # theme is guaranteed by load_settings

default_time = int(settings.get("work_time", 25))
break_time = int(settings.get("break_time", 5))
window_opacity = settings.get("window_opacity", 1)

# Validate the window opacity value
if window_opacity < 0.1 or window_opacity > 1.0:
    window_opacity = 1.0

# Define the main window
window = tk.Tk()
window.geometry("320x320")
window.minsize(200, 300)
window.maxsize(420, 420)
window.title("ProTimer")
window.attributes("-topmost", True, "-alpha", window_opacity)
# window.configure(bg="#1a1a1a")  # Theme will handle this

# Set dark title bar for Windows
try:
    from ctypes import windll, byref, sizeof, c_int
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    windll.dwmapi.DwmSetWindowAttribute(
        windll.user32.GetParent(window.winfo_id()),
        DWMWA_USE_IMMERSIVE_DARK_MODE,
        byref(c_int(1)),
        sizeof(c_int)
    )
except Exception as e:
    print(f"Could not set dark title bar: {e}")

def on_closing():
    window.destroy()
    timer.stop()
# Load icon image if available
try:
    img = PhotoImage(file='logo.png')
    window.iconphoto(False, img)
except Exception as e:
    print(f"Error loading icon: {e}")

# Create a timer label with monospace font
labelTimer = tk.Label(text=f"{default_time:02d}:00", font=("Courier New", 30))
# labelTimer.config(fg="#FFD700", bg="#1a1a1a") # Theme will handle this
labelTimer.pack(pady=20)

# Define a style for the buttons using ttk
style = ttk.Style()
style.theme_use("alt")

# Button styles will be applied by apply_theme function

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
        # Only use paused values if they exist and we're not coming from a break
        start_minutes = paused_minutes if paused_minutes is not None else default_time
        start_seconds = paused_seconds if paused_seconds is not None else 0

    labelTimer.config(text=f"{start_minutes:02d}:{start_seconds:02d}")

    timer = CountdownTimer(start_minutes, start_seconds)
    timer.is_break = is_break  # Add a flag to indicate if it's a break timer
    timer.start()
    updateLabel()

def start_break():
    global paused_minutes, paused_seconds
    # Reset paused values before starting break
    paused_minutes = None
    paused_seconds = None
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
    settings_window.geometry("300x310") # Increased height for theme option
    settings_window.minsize(300, 310) # Increased height for theme option
    settings_window.maxsize(340, 320) # Increased height for theme option
    settings_window.lift()
    settings_window.attributes("-topmost", True)
    settings_window_open = True

    # Store widgets for easy theming
    settings_widgets = {}

    def apply_settings_theme_widgets(target_window, theme_colors, combobox_style_name):
        target_window.configure(bg=theme_colors["settings_bg"])
        
        # Style general tk.Labels
        for label_widget in settings_widgets.get("labels", []):
            label_widget.config(bg=theme_colors["settings_bg"], fg=theme_colors["settings_fg"])
        
        # Style tk.Entry widgets
        for entry_widget in settings_widgets.get("entries", []):
            entry_widget.config(
                bg=theme_colors["input_bg"], 
                fg=theme_colors["input_fg"], 
                insertbackground=theme_colors["input_insert_bg"],
                relief=tk.FLAT, # Using FLAT for a more modern look with themed bg
                borderwidth=1 # Can be 0 if bg is distinct enough
            )
            
        # Style tk.Scale widget
        if "scale" in settings_widgets:
            settings_widgets["scale"].config(
                bg=theme_colors["settings_bg"], 
                fg=theme_colors["settings_fg"], 
                troughcolor=theme_colors["scale_trough_bg"],
                highlightbackground=theme_colors["settings_bg"] # Blend border with bg
            )
            
        # Style ttk.Combobox (theme_combobox)
        if "theme_combobox" in settings_widgets:
            # Define and apply style for Combobox if not already done globally
            # Note: ttk styles are global, so configure once is enough, but applying can be per widget.
            style.configure(
                combobox_style_name,
                fieldbackground=theme_colors["input_bg"],
                background=theme_colors["input_bg"], # background of dropdown arrow
                foreground=theme_colors["input_fg"],
                selectbackground=theme_colors["input_bg"], # bg of selected item
                selectforeground=theme_colors["input_fg"]  # fg of selected item
                # arrowcolor can also be themed if needed via a custom layout
            )
            # Forcing update of dropdown list style (more complex, often handled by OS or base theme)
            # For simplicity, we focus on fieldbackground, background, foreground here.
            # settings_widgets["theme_combobox"].config(style=combobox_style_name) # Already set at creation


    def on_close():
        global settings_window_open
        settings_window_open = False
        settings_window.destroy()

    settings_window.protocol("WM_DELETE_WINDOW", on_close)

    # Create and store labels
    settings_widgets["labels"] = [
        tk.Label(settings_window, text="Work Time (minutes):"),
        tk.Label(settings_window, text="Break Time (minutes):"),
        tk.Label(settings_window, text="Window Opacity (0.1 to 1.0):"),
        tk.Label(settings_window, text="Theme:")
    ]
    for label in settings_widgets["labels"]:
        label.pack(pady=5 if label.cget("text") != "Theme:" else (5,0) )


    entry_default_time = tk.Entry(settings_window)
    entry_default_time.insert(0, str(default_time))
    entry_default_time.pack(pady=5)

    entry_break_time = tk.Entry(settings_window)
    entry_break_time.insert(0, str(break_time))
    entry_break_time.pack(pady=5)
    settings_widgets["entries"] = [entry_default_time, entry_break_time]


    scale_opacity = tk.Scale(settings_window, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
    scale_opacity.set(window.attributes("-alpha"))
    scale_opacity.pack(pady=5)
    settings_widgets["scale"] = scale_opacity

    
    combobox_style_name = "Settings.TCombobox"
    theme_combobox = ttk.Combobox(settings_window, values=["Light", "Dark"], state="readonly", style=combobox_style_name)
    theme_combobox.set(current_theme.capitalize()) 
    theme_combobox.pack(pady=(0,5))
    settings_widgets["theme_combobox"] = theme_combobox
    
    # Initial theme application for settings window
    initial_colors = light_theme_colors if current_theme == "light" else dark_theme_colors
    apply_settings_theme_widgets(settings_window, initial_colors, combobox_style_name)


    def saveSettings():
        global default_time, break_time, current_theme, apply_theme, style
        
        # Update time and opacity settings
        default_time = int(entry_default_time.get())
        break_time = int(entry_break_time.get())
        new_opacity = scale_opacity.get()
        window.attributes("-alpha", new_opacity)
        labelTimer.config(text=f"{default_time:02d}:00") # Update timer display if needed

        # Update theme
        selected_theme_display = theme_combobox.get()
        new_theme = "light" if selected_theme_display == "Light" else "dark"
        
        theme_changed = False
        if current_theme != new_theme:
            current_theme = new_theme
            apply_theme(current_theme) # Apply theme immediately to main window
            theme_changed = True

        # Prepare data for saving
        data_to_save = {
            "work_time": default_time,
            "break_time": break_time,
            "window_opacity": new_opacity,
            "theme": current_theme 
        }
        # Save all settings to a JSON file
        save_settings(data_to_save)
        
        # Re-apply settings theme if it changed or just to be sure if settings window is open
        if theme_changed: # Or simply always call if settings_window is open
            updated_colors = light_theme_colors if current_theme == "light" else dark_theme_colors
            apply_settings_theme_widgets(settings_window, updated_colors, combobox_style_name)

        on_close()

    save_button = ttk.Button(settings_window, text="Save", command=saveSettings, style="Save.TButton") # Changed style
    save_button.pack(pady=10)
    # Ensure the save button itself is also themed if its style relies on settings_bg/fg
    # The "Save.TButton" style is based on StartButton colors from apply_theme, which is fine.


# Layout for Start, Pause, Reset, and Settings buttons
start_button = ttk.Button(window, text="Start", command=starter, style="StartButton.TButton")
start_button.pack(pady=5)

pause_button = ttk.Button(window, text="Pause", command=pause, style="PauseButton.TButton")
pause_button.pack(pady=5)

reset_button = ttk.Button(window, text="Reset", command=reset, style="ResetButton.TButton")
reset_button.pack(pady=5)

settings_button = ttk.Button(window, text="Settings", command=openSettings, style="SettingsButton.TButton")
settings_button.pack(pady=5)

# Copyright label with auto-updating year
from datetime import datetime
copyright_label = tk.Label(window, text=f"© {datetime.now().year} TUSI", font=("Courier New", 8))
# copyright_label.config(fg="#A9A9A9", bg="#1a1a1a") # Theme will handle this
copyright_label.pack(side=tk.BOTTOM, pady=5)

def apply_theme(theme_name):
    global window, labelTimer, style, copyright_label, light_theme_colors, dark_theme_colors
    
    colors = light_theme_colors if theme_name == "light" else dark_theme_colors

    # Apply to main window
    window.configure(bg=colors["bg"])

    # Apply to timer label
    labelTimer.config(fg=colors["label_fg"], bg=colors["label_bg"])

    # Apply to buttons using ttk style
    button_types = {
        "StartButton": ("start_button_bg", "start_button_fg", "start_button_active_bg"),
        "PauseButton": ("pause_button_bg", "pause_button_fg", "pause_button_active_bg"),
        "ResetButton": ("reset_button_bg", "reset_button_fg", "reset_button_active_bg"),
        "SettingsButton": ("settings_button_bg", "settings_button_fg", "settings_button_active_bg"),
    }

    for btn_name_prefix, (bg_key, fg_key, active_bg_key) in button_types.items():
        style_name = f"{btn_name_prefix}.TButton"
        style.configure(
            style_name,
            font=("Courier New", 10, "bold"),
            padding=10,
            relief="flat",
            background=colors[bg_key],
            foreground=colors[fg_key],
            borderwidth=0,
        )
        style.map(
            style_name,
            background=[("active", colors[active_bg_key])],
            relief=[("pressed", "flat")],
        )
        # Ensure save button in settings also uses a themed style if it's one of these
        if btn_name_prefix == "StartButton": # Example: Save button uses StartButton style
            style.configure("Save.TButton", # Assuming a new style name or reusing for simplicity
                font=("Courier New", 10, "bold"),
                padding=10,
                relief="flat",
                background=colors[bg_key],
                foreground=colors[fg_key],
                borderwidth=0,
            )
            style.map(
                "Save.TButton",
                background=[("active", colors[active_bg_key])],
                relief=[("pressed", "flat")],
            )


    # Apply to copyright label
    copyright_label.config(fg=colors["copyright_fg"], bg=colors["copyright_bg"])

# Apply the loaded theme
apply_theme(current_theme)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()