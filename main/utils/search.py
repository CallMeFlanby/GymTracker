import logging

from main.address.addresses import Addresses

# Load all available addresses.
addresses = Addresses.get()

# TODO Logging file needs to be added.
class Search:

    # Searches a keyword and compares it with the post code, street, city and part of the city.
    @staticmethod
    def search_addresses(string):

        string = string.lower()
        address_list = set()

        if not string:
            logging.info("Empty string.")
            address_list.add("No corresponding address.")
            return address_list

        logging.info("Checking if " + string + " is found.")
        for x in addresses:
            if string.isdigit:
                if string in x.post_code:
                    address_list.add(x.get_searched_address())
                    continue

            if string in x.street.lower()\
                    or string in x.city.lower()\
                    or string in x.town_part.lower():
                address_list.add(x.get_searched_address())
                continue

        if not address_list:
            logging.info("No address was found.")
            address_list.add("No corresponding address.")

        logging.info("Found " + str(len(address_list)) + " possible addresses.")

        # Sorts the list and returns it.
        return sorted(address_list)
