class AccountHolder:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def get_balance(self):
        print(f'Account holder name : {self.name}, balance : {self.balance}')


class Sav_Account(AccountHolder):
    def deposite(self,amt):
        self.balance+=amt
        print(f'{self.name}, balance after deposite : {self.balance}')
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f'{self.name}, amount after withdraw : {self.balance}')
        else:
            print(f'current amount : {self.balance}')


class Pre_Sav_Account(Sav_Account):
    def add_interest_daily(self):
        interest=self.balance*0.01
        self.balance+=interest
        print(f'premium saving account amount : {self.balance}')


class Curr_Account(AccountHolder):
    def role(self):
        print('Current Account Holder')


class Loan_Account(AccountHolder):
    def get_loan(self,amt):
        self.balance+=amt
        print(f'Loan amount : {amt}, total balance : {self.balance}')


class Fix_Account(AccountHolder):
    def fixed_dep(self,amt):
        self.balance+=amt
        print(f'fixed deposite amount : {amt}, total amount : {self.balance}')



