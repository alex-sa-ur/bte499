# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 1


class Menu:
    def __init__(self, category_containers):
        self.category_containers = category_containers

    def __str__(self):
        display_counter = 1

        output = ''

        for category_container in self.category_containers:
            output += category_container.center(60, ' ') + '\n'
            output += ('='*len(category_container)).center(60, ' ') + '\n'

            for item in self.category_containers[category_container]:
                output += str(display_counter) + '{:>{x}}'.format(str(item), x=60-len(str(display_counter))) + '\n'
                display_counter += 1

            output += '\n'

        return output

    def __len__(self):
        length = 0

        for category_container in self.category_containers:
            length += len(self.category_containers[category_container])

        return length

    def find_item(self, index):
        for category_container in self.category_containers:
            for item in self.category_containers[category_container]:
                if index == 0:
                    return item
                index -= 1

