# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 2 April 2019
# Assignment: Take Home Midterm - Question 1


def non_discounted_indexes(prices, final_prices):
    indexes = []

    for i in range(len(prices)):
        if prices[i] == final_prices[i]:
            indexes.append(i)

    indexes.sort()

    print_indexes = ''

    for index in indexes:
        print_indexes += str(index) + ' '

    print('Non discounted item indexes:', print_indexes.rstrip())


def final_price_calc(prices):
    final_prices = []
    total_price = 0

    for i in range(len(prices)):
        final_price = prices[i]

        if i < len(prices):
            prices_to_the_right = prices[i+1:]

            for compare in prices_to_the_right:
                if compare <= prices[i]:
                    final_price -= compare
                    break

        final_prices.append(final_price)
        total_price += final_price

    print('Total cost:', total_price)
    non_discounted_indexes(prices, final_prices)


def main():
    prices = [5, 1, 3, 4, 6, 2]
    final_price_calc(prices)


main()
