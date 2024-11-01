from tkinter import ttk
from tkinter import *

class DraggableUnit(ttk.Button):
    
    def __init__(self, parent, image, **kwargs):
        super().__init__(parent, image=image, **kwargs)
        self.parent = parent
        self.image = image
        self.heating_image = PhotoImage(file="homehub\models\heating_icon.png")
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)

    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def do_drag(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        self.place(x=x, y=y)
    
