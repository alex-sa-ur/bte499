# Author: Alejandro Sanchez
# Class: BTE 499
# Date: 21 March 2019


class Person(object):

    def __init__(self, ssn=0, fname=' ', lname=' ', dob=0, state=' '):
        self.ssn = ssn
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.state = state
        self.friends_list = []

    def __str__(self):
        return str(self.ssn) + ' ' + self.fname + ' ' + self.lname + ' ' + str(self.dob) + ' ' + self.state
