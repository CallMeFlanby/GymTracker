# gym class.
# Wraps name, address, contact, opening hours and coordinates from a gym.

class Gym:
    def __init__(self, name, address, contact, opening_hours, coordinates):
        self.name = name
        self.address = address
        self.contact = contact
        self.opening_hours = opening_hours
        self.coordinates = coordinates
