# Given a 2D matrix of characters and a target word, write a function that returns
#  whether the word can be found in the matrix by going left-to-right, or up-to-down
# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
#  ['O', 'B' 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word "FOAM", you should return true, since it's the leftmost column.
# Similarly, given the target word "MASS", you should return true, since it's the last row.

# def func(input_string):

#     m = {}

#     for i in range(len(input_string)):

#         c = input_string[i]

#         m[c] = i

#     return m


# print(func("timothy"))

p = 0
n = 42
for i in range(n):

    if n % 3 == 0:

        q = i + 4 if n < 40 else None

    else:

        q = i + 40

    p += float(q) / 1000

print(p)


# def print_all_codes(n, m):

#     def print_01_codes(current, num_digits):

#         if num_digits == 0:

#             print(current)

#         else:

#             print_01_codes('0' + current, num_digits - 1)

#             print_01_codes('1' + current, num_digits - 1)

#     upper_bound = 0

#     while True:

#         for i in range(upper_bound):

#             print_01_codes('', n)

#         if upper_bound > m:

#             break

#         upper_bound += 1


# print_all_codes(2, 3)
