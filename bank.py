class Account:
    def __init__(self,account_number,account_name,bank_name):
     self.account_number=account_number
     self.account_name=account_name
     self.balance=0
     self.bank_name=bank_name
     self.deposits=[]
     self.withdrawals=[]
     
    def deposit(self,amount):
         if amount<=0:
             return "Deposit must be positive amount."
         else:
             self.balance+=amount
             self.deposits.append(amount)
             return f"Hello your current balance is Ksh.{self.balance} and the withdrawal times are {self.deposits}"
     
    def withdraw(self,amount_minus):
        self.transaction=100
        if amount_minus<=0:
            return "Withdraw should be greater than 0"
        elif amount_minus>self.balance:
            return f"Your balance is ksh{self.balance},you can't withdraw {amount_minus}"  
        else:
           self.balance-=amount_minus+self.transaction
           self.deposits.append(amount_minus)
           return f"Hello your balance ksh.{self.balance}" 
       
    def deposit_statements(self):
        for x in self.deposits: 
            print (x,end="\n")
            
    def withdrawal_statements(self):
        for y in self.withdrawals: 
            print (y,end="\n")        
    
    def current_balance(self):
        return self.balance          
    