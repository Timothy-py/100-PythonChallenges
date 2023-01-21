# QUESTION
# Have you heard of the fibonacci sequence? It is defined by f0=0, f1=1 and fn=fn-1 + fn-2 for n>=2.
# This question is about a similar sequence, called gibonacci sequence. It is defined by g0 = x, g1 = y and gn = gn-1 - gn-2 for n >= 2.
# Different possible starting values of the gibonacci sequence may lead to different gibonacci sequences.
# You are given three arguments: n, x, y. Your task is to find gn using the above definition of a gibonacci sequence starting with g0 = x, g1 = y.
# Write a function gibonacci(n,x,y) that takes in 3 arguments.

# Inputs
# It is guaranteed that n,x,y are integers and 0 <= n, x, y <= 1000000000

# Outputs
# gibonacci(n,x,y) should return gn given that g0 = x, g1 = y.


# SOLUTION
def gibonacci(n, x, y):
    # Check if n is 0, if it is return x
    if n == 0:
        return x
    # Check if n is 1, if it is return y
    elif n == 1:
        return y
    # If n is greater than 1
    else:
        # Initialize g_n_2 as x and g_n_1 as y
        # g_n_2 = x
        # g_n_1 = y
        prev1 = y
        prev2 = x
        # Iterate from 2 to n+1 (inclusive)
        for i in range(2, n+1):
            # calculate the next term gn = gn-1 - gn-2
            nth = prev1 - prev2
            # update the value of g_n_2 as g_n_1
            prev2 = prev1
            # update the value of g_n_1 as g_n
            prev1 = nth
        # return the nth term g_n
        return nth


print(gibonacci(1, 0, 1))


# SOLUTION
# This function takes in 3 arguments: n, x, and y. It first checks if n is equal to 0, in which case it returns x. If n is equal to 1, it returns y.
# Otherwise, it initializes two variables g_n_2 and g_n_1 to x and y respectively, representing the 2 previous terms in the sequence.
# Then it uses a for loop to iterate from 2 to n+1 (inclusive), on each iteration it calculates the next term g_n using the definition provided by subtracting the previous term g_n_2 from the current term g_n_1. Then it updates the value of g_n_2 and g_n_1 to g_n_1 and g_n respectively.
# Finally, it returns the value of g_n which is the nth term of the gibonacci sequence given the initial values of x and y.
