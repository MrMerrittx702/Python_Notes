#Tkinter a gui library for python
#note error if you name file tkinter.py
from tkinter import *

root = Tk()
root.title("Creating Labels.")#gives the window a title

#Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")

#Shoving it onto the screen
myLabel.pack()

root.mainloop()
