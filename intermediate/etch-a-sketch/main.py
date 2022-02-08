from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()


def move_forward():
    draw.forward(20)


def move_backwards():
    draw.back(20)


def turn_right():
    heading = draw.heading()
    draw.setheading(heading + 10)


def turn_left():
    heading = draw.heading()
    draw.setheading(heading - 10)


def clear_screen():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
