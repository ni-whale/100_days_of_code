import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
condition = True
flag = True # if flag == 0 it's a dealer, if 1 - user

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


def check(score):
    if score == 21:
        return 'ok'
    elif score > 21:
        return 'Bust!'
    else:
        return 'ok'


def print_current_state(player_hand, dealer_hand, condition):
    if condition:
        print(f'Your cards: {player_hand}, current score is {score(player_hand)}')
        print(f"Dealer's first card is {dealer_hand[0]}")
    else:
        print(f'Your cards: {player_hand}, current score is {score(player_hand)}')
        print(f"Dealer's cards {dealer_hand}, final score is {score(dealer_hand)}")
    # need to change this print out. It will be a bullshit when I will need to count the score for the dialler


def game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        # print(art.logo)
        player_hand = new_hand()
        dealer_hand = new_hand()
        print_current_state(player_hand, dealer_hand, True)
        print(check(score(player_hand)))
        flag = True
        while flag:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                player_hand.append(new_card())
                print_current_state(player_hand, dealer_hand, True)
                if check(score(player_hand)) != 'ok':
                    print('You lose!')
                    exit()
                else:
                    break
            else:
                print("lol")
                flag = False

        if (score(dealer_hand)) < 12:
            dealer_hand.append(new_card())
            print_current_state(player_hand, dealer_hand, False)
        else:
            if check(score(dealer_hand)) == 'ok':
                if score(player_hand) > score(dealer_hand):
                    print('You win!')
                else:
                    print('You lose!')
            else:
                print('You win!')
                game()

    else:
        print('Good buy!')


game()