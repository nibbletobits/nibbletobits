# ********************************************
# Program Name: Day 13, HW 2
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 24, 2021
# Purpose: A program that takes program int_name and changes two functions
# Modules used: digit_name(digit), teenName(number)
# Input Variables: none
# Output: print statements that output keys of value 15 and number of 15 values
# ********************************************

##
# This program is from Python for Everyone 2nd Edition by Cay Horstman and Rance Necaise
# The program can be found on page 271 - 272.
# You can also download the code from Wiley's web site at the follow the link:
#          www.wiley.com/college/horstmann
#
# This program turns an integer into its English name.
#

def main() :
   value = int(input("Please enter a positive integer < 1000: "))
   print(intName(value))


## Turns a number into its English name.
#  @param number a positive integer < 1,000
#  @return the name of the number (e.g. "two hundred seventy four")
#
def intName(number) :
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number.

   if part >= 100 :
      name = digitName(part // 100) + " hundred"
      part = part % 100

   if part >= 20 :
      name = name + " " + tensName(part)
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0

   if part > 0 :
      name = name + " " + digitName(part)

   return name


## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digitName(digit):
    digitName = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
                 7: "seven", 8: "eight", 9: "nine"}
    if digit in digitName:
        return digitName[digit]


## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
#
def teenName(number):
    teenName = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    if number in teenName:
        return teenName[number]


## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#
def tensName(number):
    tensName = {90: "ninety", 80: 'eighty', 70: "seventy", 60: "sixty", 50: "fifty", 40: "forty",
                30: "thirty", 20: "twenty"}
    number = number // 10 * 10
    if number in tensName:
        return tensName[number]


# Start the program.
main()
