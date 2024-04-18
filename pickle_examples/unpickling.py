import pickle

# Read pickle data to file. 'rb' ---> Read Byte
with open('data.pickle', 'rb') as file:
    data_loaded = pickle.load(file)

print(data_loaded)
print(type(data_loaded))