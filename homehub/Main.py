from models import *
from Pictures import *
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

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
    
def new_window():
    window = tk.Tk()
    window.geometry("800x600")
    window.mainloop()
    
# Hoved vindu
root = tk.Tk()
root.title("Homehub")
root.geometry("800x600")

# File meny
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label='New controller', command=new_window)
file_menu.add_command(label='Open controller')
file_menu.add_command(label='Exit', command=root.destroy,)
about_menu = Menu(menubar, tearoff=0)
about_menu.add_command(label='ReadMe')
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="About", menu=about_menu)
# /File meny
root.mainloop()
# /Hoved vindu
        
    
