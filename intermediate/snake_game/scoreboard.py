from turtle import Turtle

STYLE = ("Courier", 20, "normal")
ALIGN = "center"
SET_POSITION = (0, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highscore.txt") as data:
            self.highscore = int(data.read())

        self.color("white")
        self.penup()
        self.goto(SET_POSITION)
        self.hideturtle()
        self.update_score()

    def update_score(self, start_size=0, snake_size=0):
        self.clear()
        self.score = snake_size - start_size
        self.write(arg=f"Score: {self.score} | Highscore: {self.highscore}", font=STYLE, align=ALIGN)

    def reset(self) -> None:
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()

