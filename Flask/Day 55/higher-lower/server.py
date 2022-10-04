from flask import Flask
from random import randint


app = Flask(__name__)
random_number = randint(0, 9)
print(random_number)


def user_guessing_feedback(function):
    print(f"{function.__name__}")
    def wrapper(*args):
        print(f"{function.__name__}, {args}")
        if int(function(*args)) < random_number:
            return "<h1 style='red'>Too low, try again</h1> <img " \
           "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='too low:('> "
        elif int(function(*args)) > random_number:
            return "<h1 style='blue'>Too high, try again</h1> <img " \
           "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='too high:('> "
        if int(function(*args)) == random_number:
            return "<h1 style='green'>You found me :)</h1> <img " \
           "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='it's mee:)'> "
    return wrapper


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1> <img " \
           "src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='numbers'> "


@app.route('/<number>')
@user_guessing_feedback
def guess_of_user(number):
    print(number)
    return number


if __name__ == "__main__":
    app.run(debug=True)