# ********************************************
# Program Name: Day 14, HW 1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 24, 2021
# Purpose: program that opens a file and reads than sends it to output location
# Modules used:
# Input Variables: none
# Output:
# ********************************************


def main():
    
    while True:
        try:
            file_1 = input("What file would you like to open: ")
            file_2 = input("what would you like to name the output file? ")
            read_fi = open(file_1, "r")
            write_fi = open(file_2, "w")
            in_out(read_fi, write_fi)
            break
        except:
            print("pleas enter a valid read file, include .txt extention")
            
    
# in_out creates files that are named in main
def in_out(one, two):
    line_num = 0
    for line in one.readlines():
        line_num += 1
        info = "/* " + str(line_num)+ "*/ " + line
        two.write(info)
        print(info)
    one.close()
    two.close()


main()
input("press enter to end")
