from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
B1=BankAccount(500)
B1.withdraw(200)
B1.check_balance()
print("***************************************")

B2=BankAccount(200)
B2.deposit(1000)
B2.transfer(500,B1)
B2.check_balance()
print("*****************************************")

B1.check_balance()
B2.check_balance()
print("*****************************************")


S1=SavingsAccount(2000)
S1.deposit(500)
S1.check_balance()
print("**************************************")


C1=CurrentAccount(2000)
C1.deposit(500)
C1.withdraw(100)
C1.transfer(500,S1)
C1.check_balance()
S1.check_balance()