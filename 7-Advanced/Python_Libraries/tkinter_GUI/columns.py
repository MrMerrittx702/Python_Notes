#Tkinter GUI

from tkinter import *

root = Tk()
root.title("Using columns and rows.")

#position of text is determined by a grid system. 
Label1 = Label(root, text="This is row 0, column 0").grid(row=0, column=0)
Label2 = Label(root, text="This is row 1,column 1").grid(row=1, column=1)

#or define the grid as below.
#Label1.grid(row=0, column=0)
#Label2.grid(row=1, column=1)

root.mainloop() #mainloop of the window