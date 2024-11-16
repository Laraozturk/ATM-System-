class UserAccount:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        """Hesap bakiyesini döndürür."""
        return self.balance

    def withdraw(self, amount):
        """Belirtilen tutarı hesaptan çeker."""
        if amount > self.balance:
            return False, "Insufficient Balance"
        self.balance -= amount
        return True, "Transaction Successful"

    def deposit(self, amount):
        """Belirtilen tutarı hesaba ekler."""
        self.balance += amount
        return True, "Deposit Successful"


class Transaction:
    def __init__(self, transaction_id, transaction_type, amount):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount

    def process_transaction(self):
        """İşlemi başlatır ve tamamlar."""
        print(f"Transaction {self.transaction_id}: {self.transaction_type} of {self.amount} processed.")


class ATM:
    def __init__(self):
        # ATM'deki hesaplar (önceden tanımlanmış örnek hesaplar)
        self.accounts = {
            "20211123": UserAccount("20211123", 1234, 1000),
            "654321": UserAccount("654321", 4321, 500)
        }
        self.transactions = []  # İşlemleri tutan liste

    def authenticate_user(self, account_number, pin):
        """Kullanıcıyı doğrular."""
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def withdraw_cash(self, user_account, amount):
        """Para çekme işlemini başlatır ve işlemi kaydeder."""
        success, message = user_account.withdraw(amount)
        if success:
            transaction = Transaction(len(self.transactions) + 1, "Withdrawal", amount)
            transaction.process_transaction()
            self.transactions.append(transaction)
        return success, message

    def deposit_cash(self, user_account, amount):
        """Para yatırma işlemi başlatır ve işlemi kaydeder."""
        success, message = user_account.deposit(amount)
        if success:
            transaction = Transaction(len(self.transactions) + 1, "Deposit", amount)
            transaction.process_transaction()
            self.transactions.append(transaction)
        return success, message

    def check_balance(self, user_account):
        """Kullanıcının bakiyesini döndürür."""
        return user_account.check_balance()
