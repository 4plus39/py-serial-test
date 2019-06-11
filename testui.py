import tkinter as tk
from tkinter import ttk

# Global flag
running = False


class UI:
    def __init__(self, master):
        master.title("Serial Port Test  ")
        master.geometry("200x90")

        frame = tk.Frame(master)
        frame.pack()

        self.testButton = tk.Button(frame, text="Start Test", command=self.start_test)
        self.testButton.grid(row=0, column=0, padx=0, pady=10)

        self.quitButton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=0, column=1, padx=0, pady=10)

        self.device = ttk.Combobox(frame, width=16)
        self.device['values'] = ()
        self.device.config(state='readonly')
        self.device.grid(row=1, column=0, padx=0, pady=0,columnspan=2)

    def start_test(self):
        self.testButton.config(text="Stop test", command=self.stop_test)
        global running
        running = True
        # print(self.device.current(), self.device.get())

    def stop_test(self):
        self.testButton.config(text="Start test", command=self.start_test)
        global running
        running = False
        # print(self.device.current(), self.device.get())
