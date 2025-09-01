class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"👤 Account Holder: {self.name}\n💰 Current Balance: ₹{self.balance}")


# --- Main Program ---
def main():
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(name, initial_balance)

    while True:
        print("\n====== Bank Menu ======")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("=======================")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("✅ Thank you for banking with us. Exiting...")
            break
        else:
            print("❌ Invalid option. Please try again.")

# Run the program
main()
