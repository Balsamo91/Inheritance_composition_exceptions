import pickle

data = [
    ['door', 3, 7, 0],
    ['sand', 12, 5, 1],
    ['brush', 22, 34, 5],
    ['poster', 'red', 8, 'stick']
]

# Writing pickle data to file. 'wb' ---> write byte
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)