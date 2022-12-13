# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# SOLUTION
# Here is a simple solution to determine if a string is valid according to the rules you provided:

# 1. Create a stack to keep track of the open brackets in the string.
# 2. Iterate over the characters in the string, starting from the beginning.
# 3. If the current character is an open bracket (i.e., one of '(' , '{', or '[') then push it onto the stack.
# 4. If the current character is a closing bracket (i.e., one of ')', '}', or ']') then pop the top element from the stack. If the top element of the stack does not match the current character, then the string is not valid.
# 4. After iterating over the entire string, check if the stack is empty. If it is not empty, then the string is not valid.

def is_valid(s):
    stack = []

    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack:
                return False
            if c == ')' and stack[-1] != '(':
                return False
            if c == '}' and stack[-1] != '{':
                return False
            if c == ']' and stack[-1] != '[':
                return False
            stack.pop()

    return not stack

# This code first creates an empty stack, then iterates over the characters in the string. If the character is an open bracket, it is pushed onto the stack. If the character is a closing bracket, the top element is popped from the stack and checked to see if it matches the current character. If it does not match, then the string is not valid. Finally, the function returns True if the stack is empty, and False otherwise.
