# Author:       Alejandro Sanchez Uribe
# Date:         28 January 2019
# Class:        BTE 499
# Assignment:   Assignment 2 - Question 2-C

print('Assignment 2 - Question 2-C')

price = eval(input('Input price of item: '))
weight = input('Input weight of item in pounds and ounces '
               '(values separated by a space): ').split()

pounds = eval(weight[0])

if len(weight) > 1:
    ounces = eval(weight[1])
else:
    ounces = 0

if ounces > 15:
    print('There are 16 ounces in a pound, '
          'any value greater than 15 should be converted to pounds')
else:
    pricePerOunce = round(price/(pounds * 16 + ounces), 2)

    print('This item costs ${0:.2f} per ounce'.format(pricePerOunce))
