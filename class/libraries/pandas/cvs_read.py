import pandas as pd

info = pd.read_csv("student.csv")

# print(info.to_string())
# print(info)

print(pd.options.display.max_rows)

# print(info.head())
# print(info.head(10))
print(info.tail())
print(info.info())
