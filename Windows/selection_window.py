from window_base import BaseWindow
import tkinter as tk
from tkinter import ttk


class SelectionWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setup_components()

    def setup_components(self):
        # main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # row-container frames
        param_frame = tk.Frame(main_frame)
        # button_frame = tk.Frame(main_frame)

        # genre panel
        gen_frame = tk.Frame(param_frame)
        gen_label = tk.Label(gen_frame, text="Genre:")
        gen_label.pack(side=tk.LEFT)
        gen_combobox = ttk.Combobox(gen_frame, values=('Genre', 'Pop'))
        gen_combobox.pack(side=tk.RIGHT)
        gen_frame.pack(side=tk.LEFT)

        # year panel
        yr_frame = tk.Frame(param_frame)
        yr_label = tk.Label(yr_frame, text="Year:")
        yr_label.pack(side=tk.LEFT)
        yr_combobox = ttk.Combobox(yr_frame, values=('Year', '2000'))
        yr_combobox.pack(side=tk.RIGHT)
        yr_frame.pack(side=tk.RIGHT)

        # button panel
        button_frame = tk.Frame(main_frame)
        submit_button = tk.Button(button_frame, text="Submit")
        submit_button.pack()

        # add to main frame
        param_frame.pack()
        button_frame.pack()
        main_frame.pack(expand=True)