# ********************************************
# Program Name: Day 5, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 21, 2021
# Purpose: A program to add the sum of all square roots
# Modules used:
# Input Variables: number() ect
# Output: print statements, that output variable answer
# ********************************************
def main():
    myNumber = 1
    stopNumber = 50
    total = 0
    while myNumber <= stopNumber:
        x = myNumber**2
        total = total + x
        myNumber = myNumber + 1
    print("the total is", total)


main()
input("press enter to end")
