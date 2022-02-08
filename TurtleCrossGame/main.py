import turtle
from car import Car
from my_turtle import My_turtle
from scoreboard import Scoreboard
import time
sleep_time = 0.5
screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.title("Turtle Cross")
screen.tracer(0)
screen.listen()

tim = My_turtle()
screen.onkey(fun=tim.move_up, key="Up")
screen.onkey(fun=tim.move_down, key="Down")

score = Scoreboard()

my_car = Car()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    my_car.move()
    my_car.create_cars()
    my_car.delete()
    screen.update()
    if tim.ycor() > 280:
        score.level += 1
        score.write_score()
        tim.goto(x=0, y=-290)
        sleep_time *= 0.9
    for car in my_car.present_cars:
        if car.distance(tim) < 30:
            game_is_on = False
            break
    screen.update()

screen.exitonclick()
