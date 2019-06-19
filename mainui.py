import tkinter as tk
import testio
import testui
import const


def loop():
    if testui.FLAG and app.device.get() != const.NULL_STR:
        serial_port.name = app.device.get()
        serial_port.config(const.BAU_RATE, const.TIME_OUT)
        serial_port.send()

        if serial_port.read() == const.NULL_LIST:
            app.status_fail()
        else:
            app.status_pass()

    # After LOOP_TIME millisecond, call loop() again
    root.after(const.LOOP_TIME, loop)


if __name__ == '__main__':
    serial_port = testio.SerialPort(None)
    serial_port.scan()
    root = tk.Tk()
    app = testui.UI(root)
    app.device['values'] = serial_port.device

    # After LOOP_TIME millisecond, call loop()
    root.after(const.LOOP_TIME, loop)
    root.mainloop()
