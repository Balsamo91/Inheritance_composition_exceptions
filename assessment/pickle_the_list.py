import pickle

data = [
    ["door", 3, 7, 0],
    ["sand", 12, 5, 1],
    ["brush", 22, 34, 5],
    ["poster", "red", 8, "stick"]
]

# Serialize the data
with open("in.pickle", "wb") as picklefile:
    pickle.dump(data, picklefile)


# j = [1,2,[3,4,5],6,7,[8,9,10]]
# x = len(set([2,3,4,5,7,8,2,3,2,3]))
# f = j[5][2] + j[4]


# print(f + x)