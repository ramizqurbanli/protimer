import PyInstaller.__main__
import os
import datetime

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'main.py',
    '--name=ProTimer',
    '--windowed',
    '--onefile',
    '--clean',
    '--noupx',  # Avoid UPX compression which often triggers AV
    '--disable-windowed-traceback',  # Reduce traceback information
    # Removed --uac-admin flag which can cause issues
    f'--icon={os.path.join(current_dir, "logo.png")}',
    '--add-data=logo.png;.',
    # Make sure all required files are included
    '--add-data=settings_save.py;.',
    '--add-data=timer.py;.',
    f'--version-file={os.path.join(current_dir, "version_info.txt")}',
])