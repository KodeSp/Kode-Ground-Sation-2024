import tkinter

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText


class Terminal(ttk.LabelFrame):
    def __init__(self, master, sensorname, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(text=sensorname, bootstyle="danger")

        # scrolled text with autohide vertical scrollbar
        self.st = ScrolledText(self, padding=5, height=5, vbar=False)
        self.st.pack(fill=BOTH, expand=YES)

        self.updatedata("Datos procedentes de CANSAT\n")


    def updatedata(self, data):
        self.st.insert(tkinter.INSERT, data)




