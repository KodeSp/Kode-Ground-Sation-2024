import serial
import time

ser = serial.Serial('COM32', baudrate=9600)

while True:
        # x = ser.read()  # read one byte
        #s = ser.read(10)  # read up to ten bytes (timeout)
        line = ser.readline().decode()  # read a '\n' terminated line
        print(line)



