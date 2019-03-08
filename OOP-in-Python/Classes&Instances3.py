# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:23:15 2019

@author: Lingesh K
"""

class Employee:
    emp_count = 0 # Global value to keep count of the number of employees
    # This function is a special method of a class and can be considered to be 
    # equal to the constructor or the initialization function    
    def __init__(self, first, last, pay):
        # Self can be considered as the special name given to the instance that 
        # is created for the class Employee. Whenever an instance is created for
        # the class say emp = Employee('first','last',pay_here). 
        # It automatically calls the __init__() method with itself in the place 
        # of self. Also the parameters should be passed when creating each instance
        self.first = first # First name
        self.last = last # Last name
        self.pay = pay # Pay 
        self.email = first+last+'@super.com'
        Employee.emp_count += 1
        self.id = Employee.emp_count
        
    def fullname(self):
        # This method inside the class is used to print the full name of an 
        # employee. Within this method, the only parameter that is ever needed
        # are the instance variables first and last. So, self is passed as an 
        # argument. Using that the values self.first and self.last can be 
        # accessed. Here self refers to a particular employee
        print("The full name of Employee {} is {} {}".format(self.id,self.first,self.last))
        
# Creating an Instance/Object of the class Employee - Employee 1
emp1 = Employee('Lingesh','K',20000)

# Creating an Instance/Object of the class Employee - Employee 2
emp2 = Employee('New','user',30000)

## Explanation 
# emp1 is passed as self, so 
# emp1.first = 'Lingesh'; emp1.last = 'K'; emp1.pay = 20000

emp1.fullname() # Accessing the full name of the first employee      
emp2.fullname() # Accessing the full name of the second employee
## OUTPUT:
# This prints 
# The full name of Employee 1 is Lingesh K
# The full name of Employee 2 is New user