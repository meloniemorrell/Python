import tkinter as tk
import shutil
import os
import glob
import datetime
from tkinter import filedialog
from python_232 import*


# Create the master object
master = tk.Tk()
#create window title
master.title('File Transfer')
#Width, height 
master.minsize(400,150)


originPath = '/Users/Mely Mel/Desktop/SourceA'

originPath2 = '/Users/Mely Mel/Desktop/Destination/B'



#first function paired with first button

def opendirectory():
    rep = filedialog.askdirectory(parent=master, initialdir=originPath)
    if rep:
        e1.delete(0)
        e1.insert(0,rep)

    else:
        print('Cancelled') 

def opendirectory2():
   rep = filedialog.askdirectory(parent=master, initialdir=originPath2)
   if rep:
        e2.delete(0)
        e2.insert(0,rep)

   else:
        print('Cancelled') 


def GetFileList():
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob('/Users/Mely Mel/Desktop/*/*.txt')
    



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

