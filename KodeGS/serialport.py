import serial
import terminal

class SerialPort():
    def __init__(self):

        self.ser = serial.Serial('COM3', baudrate=9600)
        self.line=""
        self.lectura = 0
        self.temp = 0
        self.presion = 0
        self. altitud = 0
        self. latitud = 0
        self.longitud = 0
        self.impacto = 0
        self.mensaje = [0,0,0,0,0,0,0]

    def actualizar(self):
            try:

                self.line = self.ser.readline().decode()  # read a '\n' terminated line
                #print(line)
                self.mensaje = self.line.split(",")

                self.lectura = self.mensaje[0]
                self.temp = self.mensaje[1]
                self.presion = self.mensaje[2]
                self.latitud = self.mensaje[4]
                self.longitud = self.mensaje[5]
                self.altitud = self.mensaje[6]
                self.impacto = self.mensaje[7]

            except:
                print("Lectura incompleta")

            try:
                with open("data.csv", "a") as f:
                    f.write(self.line)
                print("Lectura Registrada")

            except:
                print("Error de escritura en archivo")
