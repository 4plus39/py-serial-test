import os
import keyboard
import testio
import const
import time


def pause():
    print()
    try:
        input(" Press the <ENTER> key to continue...")
    except SyntaxError:
        pass
    clear_screen()


def clear_screen():
    if serial_port.system.lower() == "linux":
        os.system("clear")
    elif serial_port.system.lower() == "windows":
        os.system("cls")


def timer():
    timestamp = time.time()
    time_format = time.strftime("%m-%d %H:%M:%S", time.localtime())
    return timestamp, time_format


def testing():
    count = 0
    failed_count = 0

    start_timestamp, start_time = timer()

    while not keyboard.is_pressed('q'):
        print("-------------------------------------")
        print(" Serial port =", serial_port.name)
        print(" Baud rate =", const.BAUD_RATE)
        print(" Time out =", const.TIMEOUT)
        print("-------------------------------------")
        print(" Press key 'Q' to quit")
        
        print(" Program is ongoing ", end='')
        if int(time.time())%3 == 1:
            print(".")
        elif int(time.time())%3 == 2:
            print("..")
        else:
            print("...")

        serial_port.send()
        count += 1
        if serial_port.read() == const.NULL_LIST:
            clear_screen()
            print("-------------------------------------")
            print(" Status: FAILED ")
            failed_count += 1
        else:
            clear_screen()
            print("-------------------------------------")
            print(" Status: PASS ")
    
    end_timestamp, end_time = timer()
    report(count, failed_count, start_time, end_time, end_timestamp-start_timestamp)


def report(count, failed_count, start_time, end_time, execution_time):
    clear_screen()
    print("┌───────────────────────────────────────┐")
    print("│ Succeed count:\t%15d │" % (count-failed_count))
    print("│ Failed count:\t\t%15d │" % failed_count)
    print("│ Success rate:\t\t%14.2f%% │" % ((count-failed_count)/count*100))
    print("│ Start time: \t\t", start_time, "│")
    print("│ End time: \t\t", end_time, "│")
    print("│ Execution time:\t %13.2fs │" % execution_time)
    print("└───────────────────────────────────────┘")


if __name__ == '__main__':
    serial_port = testio.SerialPort(None)
    clear_screen()

    serial_port.scan()
    serial_port.check()
    print("-------------------------------------")
    serial_port.list()
    print("-------------------------------------")
    serial_port.input()
    print('-------------------------------------')

    serial_port.config(const.BAUD_RATE, const.TIMEOUT)

    if serial_port.port.is_open:
        print(" Serial port [", serial_port.name, "] is open")
        pause()
        testing()
        serial_port.close()

