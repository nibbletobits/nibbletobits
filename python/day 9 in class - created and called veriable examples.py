# ********************************************
# Program Name: Day 9, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 30, 2021
# Purpose: A program to practice creating and calling functions
# Modules used: none
# Input Variables: num(1-3)
# Output: print statements, that output function answers for main body
# ********************************************


# av_three
# function prints the average of three values
# @param number(1-3): 'set in main
# @return function returns the average of the 3 numbers entered
def av_three(number1, number2, number3):
    number = (number1, number2, number3)
    average = sum(number)/3
    return average
# sm_three
# function prints the lowest value of three values
# @param number(1-3): 'set in main
# @return function returns the smallest of the 3 numbers entered


def sm_three(number1, number2, number3):
    small = min(number1, number2, number3)
    return small


def main():
    r_run = "Y"
    while r_run.upper() == "Y":
        try:
            num1 = float(input("please enter your first number: "))
            num2 = float(input("please enter your second number: "))
            num3 = float(input("please enter your third number: "))
            average1 = av_three(num1, num2, num3)
            print("the average of the three numbers is %.2f" % average1)
            smallest = sm_three(num1, num2, num3)
            print("%.2f is the smallest value" % smallest)
            r_run = input("would you like to run the program again Y/N: ")

        except:
            print("input was not correct")
            r_run = input("would you like to run the program again Y/N: ")


main()
