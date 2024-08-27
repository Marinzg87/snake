from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.message = f"Scorecard: {self.points}"
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.color("white")
        self.write(self.message, align='center', font=('monaco', 10, 'normal'))

    def add_point(self):
        self.points += 1
        self.message = f"Scorecard: {self.points}"
        self.clear()
        self.write(self.message, align='center', font=('monaco', 10, 'normal'))
