# Author: Alejandro Sanchez Uribe
# Class: BTE 499
# Date: 22 March 2019
# Assignment: Assignment 5

import Deck
import FileUtils
import Shuffler
import Game


def main():
    filename = 'cards.txt'
    deck = Deck.Deck()
    FileUtils.read_deck(filename, deck)
    Shuffler.simple_shuffle(deck)
    Shuffler.fisher_yates_shuffle(deck)

    new_game = Game.Game(deck, 10)
    new_game.new_game()


main()
