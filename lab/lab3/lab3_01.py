#3.1 prime number check

# importing necessary modules
from math import sqrt

n = int(input('Enter a number greater than 2: '))

isPrime = True
div = []

for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        isPrime = False
        div.append(i)

if isPrime:
    print('Prime number')
else:
    print(div)
