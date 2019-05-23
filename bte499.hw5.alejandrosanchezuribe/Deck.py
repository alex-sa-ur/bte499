# Author: Alejandro Sanchez Uribe
# Class: BTE 499
# Date: 22 March 2019
# Assignment: Assignment 5

import DataStructures
import Card


class Deck(DataStructures.Stack):
    def __init__(self, sname = None, other_stack=None):
        super(Deck, self).__init__(sname, other_stack)

    def print(self):
        for i in range(0, self.size()):
            print(self.getInnerNode(i))

    def value_calc(self):
        value = 0

        for i in range(0, self.size()):
            value += self.getInnerNode(i).value

        return value
