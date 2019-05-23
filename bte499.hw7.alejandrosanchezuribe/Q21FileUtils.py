# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 2 - A

import Q21Person as Person


def read_file_data(plist, filename):
    ifile = open(filename, 'r')

    for line in ifile:
        ssn, fname, lname, dob, state = line.split()
        p = Person.Person(ssn, fname, lname, dob, state)
        plist.append(p)

    ifile.close()


def write_file_data(plist, filename):
    ofile = open(filename, 'w')

    for p in plist:
        ofile.write(str(p) + '\n')

    ofile.close()
