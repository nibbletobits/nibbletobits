# ********************************************
# Program Name: Day 10, hw
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 07, 10, 2021
# Purpose: main fn that validates a new password
# Modules used:
# Input Variables:
# Output:
# ********************************************


# tests the length of a string
# @parm pa55
# @parm string len should be greater than 10
# @ return len should be greater to or equal to 10
def pas_len(pa55):
    return len(pa55) >= 10
# tests string for upper and lower letters
# @parm pa55
# @pa55 len must have upper and lower
# returns bullion


def up_to_the_low(pa55):
    return any(x.isupper() for x in pa55) and any(x.islower() for x in pa55)
# tests that the password contains a number
# @param pa55
# @param requires digit
# @returns bullion


def dig_it(pa55):
    return any(x.isdigit() for x in pa55)
# cross checks two passwords to make sure they mach
#  @param password[old,new]
# @param requires pass mach
# returns true false


def pas_mach(old_password, new_password):
    return old_password == new_password


def main():
    valid = False

    while not valid:
        pass_input = input("pleas enter a password\n password must be:" +
                           " '10 characters long',\n 'contain one upper and lower' and, \n 'at least one digit': ")
        validate_length = pas_len(pass_input)
        validate_digit = dig_it(pass_input)
        validate_upper_and_lower = up_to_the_low(pass_input)

        valid = validate_length and validate_digit and validate_upper_and_lower

        if valid:
            new_password = input("pleas re-enter the password: ")
            validate_pass_match = pas_mach(pass_input, new_password)

            if not validate_pass_match:
                print("Passwords should match")

            valid = valid and validate_pass_match

        if not validate_length:
            print("Password should have a length >=10")

        if not validate_digit:
            print("Password should have at lest 1 digit")

        if not validate_upper_and_lower:
            print("Password should have at least 1 upper and 1 lower character")

    print("Password accepted!")


main()
input("press enter to end")
