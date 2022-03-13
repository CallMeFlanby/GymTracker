from _ast import If
import json

f = open('adressenliste.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

index = 0
while(True):
    
    # TODO: how can we avoid index out of range?
    for i in data[index]:
        print(i)
    index=index+1

# Closing file
f.close()
