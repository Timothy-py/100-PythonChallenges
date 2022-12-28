# QUESTION 52
# Please write a program using generator to print the even numbers between 0 and n
# in comma separated form while n is input by console.
# 	Example: If the following n is given as input to the program: 10
# 	Then, the output of the program should be: 0,2,4,6,8,10

def even_gen(n):
    for num in range(0, n+1):
        if num % 2 == 0:
            yield num


n = int(input("Enter an integer number here: "))
values = []
for _ in even_gen(n):
    values.append(str(_))

print(",".join(values))
