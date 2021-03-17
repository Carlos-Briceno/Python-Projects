

# this will show in an html file when opened

html_str = """
<html>
    <body>
        <h1>
    Stay tuned for our amazing summer sale!
        </h1>
    </body>
</html>
"""

Html_file= open("Web_page_generator.html","w")
Html_file.write(html_str)
Html_file.close()

# this is importing tkinter 
import tkinter as tk
root = tk.Tk()
root.geometry("400x50")

# this is defining setTextInput 
def setTextInput(text):
    textExample.delete(0,"end")
    textExample.insert(0, text)

textExample = tk.Entry(root)
textExample.pack()
# this is the button that will show up in tkinter as set 
btnSet = tk.Button(root, height=1, width=10, text="Set", command=lambda:setTextInput("New Text"))
btnSet.pack()

root.mainloop()

