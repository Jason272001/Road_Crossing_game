from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_cahnce=random.randint(1,4)
        if random_cahnce == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1.25, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-300, 350)
            new_car.goto(360, random_y)
            self.cars.append(new_car)
    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += 5