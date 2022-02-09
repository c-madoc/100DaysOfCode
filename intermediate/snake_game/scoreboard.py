from turtle import Turtle

STYLE = ("Courier", 20, "normal")
ALIGN = "center"
SET_POSITION = (0, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.setposition(SET_POSITION)
        self.update_score()

    def update_score(self, start_size=0, snake_size=0):
        self.clear()
        self.write(arg=f"Score: {snake_size - start_size}", font=STYLE, align=ALIGN)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", font=STYLE, align=ALIGN)
