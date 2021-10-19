# ********************************************
# Program Name: Day 5, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 16, 2021
# Purpose: A program to evaluate strings
# Modules used: none
# Input Variables: year()
# Output: print statements, that output variable answer
# ********************************************
def main():
    while True:
        year = int(input("input a Year that falls after 1582: "))
        if year < 1582:
            print("year does not meet criteria")
            return
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("is a leap year!")
                else:
                    print("Not a leap year!")
            else:
                print("is a leap year!")
        else:
            print("Not a leap year!")


main()
