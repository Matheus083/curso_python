from accounts import CurrentAccount, SavingsAccount
from persons import Client
from bank import Bank

if __name__ == "__main__":
    client = Client("John", 20, "Current")
    savings_account = SavingsAccount(12235, 54321)
    current_account = CurrentAccount(12235, 12345)
    bank_current = Bank("Bank of America", client, current_account)
    bank_savings = Bank("Bank of America", client, savings_account)

    savings_account.deposit(500)
    current_account.deposit(1000)
    savings_account.deposit(1000)
    current_account.deposit(500)
    savings_account.withdraw(200)
    current_account.withdraw(1500)

    savings_account.deposit(-100)  # This will raise a ValueError and print an error message
    current_account.deposit(-100)  # This will raise a ValueError and print an error message

    savings_account.deposit(0)  # This will raise a ValueError and print an error message
    current_account.deposit(0)  # This will raise a ValueError and print an error message

    savings_account.withdraw(-100)  # This will raise a ValueError and print an error message
    current_account.withdraw(-100)  # This will raise a ValueError and print an error message

    savings_account.withdraw(0)  # This will raise a ValueError and print an error message
    current_account.withdraw(0)  # This will raise a ValueError and print an error message

    savings_account.deposit(8800)
    current_account.deposit(12500)

    savings_account.withdraw(3720)
    current_account.withdraw(6500)

    print(bank_savings)
    print("=" * 60)
    print(bank_current)