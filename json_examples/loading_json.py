import json

with open('data.json', 'r') as file:
    data_loaded = json.load(file)

print(data_loaded)
print(type(data_loaded))