class UserAccount:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        """Returns account balance."""
        return self.balance

    def withdraw(self, amount):
        """Deduct the specified amount from the account."""
        if amount > self.balance:
            return False, "Insufficient Balance"
        self.balance -= amount
        return True, "Transaction Successful"

    def deposit(self, amount):
        """Adds the specified amount to the account."""
        self.balance += amount
        return True, "Deposit Successful"


class Transaction:
    def __init__(self, transaction_id, transaction_type, amount):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount

    def process_transaction(self):
        """Starts and completes the process."""
        print(f"Transaction {self.transaction_id}: {self.transaction_type} of {self.amount} processed.")


class ATM:
    def __init__(self):
        # Accounts at ATM (predefined sample accounts)
        self.accounts = {
            "20211123": UserAccount("20211123", 1234, 1000),
            "654321": UserAccount("654321", 4321, 500)
        }
        self.transactions = []  # The list that holds the shlems

    def authenticate_user(self, account_number, pin):
        """Verifies the user."""
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def withdraw_cash(self, user_account, amount):
        """Starts the withdrawal process and records the transaction."""
        success, message = user_account.withdraw(amount)
        if success:
            transaction = Transaction(len(self.transactions) + 1, "Withdrawal", amount)
            transaction.process_transaction()
            self.transactions.append(transaction)
        return success, message

    def deposit_cash(self, user_account, amount):
        """Starts the deposit and records the transaction."""
        success, message = user_account.deposit(amount)
        if success:
            transaction = Transaction(len(self.transactions) + 1, "Deposit", amount)
            transaction.process_transaction()
            self.transactions.append(transaction)
        return success, message

    def check_balance(self, user_account):
        """Returns the user's balance."""
        return user_account.check_balance()
