from turtle import Screen
from snake import Snake, STARTING_POSITIONS
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Cetti's Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.add_length()
        score.update_score(len(STARTING_POSITIONS), len(snake.snake))

    # collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score.reset()
        snake.reset()

    # collision with tail
    for snake_part in snake.snake[1:]:
        if snake.snake_head.distance(snake_part) < 10:
            score.reset()
            snake.reset()








screen.exitonclick()