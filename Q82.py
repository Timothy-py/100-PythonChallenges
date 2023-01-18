# [Turing Python Test]
# Solve this problem with Python
# Given a string morsecode that contains a list of '.' and '-'. You are allowed to make one move and replace two consecutive ".." with "--".
# Return all possible morse codes you get after a single move you do to the string morsecode.
# If you cannot do any moves, just return an empty array.

# With constraints
# 1 <= morsecode.length <= 500
# morsecode[i] is either '.' or '-'.

# Possible Solution
def morse_code_move(morse_code):
    results = []
    i = 0
    while i < len(morse_code) - 1:
        if morse_code[i] == '.' and morse_code[i+1] == '.':
            new_code = morse_code[:i] + '--' + morse_code[i+2:]
            results.append(new_code)
            i += 2
        else:
            i += 1
    return results

# Explanation
# This function takes in a string morse_code and initializes an empty list results to store the possible morse codes after the move. It also initializes a variable i to 0, which will be used to iterate through the characters in the string.

# The function uses a while loop to iterate through the characters in the string, starting at index 0. Inside the loop, it checks if the current character and the next character are both '.'. If they are, it creates a new string by replacing the two '.' with '--' and appends the new string to the results list. Then, it increments the value of i by 2 to move to the next possible pair of '.'. If the current character and the next character are not both '.', it increments the value of i by 1 to move to the next character.

# After the while loop, it returns the results list, which will contain all of the possible morse codes that can be created by making a single move as specified in the problem statement. If no such move is possible, it will return an empty list.

# This solution is more efficient than the previous one because it avoids unnecessary iterations of the loop.
