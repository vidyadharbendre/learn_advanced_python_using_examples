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
    width = 4
    height = 5


    circleObj = Circle(radius)
    print("Area of the circle for the given radius {}:".format(radius), circleObj.calculate_area())

    squareObj = Square(side)
    print("Area of the square for the given side {}:".format(side), squareObj.calculate_area())

    rectangleObj = Rectangle(length, width)
    print("Area of the rectangle with width {} and height {}: {}".format(length, width, rectangleObj.calculate_area()))


    # Accept inputs for radius, side length, width, and height
    radius = float(input("Enter the radius of the circle: "))
    side = float(input("Enter the side length of the square: "))
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    # Create objects for circle, square, and rectangle
    circleObj = Circle(radius)
    squareObj = Square(side)
    rectangleObj = Rectangle(length, width)

    # Calculate and print the areas
    print("Area of the circle for the given radius {}:".format(radius), circleObj.calculate_area())
    print("Area of the square for the given side {}:".format(side), squareObj.calculate_area())
    print("Area of the rectangle with width {} and height {}: {}".format(length, width, rectangleObj.calculate_area()))

#
# Add triangle directory and calculate the area of the triangle
#



if __name__ == "__main__":
    main()
