'''Python Comments,Data Types,Print Functions,Variables.'''

# use a hash tag to make a single line python comment

'''
use three single quotes to make a 
multi
line 
comment called a docstring
'''

# Use
# Ctrl + /
# to make quick multi-line comments
# or to comment out a single line easily


############################################################################################################
'''
Covered in this video:
> Single/ Multi-line comments
> Data Types (5 most common)
> Sequence (Top to Bottom, Left to Right)
> Print Function
> Literals (actual values)
> Variables (containers that store values)
> Aliases (reference the same data)
'''
############################################################################################################
'Python Syntax'
#Syntax (rules for writing the language)


############################################################################################################
'Data Types'

#Literals (are actual values)

"Hello World" # String (text) in quotes use "" or '' 
5 # integer (whole number)
3.14 #float (decimal number)
True #boolean(True or False)

["a","b","c"] #list (contains multiple items called elements)
# 0   1   2   #indexes (are used to access each element)

#There are more data types but these are the main types for beginners.

############################################################################################################
#code is executed from top to bottom left to Right
'The Print Function'

#top to bottom
print()
print("Hello World")
print(5)
print(3.14)
print(True)
print(False)

#left to right
print(); print("Hello World")


#after printing the cursor goes to a new line
#use ,end = "" to keep the cursor on the same line
print("Hello")
print("World")
#vs.
print("Hello", end = " ")
print("World")

############################################################################################################
'Variables are containers that store data values'

# use a single equals sign (=) to assign a value to a variable.

# variable //  literal
container = "Hello World"

#assigning variables
a = "Hello World"
b = 5
c = 3.14
d = False
e = ["a","b","c"]

f = 2; g = 3; h = 4 #assign on the same line with ";"

#change a variables value (reassigning)
a = 0
a = 1
a = 2
print(a)


'''
Rules for variable naming:
> They are case sensitive (a and A are not the same)
> Must start with letter or underscore "_"
> Cannot start with a number
> Can only contain a-z, A-Z, 0-9, and "_" characters
> Cannot contain spaces
'''

#Legal Variable Names
var = 0
_var = 0
_v_ar = 0
vAr = 0
VAR = 0
var1 = 0 

#Illegal Variable Names
1var = 0
v-ar = 0
v ar = 0 

############################################################################################################
'Aliases'
a = "some text"

#you can assign one variable to store another (this is an alias)
b = a 
c = b
print(c)




