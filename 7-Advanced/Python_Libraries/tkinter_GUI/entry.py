#Tkinter GUI

from tkinter import *

root = Tk() #initializes this interpreter and creates the root window. 
root.title("How to provide input.")#gives the window a title

#creating a label for the input box
entry_label = Label(root, text="Enter your name below")
entry_label.pack()

#creating the input box
some_input = Entry(root,width=50,borderwidth=5)
some_input.pack()

#creating the function of a button
def on_click():
  button_label = Label(root,text=f"Hello, {some_input.get()}")# use .get method to use the input.
  button_label.pack()

#creating a button to perform the function
a_button = Button(root, text="Submit",command=on_click)
a_button.pack()

#calling mainloop of the window
root.mainloop() 