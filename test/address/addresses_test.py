import unittest

from main.address.addresses import Addresses


class Test(unittest.TestCase):

    def test_get(self):
        # Prepare
        addresses = Addresses.get()

        # Check
        self.assertIsNot(addresses.__sizeof__(), 0)
