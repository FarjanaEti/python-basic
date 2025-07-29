import numpy as np

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# first part means  which row
# second part means column to column
# 2 value means exatly one row or column
print(array[0:3, 2])
print(array.dtype)
print(array.shape)
