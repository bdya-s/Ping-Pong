import time
from turtle import Turtle, Screen
from players import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

paddle1 = Paddle(-390, 0)
paddle2 = Paddle(380, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()
    if ball.ycor() > 290.0 or ball.ycor() < -290:
        ball.bounce(1, -1)

    if ball.distance(paddle2) < 50 and ball.xcor() > 340 or ball.distance(paddle1) < 40 and ball.xcor() < -340:
        ball.bounce(-1, 1)

    if ball.xcor() > 440:
        score.right_score_update()

    if ball.xcor() < -440:
        score.left_score_update()
        ball.reset_position()

screen.exitonclick()

