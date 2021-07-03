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

FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.penup()
t.hideturtle()

data = pandas.read_csv("50_states.csv")
guessed_states = []

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

game_is_on = True
while game_is_on:
    for state in data.state:
        if str(state).lower() == answer_state.lower():
            guessed_states.append(state)
            current_state = data[data.state == state]  # saving the filtered output to get access to x, y
            t.goto(float(current_state.x), float(current_state.y))
            t.write(f"{state}", font=FONT)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")  # updating title to keep correct answers

# Another variant:
# while game_is_on:
#     answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
#     temp = data[data.state == answer_state]
#     guessed_states.append(temp)


# def get_mouse_click_coordinates(x, y):
"""Code to find out x, y location based on the U.S.A. map attached to this project"""
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()
