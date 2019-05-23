"""
Author:       Alejandro Sanchez Uribe
Date:         29 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 1 - Question 2
"""


# Parameters:   caffeine consumed, and caffeine content desired in body
# Process:      increases amount of hours as
#               the caffeine level lowers
# Output:       prints statement of how many hours it takes to
#               get desired content level
# Assumption:   caffeine has an approximate half life of
#               5 hours once consumed

def a_hours_to_value(consumed, desired):
    body_content = consumed
    hours = 0

    while body_content > desired:
        body_content /= 1.15  # Yearly equivalent of the caffeine half life
        hours += 1

    print('The number of hours it takes for caffeine '
          'to drop from {} mg to {} mg is: {} hours'
          .format(consumed, desired, hours))


# Parameters:   caffeine consumed, and hours after which content is checked, should results print
# Process:      body content is lowered as amount of hours left decreases
# Output:       prints statement of how much caffeine is in your system at
#               the desired amount of hours passed
#               OR
#               caffeine content is returned
# Assumption:   caffeine has an approximate half life of
#               5 hours once consumed

def b_value_after_hours(consumed, hours, print_req=True):
    body_content = consumed
    hours_left = hours

    while hours_left > 0:
        body_content /= 1.15  # Yearly equivalent of the caffeine half life
        hours_left -= 1

    body_content = round(body_content, 2)

    if print_req:
        print('After {} hours, caffeine drops from {} to {}'
              .format(hours, consumed, body_content))
    else:
        return body_content


# Parameters:   caffeine consumed per intake, how many times it is consumed
# Process:      caffeine content is adjusted as repeats decrease
# Output:       prints caffeine content after all expected intakes have occurred
# Assumptions:  a single cup is consumed every hour

def c_value_continuous_consumption(consumed, repeats):
    body_content = consumed
    repeats_left = repeats

    while repeats_left > 0:
        body_content = b_value_after_hours(consumed, 1, False)
        repeats_left -= 1

    body_content = round(body_content, 2)

    print('After {} hours and consuming 1 cup per hour, '
          'caffeine drops from {} to {}'
          .format(repeats, consumed, body_content))


# Input:    none
# Process:  number of hours for amount to drop below a value,
#           amount in body after time
# Output:   number of hours (below 65mg), amount after a day (1 cup),
#           amount after a day (a cup an hour)

oneCup = 130
aDesired = 65
bHours = 24
cCupsADay = 24

a_hours_to_value(oneCup, aDesired)
b_value_after_hours(oneCup, bHours)
c_value_continuous_consumption(oneCup, cCupsADay)
