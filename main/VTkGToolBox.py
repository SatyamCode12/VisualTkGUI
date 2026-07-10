import tkinter as tk
from tkinter import ttk
import VTkGMainApp
import VTkGDesignerOrText
import VTkGPropertiesArea

class VTkGToolBox(ttk.Frame):
    tools = [
    tk.Frame,
    tk.Canvas,
    tk.Label,
    ttk.Label,
    tk.Button,
    ttk.Button,
    tk.Entry,
    ttk.Entry,
    tk.Text,
    tk.Checkbutton,
    ttk.Checkbutton,
    tk.Radiobutton,
    ttk.Radiobutton,
    ttk.Combobox,
    tk.Listbox,
    ttk.Treeview,
    tk.Scrollbar,
    ttk.Scrollbar,
    ttk.Progressbar,
    tk.Scale,
    ttk.Scale,
    tk.Spinbox,
    ttk.Spinbox,
    ttk.Notebook,
    ttk.Separator,
    ttk.Labelframe
]
    def __init__(self, mainApp, design_canvas_app):
        super().__init__(mainApp, height=900, width=300, borderwidth=5, relief='groove')
        self.design_canvas = design_canvas_app
        self.rowconfigure(0, weight=1)
        for i in range(len(self.tools)):
            self.rowconfigure(i+1, weight=1)
        
        self.columnconfigure(0, weight=1)

        self.grid_propagate(False)
        self.heading = ttk.Label(self, 
                                 text="Tool Box", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background="#c8fcff", 
                                 padding=8)
        
        self.heading.grid(row=0, column=0, sticky='n')

        for rw, tl in enumerate(self.tools, start=1):
           ttk.Button(
               self,
               text=tl.__name__,
               command= lambda widget_class = tl:self.addControl(widget_class = widget_class)
           ).grid(row=rw, column=0, sticky='ew')

        self.grid(row=0, column=0, sticky='nw')
    
    def addControl(self, widget_class):
        widget = widget_class(self.design_canvas)
        widget.place(x=0, y=0)
        self.design_canvas.add_new_control(widget)