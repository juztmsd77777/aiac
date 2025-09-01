class BankAccount:
    def __init__(self, name, initial_balance=0):
        # Initialize account holder's name and starting balance
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        # Add the deposit amount to the balance
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtract the withdrawal amount from the balance if sufficient funds exist
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Display the current balance
        print(f"Account holder: {self.name}, Balance: {self.balance}")

# Take user input for account creation and operations
name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")


