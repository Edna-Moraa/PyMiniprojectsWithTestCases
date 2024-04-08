from bank_account import *

Edna = BankAccount(2000.78, "Edna")
Moraa = BankAccount(50000, "Moraa")

Edna.getBalance()
Moraa.getBalance()
Edna.deposits(500)

Moraa.withdraw(1000)
# Edna.transfer(30000, Moraa)
Moraa.transfer(10000, Edna)
Ed = InterestAwardsAccount(900, "Ed")
Ed.getBalance()
Ed.deposits(100)
Ed.transfer(100, Edna)

Ad = SavingsAccount(200, "Ad")
Ad.getBalance()
Ad.deposits(20000)
Ad.transfer(500, Ed)

