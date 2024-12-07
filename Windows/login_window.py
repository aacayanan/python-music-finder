import os
import csv
from Windows.create_account_window import CreateAccountWindow
from Windows.selection_window import SelectionWindow
from window_base import BaseWindow
import tkinter as tk
from tkinter import messagebox
from pandas import read_csv


class LoginWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.password_entry = None
        self.username_entry = None
        self.accounts = read_csv('../accounts.csv')
        self.setup_components()

    def setup_components(self):
        # main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # username panel
        username_frame = tk.Frame(main_frame)
        username_label = tk.Label(username_frame, text="Username:")
        username_label.pack(side="left", fill="x")
        self.username_entry = tk.Entry(username_frame)
        self.username_entry.pack(side="right", fill="x")
        username_frame.pack(pady=10)

        # password panel
        password_frame = tk.Frame(main_frame)
        password_label = tk.Label(password_frame, text="Password:")
        password_label.pack(side="left", fill="x", pady=5)
        self.password_entry = tk.Entry(password_frame, show="*")
        self.password_entry.pack(side="right", fill="x", pady=5)
        password_frame.pack(pady=10)

        # buttons panel
        buttons_frame = tk.Frame(main_frame)
        login_button = tk.Button(buttons_frame, text="Login", command=self.on_login_click)
        login_button.pack(side="left", fill="x", padx=5)
        create_acct_button = tk.Button(buttons_frame, text="Create Account", command=self.on_create_account_click)
        create_acct_button.pack(side="right", fill="x", padx=5)
        buttons_frame.pack(pady=10)

        # add to main frame
        main_frame.pack(expand=True)

    def on_login_click(self):
        # check if there is a csv file
        if not os.path.exists('../accounts.csv'):
            messagebox.showinfo("Error", "No accounts found. Please create one.")
            return 0

        input_username = self.username_entry.get()
        input_password = self.password_entry.get()

        # check for match
        match = self.accounts[(self.accounts['username'] == input_username) &
                              (self.accounts['password'] == input_password)]
        if not match.empty:
            self.close()
            selection_window = SelectionWindow()
            selection_window.show()
        else:
            messagebox.showerror("Error", "Username or password is incorrect")
            # Clear the text entries
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        return 1

    def on_create_account_click(self):
        create_account = CreateAccountWindow()
        create_account.show()
