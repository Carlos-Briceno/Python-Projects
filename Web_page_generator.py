
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
Html_file = open("Web_page_generator.html","w")
Html_file.write(html_str)
Html_file.close()

# this is importing tkinter 
import tkinter as tk

import webbrowser

root = tk.Tk()
root.geometry("400x200")

# this is defining setTextInput 
def setTextInput(text):
    with open('Web_page_generator.html', 'w') as file:
        file.write(f'<html><body><h1>{text}</h1></body></html>')
        webbrowser.open('Web_page_generator.html')
        

# this will show in an html file when opened
url = "D:/cxbri/Python-Projects/Web_page_generator.html"
webbrowser.open_new_tab(url)

text = tk.Entry(root)
text.pack()


# this is the button that will show up in tkinter as set
btnSet = tk.Button(root, height=1, width=10, text="Set", command=lambda:setTextInput(text.get()))
btnSet.pack()


root.mainloop()

