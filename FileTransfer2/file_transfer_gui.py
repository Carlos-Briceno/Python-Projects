# this is importing all the modules 
from tkinter import *
import tkinter as tk
from tkinter import ttk

import FileTransfer2
import file_transfer_func
# this is defing all the buttons in tkinter 
def load_gui(self):
    self.btn_from = tk.Button(self.master, width=5, height=2, background = '#ffffff', text='From:',
                            command = lambda: file_transfer_func.choose_from(self))
    self.btn_from.grid(row=1, column=0, rowspan=4, columnspan=2, padx=(7,0), pady=(30,10),sticky=W)

    self.btn_to = tk.Button(self.master, width=5, height=2, background = '#ffffff', text='To:',
                            command = lambda: file_transfer_func.choose_to(self))
    self.btn_to.grid(row=1, column=2, rowspan=4, columnspan=2, padx=(6,0), pady=(30,10),sticky=E)

    self.btn_transfer = tk.Button(self.master, width=30, height=2, background = 'lightblue', text='File Check',
                            command = lambda: file_transfer_func.file_check(self))
    self.btn_transfer.grid(row=6, column=0, rowspan=2, columnspan=4, padx=(8,0), pady=(15,10))

# this is being passed to the main mfile that will run the program
if __name__== "__main__":
    pass
