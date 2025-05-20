random_word = "GLASS"
hangman = "HANGMAN"
length = len(hangman)

for i in range(length):
    guess = input("Enter your guess: ").upper()
    
    if guess == random_word:
        print(f"You got it right in {i + 1} tries!")
        break
    else:
        print( hangman[:i+1])
else:
    print(f"You didn't get it. Game over! The correct word was '{random_word}'.")


