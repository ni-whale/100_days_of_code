from turtle import Turtle, Screen
from random import choice


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["michelangelo", "raphael", "donatello", "leonardo", "shredder"]
turtles = []
i = -150

for turtle in names:
    turtle = Turtle(shape="turtle")
    turtle.color(choice(colors))
    turtle.penup()
    turtle.goto(-230, i+20)

print(turtles)

# leo = Turtle(shape="turtle")
# leo.penup()
# leo.goto(x=-230, y=0)

screen.exitonclick()