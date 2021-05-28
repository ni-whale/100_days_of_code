from turtle import Turtle, Screen
from random import choice


# def unique_color():
#     picked_color = choice(colors)
#     not_unique = True
#     while not_unique:
#         for used_color in used_colors:
#             if picked_color != used_color:
#                 used_colors.append(picked_color)
#                 print(used_colors)
#                 not_unique = False
#                 return picked_color
#             else:
#                 picked_color = choice(colors)

            # used_colors.append(picked_color)
            # not_unique = False
            # print(used_colors)
            # return picked_color



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "green", "blue", "purple"]
used_colors = ['yellow']
turtles = []
i = -150
c = 0

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
    turtle.color(colors[c])
    c = c + 1
    turtle.penup()
    i = i+50
    turtle.goto(-230, i)

print(turtles)



screen.exitonclick()