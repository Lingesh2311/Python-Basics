"""
Class methods - they are called by a class. In this script,
the class method new_square is called by the class Rectangle 
as Rectangle.new_square(5). Here 5 is the side_length. So,
equivalent of 
Rectangle.new_square(5) is Rectangle(5,5).
Class methods use the cls(__init__ parameter list) and these are commonly
used for factory methods, which intantiate an instance of a class, using different
parameters thatn those usually passed to the class decorator. 
Class methods are marked with a @classmethod decorator(a function that modifies another function/ method).
"""
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
