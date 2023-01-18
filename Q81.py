# [Turing Python Test]
# Solve this challenge with Python
# Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[J] = S and S < K. If no such i, j exist satisfying this equation, return -1.

def max_s(A, K):
    max_s = -1
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            s = A[i] + A[j]
            if s < K and s > max_s:
                max_s = s
    return max_s


# SOlution Discuss
# This function takes in an array A and an integer K. It initializes a variable max_s to -1 which will store the maximum value of S that satisfies the given condition. It then uses two nested loops to iterate through all pairs of elements in the array. For each pair, it calculates the value of S by adding the two elements and checks if it is less than K and greater than max_s. If it is, it updates the value of max_s. After all pairs have been checked, it returns the final value of max_s, which will be the maximum value of S that satisfies the given condition, or -1 if no such pair exists.
