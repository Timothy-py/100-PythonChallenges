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
