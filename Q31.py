# QUESTION 31
# Create a function to print the nth term of a fibonacci sequence using recursion, and
# also use memoization to cache the result.

# define a dictionary to serve as a cache
fib_cache = {}


def fib(n):
    # check if the value to be computed is in the dictionary
    # if it is there, return the result instead
    if n in fib_cache:
        return fib_cache[n]

    # do the fibonacci computation here
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n >= 2:
        value = fib(n-1) + fib(n-2)

    # store the result of any of the above computation in the cache
    fib_cache[n] = value

    return value


for i in range(100):
    print(i, ':', fib(i))
