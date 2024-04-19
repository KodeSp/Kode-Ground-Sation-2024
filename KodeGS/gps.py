import tkinter as tk
import tkinter.ttk as ttk
import tkintermapview
import serialport

class Gps(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.posiciones=[]
        self.map_widget = tkintermapview.TkinterMapView(self, corner_radius=0)
        self.map_widget.grid(row=0,column=0,sticky="nsew")
        #self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
        #                                max_zoom=22)  # google normal
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)  # google satellite


        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        #self.path = self.map_widget.set_path([(48.860381, 2.338594), (47, 2.339594)])

       # self.updateLocation((48.860381, 2.338594))
        #self.updateLocation((47.0, 2.339594))
        self.posiciones.append((48.860381, 2.338594))
        self.posiciones.append((47.0, 2.339594))
        """self.lastPosition = self.posiciones[-1]
        self.map_widget.set_position(self.lastPosition[0], self.lastPosition[1],marker=True)

        path_1 = self.map_widget.set_path(self.posiciones)"""

        self.map_widget.set_zoom(15)


    def updateLocation(self, data):
        self.posiciones.append(data)

        self.lastPosition = self.posiciones[-1]
        self.map_widget.set_position(self.lastPosition[0], self.lastPosition[1], marker=True)

        path_1 = self.map_widget.set_path(self.posiciones)


