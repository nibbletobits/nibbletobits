# ********************************************
# Program Name: Day 15, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 26, 2021
# Purpose: program that prints average yearly salary and number of years of experience for all jobs
# Modules used: ave_year_sal, ave_num_exp
# Input Variables: none
# Output: print statements for purpose.
# ********************************************


def main():
    from csv import reader
    line = 0
    ave_year_sal = 0
    ave_num_exp = 0
    in_file = open("pythonjobs.csv", "r")
    py_jobs = reader(in_file)
    for row in py_jobs:
        line += 1
        ave_num_exp += float(row[4])
        ave_year_sal += float(row[3])
    average = ave_year_sal / line
    average2 = ave_num_exp / line
    print("the average salary is %.2f" % average, "and the average years of experience is %.2f" % average2)
    in_file.close()


main()
input(press enter to end)
