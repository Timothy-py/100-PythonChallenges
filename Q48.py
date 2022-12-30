# Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5 Then, the output of the program should be: 500


def formular(n=int(input("Enter number here : "))):

    if n == 0:
        value = 1
        return value
    elif n > 0:
        value = formular(n-1) + 100
        return value


print(formular())
