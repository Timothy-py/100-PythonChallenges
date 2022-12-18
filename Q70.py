# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# SOLUTION
# To solve this problem in Python, you can use the split() method to split the string into a list of words,
# and then return the length of the last word in the list.

def last_word_length(s: str) -> int:
    # Split the string into a list of words
    words = s.split()

    # If the list is empty, return 0
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])


# This function first splits the string into a list of words using the split() method.
# If the list is empty (i.e. the input string was empty or consisted entirely of spaces),
# it returns 0. Otherwise, it returns the length of the last word in the list.

print(last_word_length("Hello World!"))  # Output: 6 (length of "World")
print(last_word_length("I love Python"))  # Output: 6 (length of "Python")
print(last_word_length(""))              # Output: 0
print(last_word_length("    "))          # Output: 0
