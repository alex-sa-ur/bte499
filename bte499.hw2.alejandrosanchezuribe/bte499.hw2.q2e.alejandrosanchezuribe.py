# Author:       Alejandro Sanchez Uribe
# Date:         28 January 2019
# Class:        BTE 499
# Assignment:   Assignment 2 - Question 2-E

print('Assignment 2 - Question 2-E')

miles = eval(input('Input miles: '))
yards = eval(input('Input yards: '))
feet = eval(input('Input feet: '))
inches = eval(input('Input inches: '))

inches += miles * 63360 + yards * 36 + feet * 12

meters = (inches / 39.37)
kilometers = meters//1000
meters -= kilometers * 1000
centimeters = round((meters - int(meters)) * 100, 1)
meters = int(meters)

print('')

if kilometers > 0:
    print('{} kilometers'.format(kilometers))
if meters > 0:
    print('{} meters'.format(meters))
if centimeters > 0:
    print('{} centimeters'.format(centimeters))
