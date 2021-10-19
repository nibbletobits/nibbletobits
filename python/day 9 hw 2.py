# ********************************************
# Program Name: Day 9, hw
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 07, 5, 2021
# Purpose: A program to practice creating functions + testing
# Modules used: none
# Input Variables: str value
# Output: print statements, that output function answers for main body
# ********************************************

def main():
    valid = True
    string = ""
    while valid == True:
        string = input("please input a string: ")
        for c in string:
            if c.isdigit():
                print("please only enter letters!")
                valid = False
                break
        if valid == True:
            break
        else:
            valid = True

    middle(string)


# middle
# fn finds and returns the middle value in the string
# @param numbers string set  def in main
# returns test mid value of string and if string is odd and or even
def middle(string):
    a = len(string)
    if a % 2 == 0:
        print("the string is even and the middle is: ", string[a//2-1] + string[a//2])

    else:
        print("the string is odd the middle is: ", string[a//2])

    return string


main()
