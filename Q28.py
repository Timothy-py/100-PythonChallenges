# Define a function that can accept two strings as input and print the string with
# maximum length in console. If two strings have the same length, then the function
# should print all strings line by line.


def func(str1, str2):

    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    elif len(str1) == len(str2):
        print(str1)
        print(str2)


func('timothy', 'ayomid')
