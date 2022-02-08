import random
import turtle

import colorgram
from turtle import Turtle


def get_color_pallet(image: str):
    rbg_colors = []
    colors = colorgram.extract(image, 30)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        if r > 220 and g > 220 and b > 220:
            continue

        if r == 0 and g == 0 and b == 0:
            continue

        rbg_colors.append(new_color)
    return rbg_colors


def random_color(colors):
    return random.choice(colors)


def flumequine_style(spacing=50, side_size=5):
    colors = get_color_pallet('mmc-bkgd.jpg')

    EAST = 0
    NORTH = 90
    WEST = 180
    SOUTH = 270

    turtle.colormode(255)

    draw = Turtle()
    draw.hideturtle()
    draw.speed("fastest")
    draw.penup()

    draw.setheading(WEST)
    draw.forward(spacing * (side_size/2))
    draw.setheading(SOUTH)
    draw.forward(spacing * (side_size/2))

    for _ in range(side_size):

        draw.setheading(EAST)
        for _ in range(side_size):
            draw.dot(20, random_color(colors))
            draw.forward(spacing)

        draw.setheading(NORTH)
        draw.forward(spacing)
        draw.setheading(WEST)
        draw.forward(spacing * side_size)


flumequine_style(side_size=10)
turtle.exitonclick()




