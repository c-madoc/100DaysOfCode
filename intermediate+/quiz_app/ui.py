from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # -- SCORE
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        # -- BUTTON
        self.true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_image, highlightthickness=0, command=self.user_guessed_true)
        self.true_btn.grid(column=1, row=2)

        # -- BUTTON
        self.false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_image, highlightthickness=0, command=self.user_guessed_false)
        self.false_btn.grid(column=0, row=2)

        # -- CANVAS
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="x",
                                                     font=FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Get the next question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def user_guessed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_guessed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

        self.score_label.config(text=f"Score: {self.quiz.score}")

