from interface import PomodoroApp
from time_manager import PomodoroTimer

timer = PomodoroTimer(None)
app = PomodoroApp(start=timer.start, reset=timer.reset)
timer.app = app

app.run()