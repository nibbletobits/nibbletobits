def main():
    # day 4 home work assignment 1
        number = int(input("enter a number less than 1 million: "))
        if number < 0:
            print(number)
            print("the positive of the number is "+str(number * -1))
        elif number>999999 and number <= 9999999:
             print("your number has 7 characters")
        elif number > -999999 and number <= -9999999:
            print("the positive of the number is " + str(number * -1))
            print("your number has 7 characters")
        elif number>99999 and number <= 999999:
              print("your number has 6 characters")
        elif number > -99999 and number <= -999999:
              print("the positive of the number is " + str(number * -1))
              print("your number has 6 characters")
        elif number>9999 and number <= 99999:
              print("your number has 5 characters")
        elif number > -9999 and number <= -99999:
            print("the positive of the number is " + str(number * -1))
            print("your number has 5 characters")
        elif number>999 and number <= 9999:
                print("your number has 4 characters")
        elif number > -999 and number <= -9999:
             print("the positive of the number is " + str(number * -1))
             print("your number has 4 characters")
        elif number>99 and number <= 999:
              print("your number has 3 characters")
        elif number > -99 and number <= -999:
              print("the positive of the number is " + str(number * -1))
              print("your number has 3 characters")
        elif number>9 and number <= 99:
              print("your number has 2 characters")
        elif number > -9 and number <= -99:
                print("the positive of the number is " + str(number * -1))
                print("your number has 2 characters")
        elif number>0 and number <= 9:
              print("your number has 1 characters")
        elif number > -0 and number <= -9:
                print("the positive of the number is " + str(number * -1))
                print("your number has 1 characters")
        else:
            print("out of range")
            print("the positive of the number is " + str(number * -1))


main()
input("press enter key to end")
