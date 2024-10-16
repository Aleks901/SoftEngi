import tkinter as tk
from draggable import *

# Demo prosjekt av ideen til gruppa.

# Hoved vinduet
root = tk.Tk()
root.title("Home Hub")
root.geometry("800x600")
root.anchor("center")
"""background_image = tk.PhotoImage(file="blueprint.png")
label = tk.Label(root, image=background_image)
label.place(relwidth=1, relheight=1)"""
background_frame = tk.Frame(root, bg="black", bd=0)
background_frame.place(relx=0.5,rely=0.5, anchor="center")

#funkjsoner
def devices_window():
    """
    Lager et vindu for devices
    """
    device_window = tk.Toplevel(root)
    device_window.title("Devices")
    
    #Finner hvor root vinduet er, også setter den geometry slik at den
    #Spawner rett til høyre for vinduet.
    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    device_window.geometry(f"300x{root_height}+{root_x + root_width}+{root_y}")
    
    #Ferdig produserte draggable button objekter
    demo_button1 = create_draggable_button(root, "Lys bryter", 50, 200)
    demo_button2 = create_draggable_button(root, "Varme ovn", 150, 180)
    demo_button3 = create_draggable_button(root, "Kaffe maskin", 600, 200)
    demo_button4 = create_draggable_button(root, "Lys", 100, 100)
    #Lukker vinduet
    button = tk.Button(device_window, text="Close", command=device_window.destroy)
    button.pack(pady=10)
    
def create_new_object():
    """_Produserer nytt objekt vindu_
    """
    create_window = tk.Toplevel(root)
    create_window.title("Add Device")
    create_window.geometry("300x300")
    name_label = tk.Label(create_window, text="Name:")
    name_label.pack()
    name_field = tk.Text(create_window, height = 1, width = 20)
    name_field.pack()
    end_button = tk.Button(create_window, text="Create", command=lambda: create_draggable_button(root,name_field.get(1.0, "end-1c"),50,50))
    end_button.pack()
    
    
def file_menu(event):
    """Lager en dropdown meny for filen

    Args:
        event (_dropdown_): _event_
    """
    menu = tk.Menu(root, tearoff=0)
    
    menu.add_command(label="New home controller", command=lambda: print("New home controller"))
    menu.add_command(label="Open home controller", command=lambda: print("Open home controller"))
    menu.add_command(label="Save home controller", command=lambda: print("Saved the home controller"))
    menu.add_command(label="Add new device", command=lambda: create_new_object())
    
    menu.post(event.x_root, event.y_root)
    

# Top menyen
# Hjem knappen
home_button = tk.Button(root, text="File")
home_button.place(x=0,y=0)
home_button.bind("<Button-1>", file_menu)
# Devices knappen
devices_button = tk.Button(root, text="Devices", command=devices_window)
devices_button.place(x=30,y=0)
# About knappen
about_button = tk.Button(root, text="About")
about_button.place(x=82,y=0)



root.mainloop()
