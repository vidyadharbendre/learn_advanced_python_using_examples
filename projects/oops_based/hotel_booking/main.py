# main.py

from hotel import Hotel
from booking import Booking
from user import User

def main():
    # Create a user
    username = input("Create a username: ")
    password = input("Create a password: ")
    user = User(username, password)
    print(f"User {user} created successfully.")

    # Authenticate the user
    entered_password = input("Enter your password to authenticate: ")
    if user.authenticate(entered_password):
        print("Authentication successful!")
    else:
        print("Authentication failed.")

    # Change the user's password
    if user.authenticate(entered_password):
        new_password = input("Enter your new password: ")
        user.change_password(new_password)
        print("Password changed successfully.")
    else:
        print("Cannot change password. Authentication failed.")

    # Continue with the hotel booking system
    booking = Booking()

    hotel1 = Hotel("Grand Hotel", 20)
    hotel2 = Hotel("City Inn", 10)

    booking.add_hotel(hotel1)
    booking.add_hotel(hotel2)

    booking.list_hotels()

    hotel1.book_room()
    hotel2.book_room()

    booking.list_hotels()

if __name__ == "__main__":
    main()
