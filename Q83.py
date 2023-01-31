# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longestCommonPrefix(["dog", "racecar", "car"]))

# The function first checks if the list strs is empty, and returns an empty string in that case. If not, it sets the first string in the list as the initial prefix. The function then loops through the rest of the strings in the list, and at each iteration, it repeatedly removes the last character from prefix until the current string in the list starts with the updated prefix. If prefix becomes an empty string before a common prefix is found, the function returns an empty string, otherwise it returns the longest common prefix.
