# ********************************************
# Program Name: Day 16, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 7 26, 2021
# Purpose: program / camel Game -
# Modules used:
# Input Variables:
# Output: print statements for purpose.
# ********************************************

import random


def main():
    print("Welcome to Camel!\n"
          "You have stolen a camel to make your way across the great Mobi desert.\n"
          "The natives want their camel back and are chasing you down! Survive your\n"
          "desert trek and outrun the natives.")
    done = False
    # variables for miles traveled, thirst, camel tiredness.
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_natives_traveled = -20
    drinks = 5
    distance_between = 0
    warning = 15
    moves_made = 0
    # natives_distance_behind = distance_natives_traveled - random native travel

    # here is the main program loop
    while done == False:
        moves_made += 1
        print("A. Drink from your canteen.\n"
              "B. Ahead moderate speed.\n"
              "C. Ahead full speed.\n"
              "D. Stop for the night.\n"
              "E. Status check.\n"
              "Q. Quit.")
        if distance_between <= 0:
            distance_between = miles_traveled - (distance_natives_traveled*-1)
        elif distance_between > 0:
            distance_between = miles_traveled - distance_natives_traveled
        user_choice = input("please choose one of the above.: ")
        if user_choice.upper() == "Q":
            print("The program has ended!")
            done = True
            continue
        elif user_choice.upper() == "E":
            print("Miles traveled ", miles_traveled, "\nDrinks in canteen: ", drinks,
                  "\nThe natives are", distance_natives_traveled - miles_traveled, "behind you.")
        elif user_choice.upper() == "D":
            print("You have chosen to stop for rest.")
            camel_tiredness = 0
            print("the camel is now rested")
            distance_natives_traveled += random.randint(7, 14)
        # 13
        elif user_choice.upper() == "C":
            print("Full speed ahead!")
            miles_moved = random.randint(10, 20)
            miles_traveled += miles_moved
            print("you moved:", miles_moved, "miles!")
            thirst += 1
            camel_tiredness += 2
            distance_natives_traveled += random.randint(7, 14)
        # 14
        elif user_choice.upper() == "B":
            print("you moved at half speed")
            miles_traveled += random.randint(5, 12)
            print("you have traveled:", miles_traveled, "miles!")
            thirst += 1
            camel_tiredness += 1
            distance_natives_traveled += random.randint(7, 14)

        # 15
        elif user_choice.upper() == "A":
            if drinks > 0:
                drinks = drinks - 1
                thirst = 0
                print("you have drank from your canteen, you have:", drinks, "left in the canteen")
                continue
            else:
                print("you do not have any drinks left")
                continue
        # 16
        while thirst < 6 and thirst >= 4:
            if user_choice.upper() != "A":
                print("you are thirsty" + " your thirst levels are, ", thirst)
                break
            continue
        # 17
        if thirst >= 6:
            done = True
            print("YOU DIED of thirst")
            continue
        # 18
        if camel_tiredness >= 5 and camel_tiredness < 8:
            print("Your camel is getting tired")
        # 19
        elif camel_tiredness >= 8:
            print("your camel has died of exhaustion")
            done = True
            continue
        # 20
        if distance_natives_traveled >= miles_traveled:
            print("'GAME OVER', the natives have caught you")
            done = True
            continue
        # 21
        elif distance_between <= warning and moves_made > 3:
            print("The natives are getting close hurry up!")
        # 22
        if miles_traveled >= 200:
            print("!A WINNER IS YOU!")
        # 23
        oasis = random.randint(1, 20)
        if oasis == 15:
            print("You have found an oasis ")
            drinks = 5
            thirst = 0
            camel_tiredness = 0
            print("your assets have been reset")


main()
