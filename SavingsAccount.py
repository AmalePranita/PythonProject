from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self,initial_amount):
        super(). __init__(initial_amount)

    def deposit(self,amount):
        interest=amount * 0.03
        total_amount=amount + interest
        self.balance= self.balance+total_amount
        print("Deposited amount with interest new balance is :",self.balance)