# QUESTION 62
# Build a tool that takes a string of text as input and encrypts it using a cipher, such as the Caesar cipher
# Cipher should not be hacked using brute force (consider security of your cipher)

while True:
    # prompt the user to enter the text message and save in the variable 'text'
    text = input("Enter message here: ")
    # create a variable named 'cipher' to store the text that will be encrypted
    cipher = ''
    # take the characters in the text one-by-one and check for the following if conditions
    for char in text:
        if char == ' ' or char.isdigit():
            # ignore spaces and digits characters in the message text
            continue
        # check if the character is a capital letter
        if char.isalpha():
            # convert the character to ASCII code and add 5 to it to shift the character 5 places to the right
            code = ord(char) + 5
        # check if the addition of 5 to the ASCII code result in an integer greater than 90(i.e Z)
        if ord(char) > ord('U'):
            # deduct 21 from the ASCII code of such character so that it can start from A
            code = ord(char) - 21
        # check if the character is a lower case letter
        if char.islower():
            # convert the character to ASCII code and deduct 3 from it to shift the character 3 places to the left
            code = ord(char) - 3
        # check if the deduction of 3 from the ASCII code result in an integer lesser than 97(i.e a)
        if ord(char) < ord('d'):
            # add 21 to the ASCII code of such character so that it can start from z
            code = ord(char) + 23
        # convert the ASCII code back to alphabet and store it in the cipher variable
        cipher += chr(code)
    # output the encrypted text message
    print(cipher)
