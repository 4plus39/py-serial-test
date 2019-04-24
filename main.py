import time
import keyboard
import testIO
import os

counter = 0

serial = testIO.SerialPort(None)

# text mode interface
print("-------------------------------------")
serial.scan()
print("-------------------------------------")
serial.list()
print("")
serial.input()
print("-------------------------------------")

# serial port settings
serial.config(115200, 0.1)

# show serial port settings
if serial.port.is_open :
    print("Serial port [",serial.name,"] is open")
    time.sleep(1)


while True:
    if serial.system.lower() == "linux":
        os.system('clear')
    elif serial.system.lower() == "windows":
        os.system('cls')

    print("-------------------------------------")
    print("!!! ---Start test--- !!!")
    print("-------------------------------------")
    print( "Serial port =",serial.name)
    print("Baud rate = 115200")
    print("Time out = 0.1")
    print("-------------------------------------")
    print("Succeed count",counter)
    print("-------------------------------------")
    serial.send()
    # print(serial.read())
    time.sleep(0.1)
    counter += 1
    if keyboard.is_pressed('q'):
        print("!!! ---Quit test--- !!!")
        print("-------------------------------------")
        break
