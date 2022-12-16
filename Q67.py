# Given an integer x, return true if x is a palindrome, and false otherwise.

# SOLUTION
# 1 Convert the integer to a string. This will make it easier to check if the number is a palindrome.
# 2 Reverse the string using slicing.
# 3 Compare the reversed string with the original string. If they are equal, then the number is a palindrome. Otherwise, it is not a palindrome.

def is_palindrome(x):
    x_str = str(x)
    rev_x_str = x_str[::-1]
    if rev_x_str == x_str:
        return True
    else:
        return False


# TEST
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
print(is_palindrome(0))    # True
