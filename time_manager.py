import math
from plyer import notification
from constants import RED, GREEN, PINK

class PomodoroTimer:
    """Handles the logic for the app timer methods."""
    def __init__(self, app):
        self.app = app
        self._reps = 0
        self._work_min = 25
        self._short_break = 5
        self._long_break = 20
        self._timer = None

    def _countdown(self, count):
        minute = math.floor(count / 60)
        seconds = count % 60

        if seconds < 10:
            seconds = f"0{seconds}"

        self.app.canvas.itemconfig(self.app.timer_text, text=f"{minute}:{seconds}")

        if count > 0:
            self._timer = self.app.root.after(1000, self._countdown, count - 1)
        else:
            self.start()
            tomato = ""
            for _ in range(math.floor(self._reps / 2)):
                tomato += "🍅"
                self.app.tomato_label.config(text=tomato)

    def start(self):
        self._reps += 1
        if self._reps % 8 == 0:
            self.app.timer_label.config(text="Long Break", fg=RED)
            self._send_notification("Time for a Long Break!", "Take 20 minutes to recharge.")
            self._countdown(self._long_break * 60)
        elif self._reps % 2 == 0:
            self.app.timer_label.config(text="Short Break", fg=PINK)
            self._send_notification("Short Break", "Take 5 minutes to stretch or grab some water.")
            self._countdown(self._short_break * 60)
        else:
            self.app.timer_label.config(text="Work", fg=GREEN)
            self._countdown(self._work_min * 60)

    def reset(self):
        self.app.root.after_cancel(self._timer)
        self.app.timer_label.config(text="Timer", fg=GREEN)
        self.app.canvas.itemconfig(self.app.timer_text, text="00:00")
        self.app.tomato_label.config(text="")
        self._reps = 0

    def _send_notification(self, title: str, message: str):
        """Send a desktop notification."""
        notification.notify(
            title = title,
            message = message,
            timeout = 10,
            app_name = "Pomodoro App",
            app_icon = "asset/tomato.ico"
        )
