import unittest

from main.utils.search import Search


class Test(unittest.TestCase):

    def test_search(self):

        # Prepare
        searched_addresses = Search.search_addresses("Test")
        harte_street = next(iter(searched_addresses))

        # Check
        self.assertIsNot(searched_addresses.__sizeof__(), 0)
        self.assertEqual(harte_street, "Hartestr., Rostock")
