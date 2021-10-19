# ********************************************
# Program Name: Day 11, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 12, 2021
# Purpose: A program that sends a word and calls a function.
# Modules used: def vert_word
# Input Variables: (word)
# Output: print statement calls function vert_word
# ********************************************

from day_11_in_class_fn import vert_word

def main():
    word = str(input("pleas enter a word: "))
    vert_word(word)

main()
input("press enter to end")
