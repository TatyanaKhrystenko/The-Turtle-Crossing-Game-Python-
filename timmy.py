from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5, 1.5)
        self.color("yellow", "green")
        self.setheading(90)
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


