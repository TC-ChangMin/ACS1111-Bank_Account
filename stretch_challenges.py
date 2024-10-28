class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Amount deposited: ${amount:,.2f} new balance: ${self.balance:,.2f}'
    
    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            return f'Insufficient funds: overdraft fee of $10.\nWithdrawing ${amount:,.2f}...\nNew balance: -${abs(self.balance - 10):,.2f}'
        return f'Amount withdrawn: ${amount:,.2f} new balance: ${self.balance:,.2f}'
    
    def statement(self, number):
        if number == self.account_number:
            return f"Account Number: {self.account_number}\nAccount Holder: {self.name}\nCurrent Balance: ${self.balance:,.2f}"
        return "Invalid account number"
    
    def get_balance(self):
        return f'Current balance: ${self.balance:,.2f}'

    # 1.2% annaul interest rate
    def add_interest(self, years):
        return f"You will have ${self.balance * (1+ 0.012 * years):,.2f} after {years} years"
    
    # 1% monthly interest rate
    def add_compounded_interest(self,years):
        return f"Your compounded interest will be ${self.balance * (1+ (0.01/12)) ** (12 * years):,.2f} after {years} years"
    

def create_account(name, account_number, balance):
    account = BankAccount(name, account_number, balance)
    return account


'''
acc1 = create_account('Mitchell', "03141592", 1000)
print(acc1)
print(acc1.statement("03141592"))
print(acc1.add_interest(5))
print(acc1.withdraw(50))
print(acc1.deposit(500))

Mitchell = BankAccount('Mitchell', "03141592", 1000)
Dani = BankAccount('Daniel', "987654321", 5000)
Braus = BankAccount('Braus', "123456789", 1000)

bank = [Mitchell, Dani, Braus]


# the math here is correct. i dont know why the one in bank_account is wrong
for account in bank:
    print(account.add_interest(5))
    print(account.add_compounded_interest(5))

# print(Mitchell.add_interest(4))
'''