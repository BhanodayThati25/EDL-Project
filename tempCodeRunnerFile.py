import tkinter as tk
from tkinter import ttk
import test1 as newuser
import test2 as existinguser
from functools import partial

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.state('zoomed')
        #self.master.attributes('-fullscreen', True)
        self.pack()
        self.create_widgets()
        
        # Create a main heading label and pack it at the top of the window
        self.heading_label = tk.Label(self, text="EDL Project", font=("Arial", 36, "bold"))
        #self.heading_label.pack(side="top", pady=20)
        self.heading_label.grid(row=0,column=2,padx=20, pady=20) 

    def create_widgets(self):
        # Create button 1 and pack it to the left half of the screen
        self.button1 = tk.Button(self, text="New User",font=("Arial", 18, "bold"),bd=10,height= 15, width=20,relief='ridge', command=partial(self.show_keypad, 0))
        self.button1.grid(row=2,column=1,padx=20, pady=20) 
        
        # Create button 2 and pack it to the right half of the screen
        self.button2 = tk.Button(self, text="Existing User",font=("Arial", 18, "bold"),bd=10,height= 15, width=20,relief='ridge', command=partial(self.show_keypad, 1))
        self.button2.grid(row=2,column=3,padx=20, pady=20) 


    def show_keypad(self, x):
        # Define a new Toplevel window for the keypad
        self.keypad_window = tk.Toplevel(self.master)
        self.keypad_window.geometry("600x500+340+110")
        #self.keypad_window.overrideredirect(True)
        self.keypad_window.resizable(False, False)
        self.label = tk.Label(self.keypad_window, text="Sample Number:",font=("Arial", 14, "bold"))
        self.label.grid(row=0,column=0,padx=3,pady=10)

        self.entry = ttk.Entry(self.keypad_window, width=15,font=("Arial", 14, "bold"))
        self.entry.grid(row=0,column=2,padx=10,pady=10)
        
        # Create the buttons for the keypad
        buttons = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            ".", "0", "⌫"
        ]
        for i in range(len(buttons)):
            button = tk.Button(self.keypad_window, text=buttons[i],font=("Arial", 14), width=12, height=4,relief='ridge')
            button.grid(row=((i // 3 + 2)-1), column=i % 3,padx=6,pady=3)
            button.bind("<Button-1>", self.keypad_button_click)

        # Create the Submit button
        submit_button = tk.Button(self.keypad_window, text="Submit", font=("Arial", 14),relief='ridge', command=partial(self.submit,x))
        submit_button.grid(row=2,column=3,padx=6,pady=3)
        cancel_button = tk.Button(self.keypad_window, text="Cancel", font=("Arial", 14),relief='ridge', command=self.keypad_window.destroy)
        cancel_button.grid(row=3,column=3,padx=6,pady=3)   

    def keypad_button_click(self, event):
        # Add the clicked button to the input field
        button = event.widget
        text = button.cget("text")
        if text == "⌫":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        else:
            self.entry.insert(tk.END, text)

    def submit(self, x):
        # Get the input value and pass it to the code file
        value = self.entry.get()
        self.keypad_window.destroy()
        if x==0:
            newuser.input(value)
            self.done = tk.Toplevel()
            self.done.title("Completed")
            self.done.geometry("300x200+490+260")
            self.done.resizable(False, False)

            self.label = tk.Label(self.done, text="   Done ",font=("Arial", 40, "bold"))
            self.label.grid(row=0,padx=20,pady=10)      

            ok_button = tk.Button(self.done, text="OK", font=("Arial", 14),relief='ridge', command=self.done.destroy)
            ok_button.grid(row=1,padx=20,pady=10)
        if x==1:
            conc = existinguser.input(value)
            self.results = tk.Toplevel()
            self.results.title("Results")
            self.results.geometry("450x200+415+260")
            self.results.resizable(False, False)

            self.label = tk.Label(self.results, text="   Results: ",font=("Arial", 40, "bold"))
            self.label.grid(row=0,column=0,padx=6,pady=10)      

            self.result_label = tk.Label(self.results, text=int(conc),font=("Arial", 40, "bold"))
            self.result_label.grid(row=0,column=1,padx=6,pady=10)

            ok_button = tk.Button(self.results, text="OK", font=("Arial", 14),relief='ridge', command=self.results.destroy)
            ok_button.grid(row=1,columnspan=2,padx=20,pady=10)

root = tk.Tk()
app = Application(master=root)
app.mainloop()