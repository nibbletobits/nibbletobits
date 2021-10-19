# ********************************************
# Program Name: Day 13, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 19, 2021
# Purpose: A program that takes a dictionary and prints the count of 15
# Modules used: none
# Input Variables: none
# Output: print statements that output keys of value 15 and number of 15 values
# ********************************************


def main():
    key_val = 0
    key_15 = []
    animals = {"Lion": 10, "Dog": 15, "Horse": 10, "Cat": 9, "Mouse": 10, "Deer": 15, "Turkey": 15}
    for key in animals:
        if animals[key] == 15:
            key_val += 1
            key_15.append(key)
        print("the key= ", key, "the value = ", animals[key])
    print("the values that are = 15 are:", key_15, "'and the value is 15:", key_val, "times")


main()
input("press enter to end")
