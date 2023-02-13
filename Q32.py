from functools import lru_cache
# Create a function to print the nth term of a fibonacci sequence using recursion, and
# also use lru_cache to cache the result.


@lru_cache(258)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fib(n-1) + fib(n-2)


for i in range(100):
    print(i, ':', fib(i))
