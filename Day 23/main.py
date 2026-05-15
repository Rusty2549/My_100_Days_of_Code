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
scoreboard.level()
level_up = False
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if counter % 6 == 0:
        car_manager.spawn_car()

    car_manager.move_cars()

    if player.ycor() >= 280.0 and not level_up:
        level_up = True
        player.finish_line()
        if scoreboard.current_level == 3:
            scoreboard.you_win()
            game_is_on = False
        else:
            scoreboard.increase_level()
            car_manager.increase_speed()
    if player.ycor() <= -280:
        level_up = False

    # collision detection
    counter += 1

    #Check distance of player to cars
    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
