from models.Heating import Heating
from models.Lightswitch import Lightswitch
from models.DraggableUnit import DraggableUnit
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import *
import os

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Homehub")
        self.root.geometry("800x600")
        
        heating_image_path = os.path.join("SoftEngi", "homehub", "pictures", "heating_icon.png")
        chilled_image_path = os.path.join("SoftEngi", "homehub", "pictures", "chilled_icon.png")
        sound_image_path = os.path.join("SoftEngi", "homehub", "pictures", "Sound_icon.png")
        self.heating_image = PhotoImage(file=heating_image_path)
        self.chilled_image = PhotoImage(file=chilled_image_path)
        self.sound_image = PhotoImage(file=sound_image_path)
        
        self.init_frames()
        
        self.show_frame("login")

    def init_frames(self):

        self.login_frame = ttk.Frame(self.root)
        self.create_login_frame()
        
        self.logged_in_frame = ttk.Frame(self.root)
        self.create_logged_in_frame()

    def create_login_frame(self):
        username = tk.StringVar()
        password = tk.StringVar()

        username_label = ttk.Label(self.login_frame, text="Username:")
        username_label.pack()

        username_entry = ttk.Entry(self.login_frame, textvariable=username)
        username_entry.pack()
        username_entry.focus()

        password_label = ttk.Label(self.login_frame, text="Password:")
        password_label.pack()

        password_entry = ttk.Entry(self.login_frame, textvariable=password, show="*")
        password_entry.pack()

        login_button = ttk.Button(self.login_frame, text="Login", command=lambda: self.show_frame("logged_in"))
        login_button.pack(pady=10)

        self.login_frame.pack(padx=10, pady=200)

    def create_logged_in_frame(self):
        btn1 = DraggableUnit(self.logged_in_frame, image=self.heating_image)
        btn1.pack()
        btn2 = DraggableUnit(self.logged_in_frame, image=self.chilled_image)
        btn2.pack()
        btn3 = DraggableUnit(self.logged_in_frame, self.sound_image)
        btn3.pack()
        loggedin_text = ttk.Label(self.logged_in_frame, text="Logged in as: TestUser")
        loggedin_text.place(x=0, y=0)

    def show_frame(self, frame_name):
        
        self.login_frame.pack_forget()
        self.logged_in_frame.pack_forget()

        if frame_name == "login":
            self.login_frame.pack(padx=10, pady=200)
        elif frame_name == "logged_in":
            self.logged_in_frame.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Window()
    app.run()
