import tkinter as tk
#Creating root window
root = tk.Tk()

#Function to assign to the button
def myClick():
    myLabel = tk.Label(root, text="Look! I clicked a button!")
    myLabel.pack()

#Creating a button and setting function for when it is clicked
my_button = tk.Button(root, text="Click Me", command=myClick, bg="purple", fg="#FFFFFF")
my_button.pack(padx=10, pady=10)

#Launching the program loop
root.mainloop()

