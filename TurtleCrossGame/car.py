import turtle
from random import randint, choice, shuffle
X = [i for i in range(260, 301, 30)]
shuffle(X)
POSITIONS = [(choice(X), i) for i in range(280, -281, -20)]

turtle.colormode(255)


class Car:

    def __init__(self):
        self.present_cars = []
        self.create_cars()

    def create_cars(self):
        global POSITIONS
        num_cars = randint(0, 2)
        while num_cars:
            new_car = turtle.Turtle(shape="square")
            new_car.penup()
            #new_car.speed("slowest")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            car_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            new_car.color(car_color)
            current_position = choice(POSITIONS)
            new_car.goto(current_position)
            POSITIONS.remove(current_position)
            self.present_cars.append(new_car)
            num_cars -= 1
        POSITIONS = [(choice(X), i) for i in range(280, -281, -20)]

    def move(self):
        for car in self.present_cars:
            car.backward(40)

    def delete(self):
        for car in self.present_cars:
            if car.xcor() < -330:
                car.hideturtle()
                self.present_cars.remove(car)
