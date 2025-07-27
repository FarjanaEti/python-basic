
# class myClass:
#     x = 5
#     print("this my class")


# p1 = myClass()
# print(p1.x)
# _init_ initialize object property and called automatically
# _str_  when you print a object and return a string


class myself():
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def __str__(self):
        return f"{self.name} {self.age} \n roll:-{self.roll}"

    def mymethod(self):
        print("My name is", self.name)


p1 = myself("eti", 23, 21024)
p1.age = 24
# del p1.roll


print(p1.name)
print(p1)
p1.mymethod()
