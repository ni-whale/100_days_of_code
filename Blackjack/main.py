import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def new_hand():
    hand = []
    for card in range(2):
        hand.append(new_card())
    return hand


def new_card():
    card = random.choice(cards)
    return card


def score(hand):
    new_score = 0
    for value in hand:
        new_score += value
    return new_score


def print_current_state(player_hand, diller_hand):
    print(f'Your cards: {player_hand}, current score is {score(player_hand)}')
    print(f"Diller's first card is {diller_hand[0]}")


def game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        # print(art.logo)
        player_hand = new_hand()
        diller_hand = new_hand()
        print_current_state(player_hand, diller_hand)

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_hand.append(new_card())
            print_current_state(player_hand, diller_hand)

    else:
        print('Good buy!')


game()