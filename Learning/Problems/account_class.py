class Account:
    def __init__(self, bank, balance, acc_no):
        self.acc_no = acc_no
        self.bank = bank
        self.balance = balance
    
    #debit method

    def debit(self, amt):
        if self.balance - amt >= 0:
            self.balance -= amt
            print(f"Rs {amt} was debited to your bank account with account number {self.acc_no}. Your new balance is {self.balance}. Thank you, {self.bank}")
        else:
            print(f"insufficient balance. Your balance of today in your account no. {self.acc_no} of {self.bank} is {self.balance}")
    
    #credit method

    def credit(self, amt):
        self.balance += amt
        print(f"Rs {amt} was credited to your bank account with account number {self.acc_no}. Your new balance is{self.balance}. Thank you, {self.bank}")

    #fetching balance

    def get_balance(self):
        print(f"Your balance of today in your account no. {self.acc_no} of {self.bank} is {self.balance}")

acc1 = Account("NIMB bank", 10000, 2345)
acc1.debit(2500)


#this is solution of the problem for banking account.
