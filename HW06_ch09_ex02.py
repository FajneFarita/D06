#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
    return 'e' not in word
#has_no_e("reward")

def percentage(part, whole):
  return round(100 * float(part)/float(whole), 2)

def print_no_e(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if has_no_e(line):
                print(line)
                count +=1
        print("{} persent of the words in the list have no 'e'".format(percentage(count, len(lines))))
##############################################################################
def main():
    print_no_e("words.txt")

if __name__ == '__main__':
    main()
