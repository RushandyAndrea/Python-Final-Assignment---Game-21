#!/usr/bin/env python3

"""
# Programmer: Rushandy Andrea
# Date: December 10th, 2021
# Description: For this assignment,
"""

# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'December 10th, 2021'
__status__ = 'Development'

import random

LINE_LENGTH = 75


def get_string(prompt):
    """
    This take user input.
    :param prompt:
    :return:
    """
    while True:
        user_input = input(f'{prompt} ')

        if user_input > '':
            return user_input
        else:
            print(f'Invalid input: Please enter a value!')


def get_yes_no(prompt='(y=Yes or n=No)'):
    """
    Here is where the function ask for user input.
    :param prompt:
    :return: exits a function and instructs Python to continue executing the main program.
    """
    while True:
        if prompt == '':
            user_input = input('(y=yes or n=no): ').lower()
        else:
            user_input = input(f'{prompt} (y=yes or n=no): ').lower()

        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print('Invalid input: Please enter a y=yes, or n=no')


def rules():
    print('The rules are simple!')
    print('1. Each player is trying to get as close to 21 without going over.')
    print('2. Each player is ONLY trying to beat the dealer hand.')
    print('3. The dealer will keep dealing himself cards \n'
          '   until he beats all players hands or goes over 21.')
    print('4. Tie goes to the player, not the dealer.')
    print('5. Each player gets dealt two card between 1 - 10.')
    print('6. The player then can choose to receive additional cards.')
    print('7. Each player starts with $1.00.')
    print('8. Default bet is 25 cents, but the player can double it after holding.')
    print('9. Winner is the last person with cash, not including the dealer.')
    print()
    print('-' * LINE_LENGTH)
    print()


def get_players(players):
    """

    :return:
    """
    print('Now lets get this game setup. Who are the people who are playing?')
    print()

    while True:
        player_name = get_string(
            "Enter the player's first name (without spaces) and type 'done' when you are done: ").title()

        if player_name == 'Done':
            return

        players[player_name] = {
            'cash': 1.0,  # each player starts off with $1 at the same of the game
            'cards': [],  # each player starts off with an empty list of cards at the start of the round
            'cards_total': 0,  # each player's card total starts off at zero at the start of the round
            'bet': 0.25  # each player's current bet start off at 25 cents at the start of the round
        }


def setup_new_round(players):
    """

    :return:
    """
    print()
    print('=' * LINE_LENGTH)
    print('Get Ready, Game is about to start...')
    print('=' * LINE_LENGTH)
    print()

    for player_name, player_info in players.items():
        player_info['cards'] = []  # each player starts off with an empty list of cards at the start of the round
        player_info['cards_total'] = 0  # each player's card total starts off at zero at the start of the round
        player_info['bet'] = 0.25  # each player's current bet start off at 25 cents at the start of the round


def deal_card(player_info):
    """

    :param player_info:
    :return:
    """
    card = random.randint(1, 10)  # get a random number between 1 and 10 inclusively
    player_info['cards'].append(card)  # add the card to the player's list of cards
    player_info['cards_total'] += card  # add the card value to the player's cards_total


def deal_to_players(players):
    """

    :return:
    """
    for player_name, player_info in players.items():  # get the player_name (key) and player_info (value)

        cash, cards, cards_total, bet = player_info.values()  # unpack the sub dictionary of the current player's data

        if cash < 0.25:  # skip the current player if they are out of money
            continue

        print('Dealing to ' + player_name)

        # deal the first two cards to the current player
        deal_card(player_info)
        deal_card(player_info)

        # unpack the sub dictionary again because the player's cards have changed
        cash, cards, cards_total, bet = player_info.values()
        display_cards(cards)

        while True:
            if get_yes_no('Do you want to play another round? y=Yes n=No'):
                deal_card(player_info)
                if cards_total > 21:
                    print('Busted, better luck next time')
                    break
            else:
                print(f'Player {player_name} is at hold, waiting for next turn.')

                # display hold if double bet


def deal_to_dealer(players):
    """

    :return: dealer_cards_total
    """
    num_players_out = 0
    highest_hand = 0

    # need to determine if there is any players still in this round or if they all exceeded 21
    for player, player_info in players.items():  # get the player_name (key) and player_info (value)
        cards_total = player_info['cards_total']

        if cards_total > 21:
            num_players_out += 1
        elif cards_total > highest_hand:
            highest_hand = cards_total

    # if there is no player left in this round
    # then there is no point dealing to the dealer
    # because the dealer automatically wins
    if num_players_out == len(players):
        return 21  # return 21 which means the dealer automatically wins because all players exceed 21

    # if there are still players in the round, then we need to deal to the dealer
    print('Dealing to dealer...')
    print()
    dealer_cards = []
    dealer_cards_total = 0

    # deal to the dealer one card at a time, until the dealer beats all players or reaches 21, or exceeds 21
    while True:
        card = random.randint(1, 10)
        dealer_cards.append(card)
        dealer_cards_total += card

        if dealer_cards_total > 21:
            display_cards(dealer_cards)
            print('Dealer is busted! He/She is out!')

        if dealer_cards_total > highest_hand:
            break

    return dealer_cards_total


def display_cards(cards):
    """

    :param cards:
    :return:
    """
    print('   Cards: ', end='')

    for card in cards:
        print(str(card) + ' ', end='')
    print()


def display_winners(players, dealer_cards_total):
    """

    :return:
    """
    total_winner = 0  # used to determine if the dealer is the automatic winner

    for player_name, player_info in players.items():

        cash, cards, cards_total, bet = player_info.values()

        if cash < 0.25:
            continue

        if dealer_cards_total > 21:  # dealer exceeded 21
            if cards_total <= 21:  # as long as the player is still in the game
                total_winner += 1
                player_info['cash'] += bet  # player won so increase their cash by the bet
                print(player_name, ' is a winner!')
            else:
                player_info['cash'] -= bet  # player lost to lower their cash by the bet
        else:
            if play # i have pictures of this


def play_round(players):
    """

    :param:
    :return:
    """
    setup_new_round(players)
    deal_to_players(players)
# dealer_cards_total = deal_to_dealer(players)
# display_winners(players, dealer_cards_total)


def display_round_summary(players):
    """

    :param players:
    :return:
    """
    print(f'End')
