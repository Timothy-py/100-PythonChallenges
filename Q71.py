# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# SOLUTION

from math import factorial


def climb_staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_staircase(n-1) + climb_staircase(n-2)


# This solution uses a recursive approach to solve the problem. The function calls itself with n-1 and n-2 as the arguments until the base case is reached.
# The base case is when n is 1 or 2, in which case the function returns 1 or 2, respectively. When the function is called with a value of n greater than 2,
# it returns the sum of the number of ways to reach n-1 steps and the number of ways to reach n-2 steps.
# This is because the number of ways to reach the nth step is equal to the number of ways to reach the n-1th step and the n-2th step,
# since you can either take 1 step or 2 steps at a time.


def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = 0
    two = n//2

    for i in range(two+1):
        t = i           # number of twos
        o = n-t*2       # number of ones
        res += factorial(t+o)/(factorial(t)*factorial(o)
                               )     # (two+one)!/ (two!*one!)

    return res
