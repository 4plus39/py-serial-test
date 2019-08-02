import tkinter as tk
import testio
import testui
import const
from history import conf_save
from history import conf_read
from history import file_rep
from history import timer


def loop():
    if testui.FLAG and app.device.get() != const.NULL_STR:
        # Repeat config same serial port will show "PermissionError" in Windows OS,but linux wouldn't
        if ser.name != app.device.get():
            # Change test port,so close the previous port
            ser.close()
            ser.name = app.device.get()
            ser.config(const.BAUD_RATE, const.TIMEOUT)
            ser.start_ts, ser.start_tf = timer()
            ser.cnt = 0
        
        ser.cnt += ser.send()

        # Maybe can express "if not ser.read()"
        if not ser.read():
            app.status_fail()
            ser.fcnt += 1
        else:
            app.status_pass()
    
    # After LOOP_TIME millisecond, call loop() again
    root.after(const.LOOP_TIME, loop)


if __name__ == '__main__':
    ser = testio.SerialPort(None)
    ser.scan()
    ser.check()
    root = tk.Tk()
    app = testui.UI(root)
    
    app.device.set(conf_read())
    app.device['values'] = ser.device

    # After LOOP_TIME millisecond, call loop()
    root.after(const.LOOP_TIME, loop)
    root.mainloop()
    
    ser.end_ts, ser.end_tf = timer()
    
    conf_save(ser.name)
    
    ser.close()
    
    if ser.end_ts != None and ser.start_ts != None:
        file_rep(ser.cnt, ser.fcnt, ser.start_tf, ser.end_tf, ser.end_ts-ser.start_ts)

