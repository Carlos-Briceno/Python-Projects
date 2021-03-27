# this is importing all the modules 
from tkinter import *
import tkinter as tk

import file_transfer_gui
import file_transfer_func

# this is setting up tkinter window and getting the sizes, title, color,and a close protocol
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(600,250)
        self.master.maxsize(600,250)
        file_transfer_func.center_window(self,600,250)
        self.master.title("File Tranfer")
        self.master.configure(bg="slategray")
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_transfer_func.ask_quit(self))
        arg = self.master

        file_transfer_gui.load_gui(self)

# this will run the program
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
