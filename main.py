import os
import keyboard
import time
import testio
import record
from const import *


def pause():
    try:
        input("\n Press the <ENTER> key to continue...")
    except SyntaxError:
        pass
    clear_screen()


def clear_screen():
    if ser.system.lower() == "linux":
        os.system("clear")
    elif ser.system.lower() == "windows":
        os.system("cls")


def testing():
    rec.timer_start()

    while not keyboard.is_pressed('q'):
        ser.send()
        rec.cnt += 1
        if not ser.read():
            clear_screen()
            print("----------------------------")
            print(" Status: FAILED ")
            rec.fcnt += 1
        else:
            clear_screen()
            print("----------------------------")
            print(" Status: PASS ")
        
        print("----------------------------")
        print(" Serial port =", ser.name)
        print(" Baud rate =", BAUD_RATE)
        print(" Time out =", TIMEOUT)
        print("----------------------------")
        print(" Program is ongoing ", end='')
        if int(time.time()) % 3 == 1:
            print(".")
        elif int(time.time()) % 3 == 2:
            print("..")
        else:
            print("...")
        print("     Press key 'Q' to quit")
        
    rec.timer_end()


if __name__ == '__main__':
    ser = testio.SerialPort(None)
    rec = record.Log()
    ser.scan()
    ser.check()
    clear_screen()
    print("----------------------------------")
    ser.list()
    print("----------------------------------")
    ser.input()
    print('----------------------------------')

    ser.config(BAUD_RATE, TIMEOUT)

    if ser.port.is_open:
        print(" Serial port [ %s ] is open" % ser.name)
        pause()
        testing()
        ser.close()
    
    rec.cfg_output(ser.name)
    clear_screen()
    if rec.end_ts is not None and rec.start_ts is not None:
        rec.log_output(ser.name)
