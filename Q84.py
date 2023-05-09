# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# SOLUTION

def plusOne(digits):
    n = len(digits)
    # Start from the least significant digit and add 1 to it
    digits[n-1] += 1

    # Propagate the carry if required
    for i in range(n-1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1

    # If the most significant digit is 10, add a new digit
    if digits[0] == 10:
        digits[0] = 0
        digits.insert(0, 1)

    return digits


print(plusOne([9]))

# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]

# Input: digits = [9]
# Output: [1,0]
