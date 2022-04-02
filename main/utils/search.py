from main.address.addresses import Addresses

# Load all available addresses.
addresses = Addresses.get()


class Search:

    # Searches a keyword and compares it with the post code, street, city and part of the city.
    @staticmethod
    def search_addresses(string):
        string = string.lower()

        address_list = set()
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

        if address_list.__sizeof__() != 0:
            return address_list
        else:
            return "No corresponding address."
