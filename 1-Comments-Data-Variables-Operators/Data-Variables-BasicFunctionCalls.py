#===============================================================================================================================#
'''Python Data Types, Variables, and Basic Function Calls'''
#===============================================================================================================================#
'''
Covered in this file:
    > General Syntax
    > Data Types
    > Literals (data)
    > Variables (pointers to data)
    > Type Annotations: Declaring Variable Type
    > Aliases (point to the same location)
    > Print Function Call
    > Input Function Call
    > Nesting (put one thing inside of another)
'''
'''
Vocabulary
    > Syntax
    > Scope/Context
    > Nesting
    > Function
    > Function Call
    > Class
    > Method
    > Argument
    > Literal
    > Mutable
    > Immutable
    > Variable
    > Memory
    > Collection
    > Member
    > Null
    > Reference
    > Alias
    > Annotation
    > Interpreter
    > Parameter
    > Cursor
    > Standard Output
    > Standard Input
'''
#===============================================================================================================================#
'> General Syntax'

' > Syntax (rules for writing the language)'
' > Code is executed from top to bottom left to right'
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

' > Every open needs a close: (), "", '', [], {}, <>'

'' # single quotes
"" # double quotes
() # parenthesis
[] # square brackets
{} # curly braces

' > Indentation is required in Python --> if,elif,else,while,for,def,class,etc.'
'   > it is used to define scope or context of code blocks.'

... # > place holder

'Conditionals'
if(...):
    ... #indented code block
#unindent to exit scope
elif(...):
    ... #indented code block
#unindent to exit scope
else:
    ... #indented code block
#unindent to exit scope

'While Loops'
while(...):
    ... #indented code block
#unindent to exit scope

'For Loops'
for _ in ...:
    ... #indented code block
#unindent to exit scope

'Function Definitions'
def function():
    ... #indented code block
#unindent to exit scope

'Class Definitions'
class foo():
    ... #indented code block
#unindent to exit scope

' > Python Programming Style Guide'
'''

  Use 4-space indentation, and no tabs. Editors like VSCode automatically covert for you.

    > 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). 
    > Tabs introduce confusion, and are best left out.

  Wrap lines so that they don't exceed 79 characters.

  Use blank lines to separate functions and classes, and larger blocks of code inside functions.

  When possible, put comments on a line of their own

  Use docstrings to document functions and classes.

  Use spaces around operators and after commas, but not directly inside bracketing constructs:
      a = f(1, 2) + g(3, 4)
      
  Name your classes and functions consistently; the convention is to
      > UpperCamelCase for classes
      > lower_snake_case for functions and methods.
      > Always use self as the name for the first method argument

'''


' > To a computer code is either perfectly written or it is wrong'

#===============================================================================================================================#
'> Data Types'

'  > Beginner'
#Literals (are actual values)(they do not represent something else)
True          # boolean(True or False)
5             # integer (whole number)
3.14          # float (decimal number)
"a"           # character (single symbol) in quotes use "" or ''
"Hello World" # String (text) in quotes use "" or '' 



["a","b","c"] # list (contains multiple items called elements)
# 0   1   2   # indexes (are used to access each element)

#There are more data types but these are the main types for beginners.

'> All Data Types'
'''
  Data types are classified into two groups
  Mutable "you can change the data it holds" 
      (Lists, Dictionaries, Sets)
  Immutable " you cannot change the data it holds" 
      (numbers, booleans, strings, tuples)
'''


#The type() function returns the type of data passed to it.
type()

type(None)                   #<class 'NoneType'>
type(True)                   # <class 'bool'>
type(5)                      # <class 'int'>
type(3.14)                   # <class 'float'>
type(1j)                     # <class 'complex'>
type("a")                    # <class 'str'>
type("Hello")                # <class 'str'>
type(["a","b","c"])          # <class 'list'>
type(("a","b","c"))          # <class 'tuple'>
type({"a","b","c"})          # <class 'set'>
type({"a":97,"b":98,"c":99}) # <class 'dict'>



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
'> Variables'
'   > act like containers that store data values.'
'   > however, variables are pointers that reference a location in memory where a data value is stored.'

# use a single equals sign (=) to assign a value to a variable.
# the equal sign must always be on the left side of the operation

# a variable stores a literal
container = "Hello World"

#assigning variables
# assigning a variables defines where the variable points to in memory.
a = "Hello World"
b = 5
c = 3.14
d = False
e = ["a","b","c"]

f = 2; g = 3; h = 4 #assign on the same line with ";"
#or
i , j , k = 5, 6, 7 

# change a variables value (reassigning)
# reassigning a variable changes where it points to in memory.
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
    > Variables should be named after what they store/reference
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
!var = 0
@#$%@ = 0
'''

'   > Variables are pointers to locations in memory.'
#Use the id() function call to return the memory location to which variable points.
# Returns a <class 'int'> that is a unique identifier for a location in memory where the data is stored.
# The number will potentially be different each time the program is executed. 
memory_pointer = "Hello World"
id(memory_pointer) # 139029363861936

memory_pointer = 10
id(memory_pointer) # 139029373780496

#===============================================================================================================================#
'> Aliases'
'   > assigning one variable to store another variable is called aliasing.'
'   > the variables pass a reference to the data they store.'
a = "some text"

#a, b, and c are aliases (ie they point to the same data)
b = a 
c = b
print(a)     # some text
print(b)     # some text
print(c)     # some text
print(id(a)) # 125810368587504 <-- Same Memory Location
print(id(b)) # 125810368587504 <-- Same Memory Location
print(id(c)) # 125810368587504 <-- Same Memory Location


# Pointing the variable 'a' to a new value
a = "a was changed"
print(a)     # a was changed
print(b)     # some text
print(c)     # some text
print(id(a)) # 125810368883120 <-- New Memory Location
print(id(b)) # 125810368587504 <-- Same Memory Location
print(id(c)) # 125810368587504 <-- Same Memory Location

# Pointing the variable 'b' to a new value
b = "b was changed"
print(a)     # a was changed
print(b)     # b was changed
print(c)     # some text
print(id(a)) # 125810368883120
print(id(b)) # 125810368882544 <-- New Memory location
print(id(c)) # 125810368587504 
 
# Pointing the variable 'c' to a new value.
c = "c was changed"
print(a)     # a was changed
print(b)     # b was changed
print(c)     # c was changed
print(id(a)) # 125810368883120 <-- Different Memory Location
print(id(b)) # 125810368882544 <-- Different Memory Location 
print(id(c)) # 125810368880496 <-- Different Memory Location


# If variables point to the same mutable data type: 
# a change in the data is reflected in all the variables. 
a = [1,2,3]
b = a
c = b
c[0] = 999
print(a)     # [999, 2, 3]
print(b)     # [999, 2, 3]
print(c)     # [999, 2, 3]
print(id(a)) # 125810368584576 <-- Same Memory Location 
print(id(b)) # 125810368584576 <-- Same Memory Location
print(id(c)) # 125810368584576 <-- Same Memory Location

#===============================================================================================================================#
'> Type Annotations: Declaring Variable type'

' > Type Annotation is a way to declare the type of data the variable is expected to store, but is not enforced by the interpreter'
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
'> The Print Function Call'

'  > Prints out data to standard output (std.out) or to a file.'
print()                   #
print(True)               # True
print(10)                 # 10
print(2.17)               # 2.17
print(5j)                 # 5j
print("Hello World")      # Hello World
print(["a","b","c"])      # [a,b,c]
print(("a","b","c"))      # (a,b,c)
print({"a","b","c"})      # {a,b,c} 
print({"a":97,"b":98})    # {a:97,b:98}

' > Print multiple comma seperated values.'
print("one", "two", "three", "four")
#one two three four

' > end parameter'
#by default after printing the cursor goes to a new line
#use ,end = "" to keep the cursor on the same line
print("Hello")
print("World")
# Hello
# World
#vs.
print("Hello", end = "") #default is a newline character
print("World")
# HelloWorld

' > sep parameter'
# specifies a separator between each value.
print("Hello", "World", sep = ":") #Default is a single space
#Hello:World

' > file parameter'
#specifies a file to write the output
print("Hello World", file = "output.txt") #default is std.out

' > flush parameter'
#specifies if the output buffer will be flushed after printing
print("Hello World", flush = True) #default is False

'''
the output buffer refers to a temporary storage area where the data to be printed by the print() function 
is held before it's actually displayed. 

When you call print(), Python doesn't immediately write the output to the console or file. 
Instead, it stores the output in this buffer until certain conditions are met.
'''

#===============================================================================================================================#
'> The Input Function Call'

' > pauses the program and wait for the user to provide input data' 
input()# the program will stop here and wait for the user to type in a value
#input reads from Standard Input (stdin)

' > prompt parameter'
input(prompt = "This is the prompt for the user: ")
#or
input("This is a prompt for the user: ")

' > Storing user input'
#The input can be stored inside of a variable
user_input = input("Please input a value: ")

#You can ask for multiple inputs
first_name = input("First name: ")
last_name = input("Last name: ")

print(first_name)
print(last_name)

' > Numbers as input'
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


