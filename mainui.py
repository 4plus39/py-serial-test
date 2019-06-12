import tkinter as tk
import testio
import testui

# CONST NAME
BAU_RATE = 115200
TIME_OUT = 0.5
NULL_LIST = []


def loop():
    # Only do this if the Stop button has not been clicked
    if testui.running and app.device.current() != -1:
        serial_port.name = app.device.get()
        serial_port.config(BAU_RATE, TIME_OUT)
        serial_port.send()

        if serial_port.read() == NULL_LIST:
            app.status_fail()
        else:
            app.status_pass()

    # After 0.1 second, call loop() again (create a recursive loop)
    root.after(TIME_OUT, loop)


serial_port = testio.SerialPort(None)
serial_port.scan()
root = tk.Tk()
app = testui.UI(root)
app.device['values'] = serial_port.device

# After 0.1 second, call scanning
root.after(TIME_OUT, loop)
root.mainloop()
