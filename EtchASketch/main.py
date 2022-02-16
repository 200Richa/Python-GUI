from turtle import Turtle, Screen
from random import randint
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("#fcd1d1")
colors = ["yellow", "red", "orange", "blue", "violet", "green"]
y_position = -110
in_motion = True
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.fillcolor(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position)
    y_position += 40
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race? Choose its color:  ")

while in_motion:
    for i in all_turtle:
        steps = randint(0, 10)
        i.forward(steps)
        if i.xcor() >= 230.0:
            in_motion = False
            if i.fillcolor() == user_bet:
                messagebox.showinfo(title="YIPPEE!!", message="You Won")
            else:
                messagebox.showinfo(title="Oops!!", message=f"You Lost\nThe {i.fillcolor()} turtle won the race.")
            break


screen.mainloop()
