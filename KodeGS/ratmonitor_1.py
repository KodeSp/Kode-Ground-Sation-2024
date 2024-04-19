from PIL import Image, ImageTk
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Monitor(ttk.LabelFrame):
    def __init__(self, master, sensorname, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(text=sensorname, bootstyle="danger")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)

        self.IMAGE_PATH = 'rat2.png'
        self.RED_IMAGE_PATH = "Red_Light_Icon.png"
        self.GREEN_IMAGE_PATH = "Green_Light_Icon.png"

        self.colorbutton = self.GREEN_IMAGE_PATH

        # Display image on a Label widget.
        self.img = ImageTk.PhotoImage(Image.open(self.IMAGE_PATH))
        self.lbl = ttk.Label(self, image=self.img,anchor="center")
        self.lbl.img = self.img  # Keep a reference in case this code put is in a function.
        self.lbl.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")  # Place label in center of parent.

        self.lblcolor = tk.Label(self, text="")
        self.lblcolor.grid(row=1,column=0,sticky="nsew", padx=100, pady=5)

        self.update(0)
    def update(self, impacto):
        if impacto == 0:
            self.lblcolor.configure(bg="green")
        else:
            self.lblcolor.configure(bg="deep pink")













