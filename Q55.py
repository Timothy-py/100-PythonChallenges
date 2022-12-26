# Please write a program which accepts basic mathematics expression from console and print the evaluation result.
# Example: If the following string is given as input to the program: 35+3
# Then, the output of the program should be: 38

def evaluator(n=input("Enter expression to evaluate here : ")):
    print(eval(n))


evaluator()
