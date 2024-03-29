# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.


def is_happy(n):
    seen = set()
    while n != 1:
        n = sum(int(d)**2 for d in str(n))
        if n in seen:
            return False
        seen.add(n)
    return True


print(is_happy(19))  # prints True
print(is_happy(7))   # prints True
print(is_happy(2))   # prints False
