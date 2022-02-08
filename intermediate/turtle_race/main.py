import random
import turtle
from turtle import Turtle, Screen

is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What color will win the race?:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtles() -> list[Turtle]:
    turtles = []

    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtles.append(turtle)

    return turtles


def turtle_start_point():
    x = -230
    y = -100

    for turtle in turtles:
        turtle.goto(x, y)
        y += 20


def start_race():
    global is_racing

    if not is_racing:
        is_racing = True

    winner = None

    while is_racing:
        for turtle in turtles:
            if turtle.xcor() >= 250:
                is_racing = False
                winner = turtle
            distance = random.randint(0, 30)
            turtle.forward(distance=distance)

    announce_results(winner=winner)


def announce_results(winner: Turtle):
    user_won = False
    if user_bet.lower() == winner.fillcolor().lower():
        user_won = True

    announce_string = ""

    if user_won:
        announce_string += "You won! "
    else:
        announce_string += "You lost! "

    turtle.textinput(f"{announce_string}", f"The winning color was {winner.fillcolor()}.")



turtles = create_turtles()
turtle_start_point()
start_race()


screen.exitonclick()
