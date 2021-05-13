import turtle as t
from random import choice

tim = t.Turtle()

side_quantity = 3

shape_colors = ["red", "blue", "green", "yellow", "pink", "orange", "DarkGreen", "AntiqueWhite", "cyan4", "DeepPink",
                "DeepSkyBlue"]

for _ in range(8):
    tim.pencolor(choice(shape_colors))
    for sides in range(side_quantity):
        tim.right(360/side_quantity)
        tim.forward(100)
    side_quantity += 1


screen = t.Screen()
screen.exitonclick()
