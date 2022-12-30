# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# Explanation
"""
This function takes in a sorted list of distinct integers nums and a target value target, and returns the index of target in nums if it exists, or the index where it would be inserted in order if it does not.

The function uses a binary search algorithm to search for the target in nums. It sets the left and right pointers to the beginning and end of the list, respectively, and then enters a loop that continues as long as left is less than or equal to right. In each iteration of the loop, it calculates the midpoint of the current search range and compares the value at the midpoint to the target. If the value at the midpoint is equal to the target, it returns the index of the midpoint. If the value at the midpoint is less than the target, it sets the left pointer to the index immediately after the midpoint, effectively narrowing the search range to the right half of the list. If the value at the midpoint is greater than the target, it sets the right pointer to the index immediately before the midpoint, narrowing the search range to the left half of the list.

If the loop finishes without finding the target, it means that the target is not in the list. In this case, the function returns the value of left, which is the index where the target would be inserted in order to maintain the sorted order of the list.
"""
