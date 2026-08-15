import tkinter as tk
from tkinter import ttk

class VTkGNewProject(tk.Tk):
    def __init__(self):
        super().__init__()

        window_height = 400
        window_width = 600
        self.title("VisualTkGUI New Project")
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
        self.columnconfigure(3, weight=1)
        # self.grid_propagate(False)


        self.NAME = tk.StringVar()
        self.PATHTOPROJECT = tk.StringVar()

        screen_text = ttk.Label(self, text="New Project!", anchor='center', font='Arial 18')
        screen_text.grid(row=1, column=1, sticky='n', columnspan=2)
        name_label = ttk.Label(self, text="Project Name:")
        name_label.grid(row=2, column=1, sticky='ew')
        name_entry = ttk.Entry(self, textvariable=self.NAME)
        name_entry.grid(row=2, column=2, sticky='ew')
        directory_label = ttk.Label(self, text="Project Directory:")
        directory_label.grid(row=3, column=1, sticky='ew')
        directory_entry = ttk.Entry(self, textvariable=self.PATHTOPROJECT)
        directory_entry.grid(row=3, column=2, sticky='ew')

        create_new = ttk.Button(self, text="Create New", command=self.create_new)
        create_new.grid(row=4, column=1, columnspan=2, sticky='ew')

    def create_new(self):
        self.destroy()

