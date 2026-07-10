import tkinter as tk
from tkinter import ttk

class VTkGPropertiesArea(ttk.Frame):
    def __init__(self, mainApp):
        super().__init__(mainApp, height=900, width=300, borderwidth=5, relief='groove')

        self.main_app_window = tk.Canvas(self, height=200, width=200)
        
        self.properties = {}
        self.valued_properties = {}
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=19)
        
        self.columnconfigure(0, weight=1)

        self.grid_propagate(False)

        self.properties_list = tk.Canvas(self, height=700, width=300)
        self.properties_list.columnconfigure(0, weight=1)
        self.properties_list.columnconfigure(1, weight=1)
        self.properties_list.grid(row=1, column= 0, sticky='nsew')
        
        self.scroller = ttk.Scrollbar(self, command=self.properties_list.yview)
        self.scroller.grid(row=1, column=1, sticky='ns')
        self.properties_list.configure(yscrollcommand=self.scroller.set)

        self.properties_list_frame = ttk.Frame(self.properties_list)
        self.properties_list.create_window((0, 0), window=self.properties_list_frame, anchor="nw")
        self.properties_list_frame.bind("<Configure>", lambda e: self.properties_list.configure(scrollregion=self.properties_list.bbox("all")))


        self.heading = ttk.Label(self, 
                                 text="Properties", 
                                 width=300, font="Arial 14", 
                                 anchor='center', 
                                 background="#c8fcff", 
                                 padding=8)
        
        self.heading.grid(row=0, column=0, columnspan=2, sticky='n')
            
        
        self.grid(row=0, column=2, sticky='ne')
    
    def get_properties_list(self, widget):
        self.properties = list(widget.config().keys())
        self.tree = ttk.Treeview(self.properties_list_frame, columns=("Property", "Value"), show="headings")
        self.tree.heading("Property", text="Property")
        self.tree.heading("Value", text="Value")

        self.tree.column("Property", width=130, anchor="center")
        self.tree.column("Value", width=170, anchor="center")

        for key in range(len(self.properties)):
            self.tree.insert("", "end", values=(self.properties[key][0], ))

            ttk.Label(
                self.properties_list_frame,
                text=self.properties[key],
                padding=(5, 2)
            ).grid(row=key+1, column=0, sticky='w')
            ttk.Entry(
                self.properties_list,
                textvariable=self.valued_properties[self.properties[key]],
                width=20
            ).grid(row=key+1, column=1, sticky='e', padx=2, pady=5)

    def get_properties_list_value(self, widget):
        print("hello")