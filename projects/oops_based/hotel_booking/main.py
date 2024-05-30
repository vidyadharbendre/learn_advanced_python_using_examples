from hotel import Hotel
from booking import Booking

def main():
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
