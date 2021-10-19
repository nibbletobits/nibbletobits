# ********************************************
# Program Name: Day 10, in class
# Programmer: Jordan P. Nolin
# CSC-119: Summer 2021
# Date: 07, 7, 2021
# Purpose: function to be imported into a nether file
# Modules used: imported math used to calculate the volume of a sphere
# Input Variables: Function gets called in diff program returns function
# Output: returns function to main file
# ********************************************


# calculate the volume of a sphere
# @parm radius indicates the length of half the length of a sphere as a float
# @ param takes radios from input in main
# @returns the volume of a sphere as a float.
def sph_vol(radius):
    from math import pi
    v = 4/3 * pi * radius ** 3
    return v
