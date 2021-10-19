# ********************************************
# Program Name: Day 12, homework 1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 17, 2021
# Purpose: A program that adds user input to a list than prints a random word from the list.
# Modules used: random
# Input Variables:
# Output: print statements, that output the sum of the numbers
# ********************************************
import random


def main():
    word_list = []
    keep_adding = ""
    while keep_adding != "N":
        a_list = input("pleas enter a word to be added to the list: ")
        word_list.append(a_list)
        keep_adding = input("would you like to keep adding words Y/N: ").upper()
        while keep_adding != "Y" and keep_adding != "N":
            keep_adding = input("Error, enter Y/N: ").upper()

    print("your list is", word_list)
    print("the random pick =", random.choice(word_list))


main()
