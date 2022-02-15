from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-250, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(POSITION)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")
