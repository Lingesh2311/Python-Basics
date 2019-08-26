# Generator function which yields even numbers lesser than the input
def generator_even_num(n):
    for i in range(n):
        if (i % 2 == 0):
            yield i


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    generator_even_num(n)
