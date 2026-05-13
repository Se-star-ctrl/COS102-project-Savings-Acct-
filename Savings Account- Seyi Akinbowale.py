
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdrawal successful. New balance:", self.balance)

class SavingsAccount(Account):
    def __init__(self, owner, balance):
        # Link to the parent class
        Account.__init__(self, owner, balance)
        
        # 1) Add an attribute called withdraw limit of $100
        self.withdraw_limit = 100

    # 2) Override the withdrawal behavior
    def withdraw(self, amount):
        # The withdrawal amount should not be more than the withdrawal limit
        if amount <= self.withdraw_limit:
            Account.withdraw(self, amount)
        else:
            print("Error: You cannot withdraw more than $100")

# Test the code
savings = SavingsAccount("Alice", 5000)
savings.withdraw(27.8)