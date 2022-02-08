from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=-210, y=240)
        self.write(f"Level:{self.level}", align="center", font=("Courier", 35, "normal"))
