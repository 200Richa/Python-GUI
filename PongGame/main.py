from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO 1.Set up the main screen
# TODO 2.Create and move the paddle
# TODO 3.Create another paddle
# TODO 4.Create and move the ball
# TODO 5.Detect collision with the wall
# TODO 6.Detect collision with the paddle
# TODO 7.Detect when paddle misses
# TODO 8.Keep score


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(x_cor=350, y_cor=0)
l_paddle = Paddle(x_cor=-350, y_cor=0)

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_down, key="d")

my_ball = Ball()
my_score = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(my_score.sleep_time)
    screen.update()
    my_ball.move()
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()
    if my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 320 or my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_x()
    if my_ball.xcor() > 380:
        my_ball.reset()
        my_score.l_score += 1
        my_score.write_score()
    if my_ball.xcor() < -380:
        my_ball.reset()
        my_score.r_score += 1
        my_score.write_score()


screen.mainloop()

