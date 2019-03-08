# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:43:53 2019

@author: Lingesh K
"""

class Myclass:
    '''
    This is an Instance method in which the instance is fed
    as an input by default. This method can modify the object
    instance state. This can also modify the state of the class
    
    '''
    def method(self):
        return 'Instance Method called', self
    
    '''
    This is a Class method and does not have access to the self 
    argument. This cannot modify the object instance state. This can
    modify the class state. To access the instance from the class method
    We can pass the type(instance) as the parameter corresponding to cls.
    Thus, this creates a more robust method to access the instance using the 
    class method.
    '''

    @classmethod # This is a class method decorator
    def classmethod(cls):
        return 'Class Method called', cls
    
    @staticmethod# This is a static method decorator
    def staticmethod():
        return 'Static Method called'
    

obj = Myclass()

# Can we access the classmethod using an instance of Myclass?
print(Myclass.classmethod())
## ANSWER: 
# Yes, we can all it does is it takes the entire class as the default argument
# Since the instance has access to all the methods in the class this works!

# Can we access the static method using an instance of Myclass?
print(Myclass.staticmethod())
## ANSWER:
# Yes, we can do this as well. It is now a normal method inside a class that
# does not need any instance or class to be passed as an argument.