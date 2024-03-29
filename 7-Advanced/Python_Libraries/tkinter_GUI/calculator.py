from tkinter import *

root=Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def button_click(num):
  current = e.get()
  e.delete(0,END)
  e.insert(0, str(current) + str(num))
  return

def add():
  number_1 = e.get()
  global f_num
  global math
  math = "+"
  f_num = int(number_1)
  e.delete(0,END)

def sub():
  number_1 = e.get()
  global f_num
  global math
  math = "-"
  f_num = int(number_1)
  e.delete(0,END)

def mult():
  number_1 = e.get()
  global f_num
  global math
  math = "*"
  f_num = int(number_1)
  e.delete(0,END)

def div():
  number_1 = e.get()
  global f_num
  global math
  math = "/"
  f_num = int(number_1)
  e.delete(0,END)

def button_equal():
  second_number = e.get()
  e.delete(0,END)
  if math == "+":
    e.insert(0,f_num + int(second_number))

  if math == "-":
    e.insert(0,f_num - int(second_number))
  
  if math == "*":
    e.insert(0,f_num * int(second_number))

  if math == "/":
    e.insert(0,f_num / int(second_number))

def button_clear():
  e.delete(0,END)

button_0 = Button(root, text="0", padx=88, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
button_mult = Button(root, text="*", padx=40, pady=20, command=mult)
button_div= Button(root, text="/", padx=40, pady=20, command=div)

button_equal = Button(root, text="=", padx=85, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=78, pady=20, command=button_clear)


#placing buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0,columnspan=2)
button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_mult.grid(row=3,column=3)
button_div.grid(row=4,column=3)
button_equal.grid(row=5,column=2, columnspan=2)
button_clear.grid(row=5,column=0, columnspan=2)



root.mainloop()





