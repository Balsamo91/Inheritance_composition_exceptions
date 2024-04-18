# import json

# data = {
#     "name" : "John",
#     "age" : 30,
#     "city" : "New York"
# }

# # Writing JSON date to file

# with open('data.json', 'w') as file:
#     json.dump(data, file)

####################################################################################

import json

data = [
    ['door', 3, 7, 0],
    ['sand', 12, 5, 1],
    ['brush', 22, 34, 5],
    ['poster', 'red', 8, 'stick']
]

# Writing JSON date to file
with open('data.json', 'w') as file:
    json.dump(data, file)