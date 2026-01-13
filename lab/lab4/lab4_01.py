#3.1

num1 = int(input('Enter a number: '))
num2 = int(input('Enter second number: '))

op = input("Select an operator: multiplication, subtraction, addition, division: ")

if op == 'addition':
    print(num1 + num2)
elif op == 'substraction':
    print(num1 -num2)
elif op == 'multiplication':
    print(num1 * num2)
elif op == 'division':
    print(num1 / num2)
else:
    print('An error occured')