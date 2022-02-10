import time
from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball

# INCOMPLETE
# TODO: Bug when ball going to left side of screen, bouncing without paddle
# TODO: Score not showing up
# TODO: Bug when hitting very top/bottom of paddle, making ball bounce between paddle and nothing for a bit


screen = Screen()

screen.bgcolor("black")
screen.title("Cetti's Pong")
screen.tracer(0)
screen.setup(width=800, height=600)

r_paddle = Paddle(player=1)
l_paddle = Paddle(player=2)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect upper wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with player 1 paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) \
            or (ball.distance(l_paddle) > -50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_score(2)

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.update_score(1)


screen.exitonclick()
