import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.title("Image Tkinter Tutorial")
# root.iconbitmap("/home/lanbow93/relearn_python/tkinter_lesson/banking.ico")


my_img1 = ImageTk.PhotoImage(Image.open("images/FLCL.PNG"))
my_img2 = ImageTk.PhotoImage(Image.open("images/Coding_Class.PNG"))
my_img3 = ImageTk.PhotoImage(Image.open("images/Diaries.PNG"))
my_img4 = ImageTk.PhotoImage(Image.open("images/Sesshomaru.PNG"))

image_list = [my_img1, my_img2, my_img3, my_img4]


my_label = tk.Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)



def change_image(image_number, direction):
    global my_label
    global button_forward
    global button_back
    global image_list



    if(direction == "forward" and image_number <= len(image_list)):
        my_label.grid_forget()
        button_forward.grid_forget()
        button_back.grid_forget()
        my_label = tk.Label(image=image_list[image_number-1] )
        my_label.grid(row=0, column=0, columnspan=3)

        button_forward = tk.Button(root, text=">>", command=lambda: change_image(image_number + 1, "forward"))
        button_forward.grid(row=1, column=2)

        button_back = tk.Button(root, text="<<", command=  lambda: change_image(image_number - 1, "backward")  )
        button_back.grid(row=1, column=0)
    elif(direction == "backward" and image_number > 0):
        my_label.grid_forget()
        button_forward.grid_forget()
        button_back.grid_forget()
        my_label = tk.Label(image=image_list[image_number-1] )
        my_label.grid(row=0, column=0, columnspan=3)

        button_forward = tk.Button(root, text=">>", command=lambda: change_image(image_number + 1, "forward"))
        button_forward.grid(row=1, column=2)

        button_back = tk.Button(root, text="<<", command=  lambda: change_image(image_number - 1, "backward")  )
        button_back.grid(row=1, column=0)


button_back = tk.Button(root, text="<<")
button_exit = tk.Button(root, text="Exit Program", command=root.quit)
button_forward = tk.Button(root, text=">>", command=lambda: change_image(2, "forward"))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()