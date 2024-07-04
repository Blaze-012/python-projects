import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.onkey(player.move, "Up")
    screen.update()

    car_manager.create()
    car_manager.move_cars()

    # Detecting collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting end of level
    if player.ycor() == player.finish:
        time.sleep(0.1)
        player.level_up()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
