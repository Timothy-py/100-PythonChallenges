# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Using binary search algorithm
def findMedianSortedArrays(nums1, nums2):
    # Ensure that nums1 is the shorter array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = (m + n + 1) // 2 - i
        if i < m and nums2[j-1] > nums1[i]:
            # i is too small, increase it
            lo = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too big, decrease it
            hi = i - 1
        else:
            # i is the perfect size
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2


# using merge sort algorithm

# To find the median of two sorted arrays, you can use the following approach:

# Merge the two arrays into a single sorted array using a merge sort algorithm.

# Find the length of the merged array.

# If the length of the merged array is odd, return the middle element.
def findMedianSortedArrays(nums1, nums2):
    # Merge the two arrays into a single sorted array
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    # Find the median of the merged array
    if len(merged) % 2 == 1:
        median = merged[len(merged) // 2]
    else:
        median = (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2

    return median


# TEST
print(findMedianSortedArrays([1, 3], [2]))  # Output: 2
print(findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
