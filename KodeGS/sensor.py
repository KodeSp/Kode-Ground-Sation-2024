import ttkbootstrap as ttk
class Sensor(ttk.LabelFrame):
    def __init__(self, master, sensorname, units, total, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(text=sensorname, bootstyle="danger")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.sensordata = ttk.DoubleVar()

        #self.lbldata = ttk.Label(self, textvariable=self.sensordata, font=("Arial", 10, "bold"))
        #self.lbldata.pack()

        self.meter = ttk.Meter(self, bootstyle="danger", metersize=180,
                            padding=5,
                            amounttotal=total,
                            amountused=self.sensordata.get(),
                            metertype="semi",
                            subtext=units,
                            subtextstyle="success",
                            interactive=False)
        self.meter.grid(row=0,column=0,sticky="ew")

    def updatedata(self, data):
        self.sensordata.set(data)
        self.meter.configure(amountused=self.sensordata.get())