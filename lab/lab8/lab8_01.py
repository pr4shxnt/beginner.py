from L8_library import BankAccount

def main():
    accounts = [BankAccount(101), BankAccount(102)]

    for acc in accounts:
        acc.deposit(100)
        print(f"Account {acc.get_account()}: Balance {acc.get_balance()}")

    print("Withdrawing 40 ")
    for acc in accounts:
        acc.withdraw(40)

    for acc in accounts:
        print(f"Account {acc.get_account()}: Balance {acc.get_balance()}")

    print("Depositing 20 ")
    for acc in accounts:
        acc.deposit(20)

    for acc in accounts:
        print(f"Account {acc.get_account()}: Balance {acc.get_balance()}")

    print("Transferring 20 from Account 102 to Account 101 ")
    accounts[1].transfer(20, accounts[0])

    for acc in accounts:
        print(f"Account {acc.get_account()}: Balance {acc.get_balance()}")

if __name__ == "__main__":
    main()
