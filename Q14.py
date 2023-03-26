# A program that computes the value of b+bb+bbb+bbbb with a given digit as the value of b.

b = input('Enter a value digit here : ')

print(int(b) + int(b+b) + int(b+b+b) + int(b+b+b+b))
