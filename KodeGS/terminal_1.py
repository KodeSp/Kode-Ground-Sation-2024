import tkinter as tk

import ttkbootstrap as ttk
from tkinter import scrolledtext as st


class Terminal(ttk.LabelFrame):
    def __init__(self, master, sensorname, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(text=sensorname, bootstyle="danger")

        self.scrolledtext = st.ScrolledText(self, padx=5, height=5, state="normal")
        self.scrolledtext.pack(fill=tk.BOTH, expand=True)

        self.updatedata("Datos procedentes de CANSAT\n")


    def updatedata(self, data):
        self.scrolledtext.insert(tk.INSERT, data)
        self.scrolledtext.see("end")






