import pandas as pd

data = pd.read_csv("employee.csv")
minvalue = data["salary"].mean()
middlevalue = data["age"].median()

data.fillna({"age": middlevalue}, inplace=True)
# wrong to right
data.loc[1, "experience_years"] = 15

for i in data.index:
    if data.loc[i, 'age'] > 40:
        data.loc[i, 'age'] = 40

# delete the coloumn data only
for x in data.index:
    if data.loc[x, 'age'] == 45:
        data.drop(x, inplace=True)

print(minvalue)
print(middlevalue)
print(data.to_string)
