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
    if sp.system.lower() == "linux":
        os.system("clear")
    elif sp.system.lower() == "windows":
        os.system("cls")


def timer():
    ts = time.time()
    tf = time.strftime("%m-%d %H:%M:%S", time.localtime())
    return ts, tf


def testing():
    cnt = 0
    fcnt = 0
    start_ts, start_tf = timer()

    while not keyboard.is_pressed('q'):
        sp.send()
        cnt += 1
        if not sp.read():
            clear_screen()
            print("----------------------------")
            print(" Status: FAILED ")
            fcnt += 1
        else:
            clear_screen()
            print("----------------------------")
            print(" Status: PASS ")
        print("----------------------------")
        print(" Serial port =", sp.name)
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
    print("┌───────────────────────────────────────┐")
    print("│ Succeed count:\t%15d │" % (cnt-fcnt))
    print("│ Failed count:\t\t%15d │" % fcnt)
    print("│ Success rate:\t\t%14.2f%% │" % ((cnt-fcnt)/cnt*100))
    print("│ Start time: \t\t", start_tf, "│")
    print("│ End time: \t\t", end_tf, "│")
    print("│ Execution time:\t %13.2fs │" % exe_time)
    print("└───────────────────────────────────────┘")


if __name__ == '__main__':
    sp = testio.SerialPort(None)

    sp.scan()
    sp.check()
    clear_screen()
    print("----------------------------------")
    sp.list()
    print("----------------------------------")
    sp.input()
    print('----------------------------------')

    sp.config(const.BAUD_RATE, const.TIMEOUT)

    if sp.port.is_open:
        print(" Serial port [", sp.name, "] is open")
        pause()
        testing()
        sp.close()

