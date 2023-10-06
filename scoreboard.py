from turtle import Turtle
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-40, 260)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(40, 260)
        self.write(self.r_score, align="center", font=FONT)

    def left_score_update(self):
        self.l_score += 1
        self.score_update()

    def right_score_update(self):
        self.r_score += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)
