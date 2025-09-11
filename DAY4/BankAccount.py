class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Deposited amount balance is ",self.__balance)
    def withdraw(self,amount):
        self.__balance-=amount
        print("Withdraw amount balance is ",self.__balance)
    def get_balance(self):
        print("Amount is ",self.__balance)
bank=BankAccount()
bank.deposit(5000)
bank.withdraw(2000)
bank.get_balance()
