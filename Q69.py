# Given a string s, return the longest palindromic substring in s


# To solve this problem, we can use a brute force approach where we check every possible substring of the input string to see if it is a palindrome.
# If it is, we update the longest palindromic substring found so far.

# SOLUTION
def longestPalindromicSubstring(s):
    # Initialize the longest palindromic substring found so far
    longest = ""

    # Consider every possible substring of s
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # Check if the substring is a palindrome
            if s[i:j] == s[i:j][::-1]:
                # Update the longest palindromic substring found so far if necessary
                if len(s[i:j]) > len(longest):
                    longest = s[i:j]

    return longest


# This solution has a time complexity of O(n^3) because we are considering every possible substring of the input string, which takes O(n^2) time, and then we are checking if each substring is a palindrome, which takes O(n) time. This means that the algorithm will take a longer time to run for larger input strings.

# There are more efficient algorithms for finding the longest palindromic substring, such as the Manacher's algorithm, which has a time complexity of O(n).
