import random as rand
import os


colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'orange': '\033[93m',
    'blue': '\033[94m',
    'reset': '\033[0m'
}

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Amount deposited: {colors['green']}${amount:,.2f}{colors['reset']} new balance: {colors['green']}${self.balance:,.2f}{colors['reset']}'
    
    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            return f'Insufficient funds: overdraft fee of {colors['red']}$10{colors['reset']}.\nWithdrawing {colors['red']}${amount:,.2f}{colors['reset']}...\nNew balance: {colors['red']}-${abs(self.balance - 10):,.2f}{colors['reset']}'
        return f'Amount withdrawn: {colors['red']}${amount:,.2f}{colors['reset']} new balance: {colors['green']}${self.balance:,.2f}{colors['reset']}'
    
    def print_reciept(self):
        return (
            f"Name: {colors['blue']}{self.name}{colors['reset']}\n"
            f"Account Number: {colors['blue']}{self.account_number}{colors['reset']}\n"
            f"Balance: {self.get_balance()}"
        )
    
    def get_balance(self):
        if self.balance < 0:
            return f"{colors['blue']}{self.name}{colors['reset']} has a current balance of: {colors['red']}-${abs(self.balance):,.2f}{colors['reset']}"
        return f"{colors['blue']}{self.name}{colors['reset']} has a current balance of: {colors['green']}${abs(self.balance):,.2f}{colors['reset']}"

    # 1.2% annaul interest rate
    def add_interest(self, years):
        if self.balance < 0:
            return f"You will have {colors['red']}-${self.balance * (1+ 0.012 * years):,.2f} after {years} years"
        return f"You will have {colors['green']}${self.balance * (1+ 0.012 * years):,.2f} after {years} years"
    
    # 1% monthly interest rate
    def add_compounded_interest(self,years):
        return f"Your compounded interest will be {colors['orange']}${self.balance * (1+ (0.01/12)) ** (12 * years):,.2f}{colors['reset']} after {colors['orange']}{years} years{colors['reset']}"
    

def create_account(name, account_number, balance):
    account = BankAccount(name, account_number, balance)
    return account

accounts = []

while True:
    print("Welcome to the bank_account. Interact with your own account(s)")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Print Reciept")
    print("5. Get Balance")
    print("6. Add Interest")
    print("7. Add Compounded Interest")
    print("8. View Accounts")
    print("9. Enter Bank?")
    print('C. Clear Terminal')
    choice = input("What would you like to do? ")

    if choice == '1':
        name = input("Enter your name: ")
        account_number = rand.randint(10000000, 99999999)
        balance = float(input("Enter your initial balance: "))
        account = create_account(name, account_number, balance)
        accounts.append(account)
        print(f"Account created for {account.name} with account number: {account.account_number} and balance: {account.balance}")
    elif choice == '2':
        amount = float(input("Enter the amount you would like to deposit: "))
        print(account.deposit(amount))
    elif choice == '3':
        amount = float(input("Enter the amount you would like to withdraw: "))
        print(account.withdraw(amount))
    elif choice == '4':
        print(account.print_reciept())
    elif choice == '5':
        print(account.get_balance())
    elif choice == '6':
        years = int(input("Enter the number of years: "))
        print(account.add_interest(years))
    elif choice == '7':
        years = int(input("Enter the number of years: "))
        print(account.add_compounded_interest(years))
    elif choice == '8':
        accounts_dict_list = [(account.name, account.account_number) for account in accounts]
        print(f"Available accounts are: {colors['orange']}{accounts_dict_list}{colors['reset']}")
    elif choice == '9':
        break
    elif choice == 'c':
        os.system('clear')
    else:
        print("Invalid choice")
    print("\n\n")
