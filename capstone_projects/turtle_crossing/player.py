from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reached_other_side(self) -> bool:
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def reset_position(self):
        self.goto(STARTING_POINT)
