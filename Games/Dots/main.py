# import colorgram

# colors = colorgram.extract('paint.jpg', 30)
# rgb_colors = []
#
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     temp = (r, g, b)
#     rgb_colors.append(temp)
#
# print(rgb_colors)

import turtle as t
from random import choice

color_list = [(188, 74, 20), (56, 34, 13), (149, 26, 9), (237, 226, 77), (24, 31, 60),
              (113, 167, 210), (45, 85, 143), (227, 243, 238), (217, 154, 82), (34, 50, 124), (191, 144, 25),
              (26, 51, 29), (201, 93, 126), (242, 214, 6), (119, 35, 51), (120, 187, 149),
              (55, 129, 74), (70, 82, 17), (36, 84, 40), (142, 51, 58), (74, 128, 200), (205, 86, 62), (82, 31, 44),
              (104, 180, 70), (148, 204, 223), (197, 120, 162), (23, 77, 100)]

"""10x10, dots should be 20 phases inside and distance between dots = 50"""

leo = t.Turtle()
screen = t.Screen()

t.colormode(255)
leo.penup()
leo.hideturtle()
x = -220
y = -200
leo.goto(x, y)
for _ in range(10):
    for _ in range(10):
        leo.pencolor(choice(color_list))
        leo.dot(20)
        leo.goto(leo.xcor() + 50, y)
    y = y + 50
    leo.goto(x, y)

screen.exitonclick()
