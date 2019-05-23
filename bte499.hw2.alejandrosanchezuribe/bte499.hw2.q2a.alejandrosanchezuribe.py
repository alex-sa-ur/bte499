# Author:       Alejandro Sanchez Uribe
# Date:         28 January 2019
# Class:        BTE 499
# Assignment:   Assignment 2 - Question 2-A & 2-B

print('Assignment 2 - Question 2-A & 2-B')

coins = [('Half Dollar(s)', 50),
         ('Quarter(s)', 25),
         ('Dime(s)', 10),
         ('Nickel(s)', 5),
         ('Penny(-ies)', 1)]

change = eval(input('Enter amount of change (0-99): '))

if change > 99:
    print('Input must be between 0 and 99')
else:
    for i in range(len(coins)):
        needed = change // coins[i][1]
        change -= (needed * coins[i][1])

        if needed != 0:
            print(str(needed) + ' ' + coins[i][0])
