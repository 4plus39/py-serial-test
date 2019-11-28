import tkinter as tk
import testio
import testui
import record
from const import *


def loop():
    if testui.FLAG and app.device.get() is not None:
        # Repeat config same serial port will show "PermissionError" in Windows OS,but linux wouldn't
        if ser.name != app.device.get():
            # Change test port,so close the previous port
            ser.close()
            ser.name = app.device.get()
            ser.config(BAUD_RATE, TIMEOUT)
            rec.timer_start()
            rec.cnt = 0
        
        rec.cnt += ser.send()

        if not ser.read():
            app.status_fail()
            rec.fcnt += 1
        else:
            app.status_pass()
    # After LOOP_TIME millisecond, call loop() again
    root.after(LOOP_TIME, loop)


if __name__ == '__main__':
    ser = testio.SerialPort(None)
    ser.scan()
    ser.check()
    root = tk.Tk()
    app = testui.UI(root)
    rec = record.Log()
    
    app.device.set(rec.cfg_input())
    app.device['values'] = ser.device

    # After LOOP_TIME millisecond, call loop()
    root.after(LOOP_TIME, loop)
    root.mainloop()
    
    rec.timer_end()
    
    rec.cfg_output(ser.name)
    
    ser.close()
    
    if rec.end_ts is not None and rec.start_ts is not None:
        rec.log_output(ser.name)
