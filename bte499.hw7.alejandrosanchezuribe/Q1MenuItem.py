# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1


class MenuItem:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + ' ' + '{:>{x}.2f}'.format(self.price, x=50-len(self.name))
