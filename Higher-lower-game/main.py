import art
import game_data
import random


log = []
the_game_is_end = False


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
        ...



print(art.logo)
while not the_game_is_end:
    selected_option_1 = random_option()
    selected_option_2 = random_option()
    print(f"Compare A: {info_printing(selected_option_1)}")
    print(art.vs)
    print(f"Compare B: {info_printing(selected_option_2)}")
    the_game_is_end = True


# print(random_option())

# info_printing(random_option())