# The Fibonacci Sequence is completed based on the following formula:
# f(n) = 0 if n=0
# f(n) = 1 if n=1
# f(n) = f(n-1) + f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# If n=7 is given as input to the program: Then, the output should be: 13

def formulae(n=int(input("Enter number here: "))):

    if n == 0:
        value = 0
        return value
    elif n == 1:
        value = 1
        return value
    elif n >= 2:
        value = formulae(n-1) + formulae(n-2)
        return value


formulae(7)
