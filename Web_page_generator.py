import subprocess
import os

# this will show in an html file when opened
url = "D:/cxbri/Python-Projects/Web_page_generator.html"
try: # should work on Windows
    os.startfile(url)
except AttributeError:
    try: # should work on MacOS and most linux versions
        subprocess.call(['open', url])
    except:
        print('Could not open URL')

# this is where the html file is made 
html_str = """
<html>
    <body>
        <h1>
    Stay tuned for our amazing summer sale!
        </h1>
    </body>
</html>
"""
# this is importing tkinter 
import tkinter as tk
root = tk.Tk()
root.geometry("400x200")

# this is defining setTextInput 
def setTextInput(text):
    textExample.delete(0,"end")
    textExample.insert(0, text)

textExample = tk.Entry(root)
textExample.pack()
# this is the button that will show up in tkinter as set 
btnSet = tk.Button(root, height=1, width=10, text="Set", command=lambda:setTextInput("New Text"))
Html_file= open("Web_page_generator.html","w")
Html_file.write(html_str)
Html_file.close()
btnSet.pack()

root.mainloop()

