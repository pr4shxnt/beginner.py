import random

a = random.randint(1, 1000)
# print(a)
i = 0
while True:
  i = i+1
  b = int(input("Guess the number: "))
  if (a == b):
    print("You guessed it right!")
    break
  elif (b > a):
    print("Your guess is too high!")
  elif (b < a):
    print("Your guess is too low!")
print(i)