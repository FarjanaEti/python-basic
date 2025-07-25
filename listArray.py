# ******list/array************

list1 = ["apple", "banana", "berry", "cherry", "mango"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
list4 = [True, 1, 2, "apple", "mango", "watermelon"]

tolist = list(("apple", "banana", "berry"))
print(type(tolist))
print(len(list2))
print(list1[1:4])

list1[4] = "watermelon"
# thislist[1:3] = ["blackcurrant", "watermelon"]
print(list1)

list4[3:5] = ["banana"]
print(list4)
# single change "" multiple change []
list4.append("5")
print(list4)

list1.insert(3, "jakefrute")
print(list1)

list2.extend(list1)
print(list2)

list2.remove(5)
print(list2)

list1.pop(1)
# list1.pop() it remove last item

del list1[3]
list3.clear()
del list3
# clear() delete all item return [] del delete all
print(list1)

# *******loop list******
for frutes in list1:
    print(frutes)

    for i in range(len(list1)):
        print(list1[i], i)
