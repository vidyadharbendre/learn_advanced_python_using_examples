# user.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, entered_password):
        """
        Authenticate the user with the entered password.

        Args:
            entered_password (str): The password entered by the user.

        Returns:
            bool: True if the entered password matches the user's password, False otherwise.
        """
        return self.password == entered_password

    def change_password(self, new_password):
        """
        Change the user's password.

        Args:
            new_password (str): The new password to set.
        """
        self.password = new_password

    def __str__(self):
        """
        Return a string representation of the user.

        Returns:
            str: The username of the user.
        """
        return self.username
