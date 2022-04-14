from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


def data_reading():
    with open("data.txt", mode="r") as file:
        return file.read()


def data_collecting(h_score):
    with open("data.txt", mode="w") as file:
        file.write(str(h_score))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        self.high_score = int(data_reading())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data_collecting(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
