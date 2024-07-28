import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.list_cars = []

    def add_car(self):
        self.createCar()

    def createCar(self):
        random_chance = random.randint(1,6)
        if(random_chance == 1):
            car = Turtle("square")
            car.penup()
            color = random.choice(COLORS)
            car.color(color)
            car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-250, 250)
            car.goto(320, y_pos)
            self.list_cars.append(car)

    def moveCar(self):
        for car in self.list_cars:
            car.goto(car.xcor()-STARTING_MOVE_DISTANCE,car.ycor())


