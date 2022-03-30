# Contact class. Handles following properties from the json file:
# telephone = props['telefon_festnetz']
# mobile = props['telefon_mobil']
# mail = props['email']
# website = props['website']

class Contact:
    def __init__(self, telephone, mobile, mail, website):
        self.telephone = telephone
        self.mobile = mobile
        self.mail = mail
        self.website = website
