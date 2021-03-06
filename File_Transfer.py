import shutil
import os
from os import path


# set where the source of the files are
source = 'D:/cxbri/Python-Projects/FolderA/'

# set the destination path to folder b
destination = 'D:/cxbri/Python-Projects/FolderB'
files = os.listdir(source)


for i in files:
    # this will move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

def main():
    if path.exists("File1.txt, File2.txt, File3.txt, File4.txt"):
               src = path.realpath("File1.txt, File2.txt, File3.txt, File4.txt");

               head,tail = path.split(src)
               print("path:" + head)
               print("file:" + tail)


            
               

from tkinter import *
from tkinter import ttk
from tkinter import filedialog



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Choose a File")
        self.minsize(640, 400)
        

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)


        self.button()



    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

      

    def fileDialog(self):
        
        self.filename = filedialog.askopenfilename(initialdir =  "D:\cxbri\Python-Projects", title = "Select A Folder", filetype =
        (("txt files","*.txt"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)


    



root = Root()
root.mainloop()



if __name__=="__main__":
    main()

