import tkinter as tk
from tkinter import messagebox, simpledialog

class ATMSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.balance = 1000  # Default balance
        self.pin = "1234"  # Default PIN
        self.is_authenticated = False
        self.transaction_history = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # PIN Entry
        self.pin_label = tk.Label(self.root, text="Enter PIN to access ATM:", font=("Arial", 14))
        self.pin_label.pack(pady=10)

        self.pin_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.authenticate_user, font=("Arial", 14))
        self.login_button.pack(pady=10)

        # Balance label (hidden until authenticated)
        self.balance_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.balance_label.pack(pady=10)

        # Deposit Entry
        self.deposit_entry = tk.Entry(self.root, font=("Arial", 14))
        self.deposit_entry.pack(pady=5)
        self.deposit_entry.insert(0, "Deposit Amount")

        # Deposit Button
        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit_money, font=("Arial", 14))
        self.deposit_button.pack(pady=5)

        # Withdraw Entry
        self.withdraw_entry = tk.Entry(self.root, font=("Arial", 14))
        self.withdraw_entry.pack(pady=5)
        self.withdraw_entry.insert(0, "Withdraw Amount")

        # Withdraw Button
        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw_money, font=("Arial", 14))
        self.withdraw_button.pack(pady=5)

        # Transaction History Button
        self.history_button = tk.Button(self.root, text="Transaction History", command=self.show_history, font=("Arial", 14))
        self.history_button.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14))
        self.exit_button.pack(pady=10)

    def authenticate_user(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.is_authenticated = True
            self.pin_label.pack_forget()
            self.pin_entry.pack_forget()
            self.login_button.pack_forget()
            self.balance_label.config(text=f"Current Balance: ${self.balance:.2f}")
            self.balance_label.pack(pady=10)
        else:
            messagebox.showwarning("Warning", "Incorrect PIN! Please try again.")

    def update_balance_label(self):
        self.balance_label.config(text=f"Current Balance: ${self.balance:.2f}")

    def deposit_money(self):
        try:
            amount = float(self.deposit_entry.get())
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited: ${amount:.2f}")
                self.update_balance_label()
                messagebox.showinfo("Success", f"${amount:.2f} has been deposited successfully.")
                self.deposit_entry.delete(0, tk.END)  # Clear the entry
            else:
                messagebox.showwarning("Warning", "Invalid deposit amount!")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number.")

    def withdraw_money(self):
        try:
            amount = float(self.withdraw_entry.get())
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount:.2f}")
                self.update_balance_label()
                messagebox.showinfo("Success", f"${amount:.2f} has been withdrawn successfully.")
                self.withdraw_entry.delete(0, tk.END)  # Clear the entry
            elif amount > self.balance:
                messagebox.showwarning("Warning", "Insufficient funds!")
            else:
                messagebox.showwarning("Warning", "Invalid withdrawal amount!")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number.")

    def show_history(self):
        if not self.transaction_history:
            messagebox.showinfo("Transaction History", "No transactions have been made.")
        else:
            history = "\n".join(self.transaction_history)
            messagebox.showinfo("Transaction History", history)

if __name__ == "__main__":
    root = tk.Tk()
    atm_simulator = ATMSimulator(root)
    root.mainloop()
