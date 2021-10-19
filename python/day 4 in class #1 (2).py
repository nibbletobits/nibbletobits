def main():
    # is it a solid gas or liquid test pass/fail
    tempType = input("Please input if the temperature is in 'Celsius'(c) or 'Fahrenheit'(f): ")

    if tempType.lower() == "c":
        temperature = float(input('Please enter the temperature to determine if it is a solid liquid or gas: '))
        if temperature >= 100:
            print("It is a gas")
        elif temperature <= 0:
            print("It is a solid")
        elif 0 < temperature < 100:
            print("It is a liquid")
    elif tempType.lower() == "f":
        temperature = float(input('Please enter the temperature to determine if it is a solid liquid or gas: '))
        if temperature >= 212:
            print("Its a gas")
        elif temperature <= 32:
            print("Its a solid")
        elif 32 < temperature < 212:
            print("It's a liquid")
    if tempType != "c" and tempType != "f":
        print('That is not a type')

# start the program
main()
print(input("press enter to end "))
