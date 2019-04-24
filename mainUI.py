import tkinter as tk
import testIO
import testUI


def scanning():
    # Only do this if the Stop button has not been clicked
    if testUI.running:
        serial.name = app.device.get()
        serial.config(115200, 0.1)
        serial.send()

    # After 0.1 second, call scanning again (create a recursive loop)
    root.after(100, scanning)


serial = testIO.SerialPort(None)
serial.scan()
root = tk.Tk()
app = testUI.UI(root)
app.device['values'] = serial.device

# After 0.1 second, call scanning
root.after(100, scanning)
root.mainloop()
