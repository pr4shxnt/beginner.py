#3.1

num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter second number: '))

op = input("Select an operator * for multiplication, - for subtraction, + for addition, / for division: ")

if op == '+':
    print(num_1 + num_2)
elif op == '-':
    print(num_1 -num_2)
elif op == '*':
    print(num_1 * num_2)
elif op == '/':
    print(num_1 / num_2)
else:
    print('An error occured')