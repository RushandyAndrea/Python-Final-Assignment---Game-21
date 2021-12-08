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

LINE_LENGTH = 75


def get_players(players):
    """

    :return:
    """
    player_name = val.get_string("Enter the player's first name (without spaces) and type 'done' when you are done: ")

    players[player_name] = {
        'cash': 1.0,  # each player starts off with $1 at the same of the game
        'cards': [],  # each player starts off with an empty list of cards at the start of the round
        'cards_total': 0,  # each player's card total starts off at zero at the start of the round
        'bet': 0.25  # each player's current bet start off at 25 cents at the start of the round
    }
    while True:
        if player_name == 'done'.lower():
            return
        else:
            val.get_string("Enter the player's first name (without spaces): ")


def display_the_cards():
    """

    :return:
    """


def sum_of_dealer_cards():
    """

    :return:
    """


def sum_of_player_cards():
    """

    :return:
    """


def compare_sum_of_all_cards():
    """

    :return:
    """


"""
def get_yn_input(promp='')

"""
