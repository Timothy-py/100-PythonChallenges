# Write a function to reverse a given string


def rev_str(str):
    n = -1
    for i in range(len(str)):
        print(str[n])
        n -= 1


a = rev_str('timothy')

#         ############## OR ##############


def rev_str(my_str):
    for i in range(len(my_str)-1, -1, -1):
        print(my_str[i])


a = rev_str('timothy')
