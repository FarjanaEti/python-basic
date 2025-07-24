def myfunc():
    return 0
# myfunc put 0 in obj and bool(0)=false


obj = myfunc()
print(bool(obj))


def func2():
    return False


if func2():
    print("yes")

else:
    print("no")


x = 10.0
print(isinstance(x, int))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
