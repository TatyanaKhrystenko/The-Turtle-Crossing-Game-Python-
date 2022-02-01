from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 260)
        self.color("black")
        self.write(f"Level: {self.level}", False, align="center", font=("Arial", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER.", False, align="center", font=("Arial", 20, "normal"))
