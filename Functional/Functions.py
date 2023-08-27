'''Python Functions'''

'''
Covered in this video:
> Function Definition
> Python Indentation and Code Blocks
> Function Calling
> returning values 
> Parameters (variables)
> Arguements (values)
> Functions with Conditionals, While Loops, and For Loops
'''
#Sequential --> a program executes from top to bottom, left to right
#Functions help simplify code

'Function Definition'
#teaching the computer how to perform a function

def function_name():
  #indent 2 spaces to be apart of the function definition block
  'Code Block Here'
#unindent 2 spaces to exit the function definition

#------------------------------#
def function_name(): #----#    #
  'Code Block Here'       #    #
  #-----------------------#    #
#------------------------------#

'Function Calling'
#telling the computer to perform a function

#call the function with its name, and parenthesis.
function_name() #caller

#functions must be defined before they are called


'return'
#-------------------------------------------------------------------------#
def bring_back():                                                         #
  #return is the keyword to send a function's result back to the caller   #
  return "this is the result" #returning exits the function               #
#-------------------------------------------------------------------------#

#calling
bring_back() 

#when using return place the call in a print() to see the result
print(bring_back())

#assigning the return to a variable
result = bring_back()
print(result) 


'Parameters'
#parameters are variables that represent unknown values in the function definition
#def function_name(parameter1, parameter2, ...):
#-------------------------------------------------------------------------#
def accept_values(parameter_1,parameter_2):                               #
  #seperate multiple parameters with comma ","                            #
  print(parameter_1)                                                      #        
  print(parameter_2)                                                      #
#-------------------------------------------------------------------------#

#calling
accept_values("Hello", "World")


'Arguments'
#arguments are the actual values used when calling the function

#-------------------------------------------------------------------------#
def accept_values(parameter_1,parameter_2):                               #
  print(parameter_1)                                                      #        
  print(parameter_2)                                                      #
#-------------------------------------------------------------------------#

#calling
#function_name(argument1,argument2,...)
accept_values("Hello", "World")
#arguments are the actual values used when calling the function
#multiple arguements are seperated with a comma

#there must be one arguement for every one parameter or you will get an error.

'Functions with Conditionals, While Loops, and For Loops'

def even_or_odd(num):
  if(num % 2 == 0):
    print("num is even")
  else:
    print("num is odd")

#calls
even_or_odd(1)
even_or_odd(2)
even_or_odd(3)
even_or_odd(4)

def count_up(start, stop, step):
  count = start
  while (count <= stop):
    print(count, end= " ")
    count += step
  print()

#calls
count_up(1,10,1)
count_up(50,100,10)
count_up(0,24,8)
count_up(5,500,5)
count_up(40,60,2)

def count_for(start, stop, step):
  for count in range(start, stop, step):
    print(count, end = " ")
  print()

#calls
count_for(0,-36,-1)
count_for(10,21,2)
count_for(-10,-6,1)
count_for(-5,16,5)
