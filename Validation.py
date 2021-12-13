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


def get_number(prompt, data_type='int'):
    """
    This get the user's input and prompt.
    :param prompt:
    :param data_type:
    :return: none
    """
    while True:
        user_input = input(f'{prompt}: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            return number

        except ValueError:
            print(f'Invalid input: Please enter a number.')


def get_poss_num(prompt, data_type='int'):
    """
    This function checks if the user inserted a number greater than 0. By using a while loop to get the user to insert a
    data or to close the program.
    :param prompt: a string that will be printed on the screen whenever the function is called.
    :param data_type: data types are the classification or categorization of data items. It represents
                      the kind of value that tells what operations can be performed on a particular data.
    :return: exits a function and instructs Python to continue executing the main program.
    """
    while True:
        user_input = input(f'{prompt} Insert a number greater than 0: ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if number > 0:
                return number
            else:
                print(f'Invalid input: Please enter a positive number')

        except ValueError:
            print(f'Invalid input: Please enter a number')


def get_range(prompt, low, high, data_type='int'):
    """
    This function checks if the user inserted a number that is in the range of
    the lowest(1) asked and in the highest(7) asked. By using a while loop to get the user to insert a
    data or to close the program.
    :param prompt: a string that will be printed on the screen whenever the function is called.
    :param low: two variables; low and high. These variables are defined by their position.
    :param high: two variables; low and high. These variables are defined by their position.
    :param data_type: data types are the classification or categorization of data items. It represents
                      the kind of value that tells what operations can be performed on a particular data.
    :return: exits a function and instructs Python to continue executing the main program.
    """

    while True:
        user_input = input(f'{prompt} (Valid {low}-{high}): ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if low <= number <= high:
                return number
            else:
                print('Entry must be greater or equal to', low,
                      'and less than or equal to', high)

        except ValueError:
            print(f'Invalid input: Please enter a number.')


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

