# ********************************************
# Program Name: Day 10, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 07, 10, 2021
# Purpose: main fn that prints the valume of a sphear
# Modules used: volume_of_sphere_fn
# Input Variables: main takes veriable radious
# Output: prints the volume of a sphear
# ********************************************


from volume_of_sphere_fn import sph_vol


def main():
    radius = float(input("enter the radius of the sphere: "))
    sphVol = sph_vol(radius)
    print("the volume of the sphear is %.2f" % sphVol)
main()
