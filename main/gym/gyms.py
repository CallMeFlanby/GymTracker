import json
import logging
import os
from pathlib import Path

from main.address.address import Address
from main.gym.gym import Gym
from main.utils.contact import Contact

#TODO Need to know how to correct log.
log = logging.getLogger(__name__)
class Gyms:

    @staticmethod
    def get():
        gyms = list()

        # Gets the file from the right directory, in this case var.
        path = Path(os.getcwd())
        file = os.path.join(path.parent.absolute().parent.absolute(), 'var', 'fitnessstudios.json')

        # Opening JSON file
        with open(file, mode="r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            log.info("Reading json file.")

            # Iterating through the json list
            for currentData in data['features']:
                # Gets the properties.
                props = currentData['properties']

                # Street name, house number, postcode, part of the city, city
                street = props['strasse_name']
                house_no = props['hausnummer']
                house_no_extra = props['hausnummer_zusatz']
                post_code = props['postleitzahl']
                city = props['gemeinde_name']
                town = props['gemeindeteil_name']

                gym_address = Address(street, house_no, house_no_extra, post_code, city, town)

                # Contact possibilities
                telephone = props['telefon_festnetz']
                mobile = props['telefon_mobil']
                mail = props['email']
                website = props['website']

                gym_contact = Contact(telephone, mobile, mail, website)

                # Gets the gyms name.
                name = props['bezeichnung']

                # Returns the opening hours.
                opening_hours = props['oeffnungszeiten']

                # Gets the coordinates.
                coordinates = currentData['geometry']['coordinates']

                gyms.append(Gym(name, gym_address, gym_contact, opening_hours, coordinates))

        log.info("Returning list with collected gyms. Total: " + str(len(gyms)) + ".")
        return gyms
