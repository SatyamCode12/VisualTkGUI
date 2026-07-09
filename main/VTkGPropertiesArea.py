import tkinter as tk
from tkinter import ttk

class VTkGPropertiesArea(ttk.Frame):
    properties = [
        # Identity
        "name",

        # Geometry
        "x",
        "y",
        "width",
        "height",

        # Appearance
        "text",
        "image",
        "font",
        "foreground",
        "background",
        "borderwidth",
        "relief",
        "padding",
        "anchor",
        "justify",

        # State
        "state",
        "takefocus",

        # Cursor
        "cursor",

        # Colors
        "activebackground",
        "activeforeground",
        "disabledforeground",

        # Values
        "value",
        "variable",
        "textvariable",

        # Entry/Text
        "show",
        "insertbackground",

        # Checkbutton/Radiobutton
        "onvalue",
        "offvalue",
        "command",

        # Scale/Progressbar
        "from_",
        "to",
        "orient",
        "length",
        "mode",
        "maximum",

        # Scrollbar
        "repeatdelay",
        "repeatinterval",

        # Listbox
        "selectmode",

        # Treeview
        "columns",
        "show",

        # Combobox
        "values",

        # Canvas
        "scrollregion",

        # Notebook
        "tabposition",
    ]
    def __init__(self, mainApp):
        super().__init__(mainApp, height=900, width=300, borderwidth=5, relief='groove')

        self.rowconfigure(0, weight=1)
        for i in range(len(self.properties)):
            self.rowconfigure(i+1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.grid_propagate(False)
        self.heading = ttk.Label(self, 
                                 text="Properties", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background="#c8fcff", 
                                 padding=8)
        
        self.heading.grid(row=0, column=0, columnspan=2, sticky='n')

        for rw, prt in enumerate(self.properties, start=1):
            tk.Label(
                self,
                text=prt
            ).grid(row=rw, column=0, sticky='ew')
            ttk.Entry(
                self
            ).grid(row=rw, column=1, sticky='ew')
            
        
        self.grid(row=0, column=2, sticky='ne')