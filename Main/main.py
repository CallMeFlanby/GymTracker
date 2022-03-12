import json

f = open('fitnessstudios.json')
f2 = open('adressenliste.json')

# returns JSON object as
# a dictionary
data = json.load(f2)

# Iterating through the json
# list
print(data)

# Closing file
f.close()
