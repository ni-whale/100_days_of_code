import art
import random
import pyautogui

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 10, 10]


def new_hand():
    """Using only for the start of the game to generate the hand for the player/dealer"""
    hand = []
    for card in range(2):
        hand.append(new_card())
    return hand


def new_card():
    """Using for getting a new card from the deck"""
    card = random.choice(cards)
    return card


def score(hand):
    """Showing the current score for the one player"""
    new_score = 0
    for value in hand:
        new_score += value
    return new_score


def check(score):
    """Simple check which shows if the user can continue the game"""
    if score > 21:
        return 'Bust!'
    else:
        return 'ok'


def ace_rule(player_hand):
    """Ace can count as 1 or 11 depends on score"""
    if score(player_hand) > 21:
        for value in player_hand:
            if value == 11:
                player_hand[player_hand.index(value)] = 1
            else:
                continue
        return player_hand
    else:
        return player_hand


def print_current_state(player_hand, dealer_hand, needs_another_card):
    """Printing the result depending on users needs to take a new card"""
    if needs_another_card:
        print('-------------------------------------------------')
        print(f'Your cards: {player_hand}, current score is {score(player_hand)}')
        print(f"Dealer's first card is {dealer_hand[0]}")
    else:
        print('-------------------------------------------------')
        print(f'Your cards: {player_hand}, current score is {score(player_hand)}')
        print(f"Dealer's cards {dealer_hand}, final score is {score(dealer_hand)}")


def game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        # print(art.logo)
        # Start of the game where player and dialer are getting initial cards and we see the current score
        player_hand = new_hand()
        player_hand = ace_rule(player_hand)
        dealer_hand = new_hand()
        print_current_state(player_hand, dealer_hand, True)
        print(check(score(player_hand)))
        # End of this section

        # Asking the user if he want to take another card and checking his score after this action
        should_take_another_card = True
        while should_take_another_card:  # loop which allows the user to take as many cards as required
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                player_hand.append(new_card())
                player_hand = ace_rule(player_hand)
                print_current_state(player_hand, dealer_hand, True)
                if check(score(player_hand)) == 'Bust!':
                    print_current_state(player_hand, dealer_hand, False)
                    print('You lose!')
                    game()
            else:
                should_take_another_card = False
                continue
        # End of this section

        # Checking dealer's score and giving him another card if score less than 12
        if (score(dealer_hand)) <= 12:
            dealer_hand.append(new_card())
            print_current_state(player_hand, dealer_hand, False)
            if check(score(dealer_hand)) == 'Bust!':
                print_current_state(player_hand, dealer_hand, False)
                print('You win!')
            # else:
        # End of this section
        # Checking who is the winner
        if check(score(dealer_hand)) == 'ok':
            print_current_state(player_hand, dealer_hand, False)
            if score(player_hand) > score(dealer_hand):
                print('You win!')
            elif score(player_hand) == score(dealer_hand):
                print('There is no winners, my friend!')
            else:
                print('You lose!')
        else:
            print('You win!')
        game()
        # End of this section
    else:
        print('Good buy!')
        exit()


game()
