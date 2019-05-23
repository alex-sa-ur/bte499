# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 2 - A

import time
import Q21FileUtils as FileUtils


def print_people_range(plist, rng=1):
    for i in range(rng):
        print(plist[i])


def basic_search(plist, name):
    search_results = []

    for p in plist:
        if p.fname.lower() == name.lower() \
                or p.lname.lower() == name.lower():
            search_results.append(p)

    return search_results


def find_oldest(plist):
    oldest = plist[0]

    for p in plist:
        if p.dob < oldest.dob:
            oldest = p

    return oldest


def promote_by_age(plist, sort_start, sort_end):
    oldest = find_oldest(plist[sort_start:sort_end])
    oldest_index = plist.index(oldest)

    plist[sort_start], plist[oldest_index] = plist[oldest_index], plist[sort_start]


def sort_by_age(plist, sort_start, sort_end):
    start_time = time.time()

    for i in range(sort_start, sort_end):
        promote_by_age(plist, i, sort_end)

    end_time = time.time()
    print('Time to sort:', end_time-start_time)


def main():
    filename = 'people1.txt'
    new_filename = 'new_people1.txt'
    plist = []
    FileUtils.read_file_data(plist, filename)

    # Part 1 - print first ten
    print_people_range(plist, 10)
    print()

    # Part 2 - basic search
    search_results = basic_search(plist, input('What name would you like to search for? > '))
    for p in search_results:
        print(p)

    print()

    # Part 3 - find oldest
    print(find_oldest(plist))
    print()

    # Part 4 (with part 6 mod) - promote oldest
    promote_by_age(plist, 0, len(plist))
    print(plist[0])
    print()

    # Part 5 (with part 6 mod) - promote second oldest
    promote_by_age(plist, 1, len(plist))
    print(plist[0])
    print(plist[1])
    print()

    # Part 7 - sort by age
    sort_by_age(plist, 0, len(plist))
    print()

    # Part 8 - write to file
    FileUtils.write_file_data(plist, new_filename)


if __name__ == '__main__':
    main()
