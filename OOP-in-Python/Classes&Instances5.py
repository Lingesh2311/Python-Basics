# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:55:12 2019

@author: Lingesh K
"""

class Pizza:
    '''
    This is a constructor. Takes in the default argument as the
    instance/object. Along with that it takes an argument which is
    a Python object like list/ tuple of ingredients and stores it in 
    the particular instance's variable ingredients.
    '''
    def __init__(self, ingredients):
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
    
## Consider we need different types of Pizzas
# Run the following on the console after defining and instantiating the class
        
# Margherita
Pizza(['cheese','tomatoes'])

# Mushroom Special
Pizza(['cheese','tomatoes','mushrooms'])

# Chicken
Pizza(['cheese','tomatoes','chicken'])

## What does each line do?
## ANSWER:
# They run the corresponding __repr__ built-in function here a method to 
# the class Pizza. Although each are by itself an independant variety.