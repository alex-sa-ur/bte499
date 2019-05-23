"""
Author:       Alejandro Sanchez Uribe
Date:         30 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 2
"""

# Adjusted to pull menu from text file

# Using camel case for variables declared outside of functions
# Using snake case for variables declared within functions

title = 'Welcome to the Miami Favorites Meal Builder'
options = [('Quit', 'q'), ('New Meal', 'n'), ('Delete Item', 'd')]

appetizers = []
entrees = []
drinks = []
desserts = []

menu = [('Appetizers', appetizers),
        ('Entrees', entrees),
        ('Drinks', drinks),
        ('Desserts', desserts)]

separator = '='

maxNumberDigits = 1
maxItemNameChars = 1
maxPriceDigits = 3
maxCatNameChar = 1
menu_item_count = 0

totalCountMultiplier = maxNumberDigits + maxItemNameChars + maxPriceDigits + 8

current_meal = []
all_meals = []


# Parameters:   filename
# Process:      adds all file lines to a list,
#               and adds all items and costs to category lists
# Output:       none

def menu_reader(file_name):
    global menu

    menu_file = open(file_name, 'r')

    for line in menu_file:
        line_content = line.strip().split()
        item_name = " ".join(line_content[1:(len(line_content)-1)])
        item_price = eval(line_content[-1])
        for category in menu:
            if line_content[0] == category[0]:
                category[1].append((item_name, item_price))

    menu_file.close()

    return


# Parameters:   none
# Process:      loops through nested lists to count off menu items,
#               determines max lengths of data types for formatting purposes
# Output:       total number of menu items

def menu_item_counter():
    global separator
    global maxNumberDigits
    global maxItemNameChars
    global maxPriceDigits
    global totalCountMultiplier
    global maxCatNameChar

    counter_item_count = 0

    for category in range(len(menu)):
        for item in range(len(menu[category][1])):
            counter_item_count += 1
            maxNumberDigits = len(str(counter_item_count))

            if len(menu[category][1][item][0]) > maxItemNameChars:
                maxItemNameChars = len(menu[category][1][item][0])

            if len(str(menu[category][1][item][1])) > maxPriceDigits:
                maxPriceDigits = len(str(menu[category][1][item][1]))

            if len(str(menu[category][0])) > maxCatNameChar:
                maxCatNameChar = len(str(menu[category][0]))

    totalCountMultiplier = maxNumberDigits + maxItemNameChars + maxPriceDigits + 9

    separator = separator * (totalCountMultiplier + maxCatNameChar) + 6 * separator

    return counter_item_count


# Parameters:   item tuple
# Process:      loops through all items to find match,
#               each loop increases the counter by 1
# Output:       match index or -1 if it fails

def global_indexer(item_to_find):
    index = 0

    for category in menu:
        for item in category[1]:
            index += 1
            if item == item_to_find:
                return index

    return -1


# Parameters:   global_index int
# Process:      loops through all items until global_index
#               reaches 0 as a countdown
# Output:       match index tuple or (-1,-1) if it fails

def find_by_global_index(global_index):
    for category in menu:
        for item in category[1]:
            global_index -= 1

            if global_index == 0:
                return item

    return -1, -1


# Parameters:   item tuple
# Process:      loops through all items to find match
#               by increasing counter
# Output:       returns category

def classifier(item_to_find):
    index = 0

    for category in menu:
        for item in category[1]:
            index += 1
            if item == item_to_find:
                return category[0]

    return -1


# Parameters:   none
# Process:      loops through all menu options to print them,
#               formats according to predetermined values
# Output:       printed title and menu options

def print_menu():
    global maxNumberDigits
    global maxItemNameChars
    global maxPriceDigits
    global totalCountMultiplier

    global_index = - 1

    for category in range(len(menu)):
        print(menu[category][0].center(46, ' '))

        print('-'*totalCountMultiplier)

        for index in range(len(menu[category][1])):
            global_index += 1
            print('{:<{x}}\t{:<{y}}\t{:>{z}f}'
                  .format(global_index + 1,
                          menu[category][1][index][0],
                          menu[category][1][index][1],
                          x=maxNumberDigits,
                          y=maxItemNameChars + 5,
                          z=maxPriceDigits+0.2))

        print('')

    print('')


# Parameters:   meal list
# Process:      loops through the meal to print all items
#               and their respective global index
# Output:       printed meal items

def print_meal(guest_num, meal):
    global maxNumberDigits
    global maxItemNameChars
    global maxPriceDigits
    global totalCountMultiplier
    global maxCatNameChar

    print('Guest {}\'s meal has {} item(s):'
          .format(guest_num, len(meal)))

    for item in range(len(meal)):
        index = global_indexer(meal[item])

        print('\t{:<{w}}\t{:<{x}}\t{:<{y}}\t{:>{z}f}'.format(index,
                                                             classifier(meal[item]),
                                                             find_by_global_index(index)[0],
                                                             find_by_global_index(index)[1],
                                                             w=maxNumberDigits,
                                                             x=maxCatNameChar,
                                                             y=maxItemNameChars + 5,
                                                             z=maxPriceDigits+0.2))


# Parameters:   none
# Process:      loops through all meals and meal items to print them
# Output:       printed meal items

def print_all_meals():
    global all_meals

    for index in range(len(all_meals) - 1, -1, -1):
        print_meal(index + 1, all_meals[index])


# Parameters:   none
# Process:      loops through all meal items to print them as part of meal
# Output:       printed meal items

def print_current_meal():
    global current_meal
    global all_meals

    print_meal(len(all_meals) + 1, current_meal)


# Parameters:   none
# Process:      adds item prices as subtotal,
#               calculates tax at 6.5%, tip at 20%,
#               adds final as total
# Output:       prints amounts owed

def print_monetary():
    global all_meals
    global current_meal

    subtotal = 0

    if len(all_meals) > 0:
        for index in range(len(all_meals) - 1, -1, -1):
            for item in all_meals[index]:
                subtotal = round(subtotal + item[1], 2)

    if len(current_meal) > 0:
        for item in current_meal:
            subtotal = round(subtotal + item[1], 2)

    tax = round(subtotal * 0.065, 2)
    tip = round(subtotal * 0.2, 2)
    total = round(subtotal + tax + tip, 2)

    max_payment_digits = len(str(total))

    print('{:>{x}} : {:>{y}f}'
          .format('Subtotal',
                  subtotal,
                  x=totalCountMultiplier+maxCatNameChar - max_payment_digits,
                  y=max_payment_digits+3.2))
    print('{:>{x}} : {:>{y}f}'
          .format('Tax',
                  tax,
                  x=totalCountMultiplier+maxCatNameChar - max_payment_digits,
                  y=max_payment_digits+3.2))
    print('{:>{x}} : {:>{y}f}'
          .format('Tip',
                  tip,
                  x=totalCountMultiplier+maxCatNameChar - max_payment_digits,
                  y=max_payment_digits+3.2))
    print('{:>{x}} : {:>{y}f}'
          .format('Total',
                  total,
                  x=totalCountMultiplier+maxCatNameChar - max_payment_digits,
                  y=max_payment_digits+3.2))
    print('')


# Input:    delete index
# Process:  finds item through global index,
#           then finds the first match of the
#           new local index in the current meal
#           and deletes it
# Output:   none

def delete_item():
    delete_choice = input('What item would you like to delete? [1-{}]: '.format(menu_item_count))

    if delete_choice.isnumeric():
        deleting_item = find_by_global_index(eval(delete_choice))
        if deleting_item in current_meal:
            current_meal.remove(deleting_item)
            print('\nItem removed!\n')

        else:
            print('\nItem was not found in the current meal\n')

    else:
        print('\nInvalid input, please try again!\n')


# Parameters:   none
# Input:        takes choice from the user
# Process:      prints non numeric options and awaits user response
# Output:       returns user input

def await_choice(choice_item_count):
    global all_meals

    print_menu()

    for option in options:
        print('{} ({})'.format(option[0],
                               option[1]),
              end='\t')

    print('\n')

    if len(current_meal) > 0 or len(all_meals) > 0:
        print(separator)

        if len(current_meal) > 0:
            print_current_meal()

        if len(all_meals) > 0:
            print_all_meals()

        print(separator, '\n')

        print_monetary()

    return input('Please enter an item [1-{}]: '.format(choice_item_count)).lower()


# Parameters:   string 'choice'
# Process:      evaluates choice with valid options
# Output:       calls function according to choice
#               or asks user to try again

def evaluate_choice(choice):
    global menu_item_count
    global current_meal
    global all_meals

    if choice == options[0][1]:
        print('\nThank you, come again!')
        exit()

    elif choice == options[1][1]:
        if len(current_meal) > 0:
            all_meals.append(current_meal)

        current_meal = []

    elif choice == options[2][1]:
        delete_item()

    elif choice.isnumeric() \
            and (eval(choice)) in range(1, menu_item_count + 1):
        choice = eval(choice)

        current_meal.append(find_by_global_index(choice))

    else:
        print('\nInvalid input, please try again!\n')


# Input:    none
# Process:  counts menu items, prints title,
#           and initiates the program loop
# Output:   none

def main():
    global menu_item_count
    global appetizers
    global entrees
    global drinks
    global desserts

    menu_file_name = 'menu.txt'
    menu_reader(menu_file_name)

    menu_item_count = menu_item_counter()

    title_text = title.center(totalCountMultiplier-2, ' ')
    title_box = '-' * len(title_text) + 2*'-'

    print(' ', title_box, sep='')
    print('|', title_text, '|')
    print(' ', title_box, sep='')

    while True:
        evaluate_choice(await_choice(menu_item_count))


main()
