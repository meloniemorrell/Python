import tkinter as tk


# Create the master object
master = tk.Tk()


#Width, height 
master.minsize(400,150)


 
# Create the entry objects using master
e1 = tk.Entry(master)
e2 = tk.Entry(master)
 
# Pack them using grid
e1.grid(row=0, column=1, columnspan=1, ipadx=55)
e2.grid(row=1, column=1, columnspan=1, ipadx=55)
 
button1 = tk.Button(master, text="Browse...")
button1.grid(row=0, column=0, columnspan=1, ipadx=19,pady=10, padx=20)
 
 
# Create another button
button2 = tk.Button(master, text="Browse...")
button2.grid(row=1, column=0, columnspan=1, ipadx=19, pady=10, padx=20)


# Create another button
button3 = tk.Button(master, text="Check for files...")
button3.grid(row=2, column=0, columnspan=1, ipadx=2, pady=10, padx=5)

# Create another button
button4 = tk.Button(master, text="Close Program")
button4.grid(row=2, column=1, columnspan=1, pady=10, ipadx=2, sticky='SE' )



 
# The mainloop
tk.mainloop()






if __name__ == "__main__":
    name()

