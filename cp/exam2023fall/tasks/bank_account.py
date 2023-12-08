"""Task 7: Bank account."""

class BankAccount():
    """A class that represents a bank account."""
    
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Withdraw failed: Insufficient funds')
        else:
            self.balance = self.balance - amount
    
    def print_balance(self):
        print(f'Balance: {self.balance} DKK')

"""Task 10: Overdraft account."""

class OverdraftAccount(BankAccount):
    """A class that represents a bank account allowing overdraft."""
    
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Withdraw failed: Overdraft limit exceeded")
        else:
            self.balance = self.balance - amount

if __name__ == '__main__':
    # Task 7
    #my_account = BankAccount(1000)
    #my_account.print_balance()
    #my_account.deposit(500)
    #my_account.print_balance()
    #my_account.withdraw(200)
    #my_account.print_balance()
    #my_account.withdraw(2000)
    #my_account.print_balance()

    # Task 10
    my_account = OverdraftAccount(0, 500)
    my_account.print_balance()
    my_account.deposit(1000)
    my_account.print_balance()
    my_account.withdraw(1300)
    my_account.print_balance()
    my_account.withdraw(500)
    my_account.print_balance()   