"""
Author:       Alejandro Sanchez Uribe
Date:         29 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 1 - Question 7
"""


# Parameters:   word to check
# Process:      checks to see if the next letters are consecutive
#               by comparing ASCII values
# Output        returns true or false
#               based on evaluation

def isTripleConsecutive(word):
    for i in range(len(word) - 2):
        if ord(word[i]) == ord(word[i+1]) - 1 and ord(word[i]) == ord(word[i+2]) - 2:
            return True
    return False


# Input:    a word from the user
# Process:  checks for consecutive letters
# Output:   true or false for evaluation
#           for consecutive letters

wordInput = input('Input word to evaluate for consecutive letters: ').lower()

if len(wordInput) >= 3:
    print(isTripleConsecutive(wordInput))
else:
    print('Word is too short, please try again')
