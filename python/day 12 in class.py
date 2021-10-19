# ********************************************
# Program Name: Day 12, class word
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 14, 2021
# Purpose: A program that goes through steps changing and testing values of a list
# Modules used:
# Input Variables:
# Output: print statements output changes made to list
# ********************************************

def main():
    my_list = [1, 10, 20, 21, 5, 7, 9, 13, 10, 20, 55]
    # 1 here I print the original list
    print(my_list)
    # 2 printing the length of the list
    len1 = len(my_list)
    print("the length of the list is:", len1)
    # 3 calculating the sum of the list
    len1 = sum(my_list)
    print("the sum of my list is:", len1)
    # 4 printing the largest number and its index
    max_n = max(my_list)
    len2 = my_list.index(max_n)
    print("the biggest number in the list is", len1, "the position of that number in the list is", len2)
    for d in my_list:
        if d == 21:
            d = my_list.index(21)
            print("the index of 21 is", d)
    # 5 all 10's in the lst get changed to 15's.
    for c in my_list:
        if c == 10:
            c = my_list.index(10)
            my_list[c] = 15
    print(my_list)
    # 6 making a new list [20, 8] and then concatenating the two lists together
    my_list2 = [20, 8]
    my_list += my_list2
    print(my_list)
    # 7 append 12 to the list
    my_list.append(12)
    print(my_list)
    # 8 insert 16 to the front of the list
    my_list.insert(0, 16)
    print(my_list)
    # 9 sort the list
    print(sorted(my_list))
    # 10 use the pop() fn to delete the last number from the list then print the deleted item and list
    my_list = sorted(my_list)
    poped = my_list.pop(-1)
    print(poped, my_list)
    # 11 print how many 20's are in the list
    count = 0
    for number in my_list:
        if number == 20:
            count += 1
    print("the number of 20s in the list is", count)
    # 12 delete the first number 20 from the list, then print the list.
    my_list.remove(20)
    print(my_list)
    # 13 test the answer
    answer = [1, 5, 7, 8, 9, 12, 13, 15, 15, 16, 20, 20, 21]
    if my_list == answer:
        print("the list is correct and this is fun practice \n", my_list)
    else:
        print("there was an error in the logic")


main()
input("press enter to end")
