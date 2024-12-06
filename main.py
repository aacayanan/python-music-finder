from Windows.login_window import LoginWindow
from Windows.selection_window import SelectionWindow
from window_base import BaseWindow
import tkinter as tk


def main():
    login_window = LoginWindow()
    login_window.show()

    selection_window = SelectionWindow()
    selection_window.show()

if __name__ == '__main__':
    main()
