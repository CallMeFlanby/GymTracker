import logging

from main.address.addresses import Addresses

# Load all available addresses.
addresses = Addresses.get()

#TODO Need to know how to correct log.
log = logging.getLogger(__name__)

class Search:

    # Searches a keyword and compares it with the post code, street, city and part of the city.
    @staticmethod
    def search_addresses(string):

        string = string.lower()
        address_list = set()

        if not string:
            log.error("Empty string.")
            address_list.add("No corresponding address.")
            return address_list

        log.info("Checking if " + string + " is found.")
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
            log.info("No address was found.")
            address_list.add("No corresponding address.")

        log.info("Found " + str(len(address_list)) + " possible addresses.")

        # Sorts the list and returns it.
        return sorted(address_list)
