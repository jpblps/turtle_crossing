import random
import time
from turtle import Turtle

COLORS = ["#BFBFBF", "#737373", "#404040"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.x_positions = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300]
        self.y_positions = [-230, -180, -130, -80, -30, 20, 70, 120, 170, 220]
        self.pu()
        self.hideturtle()
        a = -230
        for x in range(9):
            self.goto(0, a)
            self.color("#737373")
            self.write("  -  -  -  -  -  -  -  -  -  -  -  -  -  -", False, "center", ("arial", 38, "normal"))
            a += 50

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.goto(random.choice(self.x_positions), random.choice(self.y_positions))
        self.cars.append(car)

    def traffic_control(self):
        for car in self.cars:
            if car.xcor() < -310:
                car.goto(310, random.choice(self.y_positions))

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
