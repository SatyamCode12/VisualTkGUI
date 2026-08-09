import tkinter as tk
from tkinter import ttk

# the following class is for main canvas
# i.e., the main app area
class VTkGDesigner(tk.Canvas):

    # initiating VTkGDesigner
    def __init__(self, design_or_text_frame, properties_frame):
        super().__init__(design_or_text_frame, height=400, width=400, bg="white")

        # 'properties_frame' is reference to properties area in app.
        self.properties_frame = properties_frame

        #placing grid 
        self.grid(row= 1, column=0, columnspan=2, sticky='nw')

        # List of controls present in the main app
        self.control_list = []
    
    # The following function adds the new control
    # when any button in toolbox is clicked.
    # this also binds it for dragging and placing control
    def add_new_control(self, control):
        self.control_list.append(control)
        control.bind("<Button-1>", self.dragStart) # '<Button-1>' for left mouse click
        control.bind("<B1-Motion>", self.dragMotion) # '<B1-Motion>' for left mouse drag while click

    # The following function notes mouse position when left clicked to
    # start draging control
    def dragStart(self, event):
        widget = event.widget
        widget.StartX = event.x
        widget.StartY = event.y

    # The following function notes mouse position when left clicked and
    # dragged to start draging control
    def dragMotion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.StartX + event.x
        y = widget.winfo_y() - widget.StartY + event.y
        widget.place(x=x, y=y)

# the following class is for main text area
# i.e., the text editor for writing functionality of control
class VTkGText(tk.Text):

    # initiating VTkGText
    def __init__(self, design_or_text_frame):
        super().__init__(design_or_text_frame, height=42, width=100, bg="white")
        self.grid(row= 1, column=0, columnspan=2, sticky='nw')

# the following class is for main design/text area in the middle
class VTkGDesignerOrText(ttk.Frame):

    # flags for checking where is user currently
    design_selected = True
    text_selected = False

    # initiating VTkGDesignerOrText
    def __init__(self, mainApp, properties_frame):
        super().__init__(mainApp, height=900, width=1000, borderwidth=5, relief='groove')

        # 'properties_frame' is reference to properties area in app.
        self.properties_frame = properties_frame

        # configuring rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=14)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # setting the following TRUE will
        # set the size of container based on size of control
        # so keep it FALSE (recommended)
        self.grid_propagate(False)

        # the following is top design_tab to switch between design and text editor
        self.design_tab = ttk.Label(self, 
                                 text="Design Editor", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background = "#04909A" if self.design_selected else "#c8fcff", 
                                 padding=8)
        
        self.design_tab.grid(row=0, column=0, sticky='n') # placing control
        self.design_tab.bind("<Button-1>", self.selectAppropriate) # changes to design when left clicked

        # the following is top text_tab to switch between design and text editor
        self.text_tab = ttk.Label(self, 
                                 text="Text Editor", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background= "#04909A" if self.text_selected else "#c8fcff", 
                                 padding=8)
        
        self.text_tab.grid(row=0, column=1, sticky='n') # placing control
        self.text_tab.bind("<Button-1>", self.selectAppropriate) # changes to text editor when left clicked

        # instanciating text editor and canvas
        self.text_canvas = VTkGText(self)
        self.design_canvas = VTkGDesigner(self, self.properties_frame)

        # placing main frame
        self.grid(row=0, column=1, sticky='ns')

    # the following function changes what is displayed, designer or text editor
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

        # configuring color based on selection
        self.design_tab.configure(background="#04909A" if self.design_selected else "#c8fcff")
        self.text_tab.configure(background="#04909A" if self.text_selected else "#c8fcff")