# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:13:53 2019

@author: Lingesh K
"""

class Employee:
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
        
# Creating an Instance/Object of the class Employee
emp1 = Employee('Lingesh','K',20000)

## Explanation 
# emp1 is passed as self, so 
# emp1.first = 'Lingesh'; emp1.last = 'K'; emp1.pay = 20000

print(emp1.email) # Accessing the email of the first employee      

## OUTPUT:
# This prints LingeshK@super.com