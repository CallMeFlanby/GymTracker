import logging
from collections import OrderedDict

from main.address.address import Address
from main.address.addresses import Addresses

# Load all available addresses.
from main.gym.gym import Gym
from main.gym.gyms import Gyms

addresses = Addresses.get()

#TODO Need to know how to correct log.
log = logging.getLogger(__name__)

class Search:

    # Searches a keyword and compares it with the post code, street, city and part of the city.
    @staticmethod
    def search_addresses(string):

        string = string.lower()
        address_list = dict()

        if not string:
            log.error("Empty string.")
            s = "No corresponding address."
            address_list[s] = Address.empty_address()
            return address_list

        log.info("Checking if " + string + " is found.")
        for x in addresses:
            if string.isdigit:
                if string in x.post_code:
                    address_list[x.get_searched_address()] = x
                    continue

            if string in x.street.lower()\
                    or string in x.city.lower()\
                    or string in x.town_part.lower():
                address_list[x.get_searched_address()] = x
                continue

        if not address_list:
            log.info("No address was found.")
            s = "No corresponding address."
            address_list[s] = Address.empty_address()

        log.info("Found " + str(len(address_list)) + " possible addresses.")

        # Sorts the list and returns it.
        return OrderedDict(sorted(address_list.items(), key=lambda t: t[0]))

    @staticmethod
    def get_near_gyms(address):
        gyms = Gyms.get()

        nearby_gyms = list()

        if address.street == Address.empty_address().street:
            return nearby_gyms

        for x in gyms:
            if x.address.post_code == address.post_code:
                nearby_gyms.append(x)
            if x.address.street in address.street:
                nearby_gyms.append(x)

        if len(nearby_gyms) == 0:
            return Gym.no_gym_found()

        return nearby_gyms
