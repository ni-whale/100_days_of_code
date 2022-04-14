# import turtle as t
# import random
#
# tim = t.Turtle()
# screen = t.Screen()
# screen.colormode(255)
# angle = 1.5
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return tim.pencolor(r, g, b)
#
#
# tim.speed("fastest")
#
# for _ in range(240):
#     random_color()
#     tim.circle(100)
#     tim.right(angle)
#     angle += 1.5
#
#
#
# screen.exitonclick()


import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


