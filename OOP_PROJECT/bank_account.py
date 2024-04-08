class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \n Balance = ksh {self.balance:.2f}") 
        
    def getBalance(self):
        print(f"\n '{self.name}' balance = ksh{self.balance:.2f}")    
    def deposits(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit complete")  
        self.getBalance()   
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,'{self.name}' you have insufficient funds, balance = ksh{self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n ###########\n\nBegining Transfer')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposits(amount)
            print('\nTransfer complete!\n\n#############')
        except BalanceException as error:
            print(f'\nTransfer interrupted.')  


class InterestAwardsAccount(BankAccount):
    def deposits(self, amount):
        self.balance = self.balance + (amount * 1.05)         
        print("\nDeposit complete")
        self.getBalance()  

class SavingsAccount(InterestAwardsAccount):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 30

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)  
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")                  
