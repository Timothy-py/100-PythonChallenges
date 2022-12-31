import re
# QUESTION 45
# Write a program which accepts a sequence of words separated by whitespace as input to
# print the words composed of digits only.
# Example: If the following words is given as input to the program: 2 cats and 3 dogs.
# Then, the output of the program should be: ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

words = input("Enter your words here : ")

digits = []

for i in words:
    if i.isdigit():
        digits.append(i)

if digits:
    print(digits)
else:
    print("No digit found!")

# ****************OR*******************

words = input("Enter your words here : ")

num_regex = re.compile(pattern=r"[0-9]")
match_obj = num_regex.findall(words)
print(match_obj)
