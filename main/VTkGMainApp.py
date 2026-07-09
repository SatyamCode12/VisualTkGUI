import tkinter as tk
from tkinter import ttk

class VTkGMainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Basic Attributes
        # self.overrideredirect(True) This will remove all windows decorations, frame, exit/ minimize button
        window_height = 900
        window_width = 1600
        self.title("VisualTkGUI")
        x_offset = (int)(self.winfo_screenwidth()/2) - (int)(window_width/2)
        y_offset = (int)(self.winfo_screenheight()/2) - (int)(window_height/2)

        self.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")  # (width x height + xOffset + yOffset)
        self.resizable(False, False)                                            # (isHeightResizable, isWidthResizable)

        # Grid Configuration
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=1)