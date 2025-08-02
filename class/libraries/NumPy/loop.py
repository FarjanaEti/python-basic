import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

for x in arr:
    print(x)

for a in arr:
    for b in a:
        print(b)

# for m in arr2:
#     for n in m:
#         for o in n:
#             print(o)
#  or nditer() funtion also do the same

for x in np.nditer(arr2):
    print(x)

for x in np.nditer(arr2[:, ::2]):
    print("skiping 2 value", x)
