class Employee:
    'Common class for the employee'
    empCount = 0

    def __init__(self, name, age, basic):
        self.name = name
        self.age = age
        self.basic = basic
        Employee.empCount += 1
    
    def displayCount(self):
        print(f"The total employee now: {Employee.empCount}")
    
    def displayEmloyee(self):
        print(f"Name: {self.name} Salary: {self.basic} Age: {self.age}")
    
print(f"Employee.__doc__ : {Employee.__doc__}")
print(f"Employee.__name__ : {Employee.__name__}")
print(f"Employee.__module__ : {Employee.__module__}")
print(f"Employee.__bases__ : {Employee.__bases__}")
print(f"Employee.__dict__ : {Employee.__dict__}")