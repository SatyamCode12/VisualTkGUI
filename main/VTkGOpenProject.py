import tkinter as tk
from tkinter import ttk

class VTkGOpenProject(tk.Tk):
    def __init__(self):
        super().__init__()

        window_height = 400
        window_width = 600
        self.title("VisualTkGUI Open Project")
        x_offset = (int)(self.winfo_screenwidth()/2) - (int)(window_width/2)
        y_offset = (int)(self.winfo_screenheight()/2) - (int)(window_height/2)
        
        self.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")  # (width x height + xOffset + yOffset)
        self.resizable(False, False)                                            # (isHeightResizable, isWidthResizable)
        # self.overrideredirect(True)


        # State Variables
        self.new_project_folder_path = ""
        # self.is_open_project = False
        # self.is_close_window = False
        
        # Grid Configuration
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=7)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        # self.grid_propagate(False)


        screen_text = ttk.Label(self, text="Open Project!", anchor='center', font='Arial 18')
        screen_text.grid(row=1, column=1, sticky='n')

    def close_Window(self):
        self.is_close_window = True
        self.destroy()

    def open_project(self):
        self.is_open_window = True
        self.destroy()

    def new_project(self):
        self.is_new_project = True
        self.destroy()

