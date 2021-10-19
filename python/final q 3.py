# ********************************************
# Program Name: Day 17, final #3
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 8 2, 2021
# Purpose: program opens csv file find total of columns 1 and 4 and
# Modules used: none
# Input Variables: options 1-5
# Output: print statements for purpose.
# ********************************************
import csv
def main():
    my_file = (open("Q1_file.csv", "r"))
    my_reader = csv.reader(my_file)
    total = 0
    for row in my_reader:
        for i in range(0,4):
            total += float(row[i]) + float(row[i])
            print(total)
    my_file.close()
    print("10.2f%" % total)
main()
input("\npress enter to end")



2 7 6 5
