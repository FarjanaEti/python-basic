def myfunc():
    print("Hello from my function")


myfunc()

# argument


def argfunc(arg1, arg2):
    print("My " + arg1)
    print("My " + arg1 + " " + "my" + arg2)


argfunc("life", "rules")
# argfunc("rules")

# keyword argument


def childfunc(child1, child2, child3):
    print("this is my child " + child1)


childfunc(child1="A", child2="B", child3="C")


def loopfunc(fruits):
    for x in fruits:
        print(x)


fol = ['apple', 'comla', 'kola', 'jam']
loopfunc(fol)

# return


def mathfunc(x):
    return (5*x)


print(mathfunc(3))
print(mathfunc(5))


def recursion(r):
    if r > 0:
        result = r + recursion(r - 1)
        print(result)
        return result
    else:
        result = 0
        return result


recursion(5)
