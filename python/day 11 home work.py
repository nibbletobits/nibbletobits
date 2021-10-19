# ********************************************
# Program Name: Day 11, homework
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: June 30, 2021
# Purpose: A program that asks the user for two inputs [r, h] than calls the list of functions.
# Modules used: spherevolume(r,h), spheresurface(r,h), cylindervolume(r,h), cylinderserface(r,h), conevolume(r,h), conesurface(r,h)
# Input Variables: inputs for variables[r, h]
# Output: print statements, that output function answers for main body
# ********************************************
def main():
    from day_11_hw_fn import spheresurvolume, spheresurface, cylindervolume,\
        cylindersurface, conevolume, conesurface
    try:
        r = float(input("pleas enter the radius: "))
        h = float(input("pleas enter the height: "))
        print("the volume of the sphear is: %.2f" % spheresurvolume(r))
        print("the surface area of the sphear is: %.2f" % spheresurface(r))
        print("the volume of the cylinder is: %.2f" % cylindervolume(r, h))
        print("the surface area of the cylinder is: %.2f" % cylindersurface(r, h))
        print("the vloume of the cone is: %.2f" % conevolume(r, h))
        print("the surface area of the cone is: %.2f" % conesurface(r, h))
    except:
        print("'Error', please enter a Number!")

main()
input("press enter to end the program")
