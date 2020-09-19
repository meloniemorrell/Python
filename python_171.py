import sqlite3

conn = sqlite3.connect('test.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_techacad( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList STRING \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_techacad (col_fileList) VALUES \
                ('information.docx'), \
                ('Hell.txt'), \
                ('myImage.png'), \
                ('myMovie.mpg'), \
                ('World.txt'), \
                ('data.pdf'), \
                ('myPhoto.jpg')"
                )
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileList FROM tbl_techacad WHERE col_fileList LIKE '%xt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = 'File name: {}'.format(item)
        print(msg)
    
