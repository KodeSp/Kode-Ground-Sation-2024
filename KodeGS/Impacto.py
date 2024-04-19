import ttkbootstrap as ttk

class impacto(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(text="Impacto", bootstyle="danger",width=300)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1, weight=1)

        self.impacto1 = ttk.DoubleVar()
        self.impacto2 = ttk.DoubleVar()

        self.lblimpacto1 = ttk.Label(self, text="Sensor Impacto:", bootstyle= "danger", font=("Arial", 15))
        self.lblimpacto1.grid(row=0,column=0,pady=35,padx=5,sticky="n")

        self.datoimpacto1 = ttk.Label(self, textvariable=self.impacto1, bootstyle="success", font=("Arial", 15, "bold"))
        self.datoimpacto1.grid(row=0,column=1,pady=35,padx=5,sticky="nw")

    def update(self, data1):
        self.impacto1.set(data1)