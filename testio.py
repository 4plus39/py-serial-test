import platform
import glob
import serial
import sys


class SerialPort(object):
    def __init__(self, name):
        self.name = name
        self.port = serial.Serial()
        self.device = []
        self.system = platform.system()

    def scan(self):
        ports = None
        if self.system.lower() == "linux":
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif self.system.lower() == "windows":
            ports = ['COM%s' % (i + 1) for i in range(256)]
        else:
            print("Unknown os")
            
        self.try_port(ports)
            
    def try_port(self, ports):
        for port in ports:
            try:
                sp = serial.Serial(port)
                sp.close()
                self.device.append(port)
            except (OSError, serial.SerialException):
                pass
                
        self.device.sort()

    def check(self):
        # It's can be simplified than "if self.device == []:"
        if not self.device:
            print("\n No serial port was found...")
            print(" Please confirm you are root or admin.\n")
            sys.exit()

    def list(self):
        for index in range(len(self.device)):
            print(" Number:", index, "   ", "Device:", self.device[index])

    def input(self):
        self.name = self.device[int(input(" Input serial device number:"))]

    def config(self, baud_rate, time_out):
        self.port = serial.Serial(self.name, baud_rate, timeout=time_out)

    def send(self):
        self.port.write(str.encode('ATI\r'))

    def read(self):
        return self.port.readlines()
        
    def close(self):
        self.port.close()

