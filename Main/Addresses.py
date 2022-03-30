import json

with open('adressenliste.json') as json_file:
    # returns JSON object as
    # a dictionary
    data = json.load(json_file)

    # Iterating through the json
    # list
    for currentData in data:
        print(currentData['uuid'])
