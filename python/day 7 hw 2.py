# ********************************************
# Program Name: Day 5, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 16, 2021
# Purpose: A program to evaluate strings
# Modules used: none
# Input Variables: randomst()
# Output: print statements, that output variable answer
# ***************************************
def main():
    import random
    total = 0
    die = 6
    for a in range(die):
        roll = random.randint(1, 6)
        total += roll
        print(roll)
    print("the total value is: ", total)


main()
input("press enter to exit")
