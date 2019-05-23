# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 2 - B


import time
import random
import matplotlib.pyplot as plt
import Q22FileUtils as FileUtils


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


def find_most_popular(plist):
    most_popular = plist[0]

    for p in plist:
        if len(p.friends_list) > len(most_popular.friends_list):
            most_popular = p

    return most_popular


def promote_by_popularity(plist, sort_start, sort_end):
    most_popular = find_most_popular(plist[sort_start:sort_end])
    most_popular_index = plist.index(most_popular)

    plist[sort_start], plist[most_popular_index] = plist[most_popular_index], plist[sort_start]


def sort_by_popularity(plist, sort_start, sort_end):
    start_time = time.time()

    for i in range(sort_start, sort_end):
        promote_by_popularity(plist, i, sort_end)

    end_time = time.time()
    print('Time to sort:', end_time-start_time)


def common_friends(plist):
    common_friends_lists = []

    for p in plist:
        common_friends_list = []
        for compare_p in plist:
            if p != compare_p:
                for f in p.friends_list:
                    for compare_f in compare_p.friends_list:
                        if f == compare_f and f not in common_friends_list:
                            common_friends_list.append(f)
        common_friends_lists.append((p, common_friends_list))

    return common_friends_lists


def in_friends(plist):
    in_friends_lists = []

    for p in plist:
        in_friends_list = []
        for compare_p in plist:
            if p != compare_p:
                for f in compare_p.friends_list:
                    if f == p:
                        in_friends_list.append(compare_p)
                        break
        in_friends_lists.append((p, in_friends_list))

    return in_friends_lists


def random_in_range(a, b):
    return random.randint(a, b)


def random_friends_list(plist):
    for p in plist:
        for i in range(random_in_range(0, len(plist)//200)):
            new_friend_index = random_in_range(0, len(plist)-1)

            if plist[new_friend_index] not in p.friends_list and plist[new_friend_index] != p:
                p.friends_list.append(plist[new_friend_index])
            else:
                i -= 1


def random_unfriend(plist):
    for p in plist:
        for i in range(random_in_range(0, len(p.friends_list)//2)):
            unfriend_index = random_in_range(0, len(p.friends_list)-1)

            if plist[unfriend_index] in p.friends_list:
                p.friends_list.remove(plist[unfriend_index])
            else:
                i -= 1


def take_second(elem):
    return elem[1]


def birth_year_counter(plist):
    year_counter = []

    for p in plist:
        year = p.dob//10000

        if len(year_counter) > 0:

            for y in year_counter:
                if year == y[0]:
                    y[1] += 1
                    break

                if year != y[0] and y == year_counter[len(year_counter)-1]:
                    year_counter.append([year, 1])
                    break

        else:
            year_counter.append([year, 1])

    year_counter.sort(key=take_second, reverse=True)

    return year_counter


def state_counter(plist):
    state_count = []

    for p in plist:
        state = p.state

        if len(state_count) > 0:

            for s in state_count:
                if state == s[0]:
                    s[1] += 1
                    break

                if state != s[0] and s == state_count[len(state_count)-1]:
                    state_count.append([state, 1])
                    break

        else:
            state_count.append([state, 1])

    state_count.sort(key=take_second, reverse=True)

    return state_count


def name_counter(plist):
    name_count = []

    for p in plist:
        name = p.fname

        if len(name_count) > 0:

            for s in name_count:
                if name == s[0]:
                    s[1] += 1
                    break

                if name != s[0] and s == name_count[len(name_count)-1]:
                    name_count.append([name, 1])
                    break

        else:
            name_count.append([name, 1])

    name_count.sort(key=take_second, reverse=True)

    return name_count


def lname_counter(plist):
    name_count = []

    for p in plist:
        name = p.lname

        if len(name_count) > 0:

            for s in name_count:
                if name == s[0]:
                    s[1] += 1
                    break

                if name != s[0] and s == name_count[len(name_count)-1]:
                    name_count.append([name, 1])
                    break

        else:
            name_count.append([name, 1])

    name_count.sort(key=take_second, reverse=True)

    return name_count


def take_first(elem):
    return elem[0]


def age_bins(year_counter):
    year_counter.sort(key=take_first)
    bin_index = 0
    bins = []

    lower_bound = year_counter[0][0]
    upper_bound = lower_bound + 10

    bins.append([lower_bound, upper_bound, 0])

    for year in year_counter:
        if lower_bound <= year[0] <= upper_bound:
            bins[bin_index][2] += year[1]
        else:
            bin_index += 1
            lower_bound = upper_bound + 1
            upper_bound = lower_bound + 10
            bins.append([lower_bound, upper_bound, year[1]])

    return bins


def histogram(year_counter, bins):
    histogram_bins = [bins[0][0]]
    data = []
    for hbin in bins:
        histogram_bins.append(hbin[1])

    for year in year_counter:
        for i in range(year[1]):
            data.append(year[0])

    plt.hist(data, bins=histogram_bins, edgecolor='black', linewidth=1)
    plt.show()


def main():
    filename = 'people1.txt'
    plist = []
    FileUtils.read_file_data(plist, filename)

    # Part 11

    # Part e - add random friends
    random_friends_list(plist)

    # Part f - sort by popularity
    sort_by_popularity(plist, 0, len(plist))

    # Part g - find common friends
    common_friends_lists = common_friends(plist)

    for common_friends_list in common_friends_lists:
        print(common_friends_list[0].fname, common_friends_list[0].lname, 'has these friends in common:')

        for friend in common_friends_list[1]:
            print('\t', friend.fname, friend.lname)

    print()

    # Part h - find where in friends list
    in_friends_lists = in_friends(plist)

    for in_friends_list in in_friends_lists:
        print(in_friends_list[0].fname, in_friends_list[0].lname, 'is in these friends lists:')

        for friend in in_friends_list[1]:
            print('\t', friend.fname, friend.lname)

    print()

    # Part i - unfriend randomly
    random_unfriend(plist)

    # Part j - re-sort by popularity
    sort_by_popularity(plist, 0, len(plist))
    print()

    # Part 12

    # Part a - birth year counter
    year_counter = birth_year_counter(plist)

    print('People born per year:')

    for year in year_counter:
        print(year[0], ':', year[1])

    print()

    # Part b - state counter
    state_count = state_counter(plist)

    print('People born per state:')

    for state in state_count:
        print(state[0], ':', state[1])

    print()

    # Part c - most popular name
    name_count = name_counter(plist)

    print('Most popular name:', name_count[0][0])
    print()

    # Part d - name frequency
    print('Name frequency:')

    for name in name_count:
        print(name[0], ':', name[1])

    print()

    # Part e - last name frequency
    lname_count = lname_counter(plist)

    print('Most popular last name:', lname_count[0][0])
    print()

    print('Name frequency:')

    for lname in lname_count:
        print(lname[0], ':', lname[1])

    print()

    # Part f - age bins
    bins = age_bins(year_counter)

    print('Birth Year Bins:')

    for age_bin in bins:
        print(age_bin[0], '-', age_bin[1], ':', age_bin[2])

    print()

    # Part g - histogram
    histogram(year_counter, bins)


if __name__ == '__main__':
    main()
