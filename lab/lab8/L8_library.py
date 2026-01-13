class BankAccount:
    def __init__(self, acc_number: int, balance: float = 0.0):
        self.__acc_number = acc_number
        self.__balance = balance

    def get_account(self) -> int:
        return self.__acc_number

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, amount: float, acc: 'BankAccount') -> None:
        if 0 < amount <= self.__balance:
            self.withdraw(amount)
            acc.deposit(amount)
        else:
            print("Transfer failed: Insufficient funds or invalid amount.")
