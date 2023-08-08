import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.menuabar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menuabar, tearoff=0)  # tear off removes dash line at top
        self.filemenu.add_command(label="Close on command", command=exit)
        self.filemenu.add_separator()  # gives a separator line between two coomands
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.actionmenu = tk.Menu(self.menuabar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        self.menuabar.add_cascade(menu=self.actionmenu, label="File")
        self.menuabar.add_cascade(menu=self.filemenu, label="Action")
        self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 16), command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)
        self.root.config(menu=self.menuabar)
        self.label = tk.Label(self.root, text="Your message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)  # used to bind certain functionality, must be exact same string
        self.textbox.pack(padx=10, pady=10)
        self.check_state = tk.IntVar()  # contains state of variable
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 16), variable=self.check_state)
        # need to add a variable to check
        self.check.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text="Show message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        # print(self.check_state.get())  # gets the state of the checkbox
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))  # need a start and end [start is 1.0 end is END]
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))  # prints in terminal

    def shortcut(self, event):
        # print(event.keysym)
        # print(event.state)
        # in this case for key bindings check for which button joins the state
        # return == enter button on keyboard
        if event.state == 4 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        # print("Hello World!")
        if messagebox.askyesno(title="Quit?", message="Do you really wan to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete("1.0", tk.END)


MyGUI()
