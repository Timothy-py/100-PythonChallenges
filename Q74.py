from math import factorial


# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    res = 0
    two = n//2

    for i in range(two+1):
        t = i           # number of twos
        o = n-t*2       # number of ones
        res += factorial(t+o)/(factorial(t)*factorial(o)
                               )     # (two+one)!/ (two!*one!)

    return res


def climbStairs2(n):
    # create an array to store the number of ways to reach each step
    ways = [0] * (n + 1)

    # base case: there is only one way to reach the first step
    ways[0] = 1

    # base case: there is only one way to reach the second step
    ways[1] = 1

    # iterate over the remaining steps
    for i in range(2, n+1):
        # the number of ways to reach the current step is equal to the
        # number of ways to reach the previous step plus the number of
        # ways to reach the step before that
        ways[i] = ways[i-1] + ways[i-2]

    # return the number of ways to reach the top step
    return ways[n]


print(climbStairs(7))
