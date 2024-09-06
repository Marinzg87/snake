from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = int(self.read_high_score())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    def add_point(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            self.write_high_score()
        self.points = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
        return high_score

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
