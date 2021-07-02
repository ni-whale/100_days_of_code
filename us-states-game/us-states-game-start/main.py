import turtle
import pandas

""" 
- Convert the guess to Title case
    - Check if the guess is among the 50 states
    - Write correct guesses onto the map
    - Use a loop to allow the user to keep guessing
    - Record the correct guesses in a list
    - Keep track of the score     
"""


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

data = pandas.read_csv("50_states.csv")
guessed_states = []

# while game_is_on:
#     answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
#     for state in data.state:
#         if str(state).lower() == answer_state.lower():
#             guessed_states.append(answer_state)

# while game_is_on:
#     answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
#     temp = data[data.state == answer_state]
#     guessed_states.append(temp)

while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    for df in data:
        # if str(df.state).lower() == answer_state.lower():
        #     guessed_states.append(answer_state)
        print(df.state)





    print(guessed_states)



# def get_mouse_click_coordinates(x, y):
"""Code to find out x, y location based on the U.S.A. map attached to this project"""
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()

