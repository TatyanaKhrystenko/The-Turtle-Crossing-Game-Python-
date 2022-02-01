from turtle import Screen
from timmy import Timmy
from car import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

timmy = Timmy()
score = Scoreboard()
car_manager = CarManager()




screen.listen()
screen.onkey(timmy.move, "Up")



is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.car_moving()


    for car in car_manager.cars:
        if timmy.distance(car) < 30:
            score.game_over()
            is_on = False

    if timmy.ycor() == 280:
        timmy.refresh()
        score.increase_level()
        car_manager.increase_speed()
screen.exitonclick()