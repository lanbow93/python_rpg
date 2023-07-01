import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Image Tkinter Tutorial")
# root.iconbitmap("/home/lanbow93/relearn_python/tkinter_lesson/banking.ico")


my_img1 = ImageTk.PhotoImage(Image.open("images/FLCL.PNG"))
my_img2 = ImageTk.PhotoImage(Image.open("images/Coding_Class.PNG"))
my_img3 = ImageTk.PhotoImage(Image.open("images/Diaries.PNG"))
my_img4 = ImageTk.PhotoImage(Image.open("images/Insight_Tracker_Logo.PNG"))
my_img5 = ImageTk.PhotoImage(Image.open("images/Sesshomaru.PNG"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = tk.Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)



    


button_back = tk.Button(root, text="<<" )
button_exit = tk.Button(root, text="Exit Program", command=root.quit)
button_forward = tk.Button(root, text=">>", command=go_forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()