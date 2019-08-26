"""
Generator Expressions:
These are similar to list comprehensions. Instead of returning a list,\
they return a generator object which is memory efficient.\
Consider the execution of the even_number_generator.py function\
done using a generator expression.
"""


def generator_expression():
    even_integers = (n for n in range(10) if n % 2 == 0)
    print(type(even_integers))
    print()
    return True


def convert_to_integer():
    # list of mixed integers
    numbers = [7, 22, 4.5, 99.7, '5', '39_939']
    # convert to integers using generator expression
    integers = (int(n) for n in numbers)
    print(list(integers))
    return True

if __name__ == "__main__":
    generator_expression()
    print('*'*20)
    convert_to_integer()
