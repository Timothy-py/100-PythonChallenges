word_str = ''
while True:
    prompt = input('Enter sentences here : ')
    if prompt != '':
        word_str += prompt
    else:
        break
    print(word_str.upper())
