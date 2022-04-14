import turtle as t
import random

tim = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tim.pencolor(r, g, b)


directions = [0, 90, 180, 270]
tim.pensize(7)
tim.speed("fastest")
screen = t.Screen()

screen.colormode(255)

for _ in range(200):
    random_color()
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()