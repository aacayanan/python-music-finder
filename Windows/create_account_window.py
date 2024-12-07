import csv
import os
from window_base import BaseWindow
import tkinter as tk


class CreateAccountWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.username_entry = None
        self.password_entry = None
        self.setup_components()

    def setup_components(self):
        # main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # title frame
        title_label = tk.Label(main_frame, text="Create An Account")
        title_label.pack()

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

        create_acct_button = tk.Button(main_frame, text="Create Account", command=self.create_account_click)
        create_acct_button.pack(pady=10)

        main_frame.pack()

    def create_account_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        account = [[username, password]]

        # append data to csv, if not found create a new csv
        file_name = '../accounts.csv'
        file_exists = os.path.exists(file_name)

        with open(file_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)

            if not file_exists:
                writer.writerow(['username', 'password'])
            writer.writerows(account)

        self.close()
