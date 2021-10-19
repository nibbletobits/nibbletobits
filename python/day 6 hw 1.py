# ********************************************
# Program Name: Day 6, hw 1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 21, 2021
# Purpose: A program to add the sum of all even numbers form 0-500
# Modules used: %2
# Input Variables: number() ect
# Output: print statements, that output variable answer
# ********************************************
def main():
    myNumber = 0
    stopNumber = 500
    total = 0
    while myNumber <= stopNumber:
        if (myNumber % 2 == 0):
            total = total + myNumber
        myNumber = myNumber + 1
    print("the total is", total)


main()
input("press enter to end")
