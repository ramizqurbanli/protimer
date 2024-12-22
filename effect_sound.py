from audioplayer import AudioPlayer #type: ignore
import time

def play_sound(file_path, duration=3):
    """
    Play a sound file for a specified duration (default is 3 seconds).
    
    Args:
    file_path (str): The path to the audio file to play.
    duration (int): Duration in seconds to play the sound. Default is 3 seconds.
    """
    try:
        player = AudioPlayer(file_path)
        player.play(block=False)  # Play sound in the background
        time.sleep(duration)  # Wait for the sound to play for the given duration
        player.stop()  # Stop the sound after the duration
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")