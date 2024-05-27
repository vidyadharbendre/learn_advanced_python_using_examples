#!/usr/bin/env python3

import math  # Import the math module for mathematical operations

class Circle:
    def __init__(self, radius):
        """
        Constructor method (__init__):
        This method is called automatically when a new Circle object is created.
        It initializes the attributes of the Circle object.
        
        Parameters:
        - radius: The radius of the circle.
        """
        self.radius = radius  # Set the radius attribute to the value passed as an argument

    def set_radius(self, radius):
        """
        Method to set the radius of the circle.
        
        Parameters:
        - radius: The new value for the radius of the circle.
        """
        self.radius = radius  # Set the radius attribute to the new value

    def get_radius(self):
        """
        Method to get the radius of the circle.
        
        Returns:
        - The current radius of the circle.
        """
        return self.radius  # Return the value of the radius attribute

    def calculate_area(self):
        """
        Method to calculate the area of the circle.
        
        Returns:
        - The area of the circle calculated based on the radius.
        """
        return math.pi * self.radius ** 2  # Calculate and return the area of the circle

    def display_area(self):
        """
        Method to display the area of the circle.
        It prints the radius and the calculated area.
        """
        radius = self.get_radius()  # Get the radius of the circle
        area = self.calculate_area()  # Calculate the area of the circle
        print(f"Radius of the circle is: {radius}")  # Print the radius
        print(f"Area of the circle is: {area}")  # Print the calculated area
