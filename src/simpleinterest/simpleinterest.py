#!/usr/bin/env python3

class SimpleInterest:
    def __init__(self, principle, time, rate):
        """
        Constructor method (__init__):
        This method is called automatically when a new SimpleInterest object is created.
        It initializes the attributes of the SimpleInterest object.
        
        Parameters:
        - principle: The principle amount.
        - time: The time period.
        - rate: The interest rate.
        """
        self.principle = principle
        self.time = time
        self.rate = rate

    def set_principle(self, principle):
        """
        Method to set the principle.
        
        Parameters:
        - principle: The new value for the principle amount.
        """
        self.principle = principle

    def get_principle(self):
        """
        Method to get the principle amount.
        
        Returns:
        - The current principle amount.
        """
        return self.principle

    def set_time(self, time):
        """
        Method to set the time period.
        
        Parameters:
        - time: The new value for the time period.
        """
        self.time = time

    def get_time(self):
        """
        Method to get the time period.
        
        Returns:
        - The current time period.
        """
        return self.time

    def set_rate(self, rate):
        """
        Method to set the interest rate.
        
        Parameters:
        - rate: The new value for the interest rate.
        """
        self.rate = rate

    def get_rate(self):
        """
        Method to get the interest rate.
        
        Returns:
        - The current interest rate.
        """
        return self.rate

    def calculate_simple_interest(self):
        """
        Method to calculate the simple interest.
        
        Returns:
        - The calculated simple interest based on the principle, time, and rate.
        """
        return (self.principle * self.rate * self.time) / 100

    def display_simple_interest(self):
        """
        Method to display the simple interest.
        It prints the principle, time, rate, and calculated simple interest.
        """
        principle = self.get_principle()
        time = self.get_time()
        rate = self.get_rate()
        interest = self.calculate_simple_interest()
        
        print(f"The given principle: {principle}")
        print(f"The given time: {time} years")
        print(f"The given rate: {rate}%")
        print(f"The simple interest is: {interest}")