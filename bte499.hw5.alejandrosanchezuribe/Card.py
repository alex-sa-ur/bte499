# Author: Alejandro Sanchez Uribe
# Class: BTE 499
# Date: 22 March 2019
# Assignment: Assignment 5


def str_to_val(str_value):
    return_val = 1

    if str_value == 'A':
        return return_val
    elif str_value == 'J':
        return_val = 11
    elif str_value == 'Q':
        return_val = 12
    elif str_value == 'K':
        return_val = 13
    else:
        return_val = eval(str_value)

    return return_val


class Card(object):
    def __init__(self, suit, str_value):
        self.suit = suit
        self.str_value = str_value
        self.value = str_to_val(str_value)

    def __str__(self):
        return self.suit + self.str_value




