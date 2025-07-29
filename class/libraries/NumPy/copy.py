import numpy as np

arr = np.array([1, 2, 4, 6])
x = arr.copy()
y = arr.view()
y[1] = 20
arr[0] = 10

print(arr)
print(x)
print(y)
