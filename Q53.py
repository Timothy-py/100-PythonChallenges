# QUESTION 53
# 	Please write a program using generator to print the numbers which can be divisible by 5 and 7
# 	between 0 and n in comma separated form while n is input by console.
#   Example: If the following n is given as input to the program: 100
#   Then, the output of the program should be: 0,35,70

def generator(n):

    for _ in range(0, n+1):
        if _ % 5 == 0 and _ % 7 == 0:
            yield _


n_input = int(input("Enter an integer number here : "))
values = []
for i in generator(n_input):
    values.append(str(i))

print(",".join(values))
