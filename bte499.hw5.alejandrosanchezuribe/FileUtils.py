# Author: Alejandro Sanchez Uribe
# Class: BTE 499
# Date: 22 March 2019
# Assignment: Assignment 5

import Card


def write_new_deck(filename):
    ofile = open(filename, 'w')

    suit = "Spades"

    for i in range(1, 53):
        if i > 13:
            suit = "Hearts"
        if i > 26:
            suit = "Diamonds"
        if i > 39:
            suit = "Clubs"

        value = i % 13
        value_str = "Ace"

        if value == 0:
            value_str = "King"
        elif value != 1 and value < 11:
            value_str = str(value)
        elif value == 11:
            value_str = "Jack"
        elif value == 12:
            value_str = "Queen"

        ofile.write(value_str + " of " + suit + '\n')

    ofile.close()


def read_deck(filename, deck):
    ifile = open(filename, 'r')
    for line in ifile:
        str_value, suit = line.strip()[1:], line[0]
        card = Card.Card(suit, str_value)
        deck.push(card)

    ifile.close()
