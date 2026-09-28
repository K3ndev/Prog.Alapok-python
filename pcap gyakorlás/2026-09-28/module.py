from datetime import datetime
class Room:
    def __init__(self, number, room_type, price_over_night):
        self.number = number
        self.room_type = room_type
        self.price_over_night = price_over_night
        self.available = True
        self.bookings = [] #tuple datetime
    def addSzoba(self, adat):  #adat tuple
        self.bookings.add(adat)

    def is_available(self):
        return self.available

    def __str__(self):
        return f"Room {self.number} - {self.room_type} - {self.price_over_night} Ft/night"

    def check_spare_time(self, start, end):
        

class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        

class Booking:
    def __init__(self, guest: Guest, room: Room, check_in: datetime, check_out: datetime):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.room.available = False
        if self.check_in > self.check_out:
            ValueError("Invalid booking dates")
        if not self.room.is_available:
            ValueError("Room is not available")
        if self.get_nights() < 1:
            ValueError("Invalid booking dates")
        #!! átformálni    
        for item in self.room.bookings:
            if item[0] < check_in and item[0] > check_out:
                ValueError("The room is reserved at that time")
            if item[1] < check_in and item[1] > check_out:
                ValueError("The room is reserved at that time")
        self.room.bookings.append((check_in, check_out))
    def szabeE (self, datum):
        pass
        
    def get_nights(self):
        return self-self.check_out - self.check_in
    
    def get_price(self):
        return self.get_nights() * self.room.price_over_night

    #def rm(self):
    #    del(self)

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []
        self.guests = []
        #self.bookings[5] = None
        #self.bookings.remove()
    def add_room(self, room):
        self.rooms.append(room)

    def register_guest(self, guest):
        self.guests.append(guest)

    def make_booking(self, guest: Guest, room: Room, check_in: datetime, check_out: datetime):
        if guest not in self.guests:
            self.register_guest(guest)
        if room not in self.guests:
            self.register_room(room)             
        self.bookings.append(Booking(guest, room, check_in, check_out))

    def cancel_booking(self, id=None, booking=None):
        if id == None:
            self.bookings[self.bookings.index(booking)].rm()
        if booking == None:
            self.bookings[self.bookings.index(id)].rm()

    def find_spare_room(self, room_type, check_in, check_out):
        temp = list()
        for room in self.rooms:
            good = True
            if room.room_type == room_type:
                if room.is_available():
                   for booking in room.bookings:
                       if check_in < booking[0] > check_out or check_in < booking[1] > check_out:
                           good = False
            if good:
                temp.append(room)
        return temp