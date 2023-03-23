# A program which uses list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

string = input('Enter a list of comma-separated numbers here : ')
nums = string.split(',')
int_num = [int(x) for x in nums]
output = [x**2 for x in int_num if x % 2 != 0]
print(output)
