# ********************************************
# Program Name: Day 9, hw
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 07, 5, 2021
# Purpose: A program to practice creating functions + testing
# Modules used: none
# Input Variables: num(1-3)
# Output: print statements, that output function answers for main body
# ********************************************

def main():
    name = str(input("please enter your name: "))
    re_run = "Y"
    while re_run.upper() == "Y":
        try:
            x = float(input("pleas enter your first number: "))
            y = float(input("please enter your second number: "))
            z = float(input("pleas enter your third number: "))
            same = allTheSame(x, y, z)
            different = allDifferent(x, y, z)
            sort = sorted1(x, y, z)
            print(same, "\n", different, "\n", sort)
            re_run = input("'thank you for your time': %s would you like to run the program again Y/N?: " % name)
        except:
            print("input was not a number")
            re_run = input("'thank you for your time': %s would you like to run the program again Y/N?: " % name)


# allTheSame
# fn returns argument is all numbers are the same
# @param numbers x y z set in main
# returns test if all numbers are the same
def allTheSame(x, y, z):
    argument = str("")
    if x == y and x == z:
        argument = str("the arguments are all the same")
    return argument

# allDifferent
# fn returns argument is all numbers are different
# @param numbers x y z set in main
# returns test if all numbers are different
def allDifferent(x, y, z):
    argument1 = str("")
    if x != y or z != x:
        argument1 = str("the arguments are all different")
    return argument1

# sorted1
# fn returns argument are numbers in order
# @param numbers x y z set in main
# returns test if all numbers are in order
def sorted1(x, y, z):
    argument3 = str("")
    if x <= y and y <= z or z <= y and y <= x :
        argument3 = str("the arguments are sorted")
    return argument3


main()
