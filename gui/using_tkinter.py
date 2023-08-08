import tkinter
import tkinter as tk

# from tkinter import *
# not best practice cause you import more than you need
# n/b everything can be implemented without using padding

root = tk.Tk()  # window
root.geometry("800x500")  # dimensions are in pixels x by y
root.title("My First GUI")  # title of window

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))  # can be initialized without the height
textbox.pack(padx=200)

# button = tk.Button(root, text="Click", font=("Arial", 18))
# button.pack(padx=10, pady=10)

# for a calculator we would need a grid so let's try the grid layout
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# we do not pass root as the master of Button because button is in button_frame and button_frame is in root
btn1 = tk.Button(button_frame, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)  # indexes basically for the start
# sticky is used to stretch buttons across entire row, here we are stretching from west to east

btn2 = tk.Button(button_frame, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(button_frame, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(button_frame, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(button_frame, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(button_frame, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

button_frame.pack(fill="x") # stretch into the x dimension
# myentry = tk.Entry(root) # one-liner entry, useful for passwords
# myentry.pack()

# anotherbtn = tk.Button(root, text="TEST")
# anotherbtn.place(x = 200, y = 200, height=100, width=100) # place widgets where we want

root.mainloop()
