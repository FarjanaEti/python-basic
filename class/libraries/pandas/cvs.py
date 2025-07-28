#  Comma-Separated Values.
# It's a text file that stores tabular data — like rows and columns


# name,age,city   --> this line is the heading
# John,25,New York   --> row of data
# Emma,30,London
# Ali,22,Dhaka


# data's are separated by coma

# how to read
# pandas.read_csv("file.csv")

# how to write
# df = pd.DataFrame(info)
# df.to_csv("file.csv")


import pandas as pd

# Create a dictionary of data
info = {
    "name": ["Sarah", "Tom"],
    "age": [28, 35],
    "city": ["Berlin", "Tokyo"]
}

# Convert to DataFrame
df = pd.DataFrame(info)

# Save to CSV
df.to_csv("people.csv", index=False)

data = pd.read_csv("people.csv")

print(data.head())
