from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        test = "kek"
        self.write(f"Score = {test}", align="center", font=("Arial", 15, "normal"))



