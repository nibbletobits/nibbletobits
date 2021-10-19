# ********************************************
# Program Name: Day 12, homework 1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 15, 2021
# Purpose: A program that adds the numerical values in a list.
# Modules used: none
# Input Variables:
# Output: print statements, that output the sum of the numbers
# ********************************************
def main():
    list2 = []
    my_list = ["hello", "name", 6, 3.1, 7.2, 9.4, "good bye", 11.1, 22]
    for item in my_list:
        if type(item) is not str:
            list2.append(item)
    answer = sum(list2)
    print("%.2f" % answer)


main()
