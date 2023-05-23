# A program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
prompt = input('Enter text strings here: ')
parsed_text = [word for word in sorted(prompt.split(' '))]
parsed_word = []
for word in parsed_text:
    if word not in parsed_word:
        parsed_word.append(word)

print(parsed_word)
''' or use set() on parsed_text instead of the 'for' code suit '''
