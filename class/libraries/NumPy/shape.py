import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(3, 4)
newarr = arr.reshape(3, 4).base
threeD = arr.reshape(3, 2, 2)
print(newarr)
print(threeD)


multArray = np.array([[1, 2, 3], [4, 5, 6]])

oneD = multArray.reshape(-1)
print(oneD)
