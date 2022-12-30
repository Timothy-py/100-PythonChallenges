# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5
# Then, the output of the program should be: 3.55

def formula(n):
    result = 0
    if n > 0:
        list_n = [i for i in range(1, n+2)]

        for num in list_n[:-1]:
            result += num/list_n[list_n.index(num)+1]
        print(f"{result:.2f}")
    else:
        print("Value must be greater than 0")

# *******************OR*******************


def formula(n):
    result = 0
    for i in range(1, n+1):
        result += i/(i+1)
    print(f"{result:.2f}")


formula(5)
