# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1

import Q1Meal as Meal


class Order:
    def __init__(self, restaurant_name, subtotal=0.0):
        self.tax_rate = 0.065
        self.tip_rate = 0.2

        self.restaurant_name = restaurant_name
        self.meals = [Meal.Meal([])]
        self.subtotal = subtotal

        self.tax = self.subtotal * self.tax_rate
        self.tip = self.subtotal * self.tip_rate
        self.total = self.subtotal + self.tax + self.tip

    def update_order(self):
        self.subtotal = 0.0

        for meal in self.meals:
            meal.update_meal()
            self.subtotal += meal.subtotal

        self.tax = self.subtotal * self.tax_rate
        self.tip = self.subtotal * self.tip_rate
        self.total = self.subtotal + self.tax + self.tip

    def __str__(self):
        separator = '='*60 + '\n'
        output = separator

        for i in range(len(self.meals)):
            if i < len(self.meals) - 1:
                output += "Meal # {x} has {y} item(s)".format(x=i+1, y=len(self.meals[i].menu_items)) + '\n'
                output += str(self.meals[i]) + '\n'
            else:
                output += "Your current meal has {y} item(s)".format(x=i+1, y=len(self.meals[i].menu_items)) + '\n'
                output += str(self.meals[i]) + '\n'

        output += separator

        self.update_order()

        output += 'Subtotal = '.rjust(50, ' ') + '{:.2f}'.format(self.subtotal).rjust(10, ' ') + '\n'
        output += 'Tax = '.rjust(50, ' ') + '{:.2f}'.format(self.tax).rjust(10, ' ') + '\n'
        output += 'Tip = '.rjust(50, ' ') + '{:.2f}'.format(self.tip).rjust(10, ' ') + '\n'
        output += 'Total = '.rjust(50, ' ') + '{:.2f}'.format(self.total).rjust(10, ' ') + '\n'

        return output




