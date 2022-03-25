from _ast import If
import json

with open('adressenliste.json') as json_file:

# returns JSON object as
# a dictionary
    data = json.load(json_file)

# Iterating through the json
# list

    index = 0
    while(True):
    
    # TODO: how can we avoid index out of range?
        for i in data[index]:
            print(i)
        index=index+1
