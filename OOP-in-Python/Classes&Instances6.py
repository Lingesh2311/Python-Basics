# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:09:12 2019

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
    
    '''
    We are creating different factory functions for the different types 
    of pizzas that we create. Each class method returns the ingredients
    for that particular type of pizza.
    '''

    @classmethod
    def margherita(cls):
        return cls(['cheese','tomatoes'])
    
    @classmethod
    def mushroom(cls):
        return cls(['cheese','tomatoes','mushroom'])
    
    @classmethod
    def chicken(cls):
        return cls(['cheese','tomatoes','chicken'])

## Consider we need different types of Pizzas
# This is from the ClassInstances5.py script        
# =============================================================================
# # Margherita
# Pizza(['cheese','tomatoes'])
# 
# # Mushroom Special
# Pizza(['cheese','tomatoes','mushrooms'])
# 
# # Chicken
# Pizza(['cheese','tomatoes','chicken'])
# 
# =============================================================================

# Creating a Margherita pizza
Pizza.margherita() # No need to pass ingredients!
## What is the advantage?
## ANSWER:
# We can create number of pizzas of a particular type, say Margherita here. 
# We need not worry about passing in the ingredients repeatedly.
