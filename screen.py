import tkinter as tk
from tkinter import ttk
import test1 as newuser
import test2 as existinguser
from functools import partial
from PIL import ImageTk, Image
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.state('normal')
        self.master.attributes('-fullscreen', True)
        self.pack()
        self.sensor_type()
        self.configure(background="#ADD8E6")
        # Create a main heading label and pack it at the top of the window
        self.heading_label = tk.Label(self, text="EDL Project", font=("Arial", 20, "bold"))
        #self.heading_label.pack(side="top", pady=20)
        self.heading_label.grid(row=0,column=2,padx=20, pady=20) 
        self.heading_label.configure(fg="#001F54", bg="#ADD8E6")

    def sensor_type(self):
        self.button1 = tk.Button(self, text="CYFRA",font=("Arial", 12, "bold"),bd=10,height= 15, width=20,relief='ridge', command=partial(self.create_widgets, 0))
        self.button1.grid(row=2,rowspan=2,column=1,padx=20, pady=20) 
        
        # Create button 2 and pack it to the right half of the screen
        self.button2 = tk.Button(self, text="CEA",font=("Arial", 12, "bold"),bd=10,height= 15, width=20,relief='ridge', command=partial(self.create_widgets, 1))
        self.button2.grid(row=2,rowspan=2,column=3,padx=20, pady=20)

        self.button1.configure(bg="#0077B5", fg="white")
        self.button2.configure(bg="#0077B5", fg="white")

    def create_widgets(self,mode):
        self.home = tk.Toplevel()
        self.home.attributes('-fullscreen', True)
        self.heading_label = tk.Label(self.home, text="EDL Project", font=("Arial", 18, "bold"))
        #self.heading_label.pack(side="top", pady=20)
        self.heading_label.grid(row=0,column=2,padx=20, pady=20)
        self.home.configure(background="#ADD8E6")
        self.heading_label.configure(fg="#001F54", bg="#ADD8E6")

        self.delete = ImageTk.PhotoImage(Image.open("delete.png"))
        self.delete_all = ImageTk.PhotoImage(Image.open("delete_all.png"))
        self.back_p = ImageTk.PhotoImage(Image.open("back.png"))
        # Create button 1 and pack it to the left half of the screen
        self.button1 = tk.Button(self.home, text="New User",font=("Arial", 12, "bold"),bd=10,height= 15, width=20,relief='ridge', command=partial(self.show_keypad, 0, mode))
        self.button1.grid(row=2,rowspan=3,column=1,padx=40, pady=20) 
        
        # Create button 2 and pack it to the right half of the screen
        self.button2 = tk.Button(self.home, text="Existing User",font=("Arial", 12, "bold"),bd=10,height= 15, width=20,relief='ridge', command=partial(self.show_keypad, 1, mode))
        self.button2.grid(row=2,rowspan=3,column=3,padx=40, pady=20) 

        self.button3 = tk.Button(self.home,image=self.delete,text="Delete",font=("Arial", 8, "bold"),relief='ridge',compound="top", command=partial(self.show_keypad, 2, mode))
        self.button3.grid(row=2,column=2,padx=20, pady=20)

        self.button4 = tk.Button(self.home,image=self.delete_all,text="Delete All",font=("Arial", 8, "bold"),relief='ridge',compound="top", command=partial(self.confirm_window,mode))
        self.button4.grid(row=4,column=2,padx=20, pady=20)

        self.back = tk.Button(self.home,image=self.back_p,text="Mode",font=("Arial", 8, "bold"),relief='ridge',compound="top", command=self.back_tab)
        self.back.grid(row=3,column=2,padx=20, pady=20)

        self.button1.configure(bg="#0077B5", fg="white")
        self.button2.configure(bg="#0077B5", fg="white")
        self.button3.configure(bg="#0077B5", fg="white")
        self.button4.configure(bg="#0077B5", fg="white")
        self.back.configure(bg="#0077B5", fg="white")

    def show_keypad(self, x, mode):
        # Define a new Toplevel window for the keypad
        self.keypad_window = tk.Toplevel(self.master)
        self.keypad_window.geometry("500x400+150+40")
        self.keypad_window.overrideredirect(True)
        #self.keypad_window.resizable(False, False)
        self.label = tk.Label(self.keypad_window, text="Sample Number:",font=("Arial", 12, "bold"))
        self.label.grid(row=0,column=0,padx=3,pady=10)

        self.entry = ttk.Entry(self.keypad_window, width=15,font=("Arial", 12, "bold"))
        self.entry.grid(row=0,column=2,padx=10,pady=10)
        
        # Create the buttons for the keypad
        buttons = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            ".", "0", "⌫"
        ]
        for i in range(len(buttons)):
            button = tk.Button(self.keypad_window, text=buttons[i],font=("Arial", 10), width=12, height=4,relief='ridge')
            button.grid(row=((i // 3 + 2)-1), column=i % 3,padx=6,pady=3)
            button.bind("<Button-1>", self.keypad_button_click)

        # Create the Submit button
        submit_button = tk.Button(self.keypad_window, text="Submit", font=("Arial", 12),relief='ridge', command=partial(self.submit,x,mode))
        submit_button.grid(row=2,column=3,padx=3,pady=3)
        cancel_button = tk.Button(self.keypad_window, text="Cancel", font=("Arial", 12),relief='ridge', command=self.keypad_window.destroy)
        cancel_button.grid(row=3,column=3,padx=3,pady=3)   

    def keypad_button_click(self, event):
        # Add the clicked button to the input field
        button = event.widget
        text = button.cget("text")
        if text == "⌫":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)
        else:
            self.entry.insert(tk.END, text)

    def replacing(self,user,mode):
        newuser.input(user,mode)
        self.replace.destroy()
        self.common_window("Done")
        
    def back_tab(self):
        self.sensor_type
        self.home.destroy()

    def replace_window(self,user,mode):
        self.replace = tk.Toplevel()
        self.replace.geometry("300x200+250+140")
        #self.replace.resizable(False, False)
        self.replace.overrideredirect(True)

        self.label = tk.Label(self.replace, text="User Already Exists",font=("Arial", 14, "bold"))
        self.label.grid(row=0,column=0,columnspan=2,padx=15,pady=15)  

        self.labe = tk.Label(self.replace, text="Do you want to replace it?",font=("Arial", 14, "bold"))
        self.labe.grid(row=1,column=0,columnspan=2,padx=15,pady=15)    
        
        ok_button = tk.Button(self.replace, text="OK", font=("Arial", 10),relief='ridge', command=partial(self.replacing, user, mode))
        ok_button.grid(row=2,column=0,padx=20,pady=10)

        cancel = tk.Button(self.replace, text="Cancel", font=("Arial", 10),relief='ridge', command=self.replace.destroy)
        cancel.grid(row=2,column=1,padx=20,pady=10)

    def common_window(self,x):
        self.common = tk.Toplevel()
        self.common.geometry("250x150+275+165")
        #self.common.resizable(False, False)
        self.common.overrideredirect(True)

        self.label = tk.Label(self.common, text=x,font=("Arial", 18, "bold"))
        self.label.grid(row=0,column=0,padx=6,pady=10)      
        self.common.columnconfigure(0, weight=1)
        self.common.rowconfigure(0, weight=1)

        ok_button = tk.Button(self.common, text="OK", font=("Arial", 12),relief='ridge', command=self.common.destroy)
        ok_button.grid(row=1,column=0,padx=20,pady=8)
    
    def confirm_window(self,mode):
        self.confirm = tk.Toplevel()
        self.confirm.geometry("250x150+275+165")
        #self.confirm.resizable(False, False)
        self.confirm.overrideredirect(True)

        self.label = tk.Label(self.confirm, text="Do you want to delete all?",font=("Arial", 12, "bold"))
        self.label.grid(row=0,column=0,columnspan=2,padx=6,pady=30)  

        ok_button = tk.Button(self.confirm, text="OK", font=("Arial", 10),relief='ridge', command=partial(self.deleteall,mode))
        ok_button.grid(row=2,column=0,padx=20,pady=20)

        cancel = tk.Button(self.confirm, text="Cancel", font=("Arial", 10),relief='ridge', command=self.confirm.destroy)
        cancel.grid(row=2,column=1,padx=20,pady=20)

    def submit(self, x, mode):
        # Get the input user and pass it to the code file
        user = self.entry.get()
        self.keypad_window.destroy()
        
        if mode==0:
            file_path = f"/home/pi/Desktop/EDL-Project/CYFRA/{user}.txt"

            if x==0:
                list_of_files = os.listdir('/home/pi/Desktop/EDL-Project/CYFRA')
                full_path = ["/home/pi/Desktop/EDL-Project/CYFRA/{0}".format(x) for x in list_of_files]
    
                if os.path.exists(file_path):
                    self.replace_window(user,mode)
                if len(list_of_files) == 2:
                    oldest_file = min(full_path, key=os.path.getctime)
                    os.remove(oldest_file)
                else:
                    newuser.input(user,mode)
                    self.common_window("Done")

            if x==1:
                        
                if os.path.exists(file_path):
                    conc = existinguser.input(user,mode)
                    text = "Results:"+str(conc)
                    self.common_window(text)
                else:
                    self.common_window("Does not Exist")

            if x==2:
                        
                # Check if the file exists
                if os.path.exists(file_path):
                     # Delete the file
                    os.remove(file_path)
                    self.common_window("Deleted")
                else:
                    self.common_window("User not Found")
        if mode == 1:
            file_path = f"/home/pi/Desktop/EDL-Project/CEA/{user}.txt"
            
            if x==0:
                list_of_files = os.listdir('/home/pi/Desktop/EDL-Project/CEA')
                full_path = ["/home/pi/Desktop/EDL-Project/CEA/{0}".format(x) for x in list_of_files]

                if os.path.exists(file_path):
                    self.replace_window(user,mode)
                if len(list_of_files) == 2:
                    oldest_file = min(full_path, key=os.path.getctime)
                    os.remove(oldest_file)
                else:
                    newuser.input(user,mode)
                    self.common_window("Done")

            if x==1:
                if os.path.exists(file_path):
                    conc = existinguser.input(user,mode)
                    text = "Results:"+str(conc)
                    self.common_window(text)
                else:
                    self.common_window("Does not Exist")

            if x==2:
                # Check if the file exists
                if os.path.exists(file_path):
                    # Delete the file
                    os.remove(file_path)
                    self.common_window("Deleted")
                else:
                    self.common_window("User not Found")

    def deleteall(self,mode):
        self.confirm.destroy()
            # Get all the files in the folder
        if mode==0:
            files = os.listdir("/home/pi/Desktop/EDL-Project/CYFRA")

                # Loop through the files and delete them
            for file_name in files:
                file_path = os.path.join("/home/pi/Desktop/EDL-Project/CYFRA", file_name)
                os.remove(file_path)
        if mode==1:
            files = os.listdir("/home/pi/Desktop/EDL-Project/CEA")

                # Loop through the files and delete them
            for file_name in files:
                file_path = os.path.join("/home/pi/Desktop/EDL-Project/CEA", file_name)
                os.remove(file_path)
        self.common_window("Deleted")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
