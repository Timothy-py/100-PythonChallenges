import random
# QUESTION 59
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.


five_rands = [random.randint(100, 201) for i in range(5)]
print(five_rands)
# OR
five_rands = random.sample(range(100, 200), 5)
