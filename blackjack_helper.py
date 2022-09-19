from random import randint


def draw_card():
    # Implement draw_card function here
    card = randint(1, 13)
    if card == 11 or card == 12 or card == 13:
        # Jacks, Queens, and Kings are worth 10.
        card_value = 10
    elif card == 1:
        # Aces are worth 11.
        card_value = 11
    else:
        # All other cards are worth the same as
        # their rank.
        card_value = card
    return card_value


def draw_starting_hand():
    # Implement draw_starting_hand function here
    card1 = draw_card()
    card2 = draw_card()
    return card1 + card2, [card1, card2]


def get_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    if hand_value == 21:
        return 'BLACKJACK!'
    elif hand_value > 21:
        return 'BUST.'


def print_end_game_status(user_hand, dealer_hand):
    # Implement print_end_game_status function here
    if user_hand <= 21 and dealer_hand <= 21:
        if user_hand > dealer_hand:
            return 'You win!'
        elif user_hand == dealer_hand:
            return 'Push.'
        else:
            return 'Dealer wins!'
    elif user_hand <= 21 < dealer_hand:
        return 'You win!'
    else:
        return 'Dealer wins!'

