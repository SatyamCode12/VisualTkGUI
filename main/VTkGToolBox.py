import tkinter as tk
from tkinter import ttk
import VTkGMainApp
import VTkGDesignerOrText
import VTkGPropertiesArea

class VTkGToolBox(ttk.Frame):

    # list of controls that can be drag and dropped
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
    
    # initiating VTkGToolBox
    def __init__(self, mainApp, design_canvas_app):
        super().__init__(mainApp, height=900, width=300, borderwidth=5, relief='groove')

        # design_canvas_app is reference of design/ text editor frame/ area
        # used for adding controls to designer area
        self.design_canvas = design_canvas_app

        # row and column configuration
        self.rowconfigure(0, weight=1)
        for i in range(len(self.tools)):
            self.rowconfigure(i+1, weight=1)
        
        self.columnconfigure(0, weight=1)

        # setting the following TRUE will
        # set the size of container based on size of control
        # so keep it FALSE (recommended)
        self.grid_propagate(False)

        # ToolBox heading
        self.heading = ttk.Label(self, 
                                 text="Tool Box", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background="#c8fcff", 
                                 padding=8)
        
        self.heading.grid(row=0, column=0, sticky='n')

        for row, tool in enumerate(self.tools, start=1):
           ttk.Button(
               self,
               text=tool.__name__,
               command= lambda widget_class = tool:self.addControl(widget_class = widget_class)
           ).grid(row=row, column=0, sticky='ew')

        self.grid(row=0, column=0, sticky='nw')
    
    # This function adds selected/ clicked control to canvas
    def addControl(self, widget_class):
        widget = widget_class(self.design_canvas)

        # before adding the widget to canvas we will open properties window
        # to configure it before adding it to canvas
        properties_widget = tk.Tk()
        properties_widget.title(widget_class.__name__)
        properties_widget.geometry(f"{500}x{400}+{600}+{200}")  # (width x height + xOffset + yOffset)
        properties_widget.resizable(False, False)               # (isHeightResizable, isWidthResizable)

        # properties_widget.propagate(False)

        properties_widget.rowconfigure(0, weight=1)
        properties_widget.rowconfigure(1, weight=1)
        properties_widget.rowconfigure(2, weight=1)
        properties_widget.rowconfigure(3, weight=1)
        properties_widget.columnconfigure(0, weight=1)
        properties_widget.columnconfigure(1, weight=2)

        name_in_code = ttk.Label(properties_widget, text="name in code")
        name_in_code.grid(row=0, column=0, sticky='e', padx=10, pady=10)

        name_in_code_entry = ttk.Entry(properties_widget)
        name_in_code_entry.grid(row=0, column=1, sticky='w', padx=10, pady=10)

        text = ttk.Label(properties_widget, text="text")
        text.grid(row=1, column=0, sticky='e', padx=10, pady=10)

        text_entry = ttk.Entry(properties_widget)
        text_entry.grid(row=1, column=1, sticky='w', padx=10, pady=10)

        add_button = ttk.Button(properties_widget, text="Add", command=properties_widget.destroy)
        add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        properties_widget.mainloop()

        widget.place(x=0, y=0)
        self.design_canvas.add_new_control(widget)