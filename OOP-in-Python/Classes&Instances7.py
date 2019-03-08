# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:20:10 2019

@author: Lingesh K
"""
import math

class Pizza:
    '''
    This is a constructor. Takes in the default argument as the
    instance/object. Along with that it takes an argument which is
    a Python object like list/ tuple of ingredients and stores it in 
    the particular instance's variable ingredients.
    '''
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients
    
    '''
    This is a built-in function to compute the "official" string 
    representation of the object. If at all possible, this should look
    like a valid Python Expression that could be used to recreate an object
    with the same value. 
    RETURN VALUE: Must be a String object
    Also, used when an 'Informal' representation of the instance is reqd.
    '''
    def __repr__(self):
        return f'It\'s Pizza({self.ingredients})'
    
    def area(self):
        return self._circle_area(self.radius)
    
    '''
    This is a Static Method. It has no access to the Class object or the class/
    All it does is evaluvate and returns some value. It does not modify the class
    instance or the class variable directly which can happen in a class method and 
    which always happens in an Instance method.
    '''
# =============================================================================
#     The single underscore is to mark that it's not part of the public API of the 
#     class and it's an implementation level detail. This stands as an helper method
#     which can be used for testing.   
# =============================================================================
    @staticmethod
    def _circle_area(r): # Returns the area of a circle whose radius is r.
        return r ** 2 * math.pi
    # Here the radius can be the Instance's radius/ any general radius,
    
pizza1 = Pizza(12,['cheese','mushroom']) # Creating a 12" pizza

print(pizza1.area()) # This will print the area of Pizza 1

print(Pizza._circle_area(12)) # This will print the area of a circle of radius 2

#In general, Static methods can be used independently    