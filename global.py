import random
x = "awesome"
# x = 'nice' latest value will consider


def myFunc():
    #     global x
    x = "fantastic"
    print("Python is ", x)


myFunc()
print("Python is " + x)


print(random.randrange(10, 20))

# casting
print(int(4.5))
print(float(4))
print(str(3.0))
