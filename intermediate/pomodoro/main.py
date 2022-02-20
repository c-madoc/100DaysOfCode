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
    global timer
    global reps

    window.after_cancel(timer)
    check["text"] = ""
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def add_check():
    if len(check["text"]) > 0:
        check["text"] += " "
    check["text"] += "X"


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 and reps != 0:
        timer_label.config(text="Long\nBreak", fg=PINK)
        add_check()
        countdown(long_break_sec)
    elif reps % 2 == 0 and reps != 0:
        timer_label.config(text="Short\nBreak", fg=PINK)
        add_check()
        countdown(short_break_sec)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    global timer

    minutes = math.floor(count / 60)
    seconds = count % 60
    seconds = f"0{seconds}" if seconds < 10 else seconds

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count >= 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# TIMER STRING
timer_label = Label(text="TIMER", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2, sticky="e")

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2, sticky="w")

# CHECKMARK

check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
check.grid(column=1, row=3, sticky="n")

# TOMATO IMAGE
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
