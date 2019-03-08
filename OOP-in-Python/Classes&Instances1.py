# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:08:11 2019

@author: Lingesh K
"""
class Employee:
    pass

# Creating instances of the class Employee
emp1 = Employee()
emp2 = Employee()

# Giving details about the first employee
emp1.first = 'Lingesh'
emp1.last = 'K'
emp1.pay = 20000
emp1.email = 'lingeshk@some.com'

# Giving details about the second employee
emp2.first = 'New'
emp2.last = 'User'
emp2.pay = 70000
emp2.email = 'newuser@some.com'

# Printing the first and last name of the Employee
print(emp1.first+' '+emp1.last)
print(emp2.first+' '+emp2.last)