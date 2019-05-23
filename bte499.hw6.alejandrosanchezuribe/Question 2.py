# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 2 April 2019
# Assignment: Take Home Midterm - Question 2


def is_leap_year(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


def len_of_month(year, month):
    length = 31

    if (month % 2 == 0 and month < 8) or (month % 2 == 1 and month > 8):
        if month == 2:
            if is_leap_year(year):
                length = 29
            else:
                length = 28
        else:
            length = 30

    return length


def day_of_year(year, month, day):
    total_days = 0

    if month > 1:
        prev_months = [i for i in range(1, month)]

        for prev_month in prev_months:
            total_days += len_of_month(year, prev_month)

    total_days += day

    return total_days


def day_of_century(year, month, day, start_year=2000):
    total_days = 0

    if year > start_year:
        prev_years = [i for i in range(start_year, year)]

        for prev_year in prev_years:
            total_days += day_of_year(prev_year, 12, 31)

    total_days += day_of_year(year, month, day)

    return total_days


def day_of_forever(year, month, day):
    return day_of_century(year, month, day, 0)


def day_of_week(year, month, day, start_day=0):
    day_count = day_of_forever(year, month, day)

    weekday = (day_count - start_day) % 7

    return weekday


def month_calendar(start_day=0):
    weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

    year_str, month_str = input('Enter a year and a month separated by a space: ').split()
    start_weekday = input('Enter a calendar start day [Mo, Tu, We, Th, Fr, Sa, Su]: ').title()[:2]
    year = eval(year_str)
    month = eval(month_str)

    output_start_day = weekdays.index(start_weekday)
    resorted_weekdays = weekdays[output_start_day:] + weekdays[:output_start_day]

    col_counter = 0

    print()

    for weekday in resorted_weekdays:
        print(weekday, end=' ')

    print()

    if day_of_week(year, month, 1, start_day) != output_start_day:
        for i in range(resorted_weekdays.index(weekdays[day_of_week(year, month, 1, start_day)])):
            print('  ', end=' ')
            col_counter += 1

    for i in range(1, len_of_month(year, month)+1):
        str_i = str(i) if i > 9 else ' ' + str(i)
        print(str_i, end=' ')
        col_counter += 1

        if col_counter % 7 == 0:
            print()


def sundays_in_year(year, start_day=0):
    total_sundays = 0
    for i in range(1, 13):
        for j in range(1, len_of_month(year, i)+1):
            if day_of_week(year, i, j, start_day) == 6:
                total_sundays += 1

    print('Total Sundays in {x}:'.format(x=year), total_sundays)


def main():
    # Align to correct day, with Jan 1 0 being a Thursday
    starting_day = 3

    # Part 1 - Length of Month
    print('Length of January 2009:', len_of_month(2009, 1))
    print('Length of February 2009:', len_of_month(2009, 2))
    print('Length of February 2008:', len_of_month(2008, 2))
    print()

    # Part 2 - Day of the Year
    print('Day of the Year value of January 1:', day_of_year(2009, 1, 1))
    print('Day of the Year value of January 2:', day_of_year(2009, 1, 2))
    print('Day of the Year value of February 1:', day_of_year(2009, 2, 1))
    print()

    # Part 3 - Day of the Century
    print('Day of the Century value of January 1, 2000:', day_of_century(2000, 1, 1))
    print('Day of the Century value of December 31, 2000:', day_of_century(2000, 12, 31))
    print('Day of the Century value of January 1, 2001:', day_of_century(2001, 1, 1))
    print()

    # Part 4 - Day of Forever
    print('Day of the Century value of January 1, 2000:', day_of_forever(2000, 1, 1))
    print('Day of the Century value of July 4, 1776:', day_of_forever(1776, 7, 4))
    print('Day of the Century value of October 2, 2012:', day_of_forever(2012, 10, 2))
    print('Day of the Century value of October 3, 2012:', day_of_forever(2012, 10, 3))
    print('Day of the Century value of October 4, 2012:', day_of_forever(2012, 10, 4))
    print('Day of the Century value of November 27, 2737:', day_of_forever(2737, 11, 27))
    print('Day of the Century value of January 1, 10:', day_of_forever(10, 1, 1))
    print()

    # Part 5 - Day of the Week
    print('Day of the week of April 1, 2019:', day_of_week(2019, 4, 1, starting_day))
    print('Day of the week of April 2, 2019:', day_of_week(2019, 4, 2, starting_day))
    print('Day of the week of April 3, 2019:', day_of_week(2019, 4, 3, starting_day))
    print('Day of the week of April 4, 2019:', day_of_week(2019, 4, 4, starting_day))
    print('Day of the week of April 5, 2019:', day_of_week(2019, 4, 5, starting_day))
    print('Day of the week of April 6, 2019:', day_of_week(2019, 4, 6, starting_day))
    print('Day of the week of April 7, 2019:', day_of_week(2019, 4, 7, starting_day))
    print()

    # Part 6 + 7 - Calendar for a month, any year, any start day
    month_calendar(starting_day)
    print('\n')
    month_calendar(starting_day)
    print('\n')

    # Part 8 - Sundays per year
    sundays_in_year(2019, starting_day)


main()
