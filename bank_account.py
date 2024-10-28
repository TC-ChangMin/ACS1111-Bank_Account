class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
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
    
    def get_balance(self):
        return f'Current balance: ${self.balance:,.2f}'
    
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        annual = self.balance * (1+0.00083) * 12
        return f'Interest added after one month: ${interest:,.2f}\nnew balance: ${self.balance:,.2f}\nEstimated annual balance: ${annual:,.2f}'
    

Mitchell = BankAccount('Mitchell', "03141592", 1000)
Dani = BankAccount('Dani', "987654321", 5000)
Braus = BankAccount('Braus', "123456789", 1000)

print(Mitchell.deposit(400000))
# print(Mitchell.get_balance())
print(Mitchell.add_interest())
# print(Mitchell.withdraw(150))

# print(Dani.withdraw(6000))

# math for interest is a bit off, ill fix it later