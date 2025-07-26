myset = {"apple", "orange", "banana"}
x = myset.pop()
y = myset.pop()
print(x)
print(y)
print(myset)
myset.clear()
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

allset = set1.union(set2, set3, set4)
allset = set1 | set2 | set3 | set4
print(allset)
