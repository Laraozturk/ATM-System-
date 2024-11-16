import tkinter as tk
from tkinter import messagebox
from ATMSystem import UserAccount, Transaction, ATM  # ATMSystem.py dosyasını içe aktarıyoruz

class ATM_GUI:
    def __init__(self, root):
        self.atm = ATM()  # ATM sınıfını başlatıyoruz
        self.current_account = None
        self.root = root
        self.start()  # Başlangıç fonksiyonunu çağırıyoruz

    def authenticate_user(self):
        """Kullanıcıyı doğrular."""
        account_number = self.account_number_entry.get()
        pin = self.pin_entry.get()
        account = self.atm.authenticate_user(account_number, int(pin))
        if account:
            self.current_account = account
            self.show_menu()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN")

    def withdraw_cash(self):
        """Para çekme işlemi başlatır ve işlemi kaydeder."""
        try:
            amount = int(self.amount_entry.get())
            success, message = self.atm.withdraw_cash(self.current_account, amount)
            messagebox.showinfo("Transaction", message)
            if success:
                self.show_balance()  # Bakiye güncellenip gösterilecek
                self.show_menu()      # Ana menüyü tekrar göster
            else:
                self.show_balance()   # Yine bakiye göster, eğer işlem başarısızsa
                self.show_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def deposit_cash(self):
        """Para yatırma işlemi başlatır ve işlemi kaydeder."""
        try:
            amount = int(self.amount_entry.get())
            success, message = self.atm.deposit_cash(self.current_account, amount)
            messagebox.showinfo("Transaction", message)
            if success:
                self.show_balance()  # Bakiye güncellenip gösterilecek
                self.show_menu()      # Ana menüyü tekrar göster
            else:
                self.show_balance()   # Yine bakiye göster, eğer işlem başarısızsa
                self.show_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def show_balance(self):
        """Hesap bakiyesini gösterir."""
        balance = self.atm.check_balance(self.current_account)
        messagebox.showinfo("Balance", f"Your balance is: {balance}")

    def show_menu(self):
        """Ana menüyü gösterir."""
        self.clear_window()
        self.balance_button = tk.Button(self.root, text="Check Balance", command=self.show_balance)
        self.balance_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", command=self.show_withdraw)
        self.withdraw_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit Money", command=self.show_deposit)
        self.deposit_button.pack(pady=10)

    def show_withdraw(self):
        """Para çekme ekranını gösterir."""
        self.clear_window()
        self.amount_label = tk.Label(self.root, text="Enter the amount to withdraw:")
        self.amount_label.pack(pady=10)
        
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Withdraw", command=self.withdraw_cash)
        self.submit_button.pack(pady=10)

    def show_deposit(self):
        """Para yatırma ekranını gösterir."""
        self.clear_window()
        self.amount_label = tk.Label(self.root, text="Enter the amount to deposit:")
        self.amount_label.pack(pady=10)
        
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Deposit", command=self.deposit_cash)
        self.submit_button.pack(pady=10)

    def clear_window(self):
        """Mevcut widget'ları temizler."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start(self):
        """ATM'yi başlatan giriş ekranını gösterir."""
        self.clear_window()

        # "WELCOME TO ATM" mesajını ekleyelim
        welcome_label = tk.Label(self.root, text="WELCOME TO ATM", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        # "PLEASE LOGIN" mesajını ekleyelim
        login_label = tk.Label(self.root, text="PLEASE LOGIN", font=("Helvetica", 14))
        login_label.pack(pady=10)

        self.account_number_label = tk.Label(self.root, text="Account Number:")
        self.account_number_label.pack(pady=10)
        
        self.account_number_entry = tk.Entry(self.root)
        self.account_number_entry.pack(pady=10)
        
        self.pin_label = tk.Label(self.root, text="PIN:")
        self.pin_label.pack(pady=10)
        
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=10)
        
        self.login_button = tk.Button(self.root, text="Login", command=self.authenticate_user)
        self.login_button.pack(pady=20)


# Ana pencereyi oluşturma
root = tk.Tk()
root.title("ATM System")
atm_gui = ATM_GUI(root)

root.mainloop()
