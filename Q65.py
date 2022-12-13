# Given a string s, find the length of the longest substring without repeating characters.

# SOLUTION
# To find the length of the longest substring without repeating characters in a given string, you can use the following algorithm:

# 1. Set a variable maxLength to 0. This variable will store the length of the longest substring without repeating characters that we find.

# 2. Set a variable start to 0. This variable will keep track of the starting index of the current substring we are considering.

# 3. Set a variable seen to an empty dictionary. This dictionary will keep track of the characters we have seen so far in the current substring.

# 4. Iterate over the characters in the string, starting at index 0. At each step, do the following:

#       - If the current character is not in seen, add it to seen and move on to the next character.
#       - If the current character is in seen, calculate the length of the current substring by subtracting the starting index from the current index. Update maxLength if the current length is greater than maxLength. Then, update the starting index to be one character after the last time we saw the current character, and clear the seen dictionary.
# 5. After the loop has finished, calculate the length of the final substring by subtracting the starting index from the length of the string, and update maxLength if necessary.

# 6. The value of maxLength is the length of the longest substring without repeating characters.

# debug this solution
def longest_substring_without_repeating_characters(s):
    maxLength = 0
    start = 0
    seen = {}

    for i, c in enumerate(s):
        if c in seen:
            maxLength = max(maxLength, i - start)
            start = seen[c] + 1
            seen.clear()
        else:
            seen[c] = i

    return max(maxLength, len(s) - start)


s = "abcabcbb"
print(longest_substring_without_repeating_characters(s))  # Output: 3 ("abc")


# correct solution
def lengthOfLongestSubstring(self, s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength
