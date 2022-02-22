import random
from tkinter import *
import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")
TIMER = ("Ariel", 16, "bold")
DELAY = 5

df = pd.read_csv("data/french_words.csv")
words = df.to_dict(orient="records")

known_words = []

timer = None
card = None


# WORD CONTROLLER
def new_card():
    global card
    global known_words

    if card in known_words:
        words.remove(card)

    if len(words) == 0:
        canvas.itemconfig(title_text, text="Well done", fill="black")
        canvas.itemconfig(word_text, text="", fill="black")
        canvas.itemconfig(score_text, text=f"Remaining: 0")
        canvas.itemconfig(timer_text, text=f"")
        card = None

    else:
        card = random.choice(words)
        canvas.itemconfig(score_text, text=f"Remaining: {len(words)}")

        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=card["French"].lower(), fill="black")

        reset_timer()
        run_timer(DELAY)


def known_word():
    global card
    global known_words

    if card is not None:
        known_words.append(card)

    new_card()


def unknown_word():
    global card
    new_card()


def reset_timer():
    global timer

    if timer is not None:
        window.after_cancel(timer)


def run_timer(count):
    global timer
    global words

    if len(words) != 0:
        if count > 0:
            timer = window.after(1000, run_timer, count - 1)
            canvas.itemconfig(timer_text, text=count)
        else:
            flip_card()
            canvas.itemconfig(timer_text, text="")


def flip_card():
    global card

    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=card["English"], fill="black")


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# IMAGES
wrong_img = PhotoImage(file="images/wrong.png")
correct_img = PhotoImage(file="images/right.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# BUTTONS
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=unknown_word)
correct_btn = Button(image=correct_img, highlightthickness=0, command=known_word)

wrong_btn.grid(column=0, row=1)
correct_btn.grid(column=1, row=1)

# FLASHCARD
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=LANGUAGE)
word_text = canvas.create_text(400, 263, text="", font=WORD)
timer_text = canvas.create_text(700, 50, text="", font=TIMER)
score_text = canvas.create_text(700, 100, text="", font=TIMER)
canvas.grid(column=0, row=0, columnspan=2)

new_card()

window.mainloop()
