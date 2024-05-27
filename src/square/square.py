#!/usr/bin/env python3

class Square:
    def __init__(self, side):
        """
        Constructor method (__init__):
        This method is called automatically when a new Square object is created.
        It initializes the attributes of the Square object.
        
        Parameters:
        - side: The side length of the square.
        """
        self.side = side  # Set the side attribute to the value passed as an argument

    def set_side(self, side):
        """
        Method to set the side length of the square.
        
        Parameters:
        - side: The new value for the side length of the square.
        """
        self.side = side  # Set the side attribute to the new value

    def get_side(self):
        """
        Method to get the side length of the square.
        
        Returns:
        - The current side length of the square.
        """
        return self.side  # Return the value of the side attribute

    def calculate_area(self):
        """
        Method to calculate the area of the square.
        
        Returns:
        - The area of the square calculated based on the side length.
        """
        return self.side * self.side  # Calculate and return the area of the square

    def display_area(self):
        """
        Method to display the area of the square.
        It prints the side length and the calculated area.
        """
        side = self.get_side()  # Get the side length of the square
        area = self.calculate_area()  # Calculate the area of the square
        print(f"Side length of the square is: {side}")  # Print the side length
        print(f"Area of the square is: {area}")  # Print the calculated area
