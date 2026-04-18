# Q23: BankAccount class

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    # Display method
    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


# Usage
acc = BankAccount("Abhi", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()