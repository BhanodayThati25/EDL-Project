import tkinter as tk
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = tk.Button(self)
        self.button1["text"] = "Button 1"
        self.button1["command"] = self.run_code1
        self.button1.pack(side="left")

        self.button2 = tk.Button(self)
        self.button2["text"] = "Button 2"
        self.button2["command"] = self.run_code2
        self.button2.pack(side="right")

    def run_code1(self):
        subprocess.Popen(["python3", "/home/EDL-Project/newint.py"])

    def run_code2(self):
        subprocess.Popen(["python3", "/home/EDL-Project/interold.py"])

root = tk.Tk()
app = Application(master=root)
app.mainloop()
