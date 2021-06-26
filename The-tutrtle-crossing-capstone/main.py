import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_creating()
    car_manager.traffic()

    # Detect collision with cars
    for car in car_manager.cars_list:
        if player.distance(car) < 18:
            scoreboard.gave_over()
            game_is_on = False

    # Detect collision with the finish line
    if player.refresh():
        scoreboard.level += 1
        scoreboard.refresh()
        car_manager.speed_increasing()

screen.exitonclick()

