# ********************************************
# Program Name: Day 5, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 21, 2021
# Purpose: A program to evaluate a total
# Modules used: none
# Input Variables: randomst()
# Output: print statements, that output variable answer
# ********************************************
def main():
    total = 0.0
    count = 0
    print("just hit a blank return when done")
    value = input("enter an integer\n")
    while value != "":
        if value.isdigit() or value.count('.') == 1:
            num = float(value)
            total = total + num
            count = count + 1
        else:
            print("that was not a number")
        value = input("enter another number\n")
    if count > 0:
        average = total/count
    else:
        average = 0.0
    print("The total is:", total, " and the average is", average)


main()
input("press enter to end")
