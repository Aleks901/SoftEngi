from tkinter import ttk
from tkinter import *

class DraggableUnit(ttk.Button):
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)


    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y


    def do_drag(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        self.place(x=x, y=y)
        
    def create_draggable_button(parent, text, x, y):
        """_Produserer ny enhet via file menyen_"""
        button = DraggableUnit(parent, text=text)
        button.place(x=x, y=y)
        return button