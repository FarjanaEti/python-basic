a = 20
b = 30
c = 23

if (a > b):
    print("a is greater")
elif (b > c):
    print("b is greater")
else:
    print("C is greater")

print("a") if (a > b) else print("b")

print("A") if (a > b) else print("C") if (c > b) else print("B")

# **** && || ******
x = 10
y = 20
z = 30

if x < y and x < z:
    print("X")

if y > x or y > z:
    print("y")
