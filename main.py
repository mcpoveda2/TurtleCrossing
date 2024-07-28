import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun = player.move_up,key = "Up")
screen.onkey(fun = player.move_down,key = "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.moveCar()
    carManager.createCar()

    ##Collision

    for car in carManager.list_cars:
        if(car.distance(player)<20):
            scoreboard.game_over()
            game_is_on = False

    ## Wining

    if(player.is_at_finish_line()):
        player.go_to_start()
        carManager.level_up()
        scoreboard.increse_level()

screen.exitonclick()

