from bank_account import BankAccount, accounts
import os
import random as rand
# imported the class from the other file because i didnt want to recode it

colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'orange': '\033[93m',
    'blue': '\033[94m',
    'reset': '\033[0m'
}
class Bank:
    def __init__(self):
        self.list_of_accounts = accounts

    def create_account(self, name, account_number, balance):
        # Check if the account number already exists
        for account in self.list_of_accounts:
            if account.account_number == account_number:
                print(f"{colors['red']}Account number {account_number} already exists.{colors['reset']}")
                return None  # Return None if the account already exists

        # If the account number is unique, create and append the new account
        account = BankAccount(name, account_number, balance)
        self.list_of_accounts.append(account)
        return account
    
    def transfer(self, account_one_number, account_two_number, amount):
        for account in self.list_of_accounts:
            if account_one_number == account.account_number:
                recipient = account.balance
                recipient += amount
            if account_two_number == account.account_number:
                transferer = account.balance
                transferer -= amount
                return recipient, transferer


bank = Bank()
while True:
    print("Welcome to the Bank. You can transfer money between accounts")
    print("1. View Accounts")
    print("2. Transfer Money")
    print("3. View Balances")
    print("4. Create Account")
    print("5. Exit")
    print('C. Clear Terminal')
    choice = input("What would you like to do? ")

    if choice == '1':
        accounts_dict_list = [(account.name, account.account_number) for account in accounts]
        print(f"Available accounts are: {colors['orange']}{accounts_dict_list}{colors['reset']}")
    elif choice == '2':
        account1 = int(input("Enter the account number you want to transfer from: "))
        account2 = int(input("Enter the account number you want to transfer to: "))
        transaction = bank.transfer(account1, account2, float(input("Enter the amount you want to transfer: ")))

        recipient_balance = transaction[0]
        transferer_balance = transaction[1]
        print(f"Transfer Successful!")
        print(f"Recipient's new balance: ${recipient_balance:.2f}")
        print(f"Transferer's new balance: ${transferer_balance:.2f}")
    elif choice == '3':
        accounts_balances_list = [(account.name, account.balance) for account in accounts]
        print(f"Account Balances are: {colors['orange']}{accounts_balances_list}{colors['reset']}")
    elif choice == '4':
        bank_name = input("Enter your name: ")
        bank_account_number = rand.randint(10000000, 99999999)
        bank_balance = float(input("Enter your initial balance: "))

        account = bank.create_account(bank_name, bank_account_number, bank_balance)
        accounts.append(account)

        new_account = accounts[-1]
        print(f"Account created for {new_account.name} with account number: {new_account.account_number} and balance: {new_account.balance:.2f}")
    elif choice == '5':
        break
    elif choice == 'c':
        os.system('clear')
    else:
        print("Invalid choice")
    print("\n\n")
