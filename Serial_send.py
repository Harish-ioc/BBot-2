import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(x.encode())  # Encoding the string and sending it
    time.sleep(0.03)
    data = arduino.readline().decode()  # Decoding the received bytes to string
    return data

def write(x):
    arduino.write(x.encode())
    time.sleep(0.05)

def read():
    data=arduino.readline().decode()
    return data

if __name__=="__main__":
    # write('C')  # Send 'C' to Arduino
    print("")
