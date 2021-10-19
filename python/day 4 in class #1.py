def main():
    # is it a solid gas or liquid test pass/fail
    tempType = (input("Please input if the temperature is in 'Celsius'(c) or 'Fahrenheit'(f): "))
    temperature = float(input('Please enter the temperature to determine if it is a solid liquid or gas: '))

    if tempType.lower() == "c":
        if temperature >= 100:
            print("It is a gas")
        elif temperature <= 0:
            print("It is a solid")
        elif 0 < temperature < 100:
            print("It is a liquid")
    elif tempType.upper() == "f":
        if temperature >= 212:
            print("Its a gas")
        elif temperature <= 32:
            print("Its a solid")
        elif 32 < temperature < 212:
            print("It's a liquid")


# start the program
main()
print(input("press enter to end "))
