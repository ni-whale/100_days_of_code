import art
import game_data
import random


log = []
score = 0
winner = ""
the_game_is_end = False
typo_in_game = True


def random_option():
    find_a_new_one = False
    while not find_a_new_one:
        selected_option = random.choice(game_data.data)
        if selected_option in log:
            continue
        else:
            log.append(selected_option)
            find_a_new_one = True
    return selected_option


def info_printing(selected_option):
    return f"{selected_option['name']}, a {selected_option['description']}, from {selected_option['country']}."


def compare_options(selected_option_1, selected_option_2):
    if selected_option_1['follower_count'] > selected_option_2['follower_count']:
        return "A", selected_option_1
    else:
        return "B", selected_option_2


print(art.logo)
while not the_game_is_end:
    if score == 0:
        selected_option_1 = random_option()
    else:
        selected_option_1 = winner
    selected_option_2 = random_option()
    print(f"Compare A: {info_printing(selected_option_1)}")
    print(art.vs)
    print(f"Compare B: {info_printing(selected_option_2)}")
    while typo_in_game:
        try:
            guess = input("Who had more followers? Type 'A' or 'B': ")
            if guess.upper() == "A" or guess.upper() == "B":
                break
        except NameError("A"):  # Not sure which exception should be there to print the result. Need to google it.
            print("Oops! That was not valid input. Try again...")
    result_of_compare, winner = compare_options(selected_option_1, selected_option_2)
    if result_of_compare == guess.upper():
        score += 1
        print("---------------------------------")
        print(f"You're right! Current score: {score}")
        print("---------------------------------")
    else:
        print("---------------------------------")
        print(f"Sorry, that's wrong. Your final score: {score}")
        print("---------------------------------")
        the_game_is_end = True
