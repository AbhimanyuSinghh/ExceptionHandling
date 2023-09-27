class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount<0:
            raise Exception('amount cannot be negative')
        if self.balance<self.amount:
            raise Exception('amount bshould be lesser than your account balance = ', self.balance)
        
        self.balance -= self.amount
        
        
    
obj = Bank(10000)
for i in range(3):
    withdrawlAmount = int(input('enter the amount u wish to withdraw = '))
    try:
        obj.withdraw(withdrawlAmount)
    except Exception as e:
        print(e)
    else:
        print('the remaining balance in your account is ',obj.balance)
    finally:
        print('bla..bla..bla..')
        