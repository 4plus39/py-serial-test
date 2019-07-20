import os
import keyboard
import testio
import const
import time


def pause():
    print()
    try:
        input("Press the <ENTER> key to continue...")
    except SyntaxError:
        pass
    clear_screen()


def clear_screen():
    if serial_port.system.lower() == "linux":
        os.system("clear")
    elif serial_port.system.lower() == "windows":
        os.system("cls")


def printer():
    all_count = 0
    fail_count = 0
    
    start_clock = time.time()
    start_time = time.strftime("%m-%d %H:%M:%S", time.localtime())

    while not keyboard.is_pressed('q'):
        print("---Test------------------------------")
        print("Serial port =", serial_port.name)
        print("Baud rate =", const.BAU_RATE)
        print("Time out =", const.TIME_OUT)
        print("-------------------------------------")
        print("Press key 'Q' to quit")

        serial_port.send()
        all_count += 1
        # print(serial_port.read())
        if serial_port.read() == const.NULL_LIST:
            clear_screen()
            print("-------------------------------------")
            print("Status: FAILED ")
            fail_count += 1
        else:
            clear_screen()
            print("-------------------------------------")
            print("Status: PASS ")
    
    end_clock = time.time()
    end_time = time.strftime("%m-%d %H:%M:%S", time.localtime())
    clear_screen()
    print("┌───────────────────────────────────────┐")
    print("│ Succeed count:\t%15d │" %(all_count-fail_count))
    print("│ Failed count:\t\t%15d │" %fail_count)
    print("│ Success rate:\t\t%14.2f%% │" %((all_count-fail_count)/all_count*100))
    print("│ Start time: \t\t", start_time+" │")
    print("│ End time: \t\t", end_time+" │")
    print("│ Execution time:\t %13.2fs │" %(end_clock - start_clock))
    print("└───────────────────────────────────────┘")


if __name__ == '__main__':
    serial_port = testio.SerialPort(None)
    clear_screen()

    # text mode interface
    serial_port.scan()
    print("-------------------------------------")
    serial_port.list()
    print("")
    serial_port.input()
    print('-------------------------------------')

    # serial port settings
    serial_port.config(const.BAU_RATE, const.TIME_OUT)

    # show serial port settings
    if serial_port.port.is_open:
        print("Serial port [", serial_port.name, "] is open")
        pause()
        printer()
