import pandas as pd

info = pd.read_csv("employee.csv")

# withoutNaN = info.dropna()
# info.dropna(inplace=True)

# info.fillna(130, inplace=True)
info.fillna({"salary": 130}, inplace=True)

# print(withoutNaN)//it create new data form and inplace modify the original one
print(info)
