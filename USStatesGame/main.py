import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=800, height=600)
text = turtle.Turtle()
text.penup()
text.hideturtle()
image = "./blank_states_img.gif"
states = "./50_states.csv"
screen.addshape(image)
turtle.shape(image)
df = pandas.read_csv(states)
answer = screen.textinput("Guess the states", "Enter the name of the state").title()
score = 0
game_is_on = True
states = list(df.state)
while game_is_on:
    if answer in states:
        x = int(df[df.state == answer].x) - 20
        y = int(df[df.state == answer].y)
        text.goto(x, y)
        text.write(answer, font=("Courier", 12, "bold"))
        score += 1
        states.remove(answer)

    answer = screen.textinput(f"{score}/50 States correct", "Enter the name of the state").title()
    if answer == "Exit" or not states or not answer:
        break

data_dict = {"states": [state for state in states]}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("to learn.csv")

screen.mainloop()
