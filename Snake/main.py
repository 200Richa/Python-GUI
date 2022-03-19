from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_tail()

    if (snake.head.xcor() >= 300) or (snake.head.xcor() <= -300) or (snake.head.ycor() >= 300) or (snake.head.ycor() <= -300):
        game_is_on = False
        scoreboard.write_score()
        scoreboard.goto(-50, 0)
        scoreboard.write(arg="Game Over", font=("Arial", 20, "normal"))

    for segment in snake.num_of_segments[1:len(snake.num_of_segments)]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            screen.update()
            scoreboard.write_score()
            scoreboard.goto(-50, 0)
            scoreboard.write(arg="Game Over", font=("Arial", 20, "normal"))

screen.exitonclick()
