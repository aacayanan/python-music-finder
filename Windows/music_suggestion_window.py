from window_base import BaseWindow
import tkinter as tk
from openai import OpenAI
import os
from dotenv import find_dotenv, load_dotenv


class MusicSuggestionPage(BaseWindow):
    def __init__(self, name_list):
        super().__init__()
        self.name_list = name_list
        self.setup_components()
        # self.generate_suggestions()

    def setup_components(self):
        # main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # title frame
        title_label = tk.Label(main_frame, text="Here are your personalized suggestions", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # content frame
        content_frame = tk.Frame(main_frame)
        content_label = tk.Label(content_frame, text=self.generate_suggestions(), font=("Helvetica", 10))
        content_label.pack()

        # add to main frame
        title_label.pack()
        content_frame.pack()
        main_frame.pack()

    def generate_suggestions(self):
        # get api key from .env
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Given the following list of artist names, generate 10 song suggestions "
                                              "of the artist(s) in the form, \"Song\" by Artist."},
                {"role": "user", "content": str(self.name_list)}
            ]
        )
        return response.choices[0].message.content
