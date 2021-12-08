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


def display_menu():
    print('COMMAND MENU')
    print('1 - Add player(s)')
    print('2 - Play again')
    print('0 - Exit program')
    print()


def play_game():
    """

    :return:
    """


def main():
    """

    :return:
    """
    welcome()
    rules()

    print(Cards.get_players(players=''))


if __name__ == "__main__":
    main()
