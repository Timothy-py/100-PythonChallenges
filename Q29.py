# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.


def foo(number):
    dico = {}
    dico = dico.fromkeys([num for num in range(1, number+1)])
    for keys in dico:
        dico[keys] = keys**2
    print(dico)


foo(3)
