# ********************************************
# Program Name: Day 14, HW 2
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 24, 2021
# Purpose: program that opens a file and reads than passes to fn
# Modules used: flo_avg
# Input Variables: none
# Output:
# ********************************************


def main():
    while True:
        try:
            file_name = input("enter file that contanes columns: ")
            my_file = open(file_name, "r")
            flo_avg(my_file)
            break
        except:
            print("enter a valid file name!, hint(use .txt extention )")


def flo_avg(file):
    column_1 = []
    column_2 = []
    line_num = 0
    for line in file.readlines():
        line_num += 1
        spl_str = line.strip().split()
        column_1.append(float(spl_str[0]))
        column_2.append((float(spl_str[1])))
    
    avg_1 = sum(column_1) / line_num
    avg_2 = sum(column_2) / line_num
    print("%.2f" % avg_1,"%.2f" % avg_2)


main()
input("press enter to end")
