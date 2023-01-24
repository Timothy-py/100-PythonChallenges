# Write a program which can map() and filter() to make a list whose elements are square of
# even number in [1,2,3,4,5,6,7,8,9,10].

even_filtered = [even for even in filter(
    lambda u: u % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]

squared_even = [square for square in map(lambda m: m**2, even_filtered)]
