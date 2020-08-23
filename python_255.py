# Importing necessary packages 
import tkinter as tk
import os
import shutil
import glob
import datetime
from tkinter import filedialog
from tkinter import messagebox




# Create the master object
master = tk.Tk()
#create window title
master.title('File Transfer')
#Width, height 
master.minsize(400,150)


def SourceBrowse():
    rep = filedialog.askdirectory()
    if rep:
        e1.delete(0)
        e1.insert(0,rep)

    else:
        print('Cancelled')
	
def DestinationBrowse():
    rep = filedialog.askdirectory()
    if rep:
        e2.delete(0)
        e2.insert(0,rep)

    else:
        print('Cancelled')

def DestinationBrowse():
    rep = filedialog.askdirectory()
    if rep:
        e2.delete(0)
        e2.insert(0,rep)

    else:
        print('Cancelled')



src_dir = "C:\\Users\\Mely Mel\\Desktop\\SourceA\\"
dst_dir = "C:\\Users\\Mely Mel\\Desktop\\Destination B\\" 
files = os.listdir(src_dir)
path = 


def DestinationCheck():
    for i in files:
            # Get last modified date and today's date
            modifyDate = os.path.getmtime
            creationDate = os.path.getctime
            modifyDateLimit = timedelta(days=1)
            shutil.move(src_dir+i,dst_dir)
         
      



#Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)
   
 
# Pack them using grid
e1.grid(row=0, column=1, columnspan=1, ipadx=55)
e2.grid(row=1, column=1, columnspan=1, ipadx=55)


# Create the button object using master
b1 = tk.Button(master)





#create 1st button
button1 = tk.Button(master, text="Browse...", command = SourceBrowse)
button1.grid(row=0, column=0, columnspan=1, ipadx=19,pady=10, padx=20)

 
 
# Create 2nd button
button2 = tk.Button(master, text="Browse...",command = DestinationBrowse)
button2.grid(row=1, column=0, columnspan=1, ipadx=19, pady=10, padx=20 )
	
 
# Create 3rd button
button3 = tk.Button(master, text="Check for files...", command = DestinationCheck) 
button3.grid(row=2, column=0, columnspan=1, ipadx=2, pady=10, padx=5)
	
	
	
# Defining infinite loop 
master.mainloop()




if __name__ == "__main__":
    name()



