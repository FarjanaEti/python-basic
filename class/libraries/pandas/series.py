import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

a = [2, 4, 6]


#  myseries = pd.Series(a)
myseries = pd.Series(a, index=['a', 'b', 'c'])
print(myseries)
# print("series value=", myseries[2])

mark = {"bangla": 88, "english": 85, "math": 90}
mymark = pd.Series(mark)

print(mymark)
