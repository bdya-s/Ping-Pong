import random
from turtle import Turtle, Screen

class Ball(Turtle):
    screen = Screen()

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, val1, val2):
        self.x_move *= val1
        self.y_move *= val2

    def reset_position(self):
        self.home()
        self.move_ball()

