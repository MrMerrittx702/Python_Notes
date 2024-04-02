#===============================================================================================================================#
'''Python Data Types, Variables, and Basic Function Calls'''
#===============================================================================================================================#
'''
Covered in this file:
  > General Syntax
  > Beginner Data Types (5 most common)
  > All Data Types
  > Sequence (Top to Bottom, Left to Right)
  > Print Function Call
  > Literals (actual values)
  > Variables (containers that store values)
  > Type Annotations: Declaring Variable Type
  > Aliases (reference the same data)
  > Input Function Call
  > Nesting (put one thing inside of another)
'''
#===============================================================================================================================#
'> General Syntax'
#Syntax (rules for writing the language)
#Code is executed from top to bottom left to right
#Every open needs a close: (), "", '', [], {}, <>
#Indentation is required in Python --> if,elif,else,while,for,def,class,etc.
#To a computer code is either perfectly written or it is wrong

#===============================================================================================================================#
'> Beginner Data Types'

#Literals (are actual values)(they do not represent something else)
True          # boolean(True or False)
5             # integer (whole number)
3.14          # float (decimal number)
"a"           # character (single symbol) in quotes use "" or ''
"Hello World" # String (text) in quotes use "" or '' 



["a","b","c"] # list (contains multiple items called elements)
# 0   1   2   # indexes (are used to access each element)

#There are more data types but these are the main types for beginners.
#===============================================================================================================================#
'> All Data Types'
'''
  Data types are classified into two groups
  Mutable "you can change the data it holds" 
      (Lists, Dictionaries, Sets)
  Immutable " you cannot change the data it holds" 
      (numbers, booleans, strings, tuples)
'''
#The type() function can be used to check the type of data
type()


#For large numbers you can use underscores(_) to make them more readable
1_000_000_000 #1000000000 --> Notice it doesn't output with the underscores

# Scientific notation is also available use E to represent (x 10^)
1E9 #1000000000.0 --> Notice it returns a float

1j               # Complex Numbers (j replaces i as the imaginary unit--> sqrt(-1) imaginary numbers)
("a","b","c")    # Tuples a collection which is ordered, immutable and allows duplicate members.
{"a","b","c"}    # Sets a collection which is unordered, unchangeable*,unindexed, and allows NO duplicate members.
{"a":97,"b":98 } # Dictionaries are a collection of key:value pairs; they are ordered**, mutable, and allows NO duplicate members.

#Additional data types are defined by classes, here are a few examples:
range(5)            # Ranges represent a sequence of numbers 
bytearray(b'hello') # Byte Arrays are mutable sequences of bytes
None                # Null type meaning nothing

#===============================================================================================================================#
'> Sequence (Top to Bottom, Left to Right)'
#Python code is executed from top to bottom, left to right, and line by line. 
#1 Top,Left >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Top,Right>
#2    V
#3        V
#4            V
#5                V  Python
#6                    V  Requires
#7                        V  Indentation
#8                            V  In Its
#9                                V  Syntax
#10                                   V 
#11                                       V
#12                                            V
#13                                                 V
#14                                                     V
#15                                                         V
#16                                                             V
#17                                                                 V
#18 Bottom,Left >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Bottom,Right>

#===============================================================================================================================#
'> The Print Function Call'

#top to bottom
print()
print("Hello World")
print(5)
print(3.14)
print(1j)
print(True)
print(False)

#left to right
print(); print("Hello World")


#after printing the cursor goes to a new line
#use ,end = "" to keep the cursor on the same line
print("Hello")
print("World")
#vs.
print("Hello", end = "")
print("World")
#===============================================================================================================================#
'> Data Literals'
#Literal refers to a notation for representing a fixed actual value
#Literals do not represent something else

True              # boolean literal
10                # integer literal
2.17              # float literal
5j                # complex literal
"Hello"           # string literal
["a","b","c"]     # list literal
("a","b","c")     # tuple literal
{"a","b","c"}     # set literal 
{"a":97,"b":98 }  # dictionary literal

#===============================================================================================================================#
'> Variables are containers that store data values'

# use a single equals sign (=) to assign a value to a variable.
# the equal sign must always be on the left side of the operation

# a variable stores a literal
container = "Hello World"

#assigning variables
a = "Hello World"
b = 5
c = 3.14
d = False
e = ["a","b","c"]

f = 2; g = 3; h = 4 #assign on the same line with ";"
#or
i , j , k = 5, 6, 7 

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
    > Variables should be named after what they store/represent
'''

#Legal Variable Names
var = 0
_var = 0
_v_ar = 0
vAr = 0
VAR = 0
var1 = 0 

#Illegal Variable Names
'''
1var = 0
v-ar = 0
v ar = 0 
'''

#===============================================================================================================================#
'> Aliases'
a = "some text"

#you can assign one variable to store another (this is an alias)
b = a 
c = b
print(c)


#===============================================================================================================================#
'> Type Annotations: Declaring Variable type'

' > Type Annotation is a way to declare the type of data the variable is expected to store, but is not enforced by the interpretor'
#variable_name: type = literal
boolean: bool = True
num: int = 10
flo: float = 3.14
unreal: complex = 1j
string: str = "Hello World"
list1d: list = ["a","b","c"]
tuple1d: tuple = ("a","b","c")
set1d: set = {"a","b","c"}
dictionary: dict = {"a": 97, "b": 98, "c":99}

#===============================================================================================================================#
'> The Input Function Call'
#prompts the user to provide input data (values)

input()# the program will stop here and wait for the user to type in a value

input("This is a prompt for the user: ")

#The input can be stored inside of a variable
user_input = input("Please input a value: ")

#You can ask for multiple inputs
first_name = input("First name: ")
last_name = input("Last name: ")

print(first_name)
print(last_name)

#input() treats each value as a string. you will need to convert to use numbers. 
integer_ = int(input("Write a whole number: "))
float_ = float(input("Write a decimal number: "))

#===============================================================================================================================#
'> Nesting'
#to put one thing inside of another. 

#examples:
#Nested lists[[][][][]]
[[1,2,3][4,5,6][7,8,9]]

#nested conditionals
if():
  if():
    if():
      ...

#nested while loops
while():
  while():
    while():
      ...

#nested for loops
for _ in range():
  for _ in range():
    for _ in range():
      ...
      
#Nested function calls function(function(function(function())))
print(int(input("Type a number")))
#The input function is inside of the int function which is inside of the print function.

#===============================================================================================================================#
'> Coding Style Guide'
'''
  Use 4-space indentation, and no tabs.
  4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). 
    Tabs introduce confusion, and are best left out.

  Wrap lines so that they don't exceed 79 characters.

  Use blank lines to separate functions and classes, and larger blocks of code inside functions.

  When possible, put comments on a line of their own

  Use docstrings

  Use spaces around operators and after commas, but not directly inside bracketing constructs:
      a = f(1, 2) + g(3, 4)
      
  Name your classes and functions consistently; the convention is to
      use UpperCamelCase for classes
      use lower_snake_case for functions and methods.
      Always use self as the name for the first method argument

'''
#===============================================================================================================================#



