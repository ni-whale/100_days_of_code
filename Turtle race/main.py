from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
i = -150

t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")
turtles.append(t1)
turtles.append(t2)
turtles.append(t3)
turtles.append(t4)
turtles.append(t5)


for turtle in turtles:
    turtle.color(choice(colors))
    turtle.penup()
    i = i+50
    turtle.goto(-230, i)

print(turtles)

# leo = Turtle(shape="turtle")
# leo.penup()
# leo.goto(x=-230, y=0)

screen.exitonclick()