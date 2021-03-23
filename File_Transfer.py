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


if __name__=="__main__":
    main()
               

               
               


