import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset the timer and labels."""
    root.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(tagOrId=timer_canvas, text="00:00")
    tomato_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer."""
    global reps
    reps += 1

    work_in_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0: #if it's the 8th rep, long break for 20 minutes
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0: #if its 2nd/4th/6th rep, short break for 5 minutes
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break)
    else: #1st/3rd/5th/7th, work for 25 minutes
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_in_sec)


# --------------------------- COUNTDOWN MECHANISM ---------------------------- #
def count_down(count: int):
    """Start the countdown based on the given value."""
    mins = math.floor(count / 60) #rounding down the number to the nearest int
    sec = count % 60 #getting the remainder as the remaining second/s

    #dynamic typing in Python: allowing change in data type just by assigning it to different type of value
    #i.e. #a = 10 -> an int type
        #a = "hello" -> str type, changed the value type from int to str
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(tagOrId=timer_canvas, text=f"{mins}:{sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        tomato_ind = ""
        for _ in range(math.floor(reps/2)):
            tomato_ind += "🍅"
            tomato_label.config(text=tomato_ind) #adding tomato indicator for every 2 work reps



# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro App")
root.config(padx=100, pady=50, bg=YELLOW)
root.resizable(False, False)

#Setting the window to be at the center of the screen when the program runs
#Getting screen dimension
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Calculating the position
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


#Canvas creation
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_bg = PhotoImage(file="tomato.png") #adding image to canvas
canvas.create_image(100, 112, image=tomato_bg)
timer_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


#Label
timer_label = Label(text="Timer",font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

tomato_label = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=RED)
tomato_label.grid(column=1, row=3)

#Buttons
start = Button(text="Start", font=(FONT_NAME, 10, "normal"), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 10, "normal"), command=reset_timer)
reset.grid(column=2, row=2)


root.mainloop()