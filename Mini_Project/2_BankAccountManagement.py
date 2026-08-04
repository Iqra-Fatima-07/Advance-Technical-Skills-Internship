# 2. Bank Account Management System
# Suggested Classes: Bank, Account, SavingsAccount, CurrentAccount
# Features: Create account, deposit, withdraw, transfer, balance
# OOP Concepts: Encapsulation, Inheritance, Polymorphism



class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name

        # Encapsulation
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.__balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False

        if amount > self.__balance:
            print("Insufficient balance.")
            return False

        self.__balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        return True

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            print("Transfer successful.")


# Inheritance
class SavingsAccount(Account):

    def withdraw(self, amount):
        # Savings account must maintain minimum ₹500
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False

        if amount > self.get_balance() - 500:
            print("Cannot withdraw. Minimum balance of ₹500 required.")
            return False

        # Polymorphism
        return super().withdraw(amount)


class CurrentAccount(Account):

    def withdraw(self, amount):
        # Current account allows overdraft up to ₹1000
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False

        if amount > self.get_balance() + 1000:
            print("Overdraft limit exceeded.")
            return False

        # Directly handle balance change through parent method
        if amount <= self.get_balance():
            return super().withdraw(amount)

        overdraft = amount - self.get_balance()

        # Withdraw existing balance
        if self.get_balance() > 0:
            super().withdraw(self.get_balance())

        print(f"₹{overdraft} overdraft used.")
        return True


class Bank:
    def __init__(self, name):
        self.name = name

        # Encapsulation
        self.__accounts = {}

    def create_account(self, account):
        self.__accounts[account.account_number] = account
        print(
            f"Account {account.account_number} "
            f"created for {account.holder_name}."
        )

    def get_account(self, account_number):
        return self.__accounts.get(account_number)

    def show_balance(self, account_number):
        account = self.get_account(account_number)

        if account:
            print(
                f"{account.holder_name}'s balance: "
                f"₹{account.get_balance()}"
            )
        else:
            print("Account not found.")


# -------------------------
# Example Usage
# -------------------------

bank = Bank("BITM Bank")

# Create accounts
savings = SavingsAccount(
    "S101",
    "Iqra",
    10000
)

current = CurrentAccount(
    "C101",
    "Kaunain",
    5000
)

# Add accounts to bank
bank.create_account(savings)
bank.create_account(current)

print("\n--- Deposit ---")
savings.deposit(2000)

print("\n--- Withdraw ---")
savings.withdraw(3000)

print("\n--- Transfer ---")
savings.transfer(current, 2000)

print("\n--- Balances ---")
bank.show_balance("S101")
bank.show_balance("C101")

print("\n--- Polymorphism ---")

accounts = [savings, current]

for account in accounts:
    account.withdraw(1000)