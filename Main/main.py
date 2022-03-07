import json

f = open('fitnessstudios.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['features']:
    print(i)

# Closing file
f.close()
