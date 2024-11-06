from tkinter import ttk
from tkinter import *
from tkinter import Menu
from models.Unit import Unit
from models.Heating import Heating

class DraggableUnit(ttk.Button):
    
    def __init__(self, parent, image, unit_type: str, **kwargs):
        super().__init__(parent, image=image, **kwargs)
        self.parent = parent
        self.image = image 
        self.unit_type = unit_type
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)
        self.bind("<Button-3>", self.open_unit_menu)
        

    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def do_drag(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        self.place(x=x, y=y)
    
    def open_unit_menu(self, event):
        menu = Menu(self, tearoff=0)
        
        if self.unit_type.upper == "Heating".upper:
            menu.add_command(label="Change Temperature")
            
        if self.unit_type.upper == "Heating".upper:
            menu.add_command(label="Turn on")
            
        elif self.unit_type.upper == "Chill".upper:
            menu.add_command(label="Turn on")
        
        elif self.unit_type.upper == "Lightswitch".upper:
            menu.add_command(label="Turn on")
            
        if self.unit_type.upper == "Doorbell".upper:
            menu.add_command(label="Open Camera View")
        
        menu.add_command(label="Options")
        
        menu.post(event.x_root, event.y_root)

