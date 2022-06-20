from time import strftime


class Account:
    def __init__(self,account_number,account_name,bank_name):
     self.account_number=account_number
     self.account_name=account_name
     self.balance=0
     self.bank_name=bank_name
     self.deposits=[]
     self.withdrawals=[]
     self.datetime=strftime("%d/%m/%y %I:%M%P")
     self.loan_balance=0
     
    def deposit(self,amount):
         if amount<=0:
             return "Deposit must be positive amount."
         else:
             self.balance+=amount
             self.deposits.append({'date':self.datetime,'amount':amount,'narration':'deposit'})
             return f"Hello your current balance is Ksh.{self.balance} and the withdrawal times are {self.deposits}"
     
    def withdraw(self,amount_minus):
        self.transaction=100
        if amount_minus+self.transaction <100:
            return "Withdraw should be greater than 100"
        elif amount_minus>self.balance:
            return f"Your balance is ksh{self.balance},you can't withdraw {amount_minus}"  
        else:
           self.balance-=amount_minus+self.transaction
           self.deposits.append({'date':self.datetime,'amount':amount_minus,'narration':'withdraw'})
           return f"Hello your balance ksh.{self.balance}" 
       
    def deposit_statements(self):
        for x in self.deposits: 
            print (x,end="\n")
            
    def withdrawal_statements(self):
        for y in self.withdrawals: 
            print (y,end="\n")        
    
    def current_balance(self):
        return self.balance        
    
    def full_statement(self):
          statement=self.deposits + self.withdrawals
          for x in statement:
              print (x)
              
    def borrow(self,amount):
       counts=0
       for i in self.deposits:
           counts+=i['amount']
       if len(self.deposits)<10:
            return "You cannot get a loan"
       elif amount<100:
           return f"You have borrowed {amount} loan had to be more than a hundred"
       elif amount>(counts//3):
           return f"{amount}.ksh is denied you cannot withdraw"
       elif self.balance==0:
           return "You have {self.balance}.ksh you cannot get a loan"
       else:
           self.loan_balance+=amount
           total=self.loan_balance+(amount*0.03)  
           self.balance+=amount
           return f"You can borrow {amount} your new  account balance is {self.balance}. Your loan balance is {self.loan_balance}. You will pay back {total}"
       
    def loan_repayment(self,repay):
       if repay < self.loan_balance:
           self.loan_balance-=repay
           return f"You have repaid {repay} your outstanding loan is {self.loan_balance}"
       elif repay==self.loan_balance:
           self.loan_balance-=repay
           return f"You have repaid {repay}.Your outstanding loan is {self.loan_balance}"  
       elif repay > self.loan_balance:
           overpayment=repay-self.loan_balance
           self.balance+=overpayment
           remainder=repay-overpayment
           self.loan_balance-=remainder
           return f"Your loan balance is {self.loan_balance}.Your account balance {self.balance}"  
       
       
    def transfer(self,amount,account_one):
        if  amount <=0:
            return "You cannot transfer {amount}" 
        elif amount> self.balance:
            
            return f"You have insuffient funds to transfer {amount} to {self.account_name} your balance is {self.balance}" 
        else:
            self.balance-=amount
            account_one.balance+=amount            
            return f"You have transfered {amount} to {account_one.account_name}" 

            
