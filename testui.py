import tkinter as tk
from tkinter import ttk

# Global flag
running = False


class UI:
    def __init__(self, master):
        master.title("Serial Port Test  ")
        master.geometry("200x120")

        frame = tk.Frame(master)
        frame.pack()

        self.testButton = tk.Button(frame, text="Start Test", command=self.start_test)
        self.testButton.grid(row=0, column=0, padx=0, pady=10)

        self.quitButton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=0, column=1, padx=0, pady=10)

        self.device = ttk.Combobox(frame, width=16)
        self.device['values'] = ()
        self.device.config(state='readonly')
        self.device.grid(row=1, column=0, padx=0, pady=0, columnspan=2)

        self.status = tk.Label(frame, text="Status: ")
        self.status.grid(row=2, column=0, padx=0, pady=10)

        self.n_status = tk.Label(frame, text="")
        # self.n_status.grid(row=2, column=1, padx=0, pady=10)

    def start_test(self):
        global running
        running = True

        self.testButton.config(text="Stop test", command=self.stop_test)
        # print(self.device.current(), self.device.get())

        self.n_status.grid(row=2, column=1, padx=0, pady=10)

    def stop_test(self):
        global running
        running = False

        self.testButton.config(text="Start test", command=self.start_test)
        # print(self.device.current(), self.device.get())

        self.n_status.grid_forget()

    def status_pass(self):
        self.n_status.config(text="PASS", bg='green')

    def status_fail(self):
        self.n_status.config(text="FAILED", bg='red')
