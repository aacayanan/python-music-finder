from window_base import BaseWindow
import tkinter as tk


def main():
    # login window start
    login_window = BaseWindow()

    # login window components

    # main frame
    main_frame = tk.Frame(login_window.root)
    main_frame.grid(row=0, column=0)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # username panel
    username_frame = tk.Frame(main_frame)
    username_label = tk.Label(username_frame, text="Username:")
    username_label.pack(side="left", fill="x")
    username_entry = tk.Entry(username_frame)
    username_entry.pack(side="right", fill="x")
    login_window.add_component(username_frame)

    # password panel
    password_frame = tk.Frame(main_frame)
    password_label = tk.Label(password_frame, text="Password:")
    password_label.pack(side="left", fill="x", pady=5)
    password_entry = tk.Entry(password_frame)
    password_entry.pack(side="right", fill="x", pady=5)
    login_window.add_component(password_frame)

    # buttons panel
    buttons_frame = tk.Frame(main_frame)
    login_button = tk.Button(buttons_frame, text="Login")
    login_button.pack(side="left", fill="x", padx=5)
    create_acct_button = tk.Button(buttons_frame, text="Create Account")
    create_acct_button.pack(side="right", fill="x", padx=5)
    login_window.add_component(buttons_frame)


    # add main frame and show login window
    main_frame.pack(expand=True)
    login_window.show()
    # login window end


if __name__ == '__main__':
    main()
