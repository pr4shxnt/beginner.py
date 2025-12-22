#3.2 Menu driven program for making transactions of a bank account.

name= input('Enter your name: ')
balance = 1000

while True:
    print('Enter a query')
    print('Making a deposit: 1')
    print('Making a withdrawal: 2')
    print('Fetch balance: 3')
    print('Quit: q or quit')
    query = input('Enter your query: ').lower()

    if query == '1':
        add = float(input('Enter an amount to deposit: '))
        balance += add
        print(f'Dear {name}, your new balance is {balance}')
    elif query == '2':
        sub = float(input('Enter an amount to withdraw: '))
        if balance - sub >= 0:
            print('Insufficient balance')
        else:
            balance -= sub 
            print(f'Dear {name}, your new balance is {balance}')
    elif query == '3':
        print(f'Dear {name}, your balance is {balance}')
    elif query == 'q' or query == 'quit':
        print(f'Quiting menu')
        break
