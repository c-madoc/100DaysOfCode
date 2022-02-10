from turtle import Turtle


STYLE = ("Courier", 20, "normal")
ALIGN = "center"
SET_POSITION = (0, 350)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_paddle = 0
        self.l_paddle = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.setposition(SET_POSITION)
        self.goto(SET_POSITION)
        self.update_score()

    def update_score(self, player=0):
        if player == 1:
            self.r_paddle += 1
        elif player == 2:
            self.l_paddle += 1

        self.clear()
        self.write(arg=f"{self.l_paddle}  |  {self.r_paddle}", font=STYLE, align=ALIGN)

        print(f"{self.l_paddle}  |  {self.r_paddle}")

