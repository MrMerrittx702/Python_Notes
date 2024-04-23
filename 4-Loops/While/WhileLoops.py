#===============================================================================================================================#
'''Python While Loops without lists'''
#===============================================================================================================================#
'''
Covered in this file:
> Iteration Defined
> Python indentation and Code Blocks
> While Loops Syntax
> The control variable
> Counting with while loops
> Counting Up by 1 and by multiples
> Counting Down by 1 and by multiples
> Infinite Loops and Off by 1 Errors
> Special to Python: While-Else
> Nested While Loops
> Break, Continue, and Pass
'''

#===============================================================================================================================#
'> Iteration Defined'
'''
  Iteration is the repitition of a process or function.
  Iterables are data types that can return their values one at a time

  Iteration can be thought of as looping or repeating
'''

#instead of this:
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

#Try these:

#While Loops (Iteration)
num = 1
while (num <= 10):
    print(num)
    num += 1

#For Loops (Iteration)
for num in range(1,11,1):
    print(num)

#Functions (Recursion)
def count(num, stop, step = 1): #Function Definition
    if num <= stop:
        print(num)
        num += 1
        count(num,stop,step)
    return

count(1,10) #Function Call

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
'> While Loop Syntax'
'   > use a condition to determine when to stop looping. '
'   > typically used when the number of iterations is not fixed.'

condition = True or False


while(condition):
    #indent 4 spaces to be inside of the loop block (scope/context)
    'repeat this code block'
#unindent 4 spaces to exit the loop block (scope/context)

#------------------------------------#
while(condition): #-------------#    #
    'repeat this code block'    #    #
    #---------------------------#    #
#------------------------------------#


#===============================================================================================================================#
'> The control variable'
'   > while loops will often result in an infinite loop'
'   > a control variable is used to control the number of loops'

count = 0 #this is the control variable

while count < 5: #stops the loop when count is >= 5
    'repeat this code'
    count = count + 1 #increases count each time the loop occurs
    #count += 1 is shorthand for the line above

#pay attention to the indentation


#===============================================================================================================================#
'> Counting with while loops'
'   > use a control variable, and define the start, stop, and step of the loop.'

start = 0 #start: where to start counting
stop = 5 #stop: where to stop counting
step =1 #step: how much to increase or decrease by each time

count = start
while(count < stop):  #can be > < >= or <= stop

    count = count + step # can be + - * / % ...

    #or use the compound assignment operators
    count += step   #can be += -= *= /= ... 


#===============================================================================================================================#
'> Counting Up by 1 and by multiples'

#programmers with often use the letter i as a control variable
#++++++++++++++++++++++++++++++++++++++#
'0 to Positive By 1s'
i = 0 #start at 0
while(i < 5): #stop when i is 5  (i <= 4)
    print(i, end = " ") #print out i with a space at the end
    i += 1 #step  increment i by 1
# 0 1 2 3 4 

'0 to Positive By Multiples'
i = 0 #start at 0
while(i < 5): #stop when i is 5  (i <= 4)
    print(i, end = " ") #print out i with a space at the end
    i += 2 #step  increment i by 2
# 0 2 4 
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From 1 to Positive by 1s'
#From 1 to positive
i = 1 #start 
while (i < 6): #stop (i <= 5)
    print(i, end = " ")
    i += 1 #step  increment i by 1
# 1 2 3 4 5 

'From 1 to Positive by Multiples'
i = 1 #start 
while (i < 6): #stop (i <= 5)
    print(i, end = " ")
    i += 3 #step  increment i by 3
# 1 4 
#++++++++++++++++++++++++++++++++++++++# 
#++++++++++++++++++++++++++++++++++++++#
'From Positive to Positive by 1s'
i = 10 #start
while( i < 21): #stop (i <= 20)
    print(i, end = " ")
    i+=1 #step  increment i by 1
# 10 11 12 13 14 15 16 17 18 19 20 
  
'From Positive to Positive by Mutliples'
i = 10 #start
while( i < 21): #stop (i <= 20)
    print(i, end = " ")
    i+=5 #step  increment i by 5
# 10 15 20 
#++++++++++++++++++++++++++++++++++++++#  
#++++++++++++++++++++++++++++++++++++++#
'From Negative to 0 by 1s'
i = -5 #start
while(i < 1): #stop (i <= 0)
    print(i, end = " ")
    i+=1  #step increment i by 1
# -5 -4 -3 -2 -1 0 

'From Negative to 0 by Multiples'
i = -5 #start
while(i < 1): #stop (i <= 0)
    print(i, end = " ")
    i+=3  #step increment i by 3
# -5 -2 
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Negative by 1s'
i = -10 #start
while(i < -4): #stop (i <= -5)
    print(i, end = " ")
    i+=1 #step  increment i by 1
# -10 -9 -8 -7 -6 -5 

'From Negative to Negative by Multiples'
i = -10 #start
while(i < -4): #stop (i <= -5)
    print(i, end = " ")
    i+= 3 #step  increment i by 3
# -10 -7 
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Positive by 1s'
i = -3 #start
while(i < 4): #stop (i <= 3)
    print(i, end = " ")
    i+=1 #step increment i by 1
# -3 -2 -1 0 1 2 3 


'From Negative to Positive by Multiples'
i = -3 #start
while(i < 4): #stop (i <= 3)
    print(i, end = " ")
    i+= 2 #step increment i by 2
# -3 -1 1 3
#++++++++++++++++++++++++++++++++++++++#  

#===============================================================================================================================#
'> Counting Down by 1 and by multiples'


'From Positive to 0 by 1s'
i = 10 #start
while(i > -1): #stop (i >= 0)
    print(i, end = " ")
    i -= 1 #step
# 10 9 8 7 6 5 4 3 2 1 0 

'From Positive to 0 by Multiples'
i = 10 #start
while(i > -1): #stop (i >= 0)
    print(i, end = " ")
    i -= 3 #step
# 10 7 4 1 
  


'From Positive to Positive by 1s'
i = 50 #start
while(i > 39): #stop (i >= 40)
    print(i, end = " ")
    i -= 1 #step
# 50 49 48 47 46 45 44 43 42 41 40 

'From Positive to Positive by Multiples'
i = 50 #start
while(i > 39): #stop (i >= 40)
    print(i, end = " ")
    i -= 3 #step
# 50 47 44 41 



'From Positive to Negative by 1s'
i = 5 #start
while(i > -2): #stop (i >= -1)
    print(i, end = " ")
    i -= 1#step
# 5 4 3 2 1 0 -1 

'From Positive to Negative by Multiples'
i = 5 #start
while(i > -2): #stop (i >= -1)
    print(i, end = " ")
    i -= 4 #step
# 5 1 



'From 0 to Negative by 1s'
i = 0 #start
while(i > -7): #stop (i >= -6)
    print(i, end = " ")
    i -= 1#step
# 0 -1 -2 -3 -4 -5 -6 

'From 0 to Negative by Multiples'
i = 0 #start
while(i > -7): #stop (i >= -6)
    print(i, end = " ")
    i -= 3 #step
# 0 -3 -6 



'From Negative to Negative by 1s'
i = -6 #start
while(i > -15): #stop (i >= -14)
    print(i, end = " ")
    i -= 1#step
# -6 -7 -8 -9 -10 -11 -12 -13 -14 

'From Negative to Negative by Multiples'
i = -6 #start
while(i > -15): #stop (i >= -14)
    print(i, end = " ")
    i -= 4#step
# -6 -10 -14 

#===============================================================================================================================#
'> Infinite Loops and Off by 1 Errors'

'''
  Infinite Loops
  An infinite loop is a loop that continues executing 
    indefinitely because its exit condition is never met. 
'''
# examples
condition = True
while (condition):
    print("This is an infinite loop!")

i = 0
while (i < 10):
    print("This is an infinite loop")

i = 5
while( i > 0):
    print("This is an infinite loop")
    i+=1

'''
  Off-by-One Errors
  Off-by-one errors occur when a loop iterates one too 
    many or one too few times, typically due to incorrect 
      indexing or boundary conditions. 
'''

#example
#count from 0 to 5
i = 0
while (i < 5):
    print(i, end = " ")
    i+=1
#Off by 1, only counts from 0 to 4

#===============================================================================================================================#
'> Special to Python: While-Else'
'   > the else block runs on time, once the condition is false'

#when the condition is no longer true run the else
i = 1
while(i <= 5):
    print("Counting...", i)
    i+=1
else: #when i becomes 6 this block runs
    print("Finished Counting")

#===============================================================================================================================#
'> Nested While Loops'
'   > one while loop placed inside of another.'
'   > the inner loop executes completely for every 1 iteration of the outer loop.'

#Placing one While Loop into another While Loop

outer_start = 0; outer_stop = 0; outer_step = 0
inner_start = 0; inner_stop = 0; inner_step = 0


repeat = outer_start
while(repeat < outer_stop):#Outer Loop------------#
                                                  #
    count = inner_start                           #
    while(count < inner_stop):#Inner loop--#      #
        print(count, end = " ")            #      #
        count += inner_step                #      #
    #--------------------------------------#      #
    repeat += outer_step                          #
#-------------------------------------------------#

#Example count to 5, 3 times
repeat = 0
while(repeat < 3):

    count = 0
    while(count < 6):
        print(repeat, count)
        count += 1
    
    repeat += 1




#===============================================================================================================================#
'> Break and Continue'

'''
  Break
  The break statement in Python is used to exit (or "break out of") the loop prematurely. 
  It is commonly used within loops like for and while to interrupt the loop's execution based on a certain condition.
'''
while(True):
    break
#the loop will exit on the first loop

'''
  Continue
  The continue statement in Python is used to skip the rest of the code 
  inside a loop for the current iteration, and continue with the next iteration 
  of the loop.
'''
i = 0
while(i < 5):
    if(i == 2):
        i+=1
        continue
    print(i)
    i+=1
#skips the number 2

#===============================================================================================================================#

'''
Vocabulary:

Break
Conditional
Condition
Continue
Control Variable
For Loop
Function Call
Function Definition
Global Scope
Iterate
Local Scope
Pass
Recursion
Return
Scope/Context
Syntax
While Loop

Break:
Break is a keyword used in loop constructs to terminate the loop prematurely. 
When a break statement is encountered within a loop, the loop is exited immediately, and control is transferred to the statement following the loop.

Conditional:
Conditional refers to statements or constructs in programming that execute different blocks of code based on specified conditions. 
They allow for decision-making and control flow based on whether certain conditions are true or false.

Condition:
A condition is a statement or expression that evaluates to a boolean value (true or false). 
It is often used to determine the flow of execution in a program, controlling the execution of certain blocks of code based on whether the condition is true or false.

Continue:
Continue is a keyword used in loop constructs to skip the remaining code within the current iteration of the loop and proceed to the next iteration. 
When a continue statement is encountered, the loop advances to the next iteration without executing the remaining code in the loop body.

Control Variable:
A control variable is a variable used to control the behavior of a loop. 
It typically represents the iteration count or state of the loop and is updated during each iteration to determine when the loop should terminate.

For Loop:
A for loop is a control flow statement used to repeatedly execute a block of code a fixed number of times or over a sequence of elements. 
It iterates over a sequence, such as a range of numbers or elements in a collection, and executes the loop body for each iteration.

Function Call:
A function call is an instruction that invokes a specific function with provided arguments. 
It triggers the execution of the function's code, and upon completion, the function may return a result or perform other actions as defined.

Function Definition:
A function definition is the implementation of a function, including its name, parameters, and code block. 
It specifies the behavior of the function and defines how it operates when called with specific arguments.

Global Scope:
Global scope refers to the visibility and accessibility of variables, functions, and other identifiers throughout the entire program. 
Variables declared in the global scope can be accessed and modified from any part of the program.

Iterate:
Iteration is the process of repeatedly executing a set of instructions or operations, typically over a sequence of elements or until a certain condition is met. 
It involves looping constructs like for loops, while loops, or iterators.

Local Scope:
Local scope refers to the visibility and accessibility of variables, functions, and other identifiers within a specific portion of code, such as a function or block. 
Variables declared in local scope are only accessible within that scope and cannot be accessed from outside.

Pass:
Pass is a keyword used in Python to create a placeholder or empty block of code. 
It serves as a syntactic requirement where code is expected but no action is needed, allowing the program to pass over the block without causing errors.

Recursion:
Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem. 
It involves breaking down a problem into smaller subproblems and solving each subproblem recursively until a base case is reached.

Return:
Return is a keyword used in functions to specify the value that the function should produce or output when called. 
It allows functions to send back results or data to the caller for further use or processing.

Scope/Context:
Scope or context refers to the visibility and accessibility of variables, functions, and other identifiers within a program. 
It defines where variables and functions can be accessed and modified, determining their lifetime and visibility.

Syntax:
Syntax refers to the rules and structure governing the arrangement of elements in a programming language. 
It defines the correct grammar and punctuation required for valid code, ensuring that programs can be interpreted or compiled correctly.

While Loop:
A while loop is a control flow statement used to repeatedly execute a block of code as long as a specified condition is true. 
It iterates over the code block until the condition evaluates to false, allowing for flexible looping based on dynamic conditions.

    
'''
  
