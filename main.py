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

screen.listen()
screen.onkey(fun = player.move_up,key = "Up")
screen.onkey(fun = player.move_down,key = "Down")

game_is_on = True
cont = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cont +=1
    carManager.moveCar()

    ##Collision

    for car in carManager.list_cars:
        if(car.distance(player)<20):
            game_is_on = False

    if(cont==6):
        carManager.createCar()
        cont=0

time.sleep(1000)

