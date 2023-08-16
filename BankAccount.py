class BankAccount:
    balance=None
    initial_amount=None
    amount=None

    def __init__(self,initial_amount):
        self.balance=initial_amount
        print("Account created with balance is :",initial_amount)

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposited Amount to your account is:",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("Withdraw amount from your account is:",amount)
        else:
            print("Insufficient amount")

    def check_balance(self):
        print("Current balance is:",self.balance)

    def transfer(self, amount, account):
        if amount <= self.balance:
           self.balance = self.balance-amount
           account.deposit(amount)
           print("Transfer amount to another account:",amount)
        else:
            print("Insufficient balance for transfer")

