"""
Author:       Alejandro Sanchez Uribe
Date:         29 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 1 - Question 1
"""

# Input:    principle, interest, loan duration (months) from the user
# Process:  monthly payment, monthly interest rate, total interest
# Output:   monthly payment amounts, total interest

try:
    principle = eval(input('Input the principle amount of the loan: '))
    interest = eval(input('Input the yearly interest rate of the loan: '))
    duration = eval(input('Input the loan duration (in months): '))

    monthlyInterest = interest / 1200
    monthlyPayment = (principle * monthlyInterest) / (1 - (1 + monthlyInterest) ** -duration)
    totalInterest = duration * monthlyPayment - principle

    print('Monthly payments: {0:.2f}\nTotal interest: {1:.2f}'.format(monthlyPayment, totalInterest))

except (NameError, SyntaxError):
    print('There was an error in your input!\n'
          'Make sure to only input numbers and decimal points')
