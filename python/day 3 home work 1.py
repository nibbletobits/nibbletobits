import math
number1 = int(input("input first number: "))
number2 = int(input("input second number: "))
total = float(number1 + number2)
print("the sum is: ", number1+number2)
print("the sqrt of the first integer is: ", math.sqrt(number1))
print("the average is: ", total//2)
if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
input('enter to end')
