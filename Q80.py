# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. T
# he relative order of the elements may be changed.Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums. More formally,
# if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements. Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# SOLUTION
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))


# This function uses two pointers, one to iterate through the entire array and another to keep track of the position where the final result should be placed. If the current element is not equal to the given value, it is placed in the first k slots of the array and k is incremented. The final result is the first k elements of the array, and the function returns the value of k.
# This solution has a time complexity of O(n) as it iterates through the array once, and a space complexity of O(1) as it does not use any extra memory.
