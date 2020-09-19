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
	cur.execute("INSERT INTO tbl_techacad (fileList) VALUES (?), \
				('information.docx'), \
				('Hell.txt'), \
				('myImage.png'), \
				('myMovie.mpg'), \
				('World.txt'), \
				('data.pdf'), \
				('myPhoto.jpg')
				)
	conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
	cur = conn.cursor()
	cur.execute("SELECT column1 FROM tbl_techacad WHERE col_fileList LIKE '%xt'")
	varFile = cur.fetchone()
	for item in varFile:
            msg = 'Files ending in txt'.format()
        print(msg)	
				
				
