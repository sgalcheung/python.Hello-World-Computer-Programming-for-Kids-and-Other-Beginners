# -*- coding: cp936 -*-
class BankAccount:
    def __init__(self, acct_number, acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.balance = 0.0

    def displayBalance(self,):
        print "The account balance is:", self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print "You deposited", amount
        print "The new balance is:", self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print "You withdrew", amount
            print "The new balance is:",self.balance
        else:
            print "You tried to withdraw", amount
            print "The account balance is:", self.balance
            print "Withdrawal denied. Not enough funds."
#挣利息类，是BankAccount的子类
class InterestAccount(BankAccount):
    def addInterest(self, rate):
        interest = self.balance * rate
        print "adding interest to the account,",rate * 100,"percent"
        self.deposit(interest)

myAccount = InterestAccount(234567, "Warren Sande")
print "Account name", myAccount.acct_name
print "Account number", myAccount.acct_number
myAccount.displayBalance()
myAccount.deposit(34.52)
myAccount.addInterest(0.11)
