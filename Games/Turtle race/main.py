import random
from turtle import Turtle, Screen
from random import randint


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


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "purple"]
# y_positions = [-100, -50, 0, 50, 100]
i = -150
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    i = i + 50
    # tim.goto(-230, y_positions[turtle_index])
    new_turtle.goto(-230, i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You're won! The {winning_color} turtle is a winner!")
            else:
                print(f"You're lost! The {winning_color} turtle is a winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()