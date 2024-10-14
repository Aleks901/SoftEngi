from models import *
from Pictures import *
import tkinter as tk
from tkinter import ttk

lysbryter = Unit("Bryter1", True)
varmeovn = Heating("Varm1", True, 10)
lightswitch = Lightswitch("lysbryter", False)

"""
Eksisterte for å teste at hvert nye objekt fikk en unik id
print(lysbryter.unit_id)
print(varmeovn.unit_id)
"""

def create_unit(name: str, unit_type):
    if unit_type == "Varme":
        new_unit = Heating(name)
        return new_unit
    elif unit_type == "Lys":
        new_unit = Lightswitch(name)
        return new_unit

root = tk.Tk()
root.title("Homehub")
root.geometry("800x600")
# File meny
file_button = ttk.Button(root, text="File")
file_button.place(x=0, y=0)
edit_button = ttk.Button(root, text="Edit")
edit_button.place(x=75, y=0)
about_button = ttk.Button(root, text="About")
about_button.place(x=150, y=0)
# /File meny
root.mainloop()
        
    
