import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Image Tkinter Tutorial")
# root.iconbitmap("/home/lanbow93/relearn_python/tkinter_lesson/banking.ico")


my_img = ImageTk.PhotoImage(Image.open("FLCL.PNG"))
my_label = tk.Label(image=my_img)
my_label.pack()








button_quit = tk.Button(root, text = "Exit Program", command= root.quit)
button_quit.pack()

root.mainloop()