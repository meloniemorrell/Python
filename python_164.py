import sqlite3

conn = sqlite3.connect('File_DB.db')



with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_FILES(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_FileName TEXT \
    )")
    conn.commit()
conn.close()



conn = sqlite3.connect('File_DB.db')



with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('information.docx'))
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('Hello.txt'))
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('myImage.png'))
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('myMovie.mpg'))
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('World.txt'))
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_FILES(col_FileName) VALUES(?)",\
                ('myPhotol.jpg'))
    conn.commit()
conn.close()

conn = sqlite3.connect('File_DB.db')

with conn:
    cur = conn.cursor()
    cur.executive("SELECT col_FileName FROM tbl_FILES WHERE col_FileName = '().txt'")
    varFiles = cur.fetchall()
    for item in varFiles:
        msg = "File Name: ()".format(item[0])
    print(msg)



