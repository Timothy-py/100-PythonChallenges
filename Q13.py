# A program that accepts a sentence and calculate the number of letters and digits.

sentence = input('Enter a sentence containing letters and digits here : ')
letters, digits = 0, 0
for character in sentence:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1
print('Letters = {}'.format(letters))
print('Digits = %s' % digits)
