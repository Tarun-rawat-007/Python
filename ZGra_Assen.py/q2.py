class BankAccount:
    total_balance = 0  

    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
        BankAccount.total_balance += balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            BankAccount.total_balance -= amount

    def transfer(self, amount, other_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount


a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 500)

a1.deposit(200)       
a2.withdraw(100)     
a1.transfer(300, a2)  

print("a1's balance: ",a1.balance) 
print("a2's balance: ",a2.balance)  
print("Total balance across all accounts: ",BankAccount.total_balance)  

