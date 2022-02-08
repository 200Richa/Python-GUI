from turtle import Turtle


class My_turtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-290)

    def move_up(self):
        self.forward(15)

    def move_down(self):
        self.backward(15)
