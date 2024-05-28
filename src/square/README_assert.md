# Testing the Square Class with Assert Statements

## Overview

This document explains how to test the `Square` class using `assert` statements in Python. The `assert` statement is used to verify that a given condition is `True`. If the condition is `False`, an `AssertionError` is raised with an optional message.

## Square Class Implementation

Here is the implementation of the `Square` class:

```python
# square/square.py
import math

class Square:
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def get_side(self):
        return self.side

    def calculate_area(self):
        return self.side ** 2

    def display_area(self):
        print(f"Side of the square is: {self.get_side()}")
        print(f"Area of the square is: {self.calculate_area()}")

```