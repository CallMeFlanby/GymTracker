import unittest

from main.address.address import Address


class Test(unittest.TestCase):

    def test_create(self):
        # Prepare
        street = "Teststraße"
        house_number = 22
        extra = "Wohnung 42"
        post_code = 12345
        city = "Teststadt"
        town_part = "Teststadtteil"

        # Run
        address = Address(street, house_number, extra, post_code, city, town_part)

        # Check
        self.assertIs(street, address.street)
        self.assertIs(house_number, address.number)
        self.assertIs(extra, address.extra)
        self.assertIs(post_code, address.post_code)
        self.assertIs(city, address.city)
        self.assertIs(town_part, address.town_part)

        self.assertIsNot("street", address.street)
        self.assertIsNot("house_number", address.number)
        self.assertIsNot("extra", address.extra)
        self.assertIsNot("post_code", address.post_code)
        self.assertIsNot("city", address.city)
        self.assertIsNot("town_part", address.town_part)

    def test_get_address(self):
        # Prepare
        street = "Teststraße"
        house_number = 22
        extra = "Wohnung 42"
        post_code = 12345
        city = "Teststadt"
        town_part = "Teststadtteil"

        # Run
        address_with_extra = Address(street, house_number, extra, post_code, city, town_part)
        address_without_extra = Address(street, house_number, "", post_code, city, town_part)

        address_with_extra_string = street + " " + str(house_number) +  " \n " \
                         + extra + " \n " + str(post_code) + " " \
                         + city + " \n " + \
                         "OT " + town_part

        address_without_extra_string = street + " " + str(house_number) + " \n " \
                                    + str(post_code) + " " \
                                    + city + " \n " + \
                                    "OT " + town_part

        # Check
        self.assertEqual(address_with_extra.get_address(), address_with_extra_string)
        self.assertEqual(address_without_extra.get_address(), address_without_extra_string)
        self.assertNotEqual(address_with_extra.get_address(), address_without_extra_string)
        self.assertNotEqual(address_without_extra.get_address(), address_with_extra_string)

    def test_get_searched_address(self):
        # Prepare
        street = "Teststraße"
        house_number = 22
        extra = "Wohnung 42"
        post_code = 12345
        city = "Teststadt"
        city_complete = "Teststadt, Hanse- und Universitätsstadt"
        town_part = "Teststadtteil"

        # Run
        address = Address(street, house_number, extra, post_code, city, town_part)
        address_complete = Address(street, house_number, extra, post_code, city_complete, town_part)
        address_string = street + ", " + city

        # Check
        self.assertEqual(address.get_searched_address(), address_string)
        self.assertEqual(address_complete.get_searched_address(), address_string)
