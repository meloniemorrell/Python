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






#first function paired with first button

def opendirectory():
    rep = filedialog.askdirectory()
    if rep:
        e1.delete(0)
        e1.insert(0,rep)

    else:
        print('Cancelled')

#2nd function paired with 2nd button


def opendirectory2():
   rep = filedialog.askdirectory()
   if rep:
        e2.delete(0)
        e2.insert(0,rep)

   else:
        print('Cancelled') 

#if file was accessed or changed  then it needs to be moved to from source to destination folder else print cancelled

def shutil():
    # path  
    path = 'C:/Users/Mely Mel/Desktop/'
     

source = '/Users/Mely Mel/Desktop/SourceA'
 # Create list of text filenames in Origin folder
for files in source:
    # Get last modified date and today's date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(source))
    todaysDate = datetime.datetime.today()
    
    
    # If modified within last 24 hours, then copy to destination folder
    modifyDateLimit = modifyDate + datetime.timedelta(days=1)


      
# Destination path
# Move the content of source to destination  
destination = '/Users/Mely Mel/Desktop/Destination/B'
for files in source:
    if files.endswith(".txt"):
        shutil.move(source, destination) 
        


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
button3 = tk.Button(master, text="Check for files...", command = shutil) 
button3.grid(row=2, column=0, columnspan=1, ipadx=2, pady=10, padx=5)











 
# The mainloop
tk.mainloop()






if __name__ == "__main__":
    name()

