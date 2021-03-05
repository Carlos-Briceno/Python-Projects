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



conn = sqlite3.connect('my.db')

# this will insert the files into the database 


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                ('Hello.txt,'))
    cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                ('myImage.png,'))
    cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                ('myMovie.mpg,'))
    cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                ('World.txt,'))
    cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                ('data.pdf,'))
    cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                ('myPhoto.jpg,'))
    conn.commit()
conn.close()



conn = sqlite3.connect('my.db')

# this will get all the files ending with t

for x in col_fname:
    if x.endswith('t'):
        with conn:
            cur = conn.cursor()
        # will denote a one element tuple for each file ending with t 
            cur.execute("INSERT INTO tbl_file (col_fname) VALUES (?)", (x))
            print(x)
conn.close()
        
        

            


   
