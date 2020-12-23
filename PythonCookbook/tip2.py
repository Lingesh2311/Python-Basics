x = 10
a = lambda y: x + y // x is 20 here
x = 20 
b = lambda y: x + y // x is 20 here
# For an anonymous function to capture the value at the point of definition
# we need to include the value as default value
x = 10
a = lambda y, x=x: x + y // x is fixed at 10 
x = 20
a = lambda y, x=x: x + y // x is fixed at 20

# We can set instance methods to functions
# just like classes but there is no class involved
def sample():
  n = 0
  # closure function
  def func():
    print("n = ", n)
   # Accessor function
   def get_n():
    return n
   def set_n(value):
    nonlocal n
    n = value
  # Attach as function attributes
  func.get_n = get_n
  func.set_n = set_n
  retunr func

# Calling them
f = sample()
f() // will print 0
f.set_n(10) // we can do this because of the function attributes
f() // will print 10
f.get_n() // will print 10
