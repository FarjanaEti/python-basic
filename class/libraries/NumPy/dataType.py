import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])
arr2 = np.array([1, 2, 3], dtype="S")
# byte string 'b'
print(arr2)
print(arr2.dtype)
# U6 unicode string max length 6

# *******copy******astype() do copy
arrayy = np.array([1.2, 2.2, 3.3])

newArr = arrayy.astype('i')
print(newArr, newArr.dtype)
