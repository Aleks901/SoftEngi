from models.Heating import Heating
from models.Lightswitch import Lightswitch
from models.DraggableUnit import DraggableUnit
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import *


class Window():
    
    #TODO Vurder nødvendigheten av funksjonen
    def create_unit(name: str, unit_type):
        if unit_type == "Varme":
            new_unit = Heating(name)
            return new_unit
        elif unit_type == "Lys":
            new_unit = Lightswitch(name)
            return new_unit
        
        # File meny
    def file_menu(parent):
        menubar = Menu(parent)
        parent.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='New controller')
        file_menu.add_command(label='Open controller')
        file_menu.add_command(label='Save controller')
        file_menu.add_command(label='Exit', command=parent.destroy,)

        about_menu = Menu(menubar, tearoff=0)
        about_menu.add_command(label='ReadMe')

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="About", menu=about_menu)
        # /File meny  
    
    
    def root_window():
        root = tk.Tk()
        root.title("Homehub")
        root.geometry("800x600")
        Window.file_menu(root)        
        username = tk.StringVar()
        password = tk.StringVar()
        signin = ttk.Frame(root)
        signin.pack(padx=10, pady=200)

        username_label = ttk.Label(signin, text="Username:")
        username_label.pack()

        username_entry = ttk.Entry(signin, textvariable=username)
        username_entry.pack()
        username_entry.focus()

        password_label = ttk.Label(signin, text="Password:")
        password_label.pack()
        
        heating_image = PhotoImage(file="homehub\models\heating_icon.png")
        btn = DraggableUnit(root, heating_image)
        btn.place(x=300, y=300)
        
        password_entry = ttk.Entry(signin, textvariable=password, show="*")
        password_entry.pack()
        
        login_button = ttk.Button(signin, text="Login", command=Window.logged_in_window)
        login_button.pack(pady=10)

        root.mainloop()
    
    def logged_in_window():
        root = tk.Tk()
        root.geometry("800x600")
        loggedin_text = ttk.Label(root, text="Logged in as: TestUser")
        loggedin_text.place(x=0, y=0)
        root.mainloop()  