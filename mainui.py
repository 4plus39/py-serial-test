import tkinter as tk
import testio
import testui


def scanning():
    # Only do this if the Stop button has not been clicked
    if testui.running:
        serial.name = app.device.get()
        serial.config(115200, 0.5)
        serial.send()

    # After 0.1 second, call scanning again (create a recursive loop)
    root.after(500, scanning)


serial = testio.SerialPort(None)
serial.scan()
root = tk.Tk()
app = testui.UI(root)
app.device['values'] = serial.device

# After 0.1 second, call scanning
root.after(100, scanning)
root.mainloop()
