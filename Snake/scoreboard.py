from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=-20, y=270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.write_score()
        self.goto(-20, 0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)