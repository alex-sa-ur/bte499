"""
Author:       Alejandro Sanchez Uribe
Date:         29 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 1 - Question 6
"""

# Input:    item name, year purchased, cost,
#           estimated life (in years), method of depreciation
# Process:  takes input and applies the right method of depreciation
# Output:   prints out input, value at the beginning of the year,
#           amount depreciated during the year, and total depreciation

try:
    name = input('Input item name: ')
    year = eval(input('Input year the item was purchased: '))
    cost = eval(input('Input item cost: '))
    life = eval(input('Input expected live of item (in years): '))
    method = input('Input depreciation method, straight-line / double-declining [S/D]: ')

    cost = round(cost, 2)

    print('\nName: {} | Year Bought: {} | Cost: {} | Expected Life: {}\n'.format(name, year, cost, life))
    print('|Year\t|Value\t|Annual Dep\t|Total Dep\t|')

    method = method.lower()

    currentYear = 2019

    totalDepreciation = 0
    currentValue = cost
    annualDepreciation = 0

    if method == 's':
        for i in range(life):
            if (year + i) <= currentYear:
                annualDepreciation = (cost * 1/life)
                totalDepreciation += annualDepreciation
                currentValue -= annualDepreciation

                currentValue = round(currentValue, 2)
                annualDepreciation = round(annualDepreciation, 2)
                totalDepreciation = round(totalDepreciation, 2)

                print('|{}\t|{}\t|{}\t\t|{}\t\t|'
                      .format(year+i, currentValue, annualDepreciation, totalDepreciation))
            else:
                break

    elif method == 'd':
        for i in range(life - 1):
            if (year + i) <= currentYear:
                annualDepreciation = (currentValue * 2/life)
                totalDepreciation += annualDepreciation
                currentValue -= annualDepreciation

                cost = round(cost, 2)
                currentValue = round(currentValue, 2)
                annualDepreciation = round(annualDepreciation, 2)
                totalDepreciation = round(totalDepreciation, 2)

                print('|{}\t|{}\t|{}\t\t|{}\t\t|'
                      .format(year+i, currentValue, annualDepreciation, totalDepreciation))
            else:
                break

        currentValue -= currentValue

    else:
        print('Invalid depreciation method, please try again')
        exit()


except (NameError, SyntaxError):
    print('There was an error in your input!\n'
          'Make sure to input the right kind of data')
