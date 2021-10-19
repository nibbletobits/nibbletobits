# ********************************************
# Program Name: Day 15, hw
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 26, 2021
# Purpose: program calculates tax + total cost of menu item's
# Modules used: .csv
# Input Variables: (1-5)
# Output: print statements for purpose.
# ********************************************


def main():
    menu = {"1": 7.00, "2": 5.00, "3": 12.00, "4": 6.00, "5": 7.00}
    total = 0
    print('''
    Please choose the item number for the food you wish to purchase in bulk
    (1)carrots – $7.00
    (2)onions - $5.00
    (3)tomatoes - $12.00
    (4)green beans -$6.00
    (5)broccoli - $7.00
    ''')
    keep_adding = True
    while keep_adding == True:
        item_pick = input("choose an item based in the number (1-5) above: ")
        while True:
            try:
                bulk_select = int(input("how many of the bulk item would you like: "))
                break
            except:
                print("input needs to be digits 1-5:")
        for key in menu:
            if item_pick == key:
                adding_total = menu[item_pick] * bulk_select
                total += adding_total
        keep_going = input("do you want any other items 'Y'/'N': ")

        if keep_going.upper() == "Y":
            keep_adding = True
            continue
        elif keep_going.upper() == "N":
            keep_adding = False
            tax = total * state_tax()
            final_total = total + tax
            print("your final total is ", final_total)
        else:
            print("pleas enter a valid selection")
            continue


def state_tax():
    state_list = open("state_tax.csv", "r")
    # to travers in file, strip removes spaces, split
    while True:
        state_letter = input("pleas enter your state abbreviation: ")
        for item in state_list.readlines():
            item.strip()
            item1 = item.split(",")
            if state_letter.upper() == item1[0]:
                state_list.close()
                return float(item1[1])


main()
