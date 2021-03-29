# importing all the modules 
import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import shutil
import datetime
from datetime import timedelta
import time

import FileTransfer2
import file_transfer_gui

# defining the center_window 
def center_window(self, w, h): 
    
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# defing the ask_quit and displaying a message when you exit the program 
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

# defing the the from button on tkinter and the function of it 
def choose_from(self):
  self.src = filedialog.askdirectory()
  print(self.src)

# defing the to button on tkinter and the function of it 
def choose_to(self):
  self.dst = filedialog.askdirectory()
  print(self.dst)



# defing the file check button on tkinter and the function of it 
def file_check(self):
    files = os.listdir(self.src)
    print (files)
    for i in files:
        new_files = datetime.datetime.now() - datetime.timedelta(hours=24)
        mod_time = datetime.datetime.fromtimestamp(os.stat(self.src + '/' + i).st_mtime)
        if mod_time > new_files:
            shutil.move((self.src + '/' + i), self.dst + '/' + i)
            print(i + "\nhas been moved.\n")
