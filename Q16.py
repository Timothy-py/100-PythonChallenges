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

print('INSTRUCTION: Enter "=" to output ')
withdrawal, deposit = [], []
while True:
    transaction = input('Enter your transaction here : ')

    if transaction == '=':
        break
    else:
        if transaction.startswith('D' or 'd'):
            trans_split = transaction.split(' ')
            deposit.append(int(trans_split[1]))
        elif transaction.startswith('W' or 'w'):
            trans_split = transaction.split(' ')
            withdrawal.append(int(trans_split[1]))
        else:
            print('Ooops! You\'ve entered an invalid transaction')

sum_W, sum_D = sum(withdrawal), sum(deposit)
Output = sum_D - sum_W
print('Output = %s' % Output)
