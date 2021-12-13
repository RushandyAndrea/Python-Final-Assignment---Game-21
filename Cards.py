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

import Validation as val
import random

LINE_LENGTH = 75


def get_yn_input():
    """

    :return:
    """
    val.get_yes_no(prompt='Do you want to play another round? Yes=y No=n')


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
        player_name = val.get_string(
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
    for player_name, player_info in players.items(): # get the player_name (key) and player_info (value)

        cash, cards, cards_total, bet = player_info.values() # unpack the sub dictionary of the current player's data

        if cash < 0.25:  # skip the current player if they are out of money
            continue

        print('Dealing to ' + player_name)

        # deal the first two cards to the current player
        deal_card(player_info)
        deal_card(player_info)

        # unpack the sub dictionary again because the player's cards have changed
        cash, cards, cards_total, bet = player_info.values()
        display_cards(cards)


def dealer_to_dealer(players):
    """

    :return:
    """
    num_players_out = 0
    highest_hand = 0

    # need to determine if there is any players still in this round or if they all exceeded 21
    for player, player_info in players.items():  # get the player_name (key) and player_info (value)
        cards_total = player_info['cards_total']

        if cards_total > 21:
            num_players_out += 1
            print('Oh ooh, Try again later')
            print('')
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


"""
def get_yn_input(promp='')

"""
