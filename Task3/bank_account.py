# bank_account.py

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance   # protected variable

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}. Remaining Balance: {self._balance}")

    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self._balance}"


# Child class (Inheritance)
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Not enough balance in savings")
        else:
            self._balance -= amount
            print(f"Savings Withdrawn: {amount}")


# Testing
if __name__ == "__main__":
    acc = BankAccount("Ali", 1000)
    acc.deposit(500)
    acc.withdraw(300)
    print(acc)

    sav = SavingsAccount("Sara", 2000)
    sav.withdraw(500)
