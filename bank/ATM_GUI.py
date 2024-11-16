import tkinter as tk
from tkinter import messagebox
from ATMSystem import UserAccount, Transaction, ATM  # We import the ATMSystem.py file

class ATM_GUI:
    def __init__(self, root):
        self.atm = ATM()  # We are starting the ATM class
        self.current_account = None
        self.root = root
        self.start()  # We call the start function

    def authenticate_user(self):
        """Verifies the user."""
        account_number = self.account_number_entry.get()
        pin = self.pin_entry.get()
        account = self.atm.authenticate_user(account_number, int(pin))
        if account:
            self.current_account = account
            self.show_menu()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN")

    def withdraw_cash(self):
        """Starts the withdrawal transaction and saves the transaction."""
        try:
            amount = int(self.amount_entry.get())
            success, message = self.atm.withdraw_cash(self.current_account, amount)
            messagebox.showinfo("Transaction", message)
            if success:
                self.show_balance()  # The balance will be updated and shown
                self.show_menu()      # Show the main menu again
            else:
                self.show_balance()   # YShow ine balance, if the transaction fails
                self.show_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def deposit_cash(self):
        """Starts the deposit and records the transaction."""
        try:
            amount = int(self.amount_entry.get())
            success, message = self.atm.deposit_cash(self.current_account, amount)
            messagebox.showinfo("Transaction", message)
            if success:
                self.show_balance()  # The balance will be updated and shown
                self.show_menu()      # Show the main menu again
            else:
                self.show_balance()   # Show balance again, if the transaction fails
                self.show_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def show_balance(self):
        """Shows account balance."""
        balance = self.atm.check_balance(self.current_account)
        messagebox.showinfo("Balance", f"Your balance is: {balance}")

    def show_menu(self):
        """AIt shows the menu."""
        self.clear_window()
        self.balance_button = tk.Button(self.root, text="Check Balance", command=self.show_balance)
        self.balance_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", command=self.show_withdraw)
        self.withdraw_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit Money", command=self.show_deposit)
        self.deposit_button.pack(pady=10)

    def show_withdraw(self):
        """Shows withdrawal screen."""
        self.clear_window()
        self.amount_label = tk.Label(self.root, text="Enter the amount to withdraw:")
        self.amount_label.pack(pady=10)
        
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Withdraw", command=self.withdraw_cash)
        self.submit_button.pack(pady=10)

    def show_deposit(self):
        """Shows the deposit screen."""
        self.clear_window()
        self.amount_label = tk.Label(self.root, text="Enter the amount to deposit:")
        self.amount_label.pack(pady=10)
        
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Deposit", command=self.deposit_cash)
        self.submit_button.pack(pady=10)

    def clear_window(self):
        """It cleans up existing widgets."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start(self):
        """Shows the login screen that started the ATM."""
        self.clear_window()

        # "WELCOME TO ATM" Let's add the message
        welcome_label = tk.Label(self.root, text="WELCOME TO ATM", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        # "PLEASE LOGIN" Let's add the message
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


# Creating the main window
root = tk.Tk()
root.title("ATM System")
atm_gui = ATM_GUI(root)

root.mainloop()
