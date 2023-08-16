from BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self,initial_amount):
        super().__init__(initial_amount)

    def withdraw(self,amount):
        withdraw_charge=200
        total_amount=amount+withdraw_charge
        if self.balance>=total_amount:
           self.balance=self.balance-total_amount
           print("Withdrawal amount with charge new balance is:",self.balance)
        else:
            print("Insufficient amount for withdrawal")



