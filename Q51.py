# QUESTION 51
# The Fibonacci Sequence is computed based on the following formula:
# 	f(n)=0 if n=0, f(n)=1 if n=1, f(n)=f(n-1)+f(n-2) if n>1
# 	Please write a program using list comprehension to print the Fibonacci
# 	Sequence in comma separated form with a given n input by console.
# 	Example: If the following n is given as input to the program:7
# 	Then, the output of the program should be: 0,1,1,2,3,5,8,13

def fibonacci(n):

    if n == 0:
        value = 0
        return value
    elif n == 1:
        value = 1
        return value
    elif n > 1:
        value = fibonacci(n-1) + fibonacci(n-2)
        return value


i = int(input("Enter an integer value here: "))
print([fibonacci(_) for _ in range(i)])
