from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sleep_time = 0.1
        self.write_score()


    def write_score(self):
        self.clear()
        self.sleep_time *= 0.9
        self.goto(x=-100, y=200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
