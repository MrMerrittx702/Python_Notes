#===============================================================================================================================#
'''Python Conditionals'''
#===============================================================================================================================#

#iterate: repitition of a process or function
#condition: statement that evaluates True/False to determine if a code block is run.

'''
  Covered in this video:
  > Review: Booleans, Relational Operators,and  Logical Operators
  > Boolean Expressions 
  > Python Indentation and Code Blocks
  > if Statements
  > if-else Statements
  > Chained Conditionals 
  > Nested Conditionals 
  > Ternary Operators: Shorthand Conditionals`
  > Match Statements
'''

#===============================================================================================================================#
'> Review: Booleans, Relational Operators, and  Logical Operators'

#Conditionals often utilize booleans, relational operators, and logical operators. 

#Booleans (True/False)
True
False

#Relational Operators (Inequalities)
#relational operators are used for comparisons 
#evaluate to a boolean (True/False)
#Order of operations is left to right
'''
>  #greater than
<  #less than 
>= #greater than or equal to
<= #less than or equal to
== #equal to
!= #not equal to

#Special to python
is      # identical to
is not  # not identical to
in      # apart of
not in  # not apart of

#Logical Operators (for multiple conditions)
#Order of Operations NAO
not  # opposite: not T --> F // not F --> T
and  #both : T and T --> T //all others are F
or   # at least 1: F or F --> F // all others are T
'''

#Truth tables show how logical operators are evaluated

#===============================================================================================================================#
'> Boolean Expressions (evaluate True or False)'
'  > expressions that evaluate to either True or False'
'  > typically used with conditionals and while loops'

'''
Operators
relational ( ==, !=, <, >, <=, >=)
logical    (not, and, or)
membership ( in, not in)
identity   (is, is not)
'''

#String Comparisons
print("text" == "text") #True

#Number Comparisons
print(5 >= 2) #True

#Variable Comparisons
x = "some text"
y = "other text"
print(x == y) #False


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
    #start of the if code block (scope/context)
    print("Inside the if statement")

#end of the if code block (scope/context)

while(condition):
    #start of the while code block (scope/context)
    print("Inside the while loop")

#end of the while code block (scope/context)

for _ in range(10):
    #start of the for code block (scope/context)
    print("Inside the for loop")

#end of the for code block (scope/context)

def function_():
    #start of the function code block (scope/context)
    print("Inside of the function definition")

#end of the function code block (scope/context)
  
#Nested Indentation# Blocks inside of blocks
def example_():
    #start of function code block###########################
    for _ in range(5):                                     #
        #start of for code block++++++++++++++++++++++#    #
        while(condition):                             #    #
            #start of while code block============#   #    #      
            if(condition):                        #   #    #
                #Start of if code block ------#   #   #    #
                print("So many indents!")     #   #   #    #
            #end of if code block-------------#   #   #    #
        #end of while code block==================#   #    #
    #end of for code block++++++++++++++++++++++++++++#    #
#end of function code block#################################


'''
Note:
Indentation is typically achieved using spaces or tabs. 
Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior. 
Python 3 disallows mixing tabs and spaces for indentation in the same source file.

If you are using an editor like VS code using the tab key, and spaces is not a problem. 
'''

#===============================================================================================================================#
'> if Statements'
#Syntax
condition = True or False

  #the condition in parenthesis is a boolean expression
if(condition):  #end with a colon ":"
    #indent 4 spaces to be inside the if code block
    'Code Block Here'

#unident 4 spaces to be outside the if code block

#------------------------------------------------------#
if(condition): #------------------------------------#  #
    'runs this block when the condition is True'    #  #
    'skips this block when the condition if False'  #  #
    #-----------------------------------------------#  #
#------------------------------------------------------#

#each new if starts its own separate conditional

if(True): #----------#        
    'run this block' # 
#--------------------#

if(False): #----------#
    'skip this block' # 
#---------------------#

'''
  Special Notes for Conditionals:
    > When writing if statments you will often get output, 
        sometimes even correct output, but your code does not work 
        as intended in every case. 

    Integers/Floats   
        > Any non-zero number (integer, float) is evaluated as True
    
    Strings,Lists, Tuples, Sets, Dictionaries
        > Any non-empty string, list, tuple, set, or dictionary,  
          is evaluated as True
    
    Functions, Methods, Lambdas, Classes
        > Any function, method, lambda or class is evaluated as True
    
    Objects
        > By default objects are evaluated True, 
          but how an object is evaluated can be changed.
'''

#===============================================================================================================================#
'> if-else Statements'
#--------------------------------------------------------------#
if(condition): #-----------------------------------#           #
    'runs this block when the condition is True    '           #
    'skips this block when the condition is False  '           #
    #----------------------------------------------#           #
else: #-----------------------------------------------------#  #
    'runs this block when all conditions above it are False '  #
    'skips this block when any condition above it is True   '  #
    #-------------------------------------------------------#  #
#--------------------------------------------------------------#

#--------------------------#
if(True): #----------#     #
    'run this block' #     #
    #----------------#     #
else: #----------------#   #
    'skip this block'  #   #
    #------------------#   #
#--------------------------#

#---------------------------#
if(False): #-----------#    #
    'skip this block'  #    #
    #------------------#    #
else: #--------------#      #
    'run this block' #      #
    #----------------#      #
#---------------------------#

#===============================================================================================================================#
'if-elif-else (Chained Conditional)' 
#---------------------------------------------------------------------------------------#
if(condition): #------------------------------------#                                   #
    'runs this block when the condition is True'    #                                   #
    'skips this block when the condition is False'  #                                   #
    #-----------------------------------------------#                                   #
elif(condition): #------------------------------------------------------------------#   #
    'runs this block when the conditions above are False and its condition is True '#   #
    'skips this block when an above condition is True or its condition is False'    #   #
    #-------------------------------------------------------------------------------#   #
else:#------------------------------------------------------------#                     #
    'runs this block only when the conditions above it are False' #                     #
    'skips this block when any condition above it is True'        #                     #
    #-------------------------------------------------------------#                     # 
#---------------------------------------------------------------------------------------#

#---------------------------------#
if(True): #------------#          #
    'run this block'   #          #
    #------------------#          #
elif(True): #-------------#       #
    'skip this block'     #       #
    #---------------------#       #
else: #----------------#          #
    'skip this block'  #          #
    #------------------#          #
#---------------------------------#

#---------------------------------#
if(False): #------------#         #
    'skip this block'   #         #
    #-------------------#         #
elif(True): #-------------#       #
    'run this block'      #       #
    #---------------------#       #
else: #----------------#          #
    'skip this block'  #          #
    #------------------#          #
#---------------------------------#

#---------------------------------#
if(False): #------------#         #
    'skip this block'   #         #
    #-------------------#         #
elif(False): #------------#       #
    'skip this block'     #       #
    #---------------------#       #
else: #----------------#          #
    'run this block'   #          #
    #------------------#          #
#---------------------------------#
#===============================================================================================================================#
'> Nested Conditionals'
#conditionals inside conditionals
if(True):
    if(True):
        'the block runs only if both are True'

a = True or False
b = True or False
c = True or False

#=====================================================#
if(a):                                                #
    print("a is True")                                #
    #+++++++++++++++++++++++++++++++++++++++#         #
    if(b):                                  #         #
        print("a,b are True")               #         #
        #----------------------------#      #         #
        if(c):                       #      #         #
            print("a,b,c are True")  #      #         #
        else:                        #      #         #
            print("c is False")      #      #         #
        #----------------------------#      #         #
    else:                                   #         #
        print("a is True")                  #         #
    #+++++++++++++++++++++++++++++++++++++++#         #
else:                                                 #
    print("a is False")                               #
#=====================================================#

#There can many different combinations

#===============================================================================================================================#
'> Ternary Operator: Shorthand Conditionals'

#ternary operators are a shorthand way of writing if statements
#They are best used for short simple conditionals, as longer ternary operators are confusing. 

#syntax --> x if condition else y
x = 2; y = 3; z = 4
print("if") if True else print("else")
print("if") if x > 0 else print("else if") if y > 0 else print("else")

# The term "ternary" refers to the fact that it takes three operands: the condition to be evaluated, 
# the expression to be returned if the condition is true, and the expression to be returned if the 
# condition is false.

#===============================================================================================================================#
'> Match Statements'
'>> Compare an expression to one or more case blocks.'
'>> Only the first matched pattern is executed.'


https_response = ...

match https_response:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case 500:
        print("Internal Server Error")
    case _:
        print("An error occured")

# The '_' acts as a wildcard and always matches. 
# If no case matches the program continues 

'>> Combining Literals'
'Use "," combine multiple literals into one case'

https_response = ...

match https_response:
    case 400, 401, 403, 404, 418:
        print("Client Side Error")
    case 500, 501:
        print("Server Side Error")


'>> Adding a Guard' 
a = False
character = 97

match character:
    case 97 if a: #addiing an if statement to the case creates a guard
        print("a") #This line executes if the guard is true, and the case matches.
    case 98: 
        print("b")
    case 99:
        print("c")
    case _:
        print("")


#===============================================================================================================================#
'''
Vocabulary:

Arithmetic
Bitwise
Boolean Expression
Condition
Conditional
Expression
Iteration
Logical
Match
Nesting
Relational 
Scope/Context
Ternary Operator
Truth Table



Arithmetic:
Arithmetic refers to the mathematical operations performed on numerical data, such as addition, subtraction, multiplication, and division. 
It involves manipulating numerical values to perform calculations.

Bitwise:
Bitwise operations are operations performed on individual bits of binary numbers. 
They include operations such as AND, OR, XOR, and shifting, which manipulate the binary representation of numbers at the bit level.

Boolean Expression:
A boolean expression is an expression that evaluates to either true or false. 
It typically involves logical operators (such as AND, OR, NOT) applied to boolean values or conditions, used for decision-making in control structures.

Condition:
A condition is a statement or expression that evaluates to a boolean value (true or false). 
It is often used to determine the flow of execution in a program, controlling the execution of certain blocks of code based on whether the condition is true or false.

Conditional:
Conditional statements or constructs are control structures used to execute different blocks of code based on specified conditions. 
They include if statements, switch statements, and other conditional branching mechanisms.

Expression:
An expression is a combination of variables, constants, operators, and function calls that evaluates to a single value. 
Expressions can represent calculations, comparisons, or other operations, and they can be used in assignments, conditions, or function calls.

Iteration:
Iteration is the process of repeatedly executing a set of instructions or operations, typically over a sequence of elements or until a certain condition is met. 
It involves looping constructs like for loops, while loops, or iterators.

Logical:
Logical operations involve evaluating boolean expressions or conditions to determine their truth value. 
Logical operators such as AND, OR, and NOT are used to combine or negate boolean values, facilitating decision-making in control flow.

Match:
Match is a control structure used to compare an expression against multiple patterns and execute the code associated with the first matching pattern. 
It provides a concise and expressive way to handle multiple conditions or cases.

Nesting:
Nesting refers to the practice of placing one construct or block of code inside another. 
It involves encapsulating code within other code blocks, such as loops inside loops or conditional statements inside other conditionals.

Relational:
Relational operators are used to compare the relationship between two values or expressions. 
They include operators such as equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).

Scope/Context:
Scope or context refers to the visibility and accessibility of variables, functions, and other identifiers within a program. 
It defines where variables and functions can be accessed and modified, determining their lifetime and visibility.

Ternary Operator:
The ternary operator, also known as the conditional operator, is a compact form of an if-else statement used to make decisions based on a condition. 


Truth Table:
A truth table is a table used in logic to represent the truth values of logical expressions. 
It lists all possible combinations of input values for the variables in the expression and shows the resulting truth values of the expression for each combination. Truth tables are commonly used to analyze and verify the behavior of logical expressions and circuits.

'''

