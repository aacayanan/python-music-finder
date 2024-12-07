from Windows.music_suggestion_page import MusicSuggestionPage
from window_base import BaseWindow
import tkinter as tk
from tkinter import ttk
import pandas as pd


class SelectionWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.gen_combobox = None
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
        submit_button = tk.Button(button_frame, text="Submit", command=self.on_submit_click)
        submit_button.pack()

        # add to main frame
        param_frame.pack()
        button_frame.pack()
        main_frame.pack(expand=True)

    def on_submit_click(self):
        selected_genre = self.gen_combobox.get()
        genre_idx_matches_list = (self.data['genre'] == selected_genre).tolist()
        genre_idx_matches = [i for i, x in enumerate(genre_idx_matches_list) if x == True]
        self.close()
        suggestion_window = MusicSuggestionPage(self.data['art_name'][genre_idx_matches].tolist())
        suggestion_window.show()




if __name__ == '__main__':
    selection_window = SelectionWindow()
    selection_window.show()