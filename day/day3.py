# Write a program that accepts integer inputs from a user as long as the word stop is not input. Compute and print the minimum of these integers.

numbers = []

while True:
    inp = input("Enter an integer (or 'stop' to finish): ")
    if inp.lower() == 'stop':
        break
    try:
        num = int(inp)
    except ValueError:
        print("That's not a valid integer. Try again.")
        continue
    numbers.append(num)

if numbers:
    print("Minimum:", min(numbers))
else:
    print("No integers were entered.")


# 3.2 Write a menu-driven program that allows the user to make transactions to a bank account. The
# options of the menu are:
# • Option 1: Make a Deposit
# • Option 2: Make a Withdrawal
# • Option 3: Obtain a Balance
# • Option 4: Quit
# a) First the program asks the user for his/her name.
# b) The user can make many interactions as they wish until they decide to quit by pressing Q or
# q from the keyboard. (Hint: while loop)
# c) Assume that the account initially has a balance of £1000.
# d) If the user tries to withdraw an amount more than the total balance, the program should print 'It is
# not possible to withdraw beyond the account balance
# e) Ask the user to make a selection from the menu options.
# f) Make sure the user enters a proper menu number.
# g) If option one is selected, allow the addition of funds to the balance.
# h) If option two is selected, subtract the amount from the balance.
# i) If option three is selected, display the total balance of the checking account

    name = input("Enter your name: ")
    balance = 1000

    while True:
        print("\n--- Menu ---")
        print("1. Make a Deposit")
        print("2. Make a Withdrawal")
        print("3. Obtain a Balance")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4) or Q to quit: ").strip()
        
        if choice.lower() == 'q':
            print(f"Thank you for banking with us, {name}!")
            break
        
        if choice == '1':
            amount = float(input("Enter deposit amount: £"))
            balance += amount
            print(f"Deposit successful. New balance: £{balance}")
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: £"))
            if amount > balance:
                print("It is not possible to withdraw beyond the account balance")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: £{balance}")
        elif choice == '3':
            print(f"Current balance: £{balance}")
        elif choice == '4':
            print(f"Thank you for banking with us, {name}!")
            break
        else:
            print("Invalid choice. Please enter 1-4 or Q.")
