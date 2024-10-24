from stretch_challenges import BankAccount 

class Bank:
    def __init__(self, list_of_accounts):
        self.list_of_accounts = list_of_accounts

    def create_account(self, name, account_number, balance):
        account = BankAccount(name, account_number, balance)
        self.list_of_accounts.append(account)
        return self.list_of_accounts
    
    def transfer(self, account_one_number, account_two_number, amount):
        for account in self.list_of_accounts:
            if account_one_number == account.account_number:
                recipient = account.balance
                recipient += amount
            if account_two_number == account.account_number:
                transferer = account.balance
                transferer -= amount
                return f"Transfer successful. account_one has ${recipient:,.2f} and account_two has ${transferer:,.2f}"

Mitchell = BankAccount('Mitchell', "03141592", 1000)
Dani = BankAccount('Daniel', "987654321", 5000)
Braus = BankAccount('Braus', "123456789", 1000)

my_list = [Mitchell, Dani, Braus]

test = Bank(my_list)

test.create_account('person', "03141592", 1000)

# for account in test.list_of_accounts:
#     print(account.name)
#     print(account.account_number)

print(test.transfer("03141592", "987654321", 500))