from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars_list = []
        self.speed = STARTING_MOVE_DISTANCE
        self.random_chance = 0

    def car_creating(self):
        self.random_chance = random.randint(1, 6)
        if self.random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            # new_car.setheading(270)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.cars_list.append(new_car)

    def traffic(self):
        for car in self.cars_list:
            car.backward(self.speed)

    def speed_increasing(self):
        self.speed += MOVE_INCREMENT





