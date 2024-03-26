#Tkinter GUI

from tkinter import *

root = Tk() #initializes this interpreter and creates the root window. 
root.title("Creating buttons.")#gives the window a title

#creating a button
a_button = Button(root, text="Click Me!")
  
  #state
disabled_button = Button(root, text="Can't Click Me!", state=DISABLED)
  
  #padding x/y
padding_button = Button(root, text="Padded button", padx=50, pady=50)


#creating the function of a button
def on_click():
  button_label = Label(root,text="You Clicked a Working Button.")
  button_label.pack()
  

  #button with function
function_button = Button(root, text="I work", command=on_click)

  #button color change
  #fg foreground bg background
color_change = Button(root, text="In Living Color", command=on_click,fg="white",bg="black")



#placing button on the screen
a_button.pack()
disabled_button.pack()
padding_button.pack()
function_button.pack()
color_change.pack()

#calling mainloop of the window
root.mainloop() 