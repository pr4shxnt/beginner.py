#importing necessary modules ( math )
from math import sqrt

# A, B, C, root1 and root2 are variable of floating data types
# A, B and C are input values

A = float(input('Enter a number: '))
B = float(input('Enter a number: '))
C = float(input('Enter a number: '))

# Calculating d for quadratic equation

d = sqrt(B*B-4*A*C)
print(f'The value of d is {d}')

# Calculating root1
root1 = (-B+d)/(2*A)
print(f'Value for Root 1 is {root1}')


#calculating root2
root2 = (-B-d)/(2*A)
print(f'Value for Root 2 is {root2}')


# Test case 1 with A=2, B=0 and C= -4
# Root1 = 2.0
# Root2 = -2.0

# Test case 2 with A=1, B=5 and C= -36
# Root1 = 4.0
# Root2 = -9.0

# Testing with A=2, B=7.5 and C= 6
# Root1 = -1.1569296691827464
# Root2 = -2.5930703308172536

# A = 0, B = 3.5, C = 8 | this test case fails and generates an error (why?)
    # Because A is in denominator and which makes the value of root1 and root2 undefined and a ZeroDivisionError in python