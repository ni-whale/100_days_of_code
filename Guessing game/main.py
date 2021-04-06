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
        return 'Too low!'
    elif secret_number < user_guess:
        return 'Too high!'
    else:
        return 1  # with this option the user will need to try guess again


def game():
    print(art.logo)
    print("Welcome to the Guessing Game!")
    print("-----------------------------")
    print("I'm thinking of a number between 1 and 100...")
    secret_number = random.randrange(1, 100)
    print(f"Generated number is {secret_number}")
    typo_is_here = True
    while typo_is_here:
        difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
        typo_is_here = False if difficulty == 'easy' or difficulty == 'hard' else "Try again, dear."  # else statement doesn't printing for some reason...
    lives = number_of_lives(difficulty)
    print(f"You have {lives} attempts remaining to guess the number.")
    typo_is_here = True
    while typo_is_here:
        user_guess = int(input("Make a guess: "))
        if checking_the_guess(secret_number, user_guess) == 0:
            print(f"You got it! The answer is {secret_number}")
            exit()
        elif checking_the_guess(secret_number, user_guess) == 1:
            print("Try again, dear.")
        else:
            print(checking_the_guess(secret_number, user_guess))


game()







