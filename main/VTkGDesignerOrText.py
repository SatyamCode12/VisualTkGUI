import tkinter as tk
from tkinter import ttk

class VTkGDesigner(tk.Canvas):
    def __init__(self, design_or_text_frame, properties_frame):
        super().__init__(design_or_text_frame, height=850, width=1000, bg="white")
        self.properties_frame = properties_frame
        self.grid(row= 1, column=0, columnspan=2, sticky='nw')
        self.control_list = []
    
    def add_new_control(self, control):
        self.control_list.append(control)
        control.bind("<Button-1>", self.dragStart)
        control.bind("<B1-Motion>", self.dragMotion)

    def dragStart(self, event):
        widget = event.widget
        # self.properties_frame.get_properties_list(widget)
        # widget.configure(self.properties_frame.get_properties_list_value(widget))
        widget.StartX = event.x
        widget.StartY = event.y

    def dragMotion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.StartX + event.x
        y = widget.winfo_y() - widget.StartY + event.y
        widget.place(x=x, y=y)

class VTkGText(tk.Text):
    def __init__(self, design_or_text_frame):
        super().__init__(design_or_text_frame, height=42, width=100, bg="white")
        self.grid(row= 1, column=0, columnspan=2, sticky='nw')

class VTkGDesignerOrText(ttk.Frame):
    design_selected = True
    text_selected = False

    def __init__(self, mainApp, properties_frame):
        super().__init__(mainApp, height=900, width=1000, borderwidth=5, relief='groove')
        self.properties_frame = properties_frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=14)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        
        self.grid_propagate(False)
        self.design_tab = ttk.Label(self, 
                                 text="Design Editor", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background = "#04909A" if self.design_selected else "#c8fcff", 
                                 padding=8)
        
        self.design_tab.grid(row=0, column=0, sticky='n')
        self.design_tab.bind("<Button-1>", self.selectAppropriate)
        self.text_tab = ttk.Label(self, 
                                 text="Text Editor", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background= "#04909A" if self.text_selected else "#c8fcff", 
                                 padding=8)
        
        self.text_tab.grid(row=0, column=1, sticky='n')
        self.text_tab.bind("<Button-1>", self.selectAppropriate)

        
        self.text_canvas = VTkGText(self)
        self.design_canvas = VTkGDesigner(self, self.properties_frame)

        self.grid(row=0, column=1, sticky='ns')

    def selectAppropriate(self, event):
        widget = event.widget
        if widget == self.design_tab:
            self.design_selected = True
            self.text_selected = False
            self.design_canvas.focus_set()
            self.design_canvas.grid(row=1, column=0, columnspan=2, sticky='nw')
            self.text_canvas.grid_remove()
            
        elif widget == self.text_tab:
            self.design_selected = False
            self.text_selected = True
            self.text_canvas.focus_set()
            self.design_canvas.grid_remove()
            self.text_canvas.grid(row=1, column=0, columnspan=2, sticky='nw')

        self.design_tab.configure(background="#04909A" if self.design_selected else "#c8fcff")
        self.text_tab.configure(background="#04909A" if self.text_selected else "#c8fcff")