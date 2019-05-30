"""
Basic Implementation of Stack in Python
"""
class Stack():
    '''
    Stack follows LIFO just like pancakes!
    '''
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == [] # compare with empty set

    def peek(self): 
        if not self.is_empty():
            return self.items[-1] # return the last element in the stack 

    def get_stack(self):
        print(self.items)

s = Stack()
print(s.is_empty()) 
s.push("A")
s.push("B")
print(s.is_empty())
s.get_stack()
s.push("C")
print(s.is_empty())
s.get_stack()
s.pop()
print(s.is_empty())
s.get_stack()
print(s.peek())