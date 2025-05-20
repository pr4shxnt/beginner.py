random_word = "GLASS"
hangman = "HANGMAN"
length = len(hangman)

print("for loop")

for i in range(length):
    guess = input("Enter your guess: ").upper()
    
    if guess == random_word:
        print(f"You got it right in {i + 1} tries!")
        break
    else:
        print( hangman[:i+1])
else:
    print(f"You didn't get it. Game over! The correct word was '{random_word}'.")



# using while loop now

print("While loop")

i = 0

while length:
    guess = input("Enter your guess: ").upper()

    if guess == random_word:
         print(f"You got it right in {i + 1} tries!")
         break
    elif guess != random_word:
        print( hangman[:i+1])
        i += 1
    else:
        print(f"You didn't get it. Game over! The correct word was '{random_word}'.")
        break
