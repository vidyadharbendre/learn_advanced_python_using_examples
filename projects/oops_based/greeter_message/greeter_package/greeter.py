# Object-Oriented Programming (OOP) approach
#!/usr/bin/env python3


class Greeter:
    """
    A simple Greeter class that takes a name and prints a greeting.
    """

    def __init__(self, name):
        """
        Initializes the Greeter with a name.
        :param name: The name of the person to greet.
        """
        self.name = name

    def print_hi(self):
        """
        Prints a greeting message.
        """
        print(f'Hi {self.name}')

# Create an object of Greeter class
# Ensure the script runs only when executed directly
if __name__ == "__main__":
    # Create an object of Greeter class
    greeter = Greeter("Vidyadhar")
    greeter.print_hi()  # Output: Hi Vidyadhar
