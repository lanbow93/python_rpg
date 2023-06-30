import tkinter as tk
#Creating root window
root = tk.Tk()

#Creating an input box
e = tk.Entry(root, width=50, bg="black", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name:")

#Function to assign to the button
def myClick():
    hello = "Hello " + e.get() #e.get() retreived the input in e
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()

#Creating a button and setting function for when it is clicked
my_button = tk.Button(root, text="Enter Your Name", command=myClick, bg="purple", fg="#FFFFFF")
my_button.pack(padx=10, pady=10)

#Launching the program loop
root.mainloop()

