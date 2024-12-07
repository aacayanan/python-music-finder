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
        self.generate_suggestions()

    def setup_components(self):
        # main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

    def generate_suggestions(self):
        # get api key from .env
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Given the following list of names, generate 10 song suggestions."},
                {"role": "user", "content": "[Bruno Mars, Jeff Buckley]"}
            ]
        )

        print(response.choices[0].message.content)