# Author: Alejandro Sanchez Uribe
# Class: BTE 499
# Date: 22 March 2019
# Assignment: Assignment 5

import Deck
import Shuffler
from enum import Enum
import random


class TurnChoice(Enum):
    DRAW = 'draw'
    STAND = 'stand'


class WinStatus(Enum):
    WIN = 'win'
    LOSE = 'lose'
    NEUTRAL = 'neutral'


class Dealer(object):
    def __init__(self):
        self.wins = 0
        self.deck = Deck.Deck()
        self.stand_value = 17

    def choice(self):
        choice = TurnChoice.DRAW

        if self.stand_value <= self.deck.value_calc():
            choice = TurnChoice.STAND

        return choice

    def win_status(self):
        if self.deck.value_calc() == 21:
            return WinStatus.WIN
        elif self.deck.value_calc() > 21:
            return WinStatus.LOSE
        else:
            return WinStatus.NEUTRAL

    def reset_vals(self):
        self.deck = Deck.Deck()


class Player(Dealer):
    def __init__(self):
        super(Player, self).__init__()
        self.stand_value = 18
        self.optional_value = 12
        self.max_stands = 1
        self.current_stands = 0

    def choice(self):
        choice = TurnChoice.DRAW

        if self.stand_value <= self.deck.value_calc() or self.current_stands >= self.max_stands:
            choice = TurnChoice.STAND

        elif self.optional_value <= self.deck.value_calc() <= self.stand_value \
                and self.current_stands < self.max_stands:

            coin_toss = random.randint(1, 2)

            if coin_toss == 2:
                choice = TurnChoice.STAND

        return choice

    def reset_vals(self):
        super(Player, self).reset_vals()
        self.current_stands = 0


class Game:
    def __init__(self, deck, sessions):
        self.sessions_total = sessions
        self.sessions_cleared = 0
        self.deck = deck
        self.player = Player()
        self.dealer = Dealer()

    def player_turn(self):
        while self.player.choice() == TurnChoice.DRAW:
            if self.deck.size() > 1:
                self.player.deck.push(self.deck.top())
                self.deck.pop()
            else:
                break

            print('Player wins:', self.player.wins)
            print('Hand:', self.player.deck.value_calc())
            self.player.deck.print()
            print()

    def dealer_turn(self):
        while self.dealer.choice() == TurnChoice.DRAW:
            if self.deck.size() > 1:
                self.dealer.deck.push(self.deck.top())
                self.deck.pop()
            else:
                break

            print('Dealer wins:', self.dealer.wins)
            print('Hand:', self.dealer.deck.value_calc())
            self.dealer.deck.print()
            print()

    def new_game(self):
        while self.sessions_cleared < self.sessions_total and self.deck.size() > 1:

            self.player.deck.push(self.deck.top())
            self.deck.pop()
            print('Player wins:', self.player.wins)
            print('Hand:', self.player.deck.value_calc())
            self.player.deck.print()
            print()

            self.dealer.deck.push(self.deck.top())
            self.deck.pop()
            print('Dealer wins:', self.dealer.wins)
            print('Hand:', self.dealer.deck.value_calc())
            self.dealer.deck.print()
            print()

            while self.player.win_status() == WinStatus.NEUTRAL and self.dealer.win_status() == WinStatus.NEUTRAL:

                self.player_turn()
                self.dealer_turn()

                if self.player.win_status() == WinStatus.WIN \
                        or self.dealer.win_status() == WinStatus.LOSE \
                        or self.player.deck.value_calc() > self.dealer.deck.value_calc():

                    self.sessions_cleared += 1
                    print('Player wins round', self.sessions_cleared, '\n')
                    self.player.wins += 1
                    break

                elif self.dealer.win_status() == WinStatus.WIN \
                        or self.player.win_status() == WinStatus.LOSE\
                        or self.dealer.deck.value_calc() > self.player.deck.value_calc():
                    self.sessions_cleared += 1
                    print('Dealer wins round', self.sessions_cleared, '\n')
                    self.dealer.wins += 1
                    break

                else:
                    self.sessions_cleared += 1
                    print('Dealer wins round', self.sessions_cleared, '\n')
                    self.dealer.wins += 1
                    break

            Shuffler.fisher_yates_shuffle(self.deck)
            Shuffler.simple_shuffle(self.deck)
            self.player.reset_vals()
            self.dealer.reset_vals()

        print('Game Over!\nResults:\nDealer wins:', self.dealer.wins, '\nPlayer wins:', self.player.wins, '\n')




