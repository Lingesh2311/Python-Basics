## Dispatching Dictionary
## Emulating Switch case in Python
def dispatch_dict(choice, a, b):
  return {
    'add' : lambda a + b,
    'sub' : lambda a - b,
    'mul' : lambda a * b,
    'div' : lambda a / b
  }.get(choice, lambda : None)()

if __name__=='__main__':
  in_choice = input('Enter your choice: ')
  print(f"Result : {dispatch_dict()}")
