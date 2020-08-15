import tkinter as tk
import shutil
import os
import glob
import datetime
from tkinter import filedialog


# Create the master object
master = tk.Tk()
#create window title
master.title('File Transfer')
#Width, height 
master.minsize(400,150)


originPath = '/Users/Mely Mel/Desktop/A'





#first function paired with first button

def opendirectory():
    rep = filedialog.askdirectory(parent=master, initialdir=originPath)
    if rep:
        print(rep)
    else:
        print('Cancelled') 


 


# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)
   
 
# Pack them using grid
e1.grid(row=0, column=1, columnspan=1, ipadx=55)
e2.grid(row=1, column=1, columnspan=1, ipadx=55)






#create first button
button1 = tk.Button(master, text="Browse...", command = opendirectory)
button1.grid(row=0, column=0, columnspan=1, ipadx=19,pady=10, padx=20)






 
 
# Create another button
button2 = tk.Button(master, text="Browse...")
button2.grid(row=1, column=0, columnspan=1, ipadx=19, pady=10, padx=20)



# Create another button
button3 = tk.Button(master, text="Check for files...")
button3.grid(row=2, column=0, columnspan=1, ipadx=2, pady=10, padx=5)











 
# The mainloop
tk.mainloop()






if __name__ == "__main__":
    name()

