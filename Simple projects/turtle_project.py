# from turtle import Turtle, Screen
#
#
# antony = Turtle()
# print(antony)
# antony.shape("turtle")
# antony.color("DarkRed")
# antony.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "c"
print(table)