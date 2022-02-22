import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move()

    if player.reached_other_side():
        scoreboard.update_level()
        player.reset_position()
        cars.speed += 1

    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()