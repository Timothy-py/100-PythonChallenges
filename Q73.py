# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# SOLUTION
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# The XOR operation (^) has the property that a ^ a = 0 for any a, which means that if we XOR all the elements in the array together, all the elements that appear twice will cancel each other out, leaving only the element that appears once.

# This solution has a linear runtime complexity, since it iterates through the array once and performs a constant number of operations on each element.
# It also uses only constant extra space, since it only stores a single integer (the result variable).
