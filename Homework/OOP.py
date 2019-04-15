#!/usr/bin/python

import sys
import math
import pytest


class Line:
    def __init__(self, coor1, coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    
    def distance(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
    
    def slope(self):
        return float((self.y2 - self.y1))/float((self.x2 - self.x1))


class Cylinder:
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return 2.0 * Cylinder.pi * self.radius * (self.height + self.radius)


# Driver code to test all functions
def main():
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)

    li = Line(coordinate1, coordinate2)

    assert(li.distance()) == pytest.approx(9.433981132056603, 0.00000000000000001)
    assert(li.slope()) == pytest.approx(1.6, 0.00001)

    c = Cylinder(2, 3)

    assert(c.volume()) == pytest.approx(56.52, 0.000001)
    assert(c.surface_area() == pytest.approx(94.2, 0.00001)) 
    
    print "All tests passed"

if __name__ == "__main__":
    main()