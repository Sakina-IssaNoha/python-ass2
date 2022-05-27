class Account:
    def __init__(self,account_number,account_name,balance,bank_name):
     self.account_number=account_number
     self.account_name=account_name
     self.balance=balance
     self.bank_name=bank_name
     
    def deposit(self,amount):
         self.balance+=amount
         return f"Hello your current balance is Ksh.{self.balance}"
     
    def withdraw(self,amount_minus):
        self.balance-=amount_minus
        return f"Hello your balance ksh.{self.balance} " 
    