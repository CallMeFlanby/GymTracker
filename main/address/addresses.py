import json
import logging
import os
from pathlib import Path

from main.address.address import Address

#TODO Need to know how to correct log.
log = logging.getLogger(__name__)

# Responsible for the handling with the json file.
# Fetches all the available addresses within it.
class Addresses:

    @staticmethod
    def get():

        addresses = list()

        # Gets the file from the right directory, in this case var.
        path = Path(os.getcwd())
        file = os.path.join(path.parent.absolute(), 'var', 'adressenliste.json')

        with open(file, mode="r", encoding="utf-8") as json_file:
            # returns JSON object as
            # a dictionary
            log.info("Opening json address file.")
            data = json.load(json_file)

            # Iterating through the json list
            for currentData in data:
                street = currentData['strasse_name']
                house_no = currentData['hausnummer']
                house_no_extra = currentData['hausnummer_zusatz']
                post_code = currentData['postleitzahl']
                city = currentData['gemeinde_name']
                town = currentData['gemeindeteil_name']
                addresses.append(Address(street, house_no, house_no_extra, post_code, city, town))

        log.info("Returning list with collected addresses. Total: " + str(len(addresses)) + ".")
        return addresses
