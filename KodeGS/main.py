#import tkinter as tk
#import tkinter.ttk as ttk
import tkinter

import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
import threading
import time
import serial
from PIL import Image
Image.CUBIC = Image.BICUBIC
import terminal_1, ratmonitor_1, Impacto, sensor, gps, serialport



class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0,column=0,sticky="NSEW")
        self.sp = serialport.SerialPort()

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2,weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3,weight=1)
        self.columnconfigure(3, weight=1)

        self.sensortemp = sensor.Sensor(self, "Temperatura", "ºC", 50)
        self.sensortemp.grid(row=1, column=0, padx=10, pady=10,sticky="NSEW")

        self.sensorpres = sensor.Sensor(self, "Presion", "hPa", 1030)
        self.sensorpres.grid(row=1, column=1, padx=5, pady=10,sticky="NSEW")

        self.sensoraltitud = sensor.Sensor(self, "Altitud", "metros", 1500)
        self.sensoraltitud.grid(row=1, column=2, padx=10, pady=10,sticky="NSEW")

        self.ratmtr = ratmonitor_1.Monitor(self, "Monitor")
        self.ratmtr.grid(row=1, column=3, padx=5, pady=10, columnspan=2,sticky="NSEW")

        self.term = terminal_1.Terminal(self, "Terminal")
        self.term.grid(row=2, columnspan=3, padx=10,rowspan=2,sticky="NSEW")

        self.btn_start_serial = ttk.Button(self, text="Start serial", command=self.actualizar,bootstyle="danger")
        self.btn_start_serial.grid(row=2, column=4,padx=5,pady=10,sticky="NSEW")
        self.btn_clear_serial = ttk.Button(self, text="limpiar terminal", command=self.clear_terminal,bootstyle="danger")
        self.btn_clear_serial.grid(row=3, column=4, padx=5,pady=5,sticky="NSEW")

        self.impacto = Impacto.impacto(self)
        self.impacto.update(0)
        self.impacto.grid(row=2, column=3,padx=5,rowspan=2,sticky="NSEW")

        self.gps = gps.Gps(self)
        self.gps.grid(row=4,column=0,columnspan=4,pady=10,sticky="nsew")

        self.logoimg = ImageTk.PhotoImage(Image.open("icono_kode.png"))
        self.logolbl = ttk.Label(self, image=self.logoimg,anchor="center")
        self.logolbl.img = self.logoimg
        self.logolbl.grid(row=4,column=4,padx=5,pady=5,sticky="nsew")

    def actualizar(self):
        self.sp.actualizar()
        try:
            self.term.updatedata(self.sp.line)
        except:
            self.term.updatedata(0)

        try:
            self.sensortemp.updatedata(self.sp.temp)
        except:
            self.sensortemp.updatedata(0)

        try:
            self.sensorpres.updatedata(self.sp.presion)
        except:
            self.sensorpres.updatedata(0)

        try:
            self.sensoraltitud.updatedata(self.sp.altitud)
        except:
            self.sensoraltitud.updatedata(0)

        try:
            self.gps.updateLocation((float(self.sp.latitud),float(self.sp.longitud)))
        except:
            print("No GPS signal")

        try:
            self.impacto.update(self.sp.impacto)
            self.ratmtr.update(int(self.sp.impacto))
        except:
            self.impacto.update(0)
            self.ratmtr.update(0)

        root.after(500,self.actualizar)

    def clear_terminal(self):
        self.term.scrolledtext.delete("1.0", tkinter.END)

root = ttk.Window(themename="vapor")
photo = tkinter.PhotoImage(file = "favicon_kode.png")
root.iconphoto(False, photo)
root.title("KodeSpace Grown Station V.0.1")
myapp = App(root)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)


myapp.mainloop()
