from main.address.addresses import Addresses

# Load all available addresses.
addresses = Addresses.get()

class Search:

    # Searches a keyword and compares it with the post code, street, city and part of the city.
    def search_address(self, string):

        for x in addresses:
            if string.isdigit:
                if string in x.post_code:
                    return x.post_code

            if string in x.street.lower():
                return x.street

            if string in x.city.lower():
                return x.city

            if string in x.town_part.lower():
                return x.town_part

        return "No corresponding address."
