from turtle import Turtle, Screen

# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake = []
        self.create_new_snake()
        self.snake_head = self.snake[0]

    def create_new_snake(self) -> None:
        for position in STARTING_POSITIONS:
            part = Turtle("square")

            part.penup()
            part.color("white")
            part.goto(position)
            self.snake.append(part)

    def move(self):
        for part_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_num - 1].xcor()
            new_y = self.snake[part_num - 1].ycor()
            self.snake[part_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def add_length(self):
        tail = self.snake[-1]
        tails_position = tail.position()
        part = Turtle("square")
        part.penup()
        part.color("white")
        part.goto(tails_position)
        self.snake.append(part)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

