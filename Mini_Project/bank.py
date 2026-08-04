import json
import os
import random
import customtkinter as ctk

# --- VISUAL THEME SETUP ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- CORE BANKING LOGIC ---
class BankAccount:
    def __init__(self, account_num, name, pin, balance=0.0):
        self.account_num = str(account_num)
        self.name = name
        self.pin = str(pin)
        self.balance = float(balance)

    def to_dict(self):
        return {"account_num": self.account_num, "name": self.name, "pin": self.pin, "balance": self.balance}

class BankingSystem:
    def __init__(self, data_file="bank_data.json"):
        self.data_file = data_file
        self.accounts = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    for acc_num, acc_data in data.items():
                        self.accounts[acc_num] = BankAccount(
                            acc_data["account_num"], acc_data["name"], acc_data["pin"], acc_data["balance"]
                        )
            except json.JSONDecodeError:
                pass

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json_data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            json.dump(json_data, file, indent=4)

    def create_account(self, name, pin):
        while True:
            acc_num = str(random.randint(10000, 99999))
            if acc_num not in self.accounts:
                break
        new_account = BankAccount(acc_num, name, pin)
        self.accounts[acc_num] = new_account
        self.save_data()
        return acc_num

    def login(self, account_num, pin):
        acc = self.accounts.get(str(account_num))
        if acc and acc.pin == str(pin):
            return acc
        return None

# --- GUI APP WINDOW ---
class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.backend = BankingSystem()
        self.current_user = None

        self.title("Secure Banking Terminal")
        self.geometry("450x500")
        self.resizable(False, False)

        # Container frame to hold current screens
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_login_screen()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- LOGIN SCREEN ---
    def show_login_screen(self):
        self.clear_screen()

        lbl_title = ctk.CTkLabel(self.main_frame, text="Apex Bank Login", font=("Helvetica", 24, "bold"))
        lbl_title.pack(pady=30)

        self.ent_acc = ctk.CTkEntry(self.main_frame, placeholder_text="Account Number", width=250)
        self.ent_acc.pack(pady=10)

        self.ent_pin = ctk.CTkEntry(self.main_frame, placeholder_text="4-Digit PIN", show="*", width=250)
        self.ent_pin.pack(pady=10)

        self.lbl_error = ctk.CTkLabel(self.main_frame, text="", text_color="red")
        self.lbl_error.pack(pady=5)

        btn_login = ctk.CTkButton(self.main_frame, text="Login", command=self.process_login, width=250)
        btn_login.pack(pady=15)

        btn_register_page = ctk.CTkButton(self.main_frame, text="Create New Account", fg_color="transparent", hover_color="#333333", command=self.show_register_screen)
        btn_register_page.pack(pady=5)

    def process_login(self):
        acc = self.ent_acc.get().strip()
        pin = self.ent_pin.get().strip()
        
        user = self.backend.login(acc, pin)
        if user:
            self.current_user = user
            self.show_dashboard()
        else:
            self.lbl_error.configure(text="Invalid Account Number or PIN.")

    # --- REGISTRATION SCREEN ---
    def show_register_screen(self):
        self.clear_screen()

        lbl_title = ctk.CTkLabel(self.main_frame, text="Open Account", font=("Helvetica", 22, "bold"))
        lbl_title.pack(pady=25)

        self.ent_name = ctk.CTkEntry(self.main_frame, placeholder_text="Full Name", width=250)
        self.ent_name.pack(pady=10)

        self.ent_new_pin = ctk.CTkEntry(self.main_frame, placeholder_text="Choose 4-Digit PIN", show="*", width=250)
        self.ent_new_pin.pack(pady=10)

        self.lbl_reg_error = ctk.CTkLabel(self.main_frame, text="", text_color="red")
        self.lbl_reg_error.pack(pady=5)

        btn_submit = ctk.CTkButton(self.main_frame, text="Register", command=self.process_registration, width=250)
        btn_submit.pack(pady=15)

        btn_back = ctk.CTkButton(self.main_frame, text="Back to Login", fg_color="transparent", command=self.show_login_screen)
        btn_back.pack(pady=5)

    def process_registration(self):
        name = self.ent_name.get().strip()
        pin = self.ent_new_pin.get().strip()

        if not name:
            self.lbl_reg_error.configure(text="Name cannot be empty.")
            return
        if not pin.isdigit() or len(pin) != 4:
            self.lbl_reg_error.configure(text="PIN must be exactly 4 digits.")
            return

        new_acc_num = self.backend.create_account(name, pin)
        
        # Show success notification inside the window
        self.clear_screen()
        lbl_msg = ctk.CTkLabel(self.main_frame, text="Account Created Successfully!", font=("Helvetica", 18, "bold"), text_color="green")
        lbl_msg.pack(pady=30)
        
        lbl_info = ctk.CTkLabel(self.main_frame, text=f"Your Account Number is:\n\n{new_acc_num}", font=("Helvetica", 20, "bold"))
        lbl_info.pack(pady=20)

        btn_go_login = ctk.CTkButton(self.main_frame, text="Proceed to Login", command=self.show_login_screen)
        btn_go_login.pack(pady=30)

    # --- DASHBOARD SCREEN ---
    def show_dashboard(self):
        self.clear_screen()

        lbl_welcome = ctk.CTkLabel(self.main_frame, text=f"Welcome, {self.current_user.name}", font=("Helvetica", 18, "bold"))
        lbl_welcome.pack(pady=10)

        # Balance display card
        self.lbl_balance = ctk.CTkLabel(
            self.main_frame, 
            text=f"Balance: ${self.current_user.balance:.2f}", 
            font=("Helvetica", 26, "bold"), 
            fg_color="#1f2937", 
            corner_radius=10,
            width=300,
            height=80
        )
        self.lbl_balance.pack(pady=20)

        self.ent_amt = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Amount ($)", width=250)
        self.ent_amt.pack(pady=10)

        self.lbl_dash_msg = ctk.CTkLabel(self.main_frame, text="", text_color="emerald")
        self.lbl_dash_msg.pack(pady=5)

        # Action Buttons
        btn_dep = ctk.CTkButton(self.main_frame, text="Deposit Money", command=self.handle_deposit, width=250, fg_color="#10b981", hover_color="#059669")
        btn_dep.pack(pady=5)

        btn_with = ctk.CTkButton(self.main_frame, text="Withdraw Money", command=self.handle_withdrawal, width=250, fg_color="#ef4444", hover_color="#dc2626")
        btn_with.pack(pady=5)

        btn_logout = ctk.CTkButton(self.main_frame, text="Logout", fg_color="transparent", command=self.show_login_screen)
        btn_logout.pack(pady=20)

    def handle_deposit(self):
        try:
            amt = float(self.ent_amt.get())
            if amt <= 0:
                raise ValueError
            self.current_user.balance += amt
            self.backend.save_data()
            self.lbl_balance.configure(text=f"Balance: ${self.current_user.balance:.2f}")
            self.lbl_dash_msg.configure(text=f"${amt:.2f} deposited successfully.", text_color="green")
            self.ent_amt.delete(0, 'end')
        except ValueError:
            self.lbl_dash_msg.configure(text="Enter a valid positive number.", text_color="red")

    def handle_withdrawal(self):
        try:
            amt = float(self.ent_amt.get())
            if amt <= 0:
                raise ValueError
            if amt > self.current_user.balance:
                self.lbl_dash_msg.configure(text="Insufficient funds!", text_color="red")
            else:
                self.current_user.balance -= amt
                self.backend.save_data()
                self.lbl_balance.configure(text=f"Balance: ${self.current_user.balance:.2f}")
                self.lbl_dash_msg.configure(text=f"${amt:.2f} withdrawn.", text_color="green")
                self.ent_amt.delete(0, 'end')
        except ValueError:
            self.lbl_dash_msg.configure(text="Enter a valid positive number.", text_color="red")


if __name__ == "__main__":
    app = BankApp()
    app.mainloop()