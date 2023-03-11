# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

def generator(n):
    for i in range(0, n):

        if i % 7 == 0:
            yield i


for i in generator(50):
    print(i)
