# ********************************************
# Program Name: Day 7, hw 1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 23, 2021
# Purpose: A program that uses a for loop to find all positive numbers devisible by 10 less than input
# Modules used:
# Input Variables: number() ect
# Output: print statements, that output variable answer
# ********************************************
def main():
    max1 = 0
    total = 0
    list_size = int(input("please enter how many numbers you would like to use: "))
    for i in range(list_size):
        member = float(input("what number would you like to use: "))
        if member > max1:
            max1 = member
        total = total + member
    average = total / list_size
    print("the largest number is: ", max1)
    print("the average of your numbers is: ",average)
main()
input("press enter to end")
