import math
pv=float(input("input the value for pv="))
yrs=float(input("input the number of years="))
INT=float(input("input the amount of interest="))
FV=(pv*(1+(INT/100))**yrs)
print("FV is =",FV)
input("input enter to end")
