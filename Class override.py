class Parent:
    def myMethod(self):
        print("Parent method!")

class Child(Parent):
    def myMethod(self):
        print("Child method!")

c = Child()
c.myMethod()