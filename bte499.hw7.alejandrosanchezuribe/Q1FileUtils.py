# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1


import Q1Restaurant as Restaurant
import Q1Menu as Menu
import Q1MenuItem as MenuItem
import random
import string
from datetime import datetime


def item_reader(line_content):
    item_category, item_name, item_price = line_content[0:3]
    item = MenuItem.MenuItem(item_category.strip(), item_name.strip(), eval(item_price.strip()))
    return item


def menu_builder(item_list):
    category_containers = {}

    for item in item_list:
        try:
            category_containers[item.category].append(item)
        except KeyError:
            category_containers[item.category] = [item]

    menu = Menu.Menu(category_containers)

    return menu


def restaurants_reader(file_name, restaurants):
    ifile = open(file_name, 'r')

    name = ''
    item_list = []

    for line in ifile:
        line_content = line.strip().split(sep=',')
        if len(line_content) == 1:
            if line_content[0] != 'END':
                name = line_content[0].strip()
            else:
                restaurant = Restaurant.Restaurant(name, menu_builder(item_list))
                restaurants.append(restaurant)
                item_list = []

        elif len(line_content) >= 3:
            item_list.append(item_reader(line_content))

    ifile.close()


def save_order(order):
    order.update_order()

    order_filename = 'order_'
    order_filename += ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '_'
    order_filename += ''.join(order.restaurant_name.split()) + '_'
    order_filename += datetime.now().strftime('%m')
    order_filename += datetime.now().strftime('%d')
    order_filename += datetime.now().strftime('%Y') + '_'
    order_filename += datetime.now().strftime('%H')
    order_filename += datetime.now().strftime('%M')
    order_filename += datetime.now().strftime('%S')
    order_filename += '.txt'

    ofile = open(order_filename, 'w')

    ofile.write(order.restaurant_name + '\n')

    for i in range(len(order.meals)):
        ofile.write("Meal # {x} has {y} item(s)".format(x=i+1, y=len(order.meals[i].menu_items)) + '\n')

        for item in order.meals[i].menu_items:
            ofile.write(item.category + ' ' + item.name + ' ' + '{:>.2f}'.format(item.price) + '\n')

    ofile.write('Subtotal: ' + '{:>.2f}'.format(order.subtotal) + '\n')
    ofile.write('Tax: ' + '{:>.2f}'.format(order.tax) + '\n')
    ofile.write('Tip: ' + '{:>.2f}'.format(order.tip) + '\n')
    ofile.write('Total: ' + '{:>.2f}'.format(order.total) + '\n')

    ofile.close()
