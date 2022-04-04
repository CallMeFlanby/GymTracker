import unittest

from main.gym.gyms import Gyms


class Test(unittest.TestCase):

    def test_get(self):
        # Prepare
        gyms = Gyms.get()

        # Check
        self.assertIsNot(gyms.__sizeof__(), 0)
