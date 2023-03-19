import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.attributes('-fullscreen', True)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = tk.Button(self)
        self.button1["text"] = "Open Window"
        self.button1["command"] = self.open_window
        self.button1.pack(side="left", fill="both", expand=True)

    def open_window(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("New Window")
        self.new_window.geometry("300x150")

        self.button2 = tk.Button(self.new_window)
        self.button2["text"] = "Open Window 2"
        self.button2["command"] = self.open_window2
        self.button2.pack(side="left", fill="both", expand=True)

    def open_window2(self):
        self.new_window2 = tk.Toplevel(self.new_window)
        self.new_window2.title("New Window 2")
        self.new_window2.geometry("300x150")

        self.label = tk.Label(self.new_window2, text="Hello World!")
        self.label.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
