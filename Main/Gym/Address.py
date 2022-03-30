# Address class. Handles the following properties from the json file:
# street = props['strasse_name']
# number = props['hausnummer']
# extra = props['hausnummer_zusatz']
# zip = props['postleitzahl']
# townPart = props['gemeindeteil_name']
# city = props['gemeinde_name']

class Address:
    def __init__(self, street, number, extra, post_code, city, town_part):
        self.street = street
        self.number = number
        self.extra = extra
        self.post_code = post_code
        self.city = city
        self.town_part = town_part

    def get_address(self):
        address = self.street + " " + self.number + "\n"
        if self.extra:
            address = address + self.extra + "\n"
        address = address + self.post_code + " " + self.city + "\n"
        return address + "OT " + self.town_part
