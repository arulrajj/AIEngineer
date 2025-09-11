
class BankAccount:

    def __init__(self, account_holder, account_type, balance=0.0):
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def display_balance(self):
        print(f"Account Holder Name: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount

if __name__ == "__main__":
    account1 = BankAccount("Leo", "Savings", 1000.53)
    account2 = BankAccount("Vijay", "Current", 5000)

    print(f"Account details of account1 before deposit operation:")
    account1.display_balance()
    account1.deposit(100.50)
    print(f"Account details of account1 after deposit operation:")
    account1.display_balance()

    print(f"Account details of account2 before withdraw operation:")
    account2.display_balance()
    account2.withdraw(90.50)
    print(f"Account details of account2 after withdraw operation:")
    account2.display_balance()

    print("An attempt to withdraw the amount over the available balance by account holder account1:")
    account1.withdraw(2000)