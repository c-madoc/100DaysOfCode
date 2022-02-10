from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player: int):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()

        if player == 1:
            self.goto(x=350, y=0)

        elif player == 2:
            self.goto(x=-350, y=0)

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
