###############################################
# Question 1
# A program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

# finalList = []
# for num in range(2000, 3200+1):
#     if num%7 == 0 and num%5 != 0:
#         finalList.append(num)
# for i in finalList:
#     print(i, end=',')

################################################
# Question 2
# A program which can compute the factorial of a given numbers.

# number = int(input('Enter an integer'))
# multiplier = 1
# for num in range(1, number+1):
#     multiplier *= num
# print(multiplier)

################################################
# Question 3
# With a given integral number n, a program to generate a dictionary that contains (i, i*i) such that i,
# is an integral number between 1 and n (both included). and then the program should print the dictionary.

# int_num = int(input('Enter an integer'))
# int_dico = {}
# for num in range(1, int_num+1):
#     key = num
#     value = num*num
#     int_dico[key] = value
#
# print(int_dico)

###############################################
# Question 4
# A program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.

# list = []
# print('input "stop" to end')
# while True:
#     number = input('Enter number here: ')
#     if number == 'stop':
#         break
#     else:
#         list.append(number)
#
# print(list, tuple(list))

##############################################

###############
# Question 5
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also include simple test function to test the class methods.


# class String:
#     # def __init__(self):
#     #     self.string = ''
#
#     def getString(self):
#         self.string = input('Enter a string here: ')
#
#     def printString(self):
#         print(self.string.upper())
#
#
# x = String()
# x.getString()
# x.printString()
##############################################
# Question 6
# A program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

# from math import sqrt
# C, H, D = 50, 30, input('enter a comma-separated value here : ')
# D = D.split(',')
# print(D)
# for num in D:
#     Q = sqrt((2*C*int(num))//H)
#     print(round(Q))
#
##############################################
# Question 7
# A program that takes two digits ixj and generates a two-dimensional array
# array_str = input('Enter a two dimension of array here: ')
# array_dim = [int(x) for x in array_str.split('x')]
#
# rowNum = array_dim[0]
# colNum = array_dim[1]
#
# multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
# multiList[1][2] = 4
# print(multiList)

###############################################
# Question 8
# A program that accepts a comma separated sequence of names as input and
# print the names in a comma-separated sequence after sorting them alphabetically
# name_string = input('Enter sequence of names here ')
# names = name_string.split(', ')
# print(sorted(names))

###############################################
# Question 9
# A program that accepts a sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
# word_str = ''
# while True:
#     prompt = input('Enter sentences here : ')
#     if prompt != '':
#         word_str += prompt
#     else:
#         break
#     print(word_str.upper())

###############################################
# Question 10
# A program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# prompt = input('Enter text strings here: ')
# parsed_text = [word for word in sorted(prompt.split(' '))]
# parsed_word = []
# for word in parsed_text:
#     if word not in parsed_word:
#         parsed_word.append(word)
#
# print(parsed_word)
''' or use set() on parsed_text instead of the 'for' code suit '''

###############################################
# Question 11
# A program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# bin_num = input('Enter binary numbers here :')
# bin_num = bin_num.split(',')
# lists = []
# for num in bin_num:
#     if (int(num, 2)) % 5 == 0:
#         print(num, end=',')

###############################################
# Question 12
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

# for num in range(1000, 3001):
#     if num % 2 == 0:
#         print(num, end=',')

##############################################
# Question 13
# A program that accepts a sentence and calculate the number of letters and digits.

# sentence = input('Enter a sentence containing letters and digits here : ')
# letters, digits = 0, 0
# for character in sentence:
#     if character.isalpha():
#         letters += 1
#     elif character.isdigit():
#         digits += 1
# print('Letters = {}'.format(letters))
# print('Digits = %s' % digits)

##############################################
# Question 14
# A program that computes the value of b+bb+bbb+bbbb with a given digit as the value of b.

# b = input('Enter a value digit here : ')
#
# print(int(b) + int(b+b) + int(b+b+b) + int(b+b+b+b))

##############################################
# Question 15
# A program which uses list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

# string = input('Enter a list of comma-separated numbers here : ')
# nums = string.split(',')
# int_num = [int(x) for x in nums]
# output = [x**2 for x in int_num if x % 2 != 0]
# print(output)

##############################################
# Question 16
# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal. Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be: 500

# print('INSTRUCTION: Enter "=" to output ')
# withdrawal, deposit = [], []
# while True:
#     transaction = input('Enter your transaction here : ')
#
#     if transaction == '=':
#         break
#     else:
#         if transaction.startswith('D' or 'd'):
#             trans_split = transaction.split(' ')
#             deposit.append(int(trans_split[1]))
#         elif transaction.startswith('W' or 'w'):
#             trans_split = transaction.split(' ')
#             withdrawal.append(int(trans_split[1]))
#         else:
#             print('Ooops! You\'ve entered an invalid transaction')
#
# sum_W, sum_D = sum(withdrawal), sum(deposit)
# Output = sum_D - sum_W
# print('Output = %s' % Output)

##################################################
"""
QUESTION 17
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the
above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""


##################################################
# QUESTION 18
# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score.
# The priority is the same as name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# from operator import itemgetter
# output_list = []
# while True:
#     data = input('Enter a comma-separated data input here : ')
#
#     if not data:
#         break
#     else:
#         data_split_tuple = tuple(data.split(','))
#         output_list.append(data_split_tuple)
#
# print(sorted(output_list, key=itemgetter(0, 1, 2)))     # or just print(sorted(output_list))

###############################################
# QUESTION 19
# Write a function to reverse a given string

# def rev_str(str):
#     n = -1
#     for i in range(len(str)):
#         print(str[n])
#         n -= 1
#
# a = rev_str('timothy')

        ############## OR ##############

# def rev_str(my_str):
#     for i in range(len(my_str)-1, -1, -1):
#          print(my_str[i])
#
# a = rev_str('timothy')

##############################################

# QUESTION 20
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# def generator(n):
#     for i in range(0, n):
#
#         if i % 7 == 0:
#             yield i
#
# for i in generator(50):
#     print(i)

#############################################
# QUESTION 21
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2
# The numbers after the direction are steps. Write a program to compute the distance from current position after a
# sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be: 2

# from math import sqrt
#
# up = float(input('UP = '))
# down = float(input('DOWN = '))
# left = float(input('LEFT = '))
# right = float(input('RIGHT = '))
#
# up, down, left, right = int(up), int(down), int(left), int(right)
#
# y_axis = up - down
# x_axis = right - left
#
# distance = int(sqrt(y_axis**2 + x_axis**2))
#
# print('Total Distance = %s' % distance)

###################################################
# QUESTION 22
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

# parsed_text = []
# prompt = input('Enter your message here : ')
#
# prompt_split = prompt.split(' ')
#
# for text in prompt_split:
#     if text not in parsed_text:
#         parsed_text.append(text)
#
# parsed_text.sort()
# for text in parsed_text:
#     print("{}:{}".format(text, prompt_split.count(text)))

####################################################
# QUESTION 23
# Write a method which can calculate square value of number

# class Square:
#     def square(number):
#         print(number**2)
#
# Square.square(6)

###################################################
# QUESTION 24
# Write a valid HTML + Python Page that will count numbers from 1 to 1,000,000?
# i.    Display every 10th number in the series in Bold
# ii.   Display every 3rd number in the series in Italics.
# iii.  Bonus: Underline every Prime Number in this series.

# < !DOCTYPE
# html >
# < html >
# < head >
# < title > Intenship < / title >
# < / head >
#
# < body >
#
# < b > tenth_num = [num for num in range(1, 10000001) if str(num).endswith('0')] < / b >
#
# < i > third_num = [num for num in range(1, 10000001) if num % 3 == 0] < i / >
#
# remainder_list = []
# for num in range(1, 10000001):
#     for value in range(num):
#         remainder = num % value
#         remainder_list.append(remainder)
#
#     if 0 in remainder_list == False:
#         < u > print(num) < / u >
# < / body >
# < / html >

####################################################
# QUESTION 25
# Define a function that can convert an integer into a string and print it in console.

# def converter(integer):
#     return str(integer)
#
# conv = converter(3)
# print(conv)

####################################################
# QUESTION 26
# Define a function that can receive two integral numbers in string form and
# compute their sum and then print it in console.

# def func(int1, int2):
#     return int(int1) + int(int2)
#
#
# print(func('3', '7'))
####################################################
# QUESTION 27
# Define a function that can accept two strings as input and concatenate them and
# then print it in console.

# def func(str1, str2):
#     return str1 + str2
#
#
# print(func('3', '4'))

####################################################
# QUESTION 28
# Define a function that can accept two strings as input and print the string with
# maximum length in console. If two strings have the same length, then the function
# should print all strings line by line.

# def func(str1, str2):
#
#     if len(str1) > len(str2):
#         print(str1)
#     elif len(str2) > len(str1):
#         print(str2)
#     elif len(str1) == len(str2):
#         print(str1)
#         print(str2)
#
# func('timothy', 'ayomid')

####################################################
# QUESTION 29
# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

def func():





