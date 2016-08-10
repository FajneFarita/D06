#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
import string


# Body


def avoids(word, f_letters):
    """ return True if word NOT forbidden"""
    for each_letter in f_letters:
        if each_letter not in word:
            return True
        else:
            return False


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    forbidden_letters = input("Enter a string of forbidden letters: ")
    count = 0
    while True:
        if avoids(word, forbidden_letters):
        print(coun+=1)
    return count

def forbidden_param(string):
    """ return count of words NOT forbidden by param"""
    print("{} numbers don't contain any of your forbidden letters".format(forbidden_prompt()))


def find_five(filename):
    count = 0
    alpha = ascii_lowercase
    for letter in alpha:
        if letter in  open(filename, 'r').read():
            # I give up





##############################################################################
def main():
    find_five("words.txt")

if __name__ == '__main__':
    main()
