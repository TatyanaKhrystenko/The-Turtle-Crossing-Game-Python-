from turtle import Turtle
import random

car_colors = ("yellow", "blue", "grey", "pink", "green", "brown", "red")
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color("black", random.choice(car_colors))
            y_position = random.randint(-230, 230)
            new_car.goto(300, y_position)
            self.cars.append(new_car )

    def car_moving(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT