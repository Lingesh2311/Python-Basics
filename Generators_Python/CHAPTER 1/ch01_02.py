# Generator function which yields even numbers lesser than the input
"""
This Generator function returns a generator object. A generator yields rather\
than return.
"""


def generator_even_num(n):
    for i in range(n):
        if (i % 2 == 0):
            yield i


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    iterator = generator_even_num(n)
    for i in range(4):
        print(next(iterator))
