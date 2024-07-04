# PONG GAME
import turtle as t
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball_1 = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball_1.sleep_time)
    screen.update()
    ball_1.move()

    # Detect collision with the wall
    if ball_1.ycor() > 280 or ball_1.ycor() < -280:
        ball_1.bounce_y()
    # Detect collision with paddles.
    if ball_1.distance(paddle_r) < 50 and ball_1.xcor() > 320 or ball_1.distance(paddle_l) < 50 and ball_1.xcor() < -320:
        ball_1.bounce_x()
    # Detect if ball went out of bounds for left paddle
    if ball_1.xcor() > 380:
        ball_1.restart()
        scoreboard.l_point()
        sleep_time = 0.05
    if ball_1.xcor() < -380:
        ball_1.restart()
        scoreboard.r_point()
        sleep_time = 0.05


screen.exitonclick()
