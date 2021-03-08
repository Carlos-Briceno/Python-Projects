import sqlite3


filelist = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


conn = sqlite3.connect('my.db')


with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT \
            )")
        conn.commit()
conn.close()





# this will insert the files into the database




# this will get all the files ending with t

conn = sqlite3.connect('my.db')

# this will get all the files ending with t

for x in filelist:
    if x.endswith('t'):
        with conn:
            cur = conn.cursor()
        # will denote a one element tuple for each file ending with t
            cur.execute("INSERT INTO tbl_file (col_fname) VALUES (?) ", (x,))
            print(x)
        conn.commit()
conn.close()






