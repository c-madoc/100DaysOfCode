import random
import turtle
from turtle import Turtle, Screen

draw = Turtle()

draw.shape("classic")


def draw_square():
    def line_and_turn():
        draw.forward(100)
        draw.left(90)

    for i in range(4):
        line_and_turn()


def draw_dashes(amount_of_dashes=10):
    def draw_dash():
        draw.forward(10)
        draw.penup()
        draw.forward(10)
        draw.pendown()

    for i in range(amount_of_dashes):
        draw_dash()

def draw_object(sides: int, color: str):
    degree = 360 / sides

    print(degree)
    draw.speed(None)
    draw.color(color)

    turn_left = bool(random.getrandbits(1))

    for i in range(sides):
        draw.forward(100)
        if (turn_left):
            draw.left(degree)
        else:
            draw.right(degree)

# for x in range(3, 20):
#     colors = ["red", "blue", "green", "orange", "brown", "pink"]
#     color = random.choice(colors)
#     draw_object(x, color)

#
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     turtle.colormode(255)
#
#     draw.pensize(3)
#     draw.pencolor((r, g, b))
#     draw.speed(1000)
#     draw.forward(30)
#     draw.setheading(random.choice(directions))
def draw_circle():
    draw.speed("fastest")
    draw.circle(100)

def draw_spirograph(amount: int):

    radius = 360 / amount
    size = 2

    second = 360 / (amount * 2)
    third = 360 / (amount * 3)

    # dark red
    for _ in range(amount):
        draw.color("BlueViolet")
        draw.pensize(size)
        draw_circle()
        draw.setheading(draw.heading() + radius)

    for _ in range(int(second)):
        draw.color("Blue")
        draw.pensize(size)
        draw_circle()
        draw.setheading(draw.heading() + radius)

    for _ in range(int(third)):
        draw.color("Red")
        draw.pensize(size)
        draw_circle()
        draw.setheading(draw.heading() + radius)


draw_spirograph(20)

screen = Screen()

screen.exitonclick()
