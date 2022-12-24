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


print(climbStairs(7))
