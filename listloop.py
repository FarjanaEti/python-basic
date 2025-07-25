fruits = ["apple", "Banana", "cherry", "kiwi", "mango"]
# newFruits = []
# for x in fruits:
#     if 'a' in x:
#         newFruits.append(x) or,
newFruits = [x for x in fruits if "a" in x]
newFruits = [x for x in fruits if x != "banana"]
newFruits = [x for x in range(10) if x < 6]
newFruits = [x.upper() for x in fruits]
newFruits = [x if x != 'banana' else 'orange' for x in fruits]
print(newFruits)

fruits.sort()
fruits.sort(reverse=True)
print(fruits)


def myfunc(n):
    return abs(n-50)


number = [95, 85, 50, 65, 70]


number.sort(key=myfunc)
print(number)

# *****sort*******
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

copylist = thislist.copy()
copylist = list(thislist)
copylist = thislist[:]

# ****join two list****
for x in thislist:
    fruits.append(x)
    print(fruits)

    fruits.extend(thislist)
