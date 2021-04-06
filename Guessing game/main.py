import art
import random

LIVES = 5
continue_the_game = True


def number_of_lives(difficulty):
    """Define the number of lives depends on the difficulty the user chose"""
    if difficulty == 'easy':
        return LIVES * 2
    else:
        return LIVES


def checking_the_guess(secret_number, user_guess):
    """Checking if the guess which the user made is similar as secret word"""
    if secret_number == user_guess:
        return 0  # with this option the game will finish
    elif secret_number > user_guess:
        return 'Too high!'
    elif secret_number < user_guess:
        return 'Too low!'
    else:
        return 1  # with this option the user will need to try guess again


def game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    secret_number = random.randrange(1, 100)
    # print(f"Generated number is {secret_number}")


game()







