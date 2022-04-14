from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.refresh()

    def refresh(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def gave_over(self):
        self.reset()
        self.write("GAME OVER", align="center", font=FONT)

