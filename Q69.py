# Given a string s, return the longest palindromic substring in s


# To solve this problem, we can use a brute force approach where we check every possible substring of the input string to see if it is a palindrome.
# If it is, we update the longest palindromic substring found so far.

# SOLUTION
# BRUTE FORCE ALGORITHM
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


# MANACHER'S ALGORITHM
def longestPalindromicSubstring(s):
    # Preprocess the string to handle even-length palindromes
    t = preprocess(s)

    # Initialize the array to store the lengths of the palindromes
    p = [0] * len(t)

    # Initialize the center and right end of the palindrome
    c = r = 0

    # Consider every character in the preprocessed string
    for i in range(1, len(t)-1):
        # Find the mirror of the current position
        j = 2*c - i

        # If the current position is within the right end of the palindrome,
        # set the length of the palindrome at the current position to the
        # minimum of the palindrome length at the mirror position and the
        # distance from the right end of the palindrome to the current position
        if r > i:
            p[i] = min(r-i, p[j])

        # Expand the palindrome centered at the current position
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        # Update the center and right end of the palindrome if necessary
        if i + p[i] > r:
            c = i
            r = i + p[i]

    # Find the maximum length and the center of the longest palindrome
    maxLen, centerIndex = max((n, i) for i, n in enumerate(p))

    # Calculate the start and end indices of the longest palindrome
    start = (centerIndex - maxLen) // 2
    end = start + maxLen

    # Return the longest palindromic substring
    return s[start:end]


def preprocess(s):
    # Add a sentinel character to the beginning and end of the string
    # and insert a delimiter between every character
    t = "^#" + "#".join(s) + "#$"
    return t


# This solution first preprocesses the input string by adding sentinel characters and delimiters between the characters. This is done to make it easier to handle even-length palindromes. It then initializes the center and right end of the palindrome, and considers every character in the preprocessed string. For each character, it finds its mirror position, expands the palindrome centered at the current position, and updates the center and right end of the palindrome if necessary. Finally, it finds the maximum length and the center of the longest palindrome, calculates the start and end indices of the longest palindromic substring, and returns the substring.

# The time complexity of this algorithm is O(n) because we only consider each character in the preprocessed string once. This makes it much faster than the brute force approach, which has a time complexity of O(n^3).


# WORKING SOLUTION
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0
        max_p = ""
        for i in range(n):
            for j in range(i, i + 2):
                b = i
                e = j
                while b >= 0 and e < n and s[b] == s[e]:
                    b -= 1
                    e += 1
                l = e - b - 1
                if l > max_len:
                    max_len = l
                    max_p = s[b + 1: e]
        return max_p
