# To give a default value as argument
_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('b has no value supplied')
        
# spam(1) // Not OK
# spam(1, 2) // OK, b=2
# spam(1, None) // OK, b=None


# Default arguments should always be of some immutable object type
# def spam(a, b=[]) # NOT OK

# Instead we can use the None check
def spam(a, b=None):
  if b is None:
    b = []

