# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

square = map(lambda y: y**2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(square)
print(next(square, default="Stop bro!"))
