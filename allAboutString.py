a = "Hello"
print(a[1])

for x in a:
    #     print(x)
    print(len(a))
    print("ll" in a)
    print("ll" not in a)

    if "el" in a:
        print("found")

b = "farjana ahan eti"
# last theke 5 number and last theke 3 ta baad
print(b[-5:-3])

# *****Modify****
# .upper(), .lower() .strip()
print(b.replace("e", "a"))
print(b.split("a"))
c = 22

print(f"My age is {c}")
print(f"My dress price is {c:.2f}")
print(f"My dress price is {c * 10}")
