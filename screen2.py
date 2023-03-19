import tkinter as tk
from tkinter import ttk
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
        self.button1["command"] = self.open_window
        self.button1.pack(side="left")

        self.button2 = tk.Button(self)
        self.button2["text"] = "Button 2"
        self.button2["command"] = self.run_code2
        self.button2.pack(side="right")

    def open_window(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Input Window")
        self.new_window.geometry("300x150")

        self.label = tk.Label(self.new_window, text="Enter a number:")
        self.label.pack()

        self.entry = ttk.Entry(self.new_window, width=20)
        self.entry.pack(pady=10)

        self.keypad_button = tk.Button(self.new_window, text="Show Keypad", command=self.show_keypad)
        self.keypad_button.pack()

        self.submit_button = tk.Button(self.new_window, text="Submit", command=self.submit)
        self.submit_button.pack()

    def show_keypad(self):
        # Define a new Toplevel window for the keypad
        self.keypad_window = tk.Toplevel(self.master)
        self.keypad_window.title("Keypad")
        self.keypad_window.geometry("300x300")

        # Create the buttons for the keypad
        buttons = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            ".", "0", "⌫"
        ]
        for i in range(len(buttons)):
            button = tk.Button(self.keypad_window, text=buttons[i], width=5, height=2)
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            button.bind("<Button-1>", self.keypad_button_click)

    def keypad_button_click(self, event):
        # Add the clicked button to the input field
        button = event.widget
        text = button.cget("text")
        if text == "⌫":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        else:
            self.entry.insert(tk.END, text)

    def submit(self):
        # Get the input value and pass it to the code file
        a = self.entry.get()
        subprocess.Popen(["python", "C:\Academics\sem6\EDL\EDL-Project\test1.py",a])

    def run_code2(self):
        subprocess.Popen(["python", "C:\Academics\sem6\EDL\EDL-Project\test2.py"])

root = tk.Tk()
app = Application(master=root)
app.mainloop()
