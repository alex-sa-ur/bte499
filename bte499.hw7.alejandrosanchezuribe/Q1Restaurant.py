# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def __str__(self):
        output = self.name.center(60, ' ') + '\n'
        output += ('==' + '='*len(self.name) + '==').center(60, ' ') + '\n'*2

        output += str(self.menu)

        return output
