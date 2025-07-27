class parentClass:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)


class childClass(parentClass):
    #     pass
    def __init__(self, fname, lname, year):
        # parentClass.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.birthYear = year
#  using super() we don't need to use the parent class name

    def childFunc(self):
        print("welcome", self.firstname, self.lastname,
              "to the class of ", self.birthYear)


y = parentClass("konika", "eti")
x = childClass("farjana", "eti", 2002)

y.printName()
print(x.birthYear)
x.printName()
x.childFunc()
