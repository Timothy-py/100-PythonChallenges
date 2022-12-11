# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# SOLUTION
# This is a common problem in computer science known as the "Two Sum" problem. It is a common interview question and has a straightforward solution. Here is one way to solve the problem:

# - Loop through the array of integers and for each element, check if the target minus the current element is in the array.
# - If the target minus the current element is in the array, return the indices of the current element and the element that adds up to the target.
# - If the target minus the current element is not in the array, continue looping through the array until a solution is found.
# Here is an example of the solution in code:

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# This solution has a time complexity of O(n^2) because it uses two nested loops to search for the solution. There may be more efficient solutions that have a lower time complexity, but this solution is simple and easy to understand.
