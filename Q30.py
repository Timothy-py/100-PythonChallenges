# With a given tuple(1,2,3,4,5,6,7,8,9,10), write a program to print the first half
# values in one line and the last half values in one line.

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup1 = tup[:5]
tup2 = tup[5:]
print(f"First half = {tup1} \n Second half = {tup2}")
