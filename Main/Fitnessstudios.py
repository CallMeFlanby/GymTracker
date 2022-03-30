from _ast import If
import json

# Opening JSON file
with open('fitnessstudios.json') as json_file:
    data = json.load(json_file)

# Iterating through the json
# list
# TODO: UTF-8?
for currentData in data['features']:

    # Gets the properties.
    props = currentData['properties']

    # Gets the gyms name.
    gymsName = props['bezeichnung']

    # Street name, house number, postcode, part of the city, city
    streets = props['strasse_name']
    houseNo = props['hausnummer']
    houseNoExtra = props['hausnummer_zusatz']
    postCode = props['postleitzahl']
    town = props['gemeindeteil_name']
    city = props['gemeinde_name']

    print(postCode)

    # Returns the opening hours.
    openingHours = props['oeffnungszeiten']

    # Contact possibilities
    telephone = props['telefon_festnetz']
    mobile = props['telefon_mobil']
    mail = props['email']
    website = props['website']

    coordinates = currentData['geometry']['coordinates']

