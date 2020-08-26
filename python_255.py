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


#Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)

 ##shows that you're getting the path successfully
src = e1.get()
print(src)  
##shows that you're getting the path successfully 
dst = e2.get()
print(dst)

files = os.listdir(src)
print(files)



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



def DestinationCheck():
        for i in files: ##starts loop with your file list
            now=datetime.now() ##current time
            timeModified = datetime.fromtimestamp(os.path.getmtime(src +'/'+ i))##finds the time this current individual file was last modified. The src+file gets the absolute path
            timeDiff = (now - timeModified) ##finds the difference between now and when the file was modified
        print (timeDiff)
        if timeDiff > timedelta(days=1): ##See if the difference is larger than one day, if it is, it means the file hasn't been created or modified in the last day
            print ("Status: Old")
            print (i)
        else: ##if its not larger than one day it means its a newly modified or created file
            print ("Status: New")
            print (i)
            shutil.move(src+'/'+i,dst)  ##if you don't use the .join method you need to insert your own slash or it can't find the file



   
 
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



