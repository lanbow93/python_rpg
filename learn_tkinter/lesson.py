import tkinter as tk

# Create window
root = tk.Tk()

#Size of the window
root.geometry("500x500")

#Set window title
root.title("My Window Title")

# Label is text (parent_object, parameter1, parameter2, )
label = tk.Label(root, text="Hello World", font=("Arial", 18))

# Putting on the window - giving it padding around it
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack()

# my_entry = tk.Entry(root)
# my_entry.pack(padx=10)

# button = tk.Button(root, text="Click Me", font=("Arial", 15))
# button.pack(padx=20, pady=20)

button_frame = tk.Frame(root)

# weight
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)


btn1 = tk.Button(button_frame, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(button_frame, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(button_frame, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(button_frame, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(button_frame, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(button_frame, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

#Stretch into the X dimension 
button_frame.pack(fill="x")

another_btn = tk.Button(root, text="test")
another_btn.place(x=200, y=200, height=100, width=100)

# Calling constructor
root.mainloop()