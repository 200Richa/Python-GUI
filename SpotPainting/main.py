import turtle as t
from color_func import color_extract
from random import choice

tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")
list_of_colors = color_extract("spot_painting.jpg", 50)
tim.penup()
tim.setposition(-230, -200)
tim.hideturtle()

for j in range(1, 10):
    for _ in range(10):
        tim.dot(20, choice(list_of_colors))
        tim.forward(50)
    tim.setposition(-230, -200 + 50*j)

my_screen = t.Screen()
my_screen.mainloop()
