class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def checking(self):
        pass

    # 1.2% annaul interest rate
    def savings(self, balance, years):
        return f"You will have ${balance * 1.012 * years:,.2f} after {years} years"
    
    # 1% monthly interest rate
    def savings2(self, balance, years):
        return f"You will have ${balance * (1+ (0.01/12)) ** (12 * years):,.2f} after {years} years"