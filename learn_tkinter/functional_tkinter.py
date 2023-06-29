import tkinter as tk
from tkinter import messagebox
class myGUI:

    def __init__ (self):
        self.root= tk.Tk()

        #Creating a menubar on top
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        
        #Close button in dropdown menu
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        

        # Adding options to dropdown menu
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)
                                                                                                                                                                                                                                                                                                                                                                              
        self.root.title("Pop-up Box")
        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 16))

        #Binding certain KeyPress to a function
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        # Grabes the state of the checkbox
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 18), variable=self.check_state )
        self.check.pack(padx=10, pady=10)

        # Creates button that checks if box is checked, if so runs the message in show_message
        self.button = tk.Button(self.root, text="Show Message" , font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)


        self.cleartbtn = tk.Button(self.root, text="Clear", font=("Arial", 18), command = self.clear )
        self.cleartbtn.pack(padx=10, pady=10)


        # Triggers when window is closed out
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        #If the checkbox is NOT checked
        if(self.check_state.get() == 0):
            # provides the index to start getting information, to the end of the message
            print(self.textbox.get("1.0", tk.END))
        else:
            # Get the ENTIRE message from the textbox and put it in the message box
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))

    def shortcut(self, event):
        #Function trigger close when return + enter are pressed
        if(event.keysym == "Return" and event.state == 20):
            self.show_message()

    
    def on_closing(self):
        #Function to create a window to verify user meant to close
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete("1.0", tk.END)
myGUI()