import time
import threading
from effect_sound import play_sound

class CountdownTimer:
    def __init__(self, minutes: int, seconds: int = 0):
        self.total_seconds = minutes * 60 + seconds
        self.timer = f"{minutes:02d}:{seconds:02d}"
        self.is_running = False
        self.is_ended = False

    def start(self):
        self.is_running = True
        self.is_ended = False
        threading.Thread(target=self._countdown).start()

    def _countdown(self):
        while self.total_seconds > 0 and self.is_running:
            mins, secs = divmod(self.total_seconds, 60)
            self.timer = f"{mins:02d}:{secs:02d}"
            time.sleep(1)
            self.total_seconds -= 1

        if self.total_seconds == 0:
            self.timer = "Time is up!"
            self.is_ended = True
            play_sound("ringtone.mp3", duration=3)
        self.is_running = False

    def stop(self):
        self.is_running = False