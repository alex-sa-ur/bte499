# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1

import Q1FileUtils as FileUtils
import Q1Order as Order
import Q1Meal as Meal


def meal_builder(restaurant, order):
    print(restaurant)
    print('New Meal (n)' + '{:>22}'.format('Save (s)') + '{:>26}'.format('Quit (q)'))
    print(order)

    choice = input('Please input in the number of your choice >> ')

    try:
        choice_eval = eval(choice)
        if choice_eval < len(restaurant.menu):
            print()
            order.meals[len(order.meals)-1].menu_items.append(restaurant.menu.find_item(choice_eval-1))
            meal_builder(restaurant, order)
        else:
            print('\nInvalid number, please select a number between 1 and', len(restaurant.menu))
            meal_builder(restaurant, order)

    except NameError:
        if choice == 'n':
            order.meals.append(Meal.Meal([]))
            meal_builder(restaurant, order)
        elif choice == 's':
            FileUtils.save_order(order)
        elif choice == 'q':
            quit()
        else:
            print('\nInvalid input, please try again', len(restaurant.menu))
            meal_builder(restaurant, order)


def restaurants_printer(restaurants):
    welcome = 'Welcome to the Miami Favorites Meal Builder 2.0'.center(60, ' ') + '\n'
    picker = ('='*len(welcome)).center(60, ' ') + '\n'*2
    picker += welcome
    picker += ('='*len(welcome)).center(60, ' ') + '\n'*2

    for i in range(len(restaurants)):
        picker += str(i+1) + '\t' + restaurants[i].name + '\n'

    picker += '\n' + ('='*len(welcome)).center(60, ' ') + '\n'

    print(picker)


def restaurants_picker(restaurants):
    restaurants_printer(restaurants)
    print('New Meal (n)' + '{:>48}'.format('Quit (q)\n'))
    try:
        choice = eval(input('Please input in the number of your choice >> '))
    except NameError:
        print('\nInvalid input, please select a number between 1 and', len(restaurants))
        restaurants_picker(restaurants)

    if choice < len(restaurants):
        print()
        restaurant = restaurants[choice-1]
        meal_builder(restaurant, Order.Order(restaurant.name))
    else:
        print('\nInvalid input, please select a number between 1 and', len(restaurants))
        restaurants_picker(restaurants)


def main():
    restaurants = []
    FileUtils.restaurants_reader('restaurant_menus.txt', restaurants)

    restaurants_picker(restaurants)


if __name__ == '__main__':
    main()
