class Hotel:
    def __init__(self, name, available_rooms):
        self.name = name
        self.available_rooms = available_rooms

    def book_room(self):
        if self.available_rooms > 0:
            self.available_rooms -= 1
            print(f"Room booked at {self.name}. Rooms left: {self.available_rooms}")
        else:
            print(f"No rooms available at {self.name}")
