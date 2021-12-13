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

import Cards

LINE_LENGTH = 75


def welcome():
    print()
    print('*' * LINE_LENGTH)
    print('                            Welcome to Game 21')
    print('*' * LINE_LENGTH)
    print()


def display_menu():
    print('COMMAND MENU')
    print('1 - Add player(s)')
    print('2 - Play again')
    print('0 - Exit program')
    print()


def play_game():
    """

    :return: n/a
    """


def play_round(players):
    """

    :param players:
    :return:
    """
    players = {}
    Cards.setup_new_round(players)
    Cards.deal_to_players(players)
    dealer_cards_total = Cards.dealer_to_dealer(players)
    Cards.display_winners(players, dealer_cards_total)


def main():
    """

    :return:
    """
    players = {}
    welcome()
    Cards.rules()
    Cards.get_players(players)
    pl
    Cards.setup_new_round(players)
    Cards.get_yn_input()


if __name__ == "__main__":
    main()
