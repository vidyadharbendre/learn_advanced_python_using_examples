from hotel import Hotel

class Booking:
    def __init__(self):
        self.hotels = []

    def add_hotel(self, hotel):
        self.hotels.append(hotel)
        print(f"Added hotel: {hotel.name}")

    def list_hotels(self):
        for hotel in self.hotels:
            print(f"Hotel: {hotel.name}, Available Rooms: {hotel.available_rooms}")
