from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.num_of_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.setposition(position)
            self.num_of_segments.append(new_turtle)
        self.head = self.num_of_segments[0]
        self.head.color("violet")

    def move(self):
        for index in range(len(self.num_of_segments) - 1, 0, -1):
            new_x = self.num_of_segments[index - 1].xcor()
            new_y = self.num_of_segments[index - 1].ycor()
            self.num_of_segments[index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
        return

    def up(self):
        if self.head.heading() in (RIGHT, LEFT):
            self.head.setheading(UP)
            self.head.forward(MOVE_DISTANCE)
        return

    def right(self):
        if self.head.heading() in (UP, DOWN):
            self.head.setheading(RIGHT)
        return

    def left(self):
        if self.head.heading() in (UP, DOWN):
            self.head.setheading(LEFT)
        return

    def down(self):
        if self.head.heading() in (RIGHT, LEFT):
            self.head.setheading(DOWN)
            self.head.forward(MOVE_DISTANCE)
        return

    def increase_tail(self):

        tail_turtle = Turtle(shape="square")
        tail_turtle.penup()
        tail_turtle.color("white")
        self.num_of_segments.append(tail_turtle)
        self.move()

