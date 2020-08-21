import tkinter as tk
import shutil
import os
import stat
import datetime
import glob
from tkinter import filedialog


# Create the master object
master = tk.Tk()
#create window title
master.title('File Transfer')
#Width, height 
master.minsize(400,150)


filetype = '.txt'

originPath = '/Users/Mely Mel/Desktop/SourceA'

originPath2 = '/Users/Mely Mel/Desktop/Destination/B'
files = os.listdir(originPath)


#first function paired with first button

def opendirectory():
    rep = filedialog.askdirectory(parent=master, initialdir=originPath)
    if rep:
        e1.delete(0)
        e1.insert(0,rep)

    else:
        print('Cancelled')

#2nd function paired with 2nd button


def opendirectory2():
   rep = filedialog.askdirectory(parent=master, initialdir=originPath2)
   if rep:
        e2.delete(0)
        e2.insert(0,rep)

   else:
        print('Cancelled') 

#if file was accessed or changed  then it needs to be moved to from source to destination folder else print cancelled


def GetFileList(originPath, filetype):
    # Create list of text filenames in Origin folder
   

    for file in fileList:
        # Get last modified date and today's date
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        todaysDate = datetime.datetime.today()
        
        
        # If modified within last 24 hours, then copy to destination folder
        modifyDateLimit = modifyDate + datetime.timedelta(days=1)

        # If the file was edited less then 24 hours ago then copy it
        if modifyDateLimit > todaysDate:
            shutil.copy2(originPath, originPath2)



# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)
   
 
# Pack them using grid
e1.grid(row=0, column=1, columnspan=1, ipadx=55)
e2.grid(row=1, column=1, columnspan=1, ipadx=55)



#create first button
button1 = tk.Button(master, text="Browse...", command = opendirectory)
button1.grid(row=0, column=0, columnspan=1, ipadx=19,pady=10, padx=20)

 
 
# Create 2nd button
button2 = tk.Button(master, text="Browse...",command = opendirectory2)
button2.grid(row=1, column=0, columnspan=1, ipadx=19, pady=10, padx=20)



# Create 3rd button
button3 = tk.Button(master, text="Check for files...", command = GetFileList) 
button3.grid(row=2, column=0, columnspan=1, ipadx=2, pady=10, padx=5)











 
# The mainloop
tk.mainloop()






if __name__ == "__main__":
    name()

