import os
import keyboard
import testio
import const
import time
from history import timer


def pause():
    print()
    try:
        input(" Press the <ENTER> key to continue...")
    except SyntaxError:
        pass
    clear_screen()


def clear_screen():
    if ser.system.lower() == "linux":
        os.system("clear")
    elif ser.system.lower() == "windows":
        os.system("cls")


def testing():
    cnt = 0
    fcnt = 0
    start_ts, start_tf = timer()

    while not keyboard.is_pressed('q'):
        ser.send()
        cnt += 1
        if not ser.read():
            clear_screen()
            print("----------------------------")
            print(" Status: FAILED ")
            fcnt += 1
        else:
            clear_screen()
            print("----------------------------")
            print(" Status: PASS ")
        print("----------------------------")
        print(" Serial port =", ser.name)
        print(" Baud rate =", const.BAUD_RATE)
        print(" Time out =", const.TIMEOUT)
        print("----------------------------")
        print(" Program is ongoing ", end='')
        if int(time.time())%3 == 1:
            print(".")
        elif int(time.time())%3 == 2:
            print("..")
        else:
            print("...")
        print("     Press key 'Q' to quit")
        
    end_ts, end_tf = timer()
    report(cnt, fcnt, start_tf, end_tf, end_ts-start_ts)


def report(cnt, fcnt, start_tf, end_tf, exe_time):
    clear_screen()
    print("---------------------------------")
    print(" Succeed count : %d " % (cnt-fcnt))
    print(" Failed count  : %d " % fcnt)
    print(" Success rate  : %.2f%% " % ((cnt-fcnt)/cnt*100))
    print(" Start time    : %s" % (start_tf))
    print(" End time      : %s" % (end_tf))
    print(" Execution time: %.2fs" % (exe_time))
    print("---------------------------------")


if __name__ == '__main__':
    ser = testio.SerialPort(None)

    ser.scan()
    ser.check()
    clear_screen()
    print("----------------------------------")
    ser.list()
    print("----------------------------------")
    ser.input()
    print('----------------------------------')

    ser.config(const.BAUD_RATE, const.TIMEOUT)

    if ser.port.is_open:
        print(" Serial port [ %s ] is open" % (ser.name))
        pause()
        testing()
        ser.close()

