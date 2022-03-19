from turtle import Turtle
from random import uniform

DEFAULT_SHAPE = "circle"
DEFAULT_COLOR = "blue"
DEFAULT_SPEED = "fastest"
STRETCH = 0.5
LIM_CORD = 270


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(DEFAULT_SHAPE)
        self.color(DEFAULT_COLOR)
        self.shapesize(stretch_len=STRETCH, stretch_wid=STRETCH)
        self.penup()
        self.speed(DEFAULT_SPEED)
        self.refresh()

    def refresh(self):
        self.goto(x=uniform(-LIM_CORD, LIM_CORD), y=uniform(-LIM_CORD, LIM_CORD))
