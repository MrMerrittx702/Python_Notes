#===============================================================================================================================#
'''Python Functions'''
#===============================================================================================================================#
'''
Covered in this file:
> Function Definition
> Python Indentation and Code Blocks
> Function Calling
> Returning a value: return 
  > Returning multiple values
> Parameters: function variables
  > Default Parameter values
> Arguements: parameter values
> Positional Arguments vs Keyword Arguments
  > Unpacking Arguments
  > Forcing Keyword Arguments
  > Forcing Positional Arguments
> Arbitrary Arguments Lists (*args, **kwargs)
> Scope: Global vs Local
> Builtin Function Calls
> Lambda Expressions
> Documentation Strings
> Function Annotations
> Function Examples Including Control Structures
'''

#Sequential --> a program executes from top to bottom, left to right
#Functions help simplify  and group code

#===============================================================================================================================#
'Function Definition'
'''
  A Function is a self-contained block of code that performs a specific task and can be reused throughout a program. 
    > Abstraction
    > Modularity
    > Reusability
    > Organization

    
  Defining a function is like teaching a computer how to perform a task(function)
    > Name a function after what it is intended to do. 
    > Functions must be defined before they are used. 
'''
#Function Definition
def function_name():
   ...


#General Function Syntax:
#Function  Definition--------------------------------#
def function_name(parameter1,parameter2, ___ ):      #
  #indent into the function definition               #
  ... #What the function does                        #
  return #a value                                    #
#unindent to exit the function definition------------#


#Function Definition Examples
def say_hello():
   print("Hello World")

def count_to(number):
   for num in range(1,number+1):
      print(num, end = " ")
    
#===============================================================================================================================#
'> Python Indentation and Code Blocks'
'''
  Indentation creates blocks of code, which are groups of statements that are executed together as a unit. 
  Each indentation level represents a higher level of code structure(conditionals, loops, functions, classes)
  All statements within the same block must have the same level of indentation. 
  The end of a block is indicated by the decrease in indentation level. 
'''
#examples
condition = True or False

if(condition):
    #start of the if code block
    print("Inside the if statement")

#end of the if code block
while(condition):
    #start of the while code block
    print("Inside the while loop")

#end of the while code block
for _ in range(10):
    #start of the for code block
    print("Inside the for loop")

#end of the for code block
def function_():
    #start of the function code block
    print("Inside of the function definition")

#end of the function code block
  
#Nested Indentation# Blocks inside of blocks
def example_():
    #start of function code block--------------------------#
    for _ in range(5):                                     #
        #start of for code block----------------------#    #
        while(condition):                             #    #
            #start of while code block -----------#   #    #      
            if(condition):                        #   #    #
                #Start of if code block ------#   #   #    #
                print("So many indents!")     #   #   #    #
            #end of if code block-------------#   #   #    #
        #end of while code block------------------#   #    #
    #end of for code block----------------------------#    #
#end of function code block--------------------------------#

'''
Note:
  Indentation is typically achieved using spaces or tabs. 
  Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior. 
  Python 3 disallows mixing tabs and spaces for indentation in the same source file.

  If you are using an editor like VS code using the tab key, and spaces is not a problem. 
'''
#===============================================================================================================================
'Function Calling '
'''
  Calling a function is asking the computer to perform a function we defined
'''

#functions must be defined before they are called

#call the function with its name, and parenthesis.
function_name() #caller



#General Function Call Syntax
#Variables that store some value
argument1 = ...; argument2 = ... #just examples

#Function Call---------------------------#
function_name(argument1,argument2, ...)  #
#----------------------------------------#
#calling the function and providing values to assign to the parameters.

#example function calls
say_hello() # Hello World
count_to(10)# 1 2 3 4 5 6 7 8 9 10 

#===============================================================================================================================
'Returning a value: return'
'''
  > Returning multiple values

  The 'return' keyword is used to send a function's result back to the caller
    > When a function returns it immediately ends, lines after the return do not execute
    > return does not print
    > functions that do not return a value automatically return 'None'
    > None or NULL means nothing or no value
'''

#function definition
def function_name():
    return "Hello World" #returning exits the function  

#Function Call
function_name() #returns Hello World

print(function_name())#prints the return

result = function_name() #assigns the return 


'Returning multiple values'
' > Functions can return multiple values as a tuple'

def return_multiple():
    return "a", "b", "c" #return values are seperated with a comma

#Assigning each value to a variable
first, second, third = return_multiple()

print(first) # a
print(second)# b
print(third) # c

#===============================================================================================================================
'Parameters: function variables'
'''
  > Default Parameter Values

  Parameters: 
    > are named variables passed into a function definition
    > represent unknown literal values
    > are assigned values when the function is called
    > are listed in parenthesis and apart of a functions definition
    > only exist inside of the function definition (local scope)

 
  Think defining -->  Think parameters

  Functions can have 0, 1 or more parameters
    > seperated with a comma
'''


#def function_name(parameter1, parameter2, ...):
#---------------------------------------------------------------------------#
def has_parameters(parameter_1,parameter_2):                                #
    #separate multiple parameters with comma ","                            #
    print(parameter_1)                                                      #        
    print(parameter_2)                                                      #
#---------------------------------------------------------------------------#

#calling
has_parameters("Hello", "World") 
# Hello
# World


#example
def calc_product(x,y):#parameters here
    product = x * y
    return product

calc_product(4,3)# arguments here



'Default Parameter Values'
' > Parameters can be given default values'
' > Parameters with a defualt can be provided and argument, but do not require one'

#Default argument values
def has_defaults(p1,p2 = "p2 is defualt",p3 = "p3 is defualt"):
    return p1,p2,p3

first, second, third = has_defaults("p1 is required", "p2 is optional")

print(first)  # p1 is required
print(second) # p2 is optional
print(third)  # p3 is defualt


#Note: default values are evaluated at the point of function definition
#Example
number = 5
def example(arg=number):
    print(arg)

number = 6
example() # 5


#===============================================================================================================================
'Arguments: parameter values'
'''
  Arguments 
  > are the actual values assigned to a parameter when calling the function
  > are required for each parameter without a default value
  > can be passed a value from a variable
  > are listed in parenthesis and apart of a function call
  > seperated with a comma

  Think calling --> Think arguments
'''


#
#Definition-----------------------------------------------------------------#
def accepts_arguments(parameter_1,parameter_2):                             #
    print(parameter_1)                                                      #
    print(parameter_2)                                                      #
#---------------------------------------------------------------------------#


#Function Call
#function_name(argument1,argument2,...)
accepts_arguments("Hello", "World")

#example
def calc_product(x,y): #parameters here
    product = x * y
    return product

calc_product(4,3) #arguments here


#===============================================================================================================================
'Positional Arguments vs Keyword Arguments'
'''
  Positional Arguments correspond to parameters based on position
  > Unpacking Positional Arguments
  > Forcing Positional Arguments


  Keyword Arguments correspond to parameters base on name
  > Unpacking Keyword Arguments
  > Forcing Keyword Arguments
'''

'Positional Arguments'
' > assigned based on position'

#position        1       2      3
def positional(first, second, third):
    print(first)
    print(second)
    print(third)

#postion    1    2    3
positional("a", "b" ,"c")
# a
# b
# c

'> Unpacking Positional Arguments'
'   > Use the * character to unpack list like iterables as arguments'
'   > Each argument is assigned based on position'


def unpack_positional(a,b,c,d,e):
    return [a,b,c,d,e]

arguments = (1,2,3,4,5)
result = unpack_positional(*arguments) 
#        a = 1, b = 2, c = 3, d = 4 , e = 5

print(result)
#[1,2,3,4,5]

#example
print(list(range(2,9)))# [2,3,4,5,6,7,8]
nums =[1,10]
print(list(range(*nums)))  # [1,2,3,4,5,6,7,8,9]
#          * unpacks the args list

'> Forcing Positional Arguments (/)'
' > Use / to force arguments to be assigned by postion only'
' > Arguments appearing before the / are forced'
' > Arguments apperaing after the / are not'
' > use positional-only if the name of parameters do not matter, or the names should not be available to the user.'

#def function_name(pos1,pos2,/,pos_or_kwd,*,kwd1,kwd2): positional only, positional or keyword, keyword only
def position_forced(p1,p2,/):
    return p1, p2

position_forced(p2 = "World", p1 = "Hello")
# TypeError: position_forced() got some positional-only arguments passed as keyword arguments: 'p1, p2'


'Keyword Arguments'
' > assigned based on name'

def keyword(name, age, grade, school):
    return f"Hello {name}, you are {age} years old, in grade {grade}, and attend {school}"

#instead of positional assignment
keyword("Sam", 16, 11, "LWM Academy")

#Arguments can be assigned by name, in any order
keyword(grade = 11, name = "Sam", school = "LWM Academy", age = 16)

'> Unpacking Keyword Arguments'
' > Use the ** character to unpack dictionaries as keyword arguments'

def unpack_keyword(name, age, grad, school):
    return f"Hello {name}, you are {age} years old, you are in {grad} school, and attend {school}"

#Dictionary containing the arguments 
keyword_args = {
    "school": "MIT",
    "name" : "Sam",
    "age" : 20, 
    "grad" : "undergraduate"
}

unpack_keyword(**keyword_args)

#example
def display_data(name, force = 0, mass = 0 , acceleration = 0):
    print("Hello", name)
    print("The amount of force is" +" ", force)
    print("The mass of the object is" + " ", mass)
    print("The acceleration is" + " ", acceleration)
    
data = {"mass": 2, "acceleration": 5, "name": "Programmer", "force": 10 }

display_data(**data)

'> Forcing Keyword Arguments'
' > Use the * character to force arguments to be assigned by keyword only'
' > Arguments appearing after the * are forced'
' > Arguments apperaing before the * are not'
' > Use keyword-only when the names of parameters have meaning, or you want to prevent users from using positional parameters.'


# def function_name(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#                  -----------    ----------     ----------
#                   |             |                  |
#                    |        Positional or keyword   |
#                    |                                - Keyword only
#                     -- Positional only
def forced_keywords(*,name, age, grade, school):
    return f"Hello {name}, you are {age} years old, in grade {grade}, and attend {school}"

forced_keywords("Sam",18, 12, "Xavier's School for Gifted Youngsters")
# TypeError: forced_keywords() takes 0 positional arguments but 4 were given


def concat(*args, sep = "/"):# parameters after *args are keyword only
    return sep.join(args)






'''
  General Tips
    Use positional-only if you want the name of the parameters to not be available to the user. 

    Use keyword-only when names have meaning and the function definition is more understandable by being 
      explicit with names or you want to prevent users relying on the position of the argument being passed.  

    For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future
'''


#===============================================================================================================================
'> Arbitrary Arguments Lists: (*args, **kwargs)'
'''
  *args (pronounced "star-args"), also known as variable-length argument lists
    > Allow you to assign a variable number of positional arguments. 

  **kwargs (pronounced "star-star-kwargs"), also known as variable-length keyword argument lists
    >Allow you to assign a variable number of keyword arguments

  *args, and **kwargs can be used together and accept any number of arguments(including 0)
'''
# Parameters must follow this order args, *args, ** kwargs
#def function_name(arg1,arg2,*args,**kwargs)


#args can be treated as a tuple
def arbitrary_arguments(*args): #any parameters after *args must be keyword
    print(args)

arbitrary_arguments() # 
arbitrary_arguments(1)# 1
arbitrary_arguments(1,2)# 1 2
arbitrary_arguments(1,2,3)# 1 2 3

#kwargs can be treated as a dictionary
def arbitrary_keywords(**kwargs): #any positional args must come before **kwargs
    print(kwargs)

arbitrary_keywords()# {}
arbitrary_keywords(name = "sam") # {'name': 'sam'}
arbitrary_keywords(name = "sam", age = "40")# {'name': 'sam', 'age': '40'}
arbitrary_keywords(name = "sam", age = "40", phone = "123-456-7890") \
# {'name': 'sam', 'age': '40', 'phone': '123-456-7890'}

#===============================================================================================================================
'Scope: Global vs Local'
# local variables  defined in a function exist in that function only.
# Global variables defined outside of functions are visible everywhere.

global_ = 0
#Local Exists Here----------#
def example(local_):        #
    print(global_)          #
    print(local_)           #
#---------------------------#
  
example(1)
#0
#1
print(global_) # 0 
# print(local_) # NameError: name 'local_' is not defined.

'> The global Keyword'

var = 0 #global 'var'
def modify_global():
    var = 1 #local 'var' only exists in the function
    print(var)# --> 1
  

modify_global()  # 1
print(var) # 0 prints global 'var' 

'''
Use the global keyword declares that a variable inside of a function 
is referring to a global variable, not a local one.
'''

var = 0 #global 'var'

def modify_global():
    global var # declares that var is global, not local
    var = 1 #assigns global 'var" 
    print(var)# --> 1
  

modify_global()  # 1
print(var) # 1 prints global 'var' 

#===============================================================================================================================
'Builtin Function Calls'
#every language has its own pre-defined (builtin) functions that you can use.

'builtins you may have already used'
print()
input() 
range() 
len()
float()
int()
str()
type()

#notice that you are just calling the function, you do not need to define it
#these are already defined. 

#here are the builtin function calls in python:
abs()           # Returns the absolute value of a number.
aiter()         # Returns an iterator object.
all()           # Returns True if all elements of an iterable are true.
anext()         # Retrieves the next item from an iterator.
any()           # Returns True if any element of an iterable is true.
ascii()         # Returns a string containing a printable representation of an object.
bin()           # Converts an integer to a binary string.
bool()          # Returns the boolean value of an object.
breakpoint()    # Enters the debugger at the specified line.
bytearray()     # Returns a new array of bytes.
bytes()         # Returns an immutable bytes object.
callable()      # Returns True if the object appears callable.
chr()           # Returns the string representing a character whose Unicode code point is the integer.
classmethod()   # Returns a class method for the given function.
compile()       # Compiles the source into a code or AST object.
complex()       # Returns a complex number with the value real + imag*1j.
copyright()     # Prints the copyright statement.
credits()       # Prints the list of contributors.
delattr()       # Deletes the attribute of an object.
dict()          # Returns a new dictionary object.
dir()           # Returns the list of names in the current local scope or namespace.
divmod()        # Returns the quotient and remainder of the division of two numbers.
enumerate()     # Returns an enumerate object.
eval()          # Evaluates the specified expression.
exec()          # Executes the specified dynamically created code.
# exit()        # Exits the Python interpreter.
filter()        # Constructs an iterator from elements of an iterable for which a function returns true.
float()         # Returns a floating-point number constructed from a number or string.
format()        # Formats a specified value.
frozenset()     # Returns a new frozenset object.
getattr()       # Returns the value of the specified attribute of an object.
globals()       # Returns the current global symbol table as a dictionary.
hasattr()       # Returns True if the object has the specified attribute.
hash()          # Returns the hash value of an object.
help()          # Invokes the built-in help system.
hex()           # Converts an integer to a hexadecimal string.
id()            # Returns the identity of an object.
input()         # Reads a line from input, converts it to a string, and returns it.
int()           # Returns an integer object.
isinstance()    # Returns True if the specified object is an instance of the specified class.
issubclass()    # Returns True if the specified class is a subclass of another class.
iter()          # Returns an iterator object.
len()           # Returns the length (the number of items) of an object.
license()       # Prints the Python Software Foundation License.
list()          # Returns a list.
locals()        # Returns the current local symbol table as a dictionary.
map()           # Applies a function to all items in an input iterable.
max()           # Returns the largest item in an iterable or the largest of two or more arguments.
memoryview()    # Returns a memory view object.
min()           # Returns the smallest item in an iterable or the smallest of two or more arguments.
next()          # Retrieves the next item from an iterator.
object()        # Returns a new featureless object.
oct()           # Converts an integer to an octal string.
open()          # Opens a file and returns a corresponding file object.
ord()           # Returns an integer representing the Unicode character.
pow()           # Returns x to the power of y.
print()         # Prints objects to the text stream file.
property()      # Returns a property attribute.
# quit()        # Exits the Python interpreter.
range()         # Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
repr()          # Returns a string containing a printable representation of an object.
reversed()      # Returns a reverse iterator.
round()         # Returns the rounded value of a number to the specified number of decimals.
set()           # Returns a new set object.
setattr()       # Sets the value of the specified attribute of an object.
slice()         # Returns a slice object.
sorted()        # Returns a sorted list from the specified iterable.
staticmethod()  # Returns a static method for the specified function.
str()           # Returns a string object.
sum()           # Sums the items of an iterable.
super(None)     # Returns a proxy object that delegates method calls to a parent or sibling class.
tuple()         # Returns a tuple.
type()          # Returns the type of an object.
vars()          # Returns the __dict__ attribute of the given object.
zip()           # Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

# For more pre-defined functions programmers will look for code libraries.
# Libraries are just how they sound, they store code for a specific function. 
#===============================================================================================================================
'Lambda Expressions: Shorthand Functions'
' > Lambda functions are small anonymous shorthand functions'
" > Lambda's take any number of arguments, but can only have one expression"

#syntax
'lambda arguments : expression'

lambda_function = lambda a,b,c : a + b + c 
lambda_function(1,2,3) #returns 6

#Create a lambda as a functions return
def returns_lambda(n):
    return lambda a : a ** n
#returns a lambda that returns a to the power of n
squared = returns_lambda(2) # lambda a : a ** 2
cubed = returns_lambda(3)   # lambda a : a ** 3
pow_4 = returns_lambda(4)   # lambda a : a ** n

squared(2) #4
cubed(2)   #8
pow_4(2)   #16

#anonymous functions can be created with the lambda keyword

def counter(n):
    return lambda x: x+n
E = counter(0)
print(E(1))

#lambda can also be used to pass a small function as an arguement
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)

#anonymous functions can be created with the lambda keyword



#===============================================================================================================================
'Documentation Strings'
'''
> Documentation strings
  The first line should always be a short, concise summary of the object’s purpose.
  For brevity, it should not explicitly state the object’s name
      or type, since these are available by other means
          (except if the name happens to be a verb describing a function’s operation).
  This line should begin with a capital letter and end with a period.

  If there are more lines in the documentation string,
      the second line should be blank, visually separating
          the summary from the rest of the description.
  The following lines should be one or more paragraphs
      describing the object’s calling conventions,
          its side effects, etc.
'''

def multi_line_docstring():
    """ This line is a summary of the function.

    The above line should be blank. The rest describes the
    calling conventions, side effects, and etc."""
    pass
    
#The dunder attribute __doc__ returns the docstring of a function
print(multi_line_docstring.__doc__)

#===============================================================================================================================#
'> Function Annotations'
' > Function annotations are typically used to document/ provide type hints.'

"def function(parameter: type) -> return_type:"
def sum_ints(a: int, b: int) -> int:
    return a + b
#expects integer arguments, integer return

def sum_floats(x:float, y:float) -> float:
    return x + y
#expects float arguments, float return


def sum_list(list1d: list[int]) -> int:
    total = 0
    for elem in list1d:
        total += elem

    return total
#expects float arguments, float return

#===============================================================================================================================
'Function Examples Including Conditionals, While Loops, and For Loops'
#functions can include all kinds of different code
#Conditionals, While Loops, and For loops can all be used inside of functions.

def add(a,b):
    answer = a + b
    return answer

def calc_velocity(distance, time):
    velocity = distance / time
    return velocity

def calc_slope(x1,y1,x2,y2):
    slope = ((y2-y1)/(x2-x1))
    return slope

def get_quadratic(x, a, b):
    #where (x + a) (x + b) == x**2 + (a+b)x + ab
    #where x is a string
    return f"{x}^2 + {a+b}x + {a*b}"

print(get_quadratic("x",3,4))


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


def count_vowels(sentence):
    vowels = "aeiou"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

print(count_vowels("The quick brown fox jumps over the lazy dog."))


def get_sum(alist):
    total = 0
    for num in alist:
        total = total + num 
        #total += num
    return total

list1d = [1,2,3,4,5,6,7,8,9]
print(get_sum(list1d))

def get_max(alist):
    max_num = alist[0]
    for num in alist:
        if num > max_num:
            max_num = num
    return max_num

list1d = [0,5,2,20,8,6,1,10,19]
print(get_max(list1d))

def count_vowels(alist):
    count = 0
    vowels = "aeiou"
    for elem in alist:
        if elem in vowels:
            count +=1
    return count

letters = ["a","b","c","d","e"]
print(count_vowels(letters))


 


























