import os
import keyboard
import testio

# CONST NAME
BAU_RATE = 115200
TIME_OUT = 0.5


def pause():
    print()
    input("Press the <ENTER> key to continue...")


def clear_screen():
    if serial_port.system.lower() == "linux":
        os.system("clear")
    elif serial_port.system.lower() == "windows":
        os.system("cls")


def printer():
    count = 0
    f_count = 0
    n_list = []

    while not keyboard.is_pressed('q'):
        print("---Test------------------------------")
        print("Serial port =", serial_port.name)
        print("Baud rate =", BAU_RATE)
        print("Time out =", TIME_OUT)
        print("-------------------------------------")
        print("Press key 'Q' to quit")

        serial_port.send()
        count += 1
        # print(serial_port.read())
        if serial_port.read() == n_list:
            clear_screen()
            print("Status: FAILED ")
            f_count += 1
        else:
            clear_screen()
            print("Status: PASS ")

    print("---Result-----------------------------")
    print("Succeed count:", count)
    print("Failed count:", f_count)
    print("Success rate:", (count-f_count)/count*100, "%")
    print("-------------------------------------")


if __name__ == '__main__':
    serial_port = testio.SerialPort(None)

    # text mode interface
    serial_port.scan()
    print("-------------------------------------")
    serial_port.list()
    print("")
    serial_port.input()
    print('-------------------------------------')

    # serial port settings
    serial_port.config(BAU_RATE, TIME_OUT)

    # show serial port settings
    if serial_port.port.is_open:
        print("Serial port [", serial_port.name, "] is open")
        pause()
        printer()
