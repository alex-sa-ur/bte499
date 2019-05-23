# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 30 April 2019
# Assignment: Assignment 6 - Question 2 - A


class Person(object):

    def __init__(self, ssn=0, fname=' ', lname=' ', dob=0, state=' '):
        self.ssn = ssn
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.state = state

    def __str__(self):
        return str(self.ssn) + ' ' + self.fname + ' ' + self.lname + ' ' + str(self.dob) + ' ' + self.state
