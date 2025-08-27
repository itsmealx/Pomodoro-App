from tkinter import *
from constants import YELLOW, GREEN, RED, FONT_NAME

class PomodoroApp:
    """Handles the User Interface for the app."""
    def __init__(self, **timer):
        self.start_timer = timer.get("start")
        self.reset = timer.get("reset")
        self.root = Tk()
        self.root.title("Pomodoro App")
        self.root.config(padx=100, pady=50, bg=YELLOW)
        self._tomato_bg = PhotoImage(file="asset/tomato.png")
        self.display()

    def display(self):
        self._lock_screensize()
        self._canvas()
        self._labels()
        self._buttons(self.start_timer, self.reset)

    def _lock_screensize(self):
        """Lock the screensize and centers the app when running."""
        self.root.resizable(False, False)
        window_width = 500
        window_height = 500

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def run(self):
        """Runs the app."""
        self.root.mainloop()

    def _canvas(self):
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self._tomato_bg)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
        self.canvas.grid(column=1, row=1)

    def _labels(self):
        self.timer_label = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
        self.timer_label.grid(column=1, row=0)

        self.tomato_label = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=RED)
        self.tomato_label.grid(column=1, row=3)

    def _buttons(self, start_timer, reset_timer):
        start = Button(text="Start", font=(FONT_NAME, 10, "normal"), command=start_timer)
        start.grid(column=0, row=2)

        reset = Button(text="Reset", font=(FONT_NAME, 10, "normal"), command=reset_timer)
        reset.grid(column=2, row=2)