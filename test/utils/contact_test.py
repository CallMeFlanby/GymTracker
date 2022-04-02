import unittest

from main.address.address import Address
from main.utils.contact import Contact


class Test(unittest.TestCase):

    def test_create(self):
        # Prepare
        telephone = "0381 123456789"
        mobile = "0123456789"
        e_mail = "test@testmail.test"
        website = "test-gym.test"

        # Run
        contact = Contact(telephone, mobile, e_mail, website)

        # Check
        self.assertIs(telephone, contact.telephone)
        self.assertIs(mobile, contact.mobile)
        self.assertIs(e_mail, contact.mail)
        self.assertIs(website, contact.website)

        self.assertIsNot("telephone", contact.telephone)
        self.assertIsNot("mobile", contact.mobile)
        self.assertIsNot("e_mail", contact.mail)
        self.assertIsNot("website", contact.website)
        