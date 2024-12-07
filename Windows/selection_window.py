from Windows.music_suggestion_page import MusicSuggestionPage
from window_base import BaseWindow
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


class SelectionWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.selections_label = None
        self.gen_combobox = None
        self.gen_selected_list = []
        self.data = self.create_dataset()
        self.setup_components()

    def create_dataset(self):
        file = r"C:\Users\aacay\Documents\Code\MusicFinderApp\music_data.csv"
        df = pd.read_csv(file)
        dataset = {
            'genre': df['Genres'].str.split(',', n=1).str[0],
            'year': df['Release Date'].str[-4:],
            'art_name': df['Artist Name'],
            'index': df['Ranking']
        }
        return dataset

    def setup_components(self):
        # main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # row-container frames
        param_frame = tk.Frame(main_frame)
        # button_frame = tk.Frame(main_frame)

        # title_label
        title_frame = tk.Frame(main_frame)
        title_label = tk.Label(title_frame, text="Select genres to generate a customized playlist.",
                               font=("Helvetica", 14))
        title_label.pack(pady=5)

        # genre panel
        gen_frame = tk.Frame(param_frame)
        gen_label = tk.Label(gen_frame, text="Genre:")
        gen_label.pack(side=tk.LEFT)
        self.gen_combobox = ttk.Combobox(gen_frame, values=sorted(list(self.data['genre'].unique())))
        self.gen_combobox.pack(side=tk.RIGHT)
        gen_frame.pack(side=tk.LEFT)

        # # year panel
        # yr_frame = tk.Frame(param_frame)
        # yr_label = tk.Label(yr_frame, text="Year:")
        # yr_label.pack(side=tk.LEFT)
        # yr_combobox = ttk.Combobox(yr_frame, values=sorted(list(self.data['year'].unique())))
        # yr_combobox.pack(side=tk.RIGHT)
        # yr_frame.pack(side=tk.RIGHT)

        # button panel
        button_frame = tk.Frame(main_frame)
        add_button = tk.Button(button_frame, text="Add", command=self.on_add_click)
        add_button.pack(padx=5, pady=5, side=tk.LEFT)
        submit_button = tk.Button(button_frame, text="Submit", command=self.on_submit_click)
        submit_button.pack(padx=5, pady=5, side=tk.RIGHT)

        # selected title
        selections_frame = tk.Frame(main_frame)
        selected_label = tk.Label(selections_frame, text="Selected genres:")
        selected_label.pack()
        self.selections_label = tk.Label(selections_frame, text="None")
        self.selections_label.pack()

        # add to main frame
        title_frame.pack()
        param_frame.pack()
        button_frame.pack()
        selections_frame.pack()
        main_frame.pack(expand=True)

    def on_submit_click(self):
        if self.gen_selected_list:
            names_list = []
            for genre in self.gen_selected_list:
                genre_idx_matches_list = (self.data['genre'] == genre).tolist()
                genre_idx_matches = [i for i, x in enumerate(genre_idx_matches_list) if x == True]
                for genre_idx in genre_idx_matches:
                    names_list.append(self.data['art_name'][genre_idx])
            self.close()
            suggestion_window = MusicSuggestionPage(names_list)
            suggestion_window.show()
        else:
            messagebox.showerror("Error", "You did not enter any genres.")

    def on_add_click(self):
        # add selected genre to
        if self.gen_combobox.get() == '':
            messagebox.showerror("Error", "You did not enter any genres.")
        elif len(self.gen_selected_list) > 3:
            messagebox.showerror("Error", "You've entered too many genres.")
        elif self.gen_combobox.get() in self.gen_selected_list:
            messagebox.showerror("Error", "You already entered that genre.")
        else:
            self.gen_selected_list.append(self.gen_combobox.get())
            self.selections_label.config(text=", ".join(self.gen_selected_list))


if __name__ == '__main__':
    selection_window = SelectionWindow()
    selection_window.show()
