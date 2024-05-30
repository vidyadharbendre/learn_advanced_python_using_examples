#! usr/bin/env python3

class ElectricityBillCounter:
    def __init__(self, units, rate_per_unit):
        """
        Constructor to initilize the units consumed and rate per month

        :param units: Number of units consumed
        :param rate_per_month: Rate per unit of electricity

        """

        self.units = units
        self.rate_per_unit = rate_per_unit

    def set_units(self, units):
        self.units = units

    def get_units(self):
        return self.units
    
    def set_rate_per_unit(self, rate_per_unit):
        self.rate_per_unit = rate_per_unit

    def get_rate_per_unit(self):
        return self.rate_per_unit

    def calculate_bill(self):
        """
        Method to calculate the electricity bill.

        :return: The total electricity bill

        """
        return self.units * self.rate_per_unit

