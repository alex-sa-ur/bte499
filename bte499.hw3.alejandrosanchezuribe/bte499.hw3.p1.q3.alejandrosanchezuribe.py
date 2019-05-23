"""
Author:       Alejandro Sanchez Uribe
Date:         29 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 1 - Question 3
"""


# Parameters:   years to account for, interest rate, yearly deposits
# Process:      compounds interest and adds deposit value to tracker for each year
# Output:       prints total contributions to IRA and final amount at end of year count

def ira_calculator(years, rate, deposit):
    ira_balance = round(deposit * (((1 + rate) ** years - 1) / rate), 2)
    contributions = deposit * years

    return '\tBalance at retirement: {}\n' \
           '\tContributions: {}'\
        .format(ira_balance, contributions)


# Input:    none
# Process:  IRA contributions and
#           total amount of money at retirement
# Output:   Print calculation results for
#           both Earl and Larry

startYear = 2015
endYear = 2063
interest = 0.04
deposits = 5000
larryWaitTime = 15

earlYears = endYear - startYear
larryYears = endYear - startYear - larryWaitTime

print('Earl\n', ira_calculator(earlYears, interest, deposits), '\n', sep='')
print('Larry\n', ira_calculator(larryYears, interest, deposits), sep='')
