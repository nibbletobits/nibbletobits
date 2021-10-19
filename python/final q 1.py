# ********************************************
# Program Name: Day 17, final #1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 8 2, 2021
# Purpose: program opens csv file find total of columns 1 and 4 and
# Modules used: def average
# Input Variables: none
# Output: print statements for purpose.
# ********************************************

def main():
    import random
    my_list = []
    total = 0
    count = 60
    for a in range(count):
        numbers = random.randint(1, 500)
        total += numbers
        my_list.append(numbers)
    total3 = average(total, my_list)
    print(my_list, "\nthe average of the numbers selected are %.2f" % total3)


# calculates average for main
# takes perams[total, mylist]
def average(total, my_list):
    devizer = len(my_list)
    adv = total / devizer
    return adv
# function should create total

main()
input("press enter to exit")
# total in function already calculates total, need to let function do that part.

# fixed it after this line

# ********************************************
# Program Name: Day 17, final #1
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 8 2, 2021
# Purpose: program opens csv file find total of columns 1 and 4 and
# Modules used: def average
# Input Variables: none
# Output: print statements for purpose.
# ********************************************

def main():
    import random
    my_list = []
    count = 60
    for a in range(count):
        numbers = random.randint(1, 500)
        my_list.append(numbers)
    print(my_list, "\nThe average of the numbers selected are %.2f" % average(my_list))


# calculates average for main
# takes perams[total, mylist]
def average(my_list):
    total = sum(my_list)
    div = len(my_list)
    real_total = total / div
    return real_total
# function should create total
