class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling parent now!")
    
    def parentMethod(self):
        print("Calling parent method")
    
    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print(f"Parent Attribute: {Parent.parentAttr}")


class Child(Parent):
    def __init__(self):
        print("Calling child!")
    
    def childMethod(self):
        print("Calling child method!")


c = Child() # instance of Child
c.childMethod()
# Calling parent method
c.parentMethod()
# Setting parent attribute
c.setAttr(20)
# Getting parent attribute
c.getAttr()