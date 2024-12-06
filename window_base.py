import tkinter as tk

class BaseWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.title = "Music Finder"
        self.width = 480
        self.height = 240
        self.setup_window()
        self.root.resizable(False, False)

    def setup_window(self):
        self.root.title(self.title)
        self.root.geometry(f'{self.width}x{self.height}')

    def add_component(self, component):
        component.pack()

    def show(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()