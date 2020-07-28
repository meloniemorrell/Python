import sqlite3


try:
    sqliteConnection = sqlite3.connect('File_DB.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query =  """INSERT INTO FILES
                            (FileId, FileName) 
                           VALUES
                          (1,'information.docx','Hello.txt','myImage.png', 
                           'myMovie.mpg','World.txt','data.pdf','myPhotol.jpg',500)"""
                            
    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into FILES table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
