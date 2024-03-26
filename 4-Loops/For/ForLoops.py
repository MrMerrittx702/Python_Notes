#===============================================================================================================================#
'''For Loops without lists'''
#===============================================================================================================================#
'''
Covered in this file:
> Iteration Defined
> Python indentation and Code Blocks
> For Loop Syntax
> range() constructor
> Counting Up by 1 and by multiples
> Counting Down by 1 and by multiples
> Off by 1 Errors
> Special to Python: For-Else
> For Each Loop
> Throw away variable _
> Nested For loops
> Break, Continue, and Pass
'''

#iterate: repitition of a process or function
#condition: statement that evaluates True/False to determine if a code block is run.
#Syntax: rules for writing a language
#===============================================================================================================================#
'> Iteration Defined'
'''
  Iteration is the repitition of a process or function.
  Iterables are data types that can return their values one at a time

  Iteration can be thought of as looping or repeating
'''

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
    #start of for code block----------------------#      #
    while(condition):                             #      #
      #start of while code block -----------#     #      #      
      if(condition):                        #     #      #
        #Start of if code block ------#     #     #      #
        print("So many indents!")     #     #     #      #
      #end of if code block-----------#     #     #      #
    #end of while code block----------------#     #      #
  #end of for code block--------------------------#      #
#end of function code block------------------------------#


'''
Note:
  Indentation is typically achieved using spaces or tabs. 
  Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior. 
  Python 3 disallows mixing tabs and spaces for indentation in the same source file.

  If you are using an editor like VS code using the tab key, and spaces is not a problem. 
'''
#===============================================================================================================================#
'> For Loop Syntax'

for variable in range(): 
  #indent 2 spaces to be inside the loop block
  'repeat this code block'
#unindent 2 spaces to exit the loop block

#------------------------------------#
for variable in range(): #-----#     #         
  'repeat this code block'     #     #
  #----------------------------#     #
#------------------------------------# 

#===============================================================================================================================#
'> the range constructor'
start,stop,step = ...

#returns a range of numbers from start to stop-1. 
range(start, stop, step)
#start is included (default is 0)
#stop is not included (+1 if going up or -1 if going down)
#step (default is 1)

#examples
range(0,10,1) #0 to 9
range(10) #0 to 9
range(10,0,-1)#10 to 1
range(-5,6,1)#-5 to 5
range(5,-6,-1)#5 to -5

#===============================================================================================================================#
'> Counting Up by 1 and by multiples'

for number in range(start,stop,step):
  print(number, end = " ")#prints the value of number, and  adds a single space
#++++++++++++++++++++++++++++++++++++++#
'0 to Positive by 1s'
#count from 0 to 10
for number in range(11): #start = 0; default step = +1; default
  print(number, end = " ")
# 0 1 2 3 4 5 6 7 8 9 10 

for number in range(0,11,1): 
  print(number, end = " ")
# 0 1 2 3 4 5 6 7 8 9 10 
  
'0 to Positive by Multiples'
#count from 0 to 10 by 3
for number in range(0,11,3): 
  print(number, end = " ")
# 0 3 6 9
  
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From 1 to Positive by 1s'
#count from 1 to 5 
for number in range(1,6): #step = +1; default
  print(number, end = " ")
# 1 2 3 4 5

for number in range(1,6,1): 
  print(number, end = " ")
# 1 2 3 4 5

'From 1 to Postive by Multiples'
#count from 1 to 5 by 2
for number in range(1,6,2): 
  print(number, end = " ")
# 1 3 5
  
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Positive to Positive by 1s'
#count from 70 to 80
for number in range(70,81): #step = +1; default 
  print(number, end = " ")
# 70 71 72 73 74 75 76 77 78 79 80

for number in range(70,81,1): 
  print(number, end = " ")
# 70 71 72 73 74 75 76 77 78 79 80
  
'From Positive to Positive by Multiples'
#count from 70 to 100 by 5
for number in range(70,101,5): 
  print(number, end = " ")
# 70 75 80 85 90 95 100

#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Negative by 1s'
#count -35 to -24
for number in range(-35,-24): #step = +1; default
  print(number, end = " ")
# -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -25
  
for number in range(-35,-24,1):
  print(number, end = " ")
# -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -25
  
'From Negative to Negative by Multiples'
#count from -100 to -10 by 10
for number in range(-100,-9,10):
  print(number, end = " ")
# -100 -90 -80 -70 -60 -50 -40 -30 -20 -10
  
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Positive by 1s'
#count from -5 to 5
for number in range(-5,6): #step = +1; default
  print(number, end = " ")
# -5 -4 -3 -2 -1 0 1 2 3 4 5

for number in range(-5,6,1):
  print(number, end = " ")
# -5 -4 -3 -2 -1 0 1 2 3 4 5

'From Negative to Positive by Multiples'
#count from -5 to 5 by 4
for number in range(-5,6,4):
  print(number, end = " ")
# -5 -1 3
  
#++++++++++++++++++++++++++++++++++++++#

#===============================================================================================================================#
'Counting Down by 1 and by multiples'

#++++++++++++++++++++++++++++++++++++++#
'From Positive to 0 by 1s'
#count from 10 to 0 
for number in range(10,-1,-1):
  print(number, end = " ")
# 10 9 8 7 6 5 4 3 2 1 0
  
'From Positive to 0 by Multiples'
#count from 10 to 0 by 3
for number in range(10,-1,-3):
  print(number, end = " ")
# 10 7 4 1
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Positive to Positive by 1s'
#count from 50 to 40
for number in range(50,39,-1):
  print(number, end = " ")
# 50 49 48 47 46 45 44 43 42 41 40
  
'From Positive to Positive by Multiples'
#count from 100 to 50 by 5s
for number in range(100,49,-5):
  print(number, end = " ")
# 100 95 90 85 80 75 70 65 60 55 50
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From 0 to Negative by 1s'
#count from 0 to -10 
for number in range(0,-11,-1):
  print(number, end = " ")
# 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
  
'From 0 to Negative by Multiples'
#count from 0 to -100 by 20
for number in range(0,-101,-20):
  print(number, end = " ")
# 0 -20 -40 -60 -80 -100
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Positive to Negative by 1s'
#count from 5 to -5
for number in range(5,-6,-1):
  print(number, end = " ")
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
  
'From Positive to Negative by Multiples'
#count from 100 to -100 by 50
for number in range(100,-101,-50):
  print(number, end = " ")
# 100 50 0 -50 -100
#++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++#
'From Negative to Negative 1s'
#count from -85 to -95
for number in range(-85,-96,-1):
  print(number, end = " ")
# -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95
  
'From Negative to Negative Mutliples'
#count from -200 to -1500 by 100
for number in range(-200,-1501,-100):
  print(number, end = " ")
# -200 -300 -400 -500 -600 -700 -800 -900 -1000 -1100 -1200 -1300 -1400 -1500
#++++++++++++++++++++++++++++++++++++++#



#===============================================================================================================================#
'> Off by 1 Errors'
'''
  Off-by-One Errors
  Off-by-one errors occur when a loop iterates one too 
    many or one too few times, typically due to incorrect 
      indexing or boundary conditions. 
'''


#===============================================================================================================================#
'> Special to Python: For-Else'

#when the for loop ends execute the else block
for number in range(1,11,1):
  print(number, end = " ")
else:
  print("\nDone Printing!")

#===============================================================================================================================#
'The For Each Loop'
'''
For eaach loops allow direct access to the items in an iterable
'''

#special way to write a for loop
iterable = ["list","tuple","set","dictionary","some objects"]

#Syntax
for variable in iterable:
  'code block to execute'
#iterables are something that can be repeated through 
# a list is iterable

#element does not represent an index, but the actual element. 
for element in iterable:
  print(element, end = "|")

#===============================================================================================================================#
'> Throw away variable _ '
#sometimes we don't use a variable but need a place holder
#use underscores as throw away variables

for _ in range(5): #here we don't use the variable for this loop so we use an _
  for number in range(10): # 0 (default) to 9 by 1s (default)
    print(number, end = " ")
  print() # added to format output

#===============================================================================================================================#
'> Nested For Loops'

#Syntax
for variable_1 in range():
  #indent 2 spaces to be inside the outer loop block
  for variable_2 in range():
    #indent 2 spaces to be inside the inner loop block
    'repeat the code block'
  #unindent to exit the inner loop block
#unindent to exit the outer loop block

#-------------------------------------------#
for variable_1 in range(): #-----------#    #
                                       #    #
  for variable_2 in range(): #----#    #    # 
    'repeat the code block'       #    #    #
    #-----------------------------#    #    #
  #------------------------------------#    #
#-------------------------------------------#

#examples

for repeat in range(3):# repeat 3 times
  for number in range(0,5,1):# 0 to 4 by 1s
    print(number, end = " ")
  print() #added to format output
#output:
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 

for repeat in range(2):# repeat 2 times
  for number in range(0,101,20):# 0 to 100 by 20s
    print(number, end = " ")
  print() #added to format output
#output:
# 0 20 40 60 80 100 
# 0 20 40 60 80 100 

for repeat in range(4):# repeat 4 times
  for number in range(5,-6,-1):# 5 to -5 by 1s
    print(number, end = " ")
  print() #added to format output
#output:
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5

for repeat in range(4):# repeat 4 times
  for number in range(20,9,-2):# 20 to 10 by 2s
    print(number, end = " ")
  print() #added to format output
#output:
# 20 18 16 14 12 10 
# 20 18 16 14 12 10
# 20 18 16 14 12 10
# 20 18 16 14 12 10

#===============================================================================================================================#
'> Break, and  Continue'

'''
  Break
  The break statement in Python is used to exit (or "break out of") the loop prematurely. 
  It is commonly used within loops like for and while to interrupt the loop's execution based on a certain condition.
'''

'example: checking prime numbers'
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"equals",x,"*",n//x)
            break
    #loop fell through without finding a factor
    else:
        print(n,"is a prime number")
#the loop will exit on the first loop

'''
  Continue
  The continue statement in Python is used to skip the rest of the code 
  inside a loop for the current iteration, and continue with the next iteration 
  of the loop.
'''
#Not printing values divisible by 7
for x in range(50):
  if(x % 7 == 0):
    continue
  else:
    print(x)




