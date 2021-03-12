#
#Python version 3.9.1
#
#Author:    Carlos X. Briceno
#
#Purpose:   Phonebook Demo. Demostrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships.
#
#Tested OS:     This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk

import phonebook_gui

import phonebook_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # This defines the master frame
        self.master = master
        self.master.minsize(500,300) #(Height,Width)
        self.master.maxsize(500,300)

        # This center window will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="slategray")

        # This protocol method is a tkinter buit-in method to catch if 
        # the user clicks the upper corner, "X" on window OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))

        # load in the gui widgets from a seperate module
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
