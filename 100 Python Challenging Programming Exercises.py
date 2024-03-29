# ###############################################
# Question 1
# A program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

from random import shuffle
import random
import math
import re
from math import pi
from functools import lru_cache
from operator import itemgetter
from math import sqrt
finalList = []
for num in range(2000, 3200+1):
    if num % 7 == 0 and num % 5 != 0:
        finalList.append(num)
for i in finalList:
    print(i, end=',')

# ################################################
# Question 2
# A program which can compute the factorial of a given numbers.

number = int(input('Enter an integer'))
multiplier = 1
for num in range(1, number+1):
    multiplier *= num
print(multiplier)

# ###############################################
# Question 3
# With a given integral number n, a program to generate a dictionary that contains (i, i*i) such that i,
# is an integral number between 1 and n (both included). and then the program should print the dictionary.

int_num = int(input('Enter an integer'))
int_dico = {}
for num in range(1, int_num+1):
    key = num
    value = num*num
    int_dico[key] = value

print(int_dico)

# ###############################################
# Question 4
# A program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.

list = []
print('input "stop" to end')
while True:
    number = input('Enter number here: ')
    if number == 'stop':
        break
    else:
        list.append(number)

print(list, tuple(list))

# ##############################################
# Question 5
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also include simple test function to test the class methods.


class String:
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input('Enter a string here: ')

    def print_string(self):
        print(self.string.upper())


x = String()
x.getString()
x.printString()

# ##############################################
# Question 6
# A program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

C, H, D = 50, 30, input('enter a comma-separated value here : ')
D = D.split(',')
print(D)
for num in D:
    Q = sqrt((2*C*int(num))//H)
    print(round(Q))

# ##############################################
# Question 7
# A program that takes two digits ixj and generates a two-dimensional array
array_str = input('Enter a two dimension of array here: ')
array_dim = [int(x) for x in array_str.split('x')]

rowNum = array_dim[0]
colNum = array_dim[1]

multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
multiList[1][2] = 4
print(multiList)

# ###############################################
# Question 8
# A program that accepts a comma separated sequence of names as input and
# print the names in a comma-separated sequence after sorting them alphabetically
name_string = input('Enter sequence of names here ')
names = name_string.split(', ')
print(sorted(names))

# ###############################################
# Question 9
# A program that accepts a sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
word_str = ''
while True:
    prompt = input('Enter sentences here : ')
    if prompt != '':
        word_str += prompt
    else:
        break
    print(word_str.upper())

# ###############################################
# Question 10
# A program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.

# ###############################################
# Question 11
# A program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# ###############################################
# Question 12
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

# ##############################################
# Question 13
# A program that accepts a sentence and calculate the number of letters and digits.


# ##############################################
# Question 14
# A program that computes the value of b+bb+bbb+bbbb with a given digit as the value of b.


# ##############################################
# Question 15
# A program which uses list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

# ##############################################
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


# ##################################################
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


# ##################################################
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


# ###############################################
# QUESTION 19
# Write a function to reverse a given string


# ##############################################
# QUESTION 20
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# #############################################
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

# ###################################################
# QUESTION 22
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1


# ####################################################
# QUESTION 23
# Write a method which can calculate square value of number


# ###################################################
# QUESTION 24
# Write a valid HTML + Python Page that will count numbers from 1 to 1,000,000?
# i.    Display every 10th number in the series in Bold
# ii.   Display every 3rd number in the series in Italics.
# iii.  Bonus: Underline every Prime Number in this series.


# ####################################################
# QUESTION 25
# Define a function that can convert an integer into a string and print it in console.


# ####################################################
# QUESTION 26
# Define a function that can receive two integral numbers in string form and
# compute their sum and then print it in console.


# ####################################################
# QUESTION 27
# Define a function that can accept two strings as input and concatenate them and
# then print it in console.


# ####################################################
# QUESTION 28
# Define a function that can accept two strings as input and print the string with
# maximum length in console. If two strings have the same length, then the function
# should print all strings line by line.


# ####################################################
# QUESTION 29
# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.


# #####################################################
# QUESTION 30
# With a given tuple(1,2,3,4,5,6,7,8,9,10), write a program to print the first half
# values in one line and the last half values in one line.


# ######################################################
# QUESTION 31
# Create a function to print the nth term of a fibonacci sequence using recursion, and
# also use memoization to cache the result.


# ##################################################
# QUESTION 32
# Create a function to print the nth term of a fibonacci sequence using recursion, and
# also use lru_cache to cache the result.


# ######################################################
# QUESTION 33
# Write a program which can filter even numbers in a list by using filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].


# ###################################################
# QUESTION 34
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].


# ####################################################
# QUESTION 35
# Write a program which can map() and filter() to make a list whose elements are square of
# even number in [1,2,3,4,5,6,7,8,9,10].


# ####################################################
# QUESTION 36
# Define a class named American which has a static method called printNationality.

# ####################################################
# QUESTION 37
# Define a class named American and its subclass NewYorker.


# ####################################################
# QUESTION 38
# Define a class named Circle which can be constructed by a radius. The Circle class
# has a method which can compute the area.


# ####################################################
# QUESTION 39
# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

# ####################################################
# QUESTION 40
# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

####################################################
# QUESTION 41
# Pleas raise a RuntimeError exception.

####################################################
# QUESTION 42
# Write a function to compute 5/0 and use try/except to catch the exceptions.


####################################################
# QUESTION 43
# Define a custom exception class which takes a string message as attribute.

####################################################
# QUESTION 44
# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be: john
# In case of input data being supplied to the question, it should be assumed to be a console input.

####################################################
# QUESTION 45
# Write a program which accepts a sequence of words separated by whitespace as input to
# print the words composed of digits only.
# Example: If the following words is given as input to the program: 2 cats and 3 dogs.
# Then, the output of the program should be: ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.


# ###########################################################
# QUESTION 46
# Listen to this story, a boy and his father, a programmer are playing with wooden blocks.
# They a're building a pyramid, their pyramid is a bit weird, as it's actually a pyramid-shaped
# wall -  it's flat. The pyramid is stacked according to one simple principle, each lower layer
# contains one block more than the layer above.
# Your task is to write a program which reads the number of blocks the builders have, and outputs
# the  height of the pyramid that can be built using these blocks.
# NOTE: The height is measured by the number of fully completed layers - if the builders doesn't
# have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.


# ###########################################################
# QUESTION 47
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5
# Then, the output of the program should be: 3.55


# ###########################################################
# QUESTION 48
# Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5 Then, the output of the program should be: 500


# ###########################################################
# QUESTION 49
# The Fibonacci Sequence is completed based on the following formula:
# f(n) = 0 if n=0
# f(n) = 1 if n=1
# f(n) = f(n-1) + f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# If n=7 is given as input to the program: Then, the output should be: 13


# ###########################################################
# QUESTION 50
# Given array {2,4,6,10}
# target say (16)
# Find the number of possible subsets that will sum up to the target.
# Assumptions: i. all elements inside the array is non-negative.
# ii. You cannot repeat number.
# iii. if 0 is given as the target, the possible subset is 1 i.e {}.


# ###########################################################
# QUESTION 51
# The Fibonacci Sequence is computed based on the following formula:
# 	f(n)=0 if n=0, f(n)=1 if n=1, f(n)=f(n-1)+f(n-2) if n>1
# 	Please write a program using list comprehension to print the Fibonacci
# 	Sequence in comma separated form with a given n input by console.
# 	Example: If the following n is given as input to the program:7
# 	Then, the output of the program should be: 0,1,1,2,3,5,8,13


# ###########################################################
# QUESTION 52
# Please write a program using generator to print the even numbers between 0 and n
# in comma separated form while n is input by console.
# 	Example: If the following n is given as input to the program: 10
# 	Then, the output of the program should be: 0,2,4,6,8,10


# ###########################################################
# QUESTION 53
# 	Please write a program using generator to print the numbers which can be divisible by 5 and 7
# 	between 0 and n in comma separated form while n is input by console.
#   Example: If the following n is given as input to the program: 100
#   Then, the output of the program should be: 0,35,70


# ##########################################################
# QUESTION 54
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.


# ##########################################################
# QUESTION 55
# Please write a program which accepts basic mathematics expression from console and print the evaluation result.
# Example: If the following string is given as input to the program: 35+3
# Then, the output of the program should be: 38


# ##########################################################
# QUESTION 56
# Please write a binary search function which searches an item in a sorted list. The function should return
# the index of element to be searched in the list.


# ##########################################################
# QUESTION 57
# Please generate a random float where the value is between 10 and 100 using Python math module.


# ##########################################################
# QUESTION 58
# Please write a program to output a random even number between 0 and 10 inclusive using random module
# and list comprehension.


# ##########################################################
# QUESTION 59
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.


# ##########################################################
# QUESTION 60
# Write a program to shuffle and print a list.


# ########################################################################
# QUESTION 61
# Have the function StringChallenge(str) read str which will contain two strings separated by a space.
# The first string will consist of the following sets of characters: +, *, $, and {N} which is optional.
# The plus (+) character represents a single alphabetic character, the ($) character represents a number between 1-9,
# and the asterisk (*) represents a sequence of the same character of length 3 unless it is followed by {N}
# which represents how many characters should appear in the sequence where N will be at least 1.
# Your goal is to determine if the second string exactly matches the pattern of the first string in the input.

# For example: if str is "++*{5} jtggggg" then the second string in this case does match the pattern,
# so your program should return the string true. If the second string does not match the pattern
# your program should return the string false.
# Examples
# Input: "+++++* abcdehhhhhh"
# Output: false
# Input: "$**+*{2} 9mmmrrrkbb"
# Output: true


# ##########################################################
