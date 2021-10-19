import math

a = float(input("Input a number a="))
b = float(input("Input a number b="))
gamma = float(input("Input an angle C="))
v=math.cos(gamma)
first = ((a ** 2) + (b ** 2)) - (2 * a * b * v)

final = math.sqrt(first)
print("c={}".format(final))
input("input enter to end")
