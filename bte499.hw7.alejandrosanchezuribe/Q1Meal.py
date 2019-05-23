# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1


class Meal:
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.subtotal = 0.0

        for menu_item in menu_items:
            self.subtotal += menu_item.price

    def __str__(self):
        output = ''

        for menu_item in self.menu_items:
            output += str(menu_item) + '\n'

        return output

    def update_meal(self):
        self.subtotal = 0.0

        for item in self.menu_items:
            self.subtotal += item.price
