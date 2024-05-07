#!/usr/bin/env python3

import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the 'src' directory
src_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the 'src' directory to the Python path
sys.path.append(src_dir)

#print(src_dir)

from circle.circle import Circle
from rectangle.rectangle import Rectangle
from square.square import Square

def main():
    radius = 1
    side = 2
    length = 3
    width = 3
    height = 9


    circleObj = Circle(radius)
    print("Area of the circle for the given radius {}:".format(radius), circleObj.area())

    squareObj = Square(side)
    print("Area of the square for the given side {}:".format(side), squareObj.area())

    rectangleObj = Rectangle(length, width)
    print("Area of the rectangle with width {} and height {}: {}".format(length, width, rectangleObj.area()))



if __name__ == "__main__":
    main()
