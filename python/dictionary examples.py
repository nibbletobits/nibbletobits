# ********************************************
# Program Name: Day 13, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 19, 2021
# Purpose: A program that takes a dictionary/ collection and completes a number of actions.
# Modules used: none
# Input Variables: none
# Output: print statements, that output the dictionary through out a set of steps
# ********************************************


def main():
    total = 0
    my_dictionary = {"Red": 104, "Green": 612, "Blue": 920}
    # step 1
    print(len(my_dictionary))
    # step 2
    print(my_dictionary.get("Blue"))
    # step 3
    for key in my_dictionary:
        if key == "Red" or key == "Green" or key == "Blue":
            total1 = my_dictionary["Red"]
            total2 = my_dictionary["Green"]
            total3 = my_dictionary["Blue"]
            total = total1 + total2 + total3
        else:
            print("the item is not in my dictionary")
    print(total)
    # step 4
    if "Red" in my_dictionary == 612:
        print("true")
    else:
        print("false")
    # step 5
    if "Green" in my_dictionary:
        my_dictionary["Green"] = 710
        print(my_dictionary)
    # step 6
    key1 = "Orange"
    value = 832
    if key1 not in my_dictionary:
        my_dictionary[key1] = value
    print(my_dictionary)
    # step 8
    your_dictionary = {"Yellow": 1040, "Orange": 1214}
    my_dictionary = my_dictionary | your_dictionary
    print(my_dictionary)
    # step 9
    the_key = "Yellow"
    if the_key in my_dictionary:
        del my_dictionary[the_key]
    print(my_dictionary)
    

main()
input("press enter to end")
