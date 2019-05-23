"""
Author:       Alejandro Sanchez Uribe
Date:         29 January 2019
Class:        BTE 499
Assignment:   Assignment 3 - Part 1 - Question 4
"""

import string

# Input:    phrase from the user
# Process:  remove punctuation and whitespace,
#           lowercase all letters,
#           evaluate for palindrome
# Output:   Evaluation as a palindrome (yes or no)

phrase = input('Input a phrase for palindrome evaluation: ')

phrase = ''.join(phrase.translate(str.maketrans('', '', string.punctuation)).lower().strip().split())
backwards = "".join(reversed(phrase))

print('\nEvaluation: {} == {} ?\n'.format(phrase, backwards))

if phrase == backwards:
    print('This phrase is a palindrome!')
    exit()

print('This phrase is not a palindrome')
