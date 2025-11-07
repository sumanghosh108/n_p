import bank

print('               Account Details             ')
print()
premium=bank.Pre_Sav_Account('Sum',50000)
premium.add_interest_daily()
premium.deposite(200)
premium.withdraw(100)
premium.get_balance()

print()
print(50*'*')

savings = bank.Sav_Account('Suman', 1000)
savings.get_balance()
savings.deposite(500)
savings.withdraw(200)

print()
print(50*'*')

current = bank.Curr_Account("Sunny", 100000)
current.role()
current.get_balance()

print()
print(50*'*')

loan_acc = bank.Loan_Account("Rohan", 0)
loan_acc.get_loan(75000)
loan_acc.get_balance()

print()
print(50*'*')

fd_acc = bank.Fix_Account("Priya", 25000)
fd_acc.fixed_dep(10000)
fd_acc.get_balance()

print()
print(50*'*')

digitalcustomer = bank.Dig_Customer() 
digitalcustomer.role()
digitalcustomer.on_service()
digitalcustomer.mob_service()

print(50*'*')

