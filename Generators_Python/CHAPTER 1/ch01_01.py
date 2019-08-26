# function to return a list of even numbers
def even_num_list(n):
    result = []
    for i in range(n):
        if (i % 2 == 0):
            result.append(i)
    return result

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    even_num_list(n)
