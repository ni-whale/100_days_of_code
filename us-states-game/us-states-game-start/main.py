import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
# turtle.shape(image)

game_is_on = True

data = pandas.read_csv("50_states.csv")
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    if data.state.:
        guessed_states.append(answer_state)

    print(guessed_states)



# def get_mouse_click_coordinates(x, y):
"""Code to find out x, y location based on the U.S.A. map attached to this project"""
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()

