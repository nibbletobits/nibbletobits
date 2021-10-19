## functions for day 11 home work main
## @parm are all set in main for the radious and height


# computes the volume of a sphear
# returns v for volume
def spheresurvolume(r):
    from math import pi
    v = (4/3) * pi * (r ** 3)
    return v


# computes the surface area of a sphear
# returns a for area
def spheresurface(r):
    from math import pi
    a = 4 * pi * (r ** 2)
    return a


# computes the volume of a cylinder
# returns v for volume
def cylindervolume(r, h):
    import math
    v = math.pi * (r ** 2) * h
    return v


# computes surface area for a cylinder
# returns a for area
def cylindersurface(r, h):
    from math import pi
    a = (2 * pi) * (r ** 2) + (2 * pi) * (r * h)
    return a


# computes the volume of a cone 
# returns v for volume
def conevolume(r, h):
    from math import pi
    v = (pi * (r ** 2) * (h/3))
    return v


# computes the surface area of a cone
# returnes the area
def conesurface(r, h):
    from math import pi, sqrt
    a = pi * r + sqrt((h ** 2) + (r ** 2))
    return a
