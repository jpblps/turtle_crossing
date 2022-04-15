import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#262626")
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "w")

scoreboard = Scoreboard()

car_manager = CarManager()

for _ in range(20):
    car_manager.create_car()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.traffic_control()
    car_manager.move_cars()

    if player.ycor() > 270:
        player.player_wins()
        scoreboard.level += 1
        car_manager.level_up()
        time.sleep(3)

    for car in car_manager.cars:
        if player.distance(car) < 29:
            scoreboard.player_loses()
            time.sleep(0.1)
            game_is_on = False

    scoreboard.track_level()
