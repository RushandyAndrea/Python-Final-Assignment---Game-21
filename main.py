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


def main():
    """

    :return:
    """
    players = {}
    welcome()
    Cards.rules()
    Cards.get_players(players)

    while True:
        Cards.play_round(players)
        if not Cards.get_yes_no('Do you want to play another round? Y=Yes N=No'):
            break


if __name__ == "__main__":
    main()
