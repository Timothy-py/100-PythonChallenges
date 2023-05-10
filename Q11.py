# Question 11
# A program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

bin_num = input('Enter binary numbers here :')
bin_num = bin_num.split(',')
lists = []
for num in bin_num:
    if (int(num, 2)) % 5 == 0:
        print(num, end=',')
