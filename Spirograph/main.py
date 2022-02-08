import turtle
from func import random_colors
tim = turtle.Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.hideturtle()

for _ in range(36):
    tim.pencolor(random_colors())
    tim.circle(radius=100)
    tim.setheading(tim.heading()+10)

my_screen = turtle.Screen()
my_screen.exitonclick()

# # Turtle Star
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
