from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
counter = 0
screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

game_is_on = True

player=Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_up, "Up")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if counter % 6 == 0:
        car_manager.spawn_car()
    car_manager.move_cars()
    counter += 1

    #Check distance of player to cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
screen.exitonclick()
