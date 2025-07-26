fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "apple":
        continue
print(x)


# for x in range( 5):
# for x in range(2, 5):
# for x in range(2, 15, 2):
#     print(x)


for x in range(10):
    if x == 3:
        break
    print(x)
else:
    print("finish")
