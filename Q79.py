# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


def reverse_integer(x):
    # Check if x is within the signed 32-bit integer range
    if x < -2147483648 or x > 2147483647:
        return 0

    # Convert x to a string and reverse it
    x_str = str(x)
    reversed_str = x_str[::-1]

    # If the first character is a "-", remove it and negate the result
    if reversed_str[0] == "-":
        reversed_int = -1 * int(reversed_str[1:])
    else:
        reversed_int = int(reversed_str)

    # Check if the result is within the signed 32-bit integer range
    if reversed_int < -2147483648 or reversed_int > 2147483647:
        return 0
    else:
        return reversed_int


print(reverse_integer(123))
print(reverse_integer(-123))


# This solution first checks if the input is within the signed 32-bit integer range. If it is, it converts the input to a string and reverses it. It then checks if the first character of the reversed string is a "-", and if it is, it removes the "-" and negates the result. Finally, it checks if the result is within the signed 32-bit integer range and returns it, or returns 0 if it is not.
