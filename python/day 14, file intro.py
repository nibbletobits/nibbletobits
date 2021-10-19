# ********************************************
# Program Name: Day 14, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 21, 2021
# Purpose: A program that opens a file writes in a file closes and reads it.
# Modules used: none
# Input Variables: none
# Output: program outputs string to file hello.txt 
# ********************************************


def main():
    file = open("hello.txt", "w")
    file.write("hello world!")
    file.close()
    read_file = open("hello.txt", "r")
    file_read = read_file.read()
    print(file_read)
    read_file.close()


main()
