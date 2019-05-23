# Author:       Alejandro Sanchez Uribe
# Date:         28 January 2019
# Class:        BTE 499
# Assignment:   Assignment 2 - Question 2-D

print('Assignment 2 - Question 2-D')

investmentSPY = eval(input('Amount invested in SPY: '))
investmentQQQ = eval(input('Amount invested in QQQ: '))
investmentEEM = eval(input('Amount invested in EEM: '))
investmentVXX = eval(input('Amount invested in VXX: '))

investmentTotal = investmentSPY + investmentQQQ + investmentEEM + investmentVXX

print('')
print('SPY investment: {0:.2f}%'.format(investmentSPY/investmentTotal))
print('QQQ investment: {0:.2f}%'.format(investmentQQQ/investmentTotal))
print('EEM investment: {0:.2f}%'.format(investmentEEM/investmentTotal))
print('VXX investment: {0:.2f}%'.format(investmentVXX/investmentTotal))
print('Total investment:', investmentTotal)
