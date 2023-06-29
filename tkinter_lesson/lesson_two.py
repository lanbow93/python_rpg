import tkinter as tk
#Creating root window
root = tk.Tk()

#Creating a Label widget
myLabel1 = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="My Name Is Lance Bowers")
myLabel3 = tk.Label(root, text="SPACE")

#Grid sytem of putting thing on screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1, column=3)
myLabel3.grid(row=1, column=1)

#Launching the program loop
root.mainloop()

