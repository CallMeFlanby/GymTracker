import unittest

from main.address.address import Address
from main.gym.gym import Gym
from main.utils.contact import Contact


class Test(unittest.TestCase):

    def test_create(self):
        # Prepare
        street = "Teststraße"
        house_number = 22
        extra = "Wohnung 42"
        post_code = 12345
        city = "Teststadt"
        town_part = "Teststadtteil"
        address = Address(street, house_number, extra, post_code, city, town_part)
        contact = Contact("0381 123456789", "0123456789", "test@testmail.test", "test-gym.test")

        # Run
        gym = Gym("Test gym", address, contact, "08:00 - 19:00", "1111111,2222222")

        # Check
        self.assertIs("Test gym", gym.name)
        self.assertIs(address, gym.address)
        self.assertIs(contact, gym.contact)
        self.assertIs("08:00 - 19:00", gym.opening_hours)
        self.assertIs("1111111,2222222", gym.coordinates)

        self.assertIsNot("Test gym wrong", gym.name)
        self.assertIsNot("address", gym.address)
        self.assertIsNot("contact", gym.contact)
        self.assertIsNot("08:15 - 19:00", gym.opening_hours)
        self.assertIsNot("333333,2222222", gym.coordinates)
