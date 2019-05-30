"""
__varname can be used to denote some hidden variable in Python classes  
"""
class Secret:
    __count = 0
    def count(self):
        self.__count += 1
        print(self.__count)
    
obj = Secret()
obj.count()
obj.count()
#print(obj.__count)
print(f"Hidden count is {obj._Secret__count}")
