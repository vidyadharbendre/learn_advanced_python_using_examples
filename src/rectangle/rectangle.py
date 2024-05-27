#!/usr/bin/env python3

class Rectangle:
    def __init__(self, length, width):
        """
        Constructor method (__init__):
        This method is called automatically when a new Rectangle object is created.
        It initializes the attributes of the Rectangle object.
        
        Parameters:
        - length: The length of the rectangle.
        - width: The width of the rectangle.
        """
        self.length = length  # Set the length attribute to the value passed as an argument
        self.width = width  # Set the width attribute to the value passed as an argument

    def set_length(self, length):
        """
        Method to set the length of the rectangle.
        
        Parameters:
        - length: The new value for the length of the rectangle.
        """
        self.length = length  # Set the length attribute to the new value

    def get_length(self):
        """
        Method to get the length of the rectangle.
        
        Returns:
        - The current length of the rectangle.
        """
        return self.length  # Return the value of the length attribute

    def set_width(self, width):
        """
        Method to set the width of the rectangle.
        
        Parameters:
        - width: The new value for the width of the rectangle.
        """
        self.width = width  # Set the width attribute to the new value

    def get_width(self):
        """
        Method to get the width of the rectangle.
        
        Returns:
        - The current width of the rectangle.
        """
        return self.width  # Return the value of the width attribute

    def calculate_area(self):
        """
        Method to calculate the area of the rectangle.
        
        Returns:
        - The area of the rectangle calculated based on the length and width.
        """
        return self.length * self.width  # Calculate and return the area of the rectangle

    def display_area(self):
        """
        Method to display the area of the rectangle.
        It prints the length, width, and the calculated area.
        """
        length = self.get_length()  # Get the length of the rectangle
        width = self.get_width()  # Get the width of the rectangle
        area = self.calculate_area()  # Calculate the area of the rectangle
        print(f"Length of the rectangle is: {length}")  # Print the length
        print(f"Width of the rectangle is: {width}")  # Print the width
        print(f"Area of the rectangle is: {area}")  # Print the calculated area
