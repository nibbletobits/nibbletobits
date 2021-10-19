# ********************************************
# Program Name: Day 6, home work 2
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 22, 2021
# Purpose: A program that reads and tests floating numbers and prints the difference between the largest and smallest
# Modules used:
# Input Variables: number() ect
# Output: print statements, that output variable answer
# ********************************************
def main():
    number_list = []
    while True:
        number = input("input floating point numbers than enter N to run program: ")
        if number == "N":
            break
        try:
            number = float(number)
            number_list.append(number)
        except ValueError as e:
            print(e)
    if len(number_list) != 0 :
        print("your input numbers: ", number_list)
        print("your min number is: ", min(number_list), "your max number is: ", max(number_list))
        print("the range of your list is: ", max(number_list) - min(number_list))
    else:
        print("you must enter numbers")


main()
input("press enter to end")
