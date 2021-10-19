# ********************************************
# Program Name: Day 7, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 23, 2021
# Purpose: A program that uses a for loop to find all positive numbers devisible by 10 less than input
# Modules used:
# Input Variables: number() ect
# Output: print statements, that output variable answer
# ********************************************
def main():
    n = int(input("input a number to be tested: "))
    numbers = range(0, n+1, 10)
    if n > 0:
        print("the numbers that are less than your number and divisible by 10 are")
        for i in numbers:
            print(i)
    else:
        print("your number is not positive")
main()
input("press enter to end")
