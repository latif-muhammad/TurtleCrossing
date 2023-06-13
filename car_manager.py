import random
from turtle import Turtle


COLORS = ["red", "blue", "green", "yellow", "purple"]
STARTING_MOVE_DIS = 0.19
MOVE_INC = 0.2


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        change_of_new = random.randint(0, 100)
        if change_of_new == 4:
            new_car = Turtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            car_position = random.randint(-220, 250)
            new_car.goto(300, car_position)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DIS)

    def increase_speed(self):
        global STARTING_MOVE_DIS
        STARTING_MOVE_DIS += MOVE_INC

