import tkinter as tk
import testio
import testui
import const
import record


def loop():
    if testui.FLAG and app.device.get() is not None:
        # Repeat config same serial port will show "PermissionError" in Windows OS,but linux wouldn't
        if ser.name != app.device.get():
            # Change test port,so close the previous port
            ser.close()
            ser.name = app.device.get()
            ser.config(const.BAUD_RATE, const.TIMEOUT)
            rec.timer_start()
            rec.cnt = 0
        
        rec.cnt += ser.send()

        if not ser.read():
            app.status_fail()
            rec.fcnt += 1
        else:
            app.status_pass()
    print("sc", rec.cnt)
    print("sc", rec.fcnt)
    # After LOOP_TIME millisecond, call loop() again
    root.after(const.LOOP_TIME, loop)


if __name__ == '__main__':
    ser = testio.SerialPort(None)
    ser.scan()
    ser.check()
    root = tk.Tk()
    app = testui.UI(root)
    rec = record.Log()
    
    app.device.set(rec.conf_read())
    app.device['values'] = ser.device

    # After LOOP_TIME millisecond, call loop()
    root.after(const.LOOP_TIME, loop)
    root.mainloop()
    
    rec.timer_end()
    
    rec.conf_save(ser.name)
    
    ser.close()
    
    if rec.end_ts is not None and rec.start_ts is not None:
        rec.file_rep()
