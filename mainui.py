import tkinter as tk
import testio
import testui
import const
from history import conf_save
from history import conf_read
from history import file_rep


def loop():
    if testui.FLAG and app.device.get() != const.NULL_STR:
        # Repeat config same serial port will show "PermissionError" in Windows OS,but linux wouldn't
        if serial_port.name != app.device.get():
            # Change test port,so close the previous port
            serial_port.close()
            serial_port.name = app.device.get()
            serial_port.config(const.BAUD_RATE, const.TIMEOUT)
        serial_port.send()

        # Maybe can express "if not serial_port.read()"
        if serial_port.read() == const.NULL_LIST:
            app.status_fail()
        else:
            app.status_pass()
    
    # After LOOP_TIME millisecond, call loop() again
    root.after(const.LOOP_TIME, loop)


if __name__ == '__main__':
    serial_port = testio.SerialPort(None)
    serial_port.scan()
    serial_port.check()
    root = tk.Tk()
    app = testui.UI(root)
    

    app.device.set(conf_read())
    app.device['values'] = serial_port.device

    # After LOOP_TIME millisecond, call loop()
    root.after(const.LOOP_TIME, loop)
    root.mainloop()
    
    conf_save(serial_port.name)
    
    serial_port.close()
    
    # file_rep(100, 50, 777, 888, 999)
