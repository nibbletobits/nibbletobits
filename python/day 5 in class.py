def main():
    #********************************************
    # Program Name: Day 5, in class
    # Programmer: Jordan P. Nolin
    # CSC-119: Summer 2021
    # Date: June 16, 2021
    # Purpose: A program to evaluate strings
    # Modules used: none
    # Input Variables: randomst()
    # Output: print statements, that output variable answer
    #********************************************

    random = input("input_variable_information: ")
    if random[0].upper():
        print("it starts with an uppercase")
    else:
        print("does not start with an upper")
    if random.isdigit():
        print("contains only digits")
    else:
        print("is not a digit")
    if random.isalpha():
        print("contains only letters")
    else:
        print("does not contain only letters")
    if random.isalnum() and not random.isalpha() and not random.isdigit():
        print("contains letters and numbers")
    else:
        print("does not contain both")
    if random.endswith("."):
        print("ends with a .")
    else:
        print("does not end with a .")
    if random.startswith("T"):
        print("starts with T")
    else:
        print("does not start with T")
    print(" length of the string is: ", len(random))


main()
input("exit to enter")
