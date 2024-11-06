import tkinter as tk
from tkinter import *

class DraggableButton(tk.Button, tk.Menu):

    def __init__(self, parent, bg="black", fg="red", **kwargs):
        """_Klassen eksisterer for å kunne lage en representasjon av en enhet
            som kan dras rundt på blueprint kartet._

        Args:
            parent (_type_): _tk library_
            bg (str, optional): _Setter bakgrunn farge_. Defaults to "black".
            fg (str, optional): _Setter tekst farge_. Defaults to "red".
        """
        if bg is not None:
            kwargs['bg'] = bg
        if fg is not None:
            kwargs['fg'] = fg
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)
        self.bind("<Button-3>", self.menu)


    def start_drag(self, event):
        """_Simpelt forklart, når en event som et trykk skjer 
        så kjøres funksjonen_

        Args:
            event: _tkinter magi_
        """
        self.start_x = event.x
        self.start_y = event.y


    def do_drag(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        self.place(x=x, y=y)
        
        
    def menu(self, event):
        """_Menyen når du høyre klikker på en enhet_

        Args:
            event: _tkinter magi_
        """
        menu = tk.Menu(self.parent, tearoff=0)
        menu.add_command(label="Set timer", command=lambda: print("New home controller"))
        menu.add_command(label="Set temperature", command=lambda: print("Open home controller"))
        menu.add_command(label="Options", command=lambda: options(self.parent))
        menu.post(event.x_root, event.y_root)

    
def options(parent):
        """_Representasjon av options vinduet_"""
        window = tk.Toplevel(parent)
        window.title("Options")
        window.geometry("300x300")
        slider = tk.Scale(window, orient=HORIZONTAL)
        slider.pack()

        
def create_draggable_button(parent, text, x, y):
        """_Produserer ny enhet via file menyen_"""
        button = DraggableButton(parent, text=text)
        button.place(x=x, y=y)
        return button
